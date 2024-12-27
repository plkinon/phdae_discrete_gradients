import pydykit
import pydykit.postprocessors as postprocessors
import pydykit.systems_port_hamiltonian as phs

name = "four_particle_system_DG_no_diss"

manager = pydykit.managers.Manager()

path_config_file = f"./input_files/{name}.yml"

manager.configure_from_path(path=path_config_file)

porthamiltonian_system = phs.PortHamiltonianMBS(manager=manager)
# creates an instance of PHS with attribute MBS
manager.system = porthamiltonian_system

result = pydykit.results.Result(manager=manager)
result_3 = manager.manage(result=result)

df = result.to_df()
postprocessor = postprocessors.Postprocessor(manager, state_results_df=df)
postprocessor.postprocess(
    quantities_and_evaluation_points={
        "hamiltonian": ["current_time", "interval_increment"]
    }
)

# Plotter object gets result dataframe
plotter = postprocessors.Plotter(results_df=postprocessor.results_df)

# Hamiltonian
fig01 = plotter.visualize_time_evolution(quantities=["hamiltonian_current_time"])
fig01.show()

fig02 = plotter.visualize_time_evolution(
    quantities=["hamiltonian_interval_increment"],
)
fig02.show()

postprocessor.results_df.to_csv(f"./results/{name}.csv", index=False)
