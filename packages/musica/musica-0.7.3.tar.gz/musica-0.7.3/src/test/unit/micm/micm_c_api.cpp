#include <musica/micm.hpp>
#include <musica/util.hpp>

#include <micm/util/error.hpp>

#include <gtest/gtest.h>

#include <iostream>

using namespace musica;

// Test fixture for the MICM C API
class MicmCApiTest : public ::testing::Test
{
 protected:
  MICM* micm;
  const char* config_path = "configs/chapman";
  int num_grid_cells = 1;

  void SetUp() override
  {
    micm = nullptr;
    Error error;
    micm = CreateMicm(config_path, MICMSolver::Rosenbrock, num_grid_cells, &error);

    ASSERT_TRUE(IsSuccess(error));
    DeleteError(&error);
  }

  void TearDown() override
  {
    Error error;
    DeleteMicm(micm, &error);
    ASSERT_TRUE(IsSuccess(error));
    DeleteError(&error);
  }
};

// Test case for bad configuration file path
TEST_F(MicmCApiTest, BadConfigurationFilePath)
{
  int num_grid_cells = 1;
  Error error = NoError();
  auto micm_bad_config = CreateMicm("bad config path", MICMSolver::Rosenbrock, num_grid_cells, &error);
  ASSERT_EQ(micm_bad_config, nullptr);
  ASSERT_TRUE(IsError(error, MICM_ERROR_CATEGORY_CONFIGURATION, MICM_CONFIGURATION_ERROR_CODE_INVALID_FILE_PATH));
  DeleteError(&error);
}

// Test case for bad input for solver type
TEST_F(MicmCApiTest, BadSolverType)
{
  short solver_type = 999;
  int num_grid_cells = 1;
  Error error = NoError();
  auto micm_bad_solver_type = CreateMicm("configs/chapman", static_cast<MICMSolver>(solver_type), num_grid_cells, &error);
  ASSERT_EQ(micm_bad_solver_type, nullptr);
  ASSERT_TRUE(IsError(error, MUSICA_ERROR_CATEGORY, MUSICA_ERROR_CODE_SOLVER_TYPE_NOT_FOUND));
  DeleteError(&error);
}

// Test case for missing species property
TEST_F(MicmCApiTest, MissingSpeciesProperty)
{
  Error error = NoError();
  String string_value;
  string_value = GetSpeciesPropertyString(micm, "O3", "bad property", &error);
  ASSERT_TRUE(IsError(error, MICM_ERROR_CATEGORY_SPECIES, MICM_SPECIES_ERROR_CODE_PROPERTY_NOT_FOUND));
  ASSERT_STREQ(string_value.value_, nullptr);
  DeleteString(&string_value);
  DeleteError(&error);
  error = NoError();
  ASSERT_EQ(GetSpeciesPropertyDouble(micm, "O3", "bad property", &error), 0.0);
  ASSERT_TRUE(IsError(error, MICM_ERROR_CATEGORY_SPECIES, MICM_SPECIES_ERROR_CODE_PROPERTY_NOT_FOUND));
  DeleteError(&error);
  error = NoError();
  ASSERT_EQ(GetSpeciesPropertyInt(micm, "O3", "bad property", &error), 0);
  ASSERT_TRUE(IsError(error, MICM_ERROR_CATEGORY_SPECIES, MICM_SPECIES_ERROR_CODE_PROPERTY_NOT_FOUND));
  DeleteError(&error);
  error = NoError();
  ASSERT_FALSE(GetSpeciesPropertyBool(micm, "O3", "bad property", &error));
  ASSERT_TRUE(IsError(error, MICM_ERROR_CATEGORY_SPECIES, MICM_SPECIES_ERROR_CODE_PROPERTY_NOT_FOUND));
  DeleteError(&error);
}

// Test case for creating the MICM instance
TEST_F(MicmCApiTest, CreateMicmInstance)
{
  ASSERT_NE(micm, nullptr);
}

// Test case for getting species ordering
TEST_F(MicmCApiTest, GetSpeciesOrdering)
{
  Error error;
  std::size_t array_size;
  Mapping* species_ordering = GetSpeciesOrdering(micm, &array_size, &error);
  ASSERT_TRUE(IsSuccess(error));
  DeleteError(&error);
  ASSERT_EQ(array_size, 4);
  bool found = false;
  for (std::size_t i = 0; i < array_size; i++)
  {
    if (strcmp(species_ordering[i].name_.value_, "O3") == 0)
    {
      found = true;
      break;
    }
  }
  ASSERT_TRUE(found);
  found = false;
  for (std::size_t i = 0; i < array_size; i++)
  {
    if (strcmp(species_ordering[i].name_.value_, "O") == 0)
    {
      found = true;
      break;
    }
  }
  ASSERT_TRUE(found);
  found = false;
  for (std::size_t i = 0; i < array_size; i++)
  {
    if (strcmp(species_ordering[i].name_.value_, "O2") == 0)
    {
      found = true;
      break;
    }
  }
  ASSERT_TRUE(found);
  found = false;
  for (std::size_t i = 0; i < array_size; i++)
  {
    if (strcmp(species_ordering[i].name_.value_, "O1D") == 0)
    {
      found = true;
      break;
    }
  }
  ASSERT_TRUE(found);
  DeleteMappings(species_ordering, array_size);
}

// Test case for getting user-defined reaction rates ordering
TEST_F(MicmCApiTest, GetUserDefinedReactionRatesOrdering)
{
  Error error;
  std::size_t array_size;
  Mapping* reaction_rates_ordering = GetUserDefinedReactionRatesOrdering(micm, &array_size, &error);
  ASSERT_TRUE(IsSuccess(error));
  DeleteError(&error);
  ASSERT_EQ(array_size, 3);
  bool found = false;
  for (std::size_t i = 0; i < array_size; i++)
  {
    if (strcmp(reaction_rates_ordering[i].name_.value_, "PHOTO.R1") == 0)
    {
      found = true;
      break;
    }
  }
  ASSERT_TRUE(found);
  found = false;
  for (std::size_t i = 0; i < array_size; i++)
  {
    if (strcmp(reaction_rates_ordering[i].name_.value_, "PHOTO.R3") == 0)
    {
      found = true;
      break;
    }
  }
  ASSERT_TRUE(found);
  found = false;
  for (std::size_t i = 0; i < array_size; i++)
  {
    if (strcmp(reaction_rates_ordering[i].name_.value_, "PHOTO.R5") == 0)
    {
      found = true;
      break;
    }
  }
  ASSERT_TRUE(found);
  DeleteMappings(reaction_rates_ordering, array_size);
}

// Test case for solving system using vector-ordered Rosenbrock solver
TEST_F(MicmCApiTest, SolveUsingVectorOrderedRosenbrock)
{
  double time_step = 200.0;
  double temperature = 272.5;
  double pressure = 101253.3;
  constexpr double GAS_CONSTANT = 8.31446261815324;  // J mol-1 K-1
  double air_density = pressure / (GAS_CONSTANT * temperature);
  int num_concentrations = 4;
  double concentrations[] = { 0.4, 0.8, 0.01, 0.02 };
  std::size_t num_user_defined_reaction_rates = 3;
  double user_defined_reaction_rates[] = { 0.1, 0.2, 0.3 };
  String solver_state;
  SolverResultStats solver_stats;
  Error error;

  Mapping* ordering = GetUserDefinedReactionRatesOrdering(micm, &num_user_defined_reaction_rates, &error);
  ASSERT_TRUE(IsSuccess(error));

  std::vector<double> custom_rate_parameters(num_user_defined_reaction_rates, 0.0);
  for (std::size_t i = 0; i < num_user_defined_reaction_rates; i++)
  {
    custom_rate_parameters[ordering[i].index_] = 0.0;
  }

  MicmSolve(
      micm,
      time_step,
      temperature,
      pressure,
      air_density,
      num_concentrations,
      concentrations,
      custom_rate_parameters.size(),
      custom_rate_parameters.data(),
      &solver_state,
      &solver_stats,
      &error);
  ASSERT_TRUE(IsSuccess(error));

  // Add assertions to check the solved concentrations
  ASSERT_NE(concentrations[0], 0.4);
  ASSERT_NE(concentrations[1], 0.8);
  ASSERT_NE(concentrations[2], 0.01);
  ASSERT_NE(concentrations[3], 0.02);

  std::cout << "Solver state: " << solver_state.value_ << std::endl;
  std::cout << "Function Calls: " << solver_stats.function_calls_ << std::endl;
  std::cout << "Jacobian updates: " << solver_stats.jacobian_updates_ << std::endl;
  std::cout << "Number of steps: " << solver_stats.number_of_steps_ << std::endl;
  std::cout << "Accepted: " << solver_stats.accepted_ << std::endl;
  std::cout << "Rejected: " << solver_stats.rejected_ << std::endl;
  std::cout << "Decompositions: " << solver_stats.decompositions_ << std::endl;
  std::cout << "Solves: " << solver_stats.solves_ << std::endl;
  std::cout << "Singular: " << solver_stats.singular_ << std::endl;
  std::cout << "Final time: " << solver_stats.final_time_ << std::endl;

  DeleteMappings(ordering, num_user_defined_reaction_rates);
  DeleteString(&solver_state);
  DeleteError(&error);
}

// Test case for solving system using standard-ordered Rosenbrock solver
TEST(RosenbrockStandardOrder, SolveUsingStandardOrderedRosenbrock)
{
  const char* config_path = "configs/chapman";
  int num_grid_cells = 1;
  Error error;
  MICM* micm = CreateMicm(config_path, MICMSolver::RosenbrockStandardOrder, num_grid_cells, &error);

  double time_step = 200.0;
  double temperature = 272.5;
  double pressure = 101253.3;
  constexpr double GAS_CONSTANT = 8.31446261815324;  // J mol-1 K-1
  double air_density = pressure / (GAS_CONSTANT * temperature);
  int num_concentrations = 4;
  double concentrations[] = { 0.4, 0.8, 0.01, 0.02 };
  std::size_t num_user_defined_reaction_rates = 3;
  double user_defined_reaction_rates[] = { 0.1, 0.2, 0.3 };
  String solver_state;
  SolverResultStats solver_stats;

  Mapping* ordering = GetUserDefinedReactionRatesOrdering(micm, &num_user_defined_reaction_rates, &error);
  ASSERT_TRUE(IsSuccess(error));

  std::vector<double> custom_rate_parameters(num_user_defined_reaction_rates, 0.0);
  for (std::size_t i = 0; i < num_user_defined_reaction_rates; i++)
  {
    custom_rate_parameters[ordering[i].index_] = 0.0;
  }

  MicmSolve(
      micm,
      time_step,
      temperature,
      pressure,
      air_density,
      num_concentrations,
      concentrations,
      custom_rate_parameters.size(),
      custom_rate_parameters.data(),
      &solver_state,
      &solver_stats,
      &error);
  ASSERT_TRUE(IsSuccess(error));

  ASSERT_NE(concentrations[0], 0.4);
  ASSERT_NE(concentrations[1], 0.8);
  ASSERT_NE(concentrations[2], 0.01);
  ASSERT_NE(concentrations[3], 0.02);

  std::cout << "Solver state: " << solver_state.value_ << std::endl;
  std::cout << "Function Calls: " << solver_stats.function_calls_ << std::endl;
  std::cout << "Jacobian updates: " << solver_stats.jacobian_updates_ << std::endl;
  std::cout << "Number of steps: " << solver_stats.number_of_steps_ << std::endl;
  std::cout << "Accepted: " << solver_stats.accepted_ << std::endl;
  std::cout << "Rejected: " << solver_stats.rejected_ << std::endl;
  std::cout << "Decompositions: " << solver_stats.decompositions_ << std::endl;
  std::cout << "Solves: " << solver_stats.solves_ << std::endl;
  std::cout << "Singular: " << solver_stats.singular_ << std::endl;
  std::cout << "Final time: " << solver_stats.final_time_ << std::endl;

  DeleteMappings(ordering, num_user_defined_reaction_rates);
  DeleteString(&solver_state);
  DeleteMicm(micm, &error);
  ASSERT_TRUE(IsSuccess(error));
  DeleteError(&error);
}

// Test case for getting species properties
TEST_F(MicmCApiTest, GetSpeciesProperty)
{
  Error error;
  String string_value;
  string_value = GetSpeciesPropertyString(micm, "O3", "__long name", &error);
  ASSERT_TRUE(IsSuccess(error));
  ASSERT_STREQ(string_value.value_, "ozone");
  DeleteString(&string_value);
  ASSERT_EQ(GetSpeciesPropertyDouble(micm, "O3", "molecular weight [kg mol-1]", &error), 0.048);
  ASSERT_TRUE(IsSuccess(error));
  ASSERT_TRUE(GetSpeciesPropertyBool(micm, "O3", "__do advect", &error));
  ASSERT_TRUE(IsSuccess(error));
  ASSERT_EQ(GetSpeciesPropertyInt(micm, "O3", "__atoms", &error), 3);
  ASSERT_TRUE(IsSuccess(error));
  GetSpeciesPropertyBool(micm, "bad species", "__is gas", &error);
  ASSERT_TRUE(IsError(error, MUSICA_ERROR_CATEGORY, MUSICA_ERROR_CODE_SPECIES_NOT_FOUND));
  GetSpeciesPropertyDouble(micm, "O3", "bad property", &error);
  ASSERT_TRUE(IsError(error, MICM_ERROR_CATEGORY_SPECIES, MICM_SPECIES_ERROR_CODE_PROPERTY_NOT_FOUND));
  DeleteError(&error);
}