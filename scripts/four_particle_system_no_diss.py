import pydykit
import pydykit.postprocessors as postprocessors
import pydykit.systems_port_hamiltonian as phs

name = "four_particle_system_no_diss"

manager_3 = pydykit.managers.Manager()

path_config_file_3 = f"./input_files/{name}.yml"

manager_3.configure_from_path(path=path_config_file_3)

porthamiltonian_system_3 = phs.PortHamiltonianMBS(manager=manager_3)
# creates an instance of PHS with attribute MBS
manager_3.system = porthamiltonian_system_3

result_3 = pydykit.results.Result(manager=manager_3)
result_3 = manager_3.manage(result=result_3)

df_3 = result_3.to_df()
postprocessor_3 = postprocessors.Postprocessor(manager_3, state_results_df=df_3)
postprocessor_3.postprocess(
    quantities=["hamiltonian", "hamiltonian"],
    evaluation_points=["current_time", "interval_increment"],
)

# Hamiltonian
fig01 = postprocessor_3.visualize(quantities=["hamiltonian_current_time"])
# fig01.show()

fig02 = postprocessor_3.visualize(
    quantities=["hamiltonian_interval_increment"],
)
# fig02.show()

# postprocessor_3.results_df.to_csv(
#     f"./test/publications/{project}/{name}.csv", index=False
# )
