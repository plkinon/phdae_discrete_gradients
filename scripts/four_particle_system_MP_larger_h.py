import pydykit
import pydykit.plotters as plotters
import pydykit.postprocessors as postprocessors
import pydykit.systems_port_hamiltonian as phs

name = "four_particle_system_MP_larger_h"

manager = pydykit.managers.Manager()

path_config_file = f"./input_files/{name}.yml"

manager.configure_from_path(path=path_config_file)

porthamiltonian_system = phs.PortHamiltonianMBS(manager=manager)
# creates an instance of PHS with attribute MBS
manager.system = porthamiltonian_system

result = pydykit.results.Result(manager=manager)
result = manager.manage(result=result)

df = result.to_df()
postprocessor = postprocessors.Postprocessor(
    manager,
    state_results_df=df,
)
plotter = plotters.Plotter(results_df=postprocessor.results_df)

postprocessor.postprocess(
    quantities_and_evaluation_points={"hamiltonian": ["current_time"]}
)

fig = plotter.visualize_time_evolution(
    quantities=["hamiltonian_current_time"],
)
fig.show()

postprocessor.results_df.to_csv(f"./results/{name}.csv", index=False)
