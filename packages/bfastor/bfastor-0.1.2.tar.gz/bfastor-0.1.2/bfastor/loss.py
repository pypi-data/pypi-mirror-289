import typing
from dataclasses import fields
import jax.numpy as jnp
from bfastor import blur, core
import jax
import jax.scipy as jscipy
import optax


def density_loss(indexed_data: jax.Array, simulated_data: jax.Array) -> jax.Array:
    dloss = optax.cosine_distance(simulated_data, jnp.squeeze(indexed_data))
    return jnp.nansum(dloss)


def neighbour_loss(
    sigmas: jax.Array, neighbour_indexes: jax.Array, neighbour_distances: jax.Array
) -> jax.Array:
    weights = jscipy.stats.norm.pdf(neighbour_distances, 0, 2.0)
    weights = weights / weights.max(axis=-1, keepdims=True)
    # means = jnp.average(sigmas[neighbour_indexes], axis=-1, weights=weights)
    vals = sigmas[neighbour_indexes] - sigmas[:, None]
    losses = jax.vmap(
        jscipy.stats.norm.pdf,
        in_axes=(1, None, None),
        out_axes=1,
    )(vals, 0, 1.75)
    losses = jnp.average(losses, axis=-1, weights=weights)
    return -jnp.nansum(losses)


def get_loss_function(
    simulation_function: typing.Callable,
    reconstruction_loss_function: typing.Callable = density_loss,
    regularisation_loss_function: typing.Callable = neighbour_loss,
    gradient_params: typing.Tuple[str] = ("sigmas",),
) -> typing.Callable:
    def loss_function(
        params: core.Parameters,
        x: jax.Array,
        indexed_densities: jax.Array,
        neighbour_indexes: jax.Array,
        neighbour_distances: jax.Array,
    ) -> jnp.ndarray:
        for p in fields(params):
            if p.name in gradient_params:
                continue
            setattr(params, p.name, jax.lax.stop_gradient(getattr(params, p.name)))

        simulated_densities = simulation_function(params, x, neighbour_indexes)

        reconstruction_loss = reconstruction_loss_function(
            indexed_densities,
            simulated_densities,
        )
        regularisation_loss = regularisation_loss_function(
            params.sigmas, neighbour_indexes, neighbour_distances
        )

        return reconstruction_loss + regularisation_loss

    return loss_function


@jax.jit
def warmup_loss(
    sigmas: jax.Array,
    params: core.Parameters,
    indexed_density: jax.Array,
    random_vectors: jax.Array,
    neighbours_ij: jax.Array,
) -> jax.Array:
    simulated_density = blur.log_sp.simulate_summed_densities_from_all_atoms(
        random_vectors,
        params.coordinates[neighbours_ij],
        sigmas[neighbours_ij],
        params.a[neighbours_ij],
        params.b[neighbours_ij],
        params.mass[neighbours_ij],
    )
    return optax.cosine_distance(simulated_density, jnp.squeeze(indexed_density))
