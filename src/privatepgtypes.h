/*
 * Copyright 2010,
 *
 * Andrei Herdt
 * Olivier  Stasse
 *
 * JRL, CNRS/AIST
 *
 * This file is part of walkGenJrl.
 * walkGenJrl is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * walkGenJrl is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Lesser Public License for more details.
 * You should have received a copy of the GNU Lesser General Public License
 * along with walkGenJrl.  If not, see <http://www.gnu.org/licenses/>.
 *
 *  Research carried out within the scope of the
 *  Joint Japanese-French Robotics Laboratory (JRL)
 */
/*! \file privatepgtypes.h
  \brief Defines basic types for the Humanoid Walking Pattern Generator.
*/

#ifndef _PATTERN_GENERATOR_INTERNAL_PRIVATE_H_
#define  _PATTERN_GENERATOR_INTERNAL_PRIVATE_H_

#include <jrl/mal/matrixabstractlayer.hh>
#include <boost/numeric/ublas/matrix_sparse.hpp>
#include <boost/numeric/ublas/matrix_proxy.hpp>

#include <deque>

namespace PatternGeneratorJRL
{

  //
  // Enum types
  //

  /// \name Enum types
  /// \{
  enum foot_type_e
  {
    LEFT, RIGHT
  };

  enum PhaseType
  {
    SS, DS
  };

  enum ineq_e
  {
    INEQ_COP, INEQ_COM, INEQ_FEET
  };

  enum objective_e
  {
    INSTANT_VELOCITY, COP_CENTERING, JERK_MIN
  };

  enum dynamics_e
  {
    POSITION, VELOCITY, ACCELERATION,
    JERK, COP_POSITION
  };

  enum qp_element_e
  {
    MATRIX_Q,
    MATRIX_DU,
    VECTOR_D,
    VECTOR_DS,
    VECTOR_DL,
    VECTOR_XL,
    VECTOR_XU
  };

  enum solver_e
  {
    QLD,
    LSSOL
  };

  enum tests_e
  {
      NONE,
      ALL,
      ITT,
      CTR1,
      CTR2,
      SOLVER
  };

  enum axis_e
  {
    X_AXIS, Y_AXIS, Z_AXIS, YAW, PITCH, ROLL
  };
  /// \}

  //
  // Structures
  //

  /// \name Structures
  /// \{
  /// \brief State of the center of mass
  struct com_t
  {
    MAL_VECTOR(x,double);
    MAL_VECTOR(y,double);
    MAL_VECTOR(z,double);

    struct com_t & operator=(const com_t &aCS);

    void reset();

    com_t();
  };


  // Support state of the robot at a certain point in time
  struct trunk_t
  {
    MAL_VECTOR(x,double);
    MAL_VECTOR(y,double);
    MAL_VECTOR(z,double);

    MAL_VECTOR(yaw,double);
    MAL_VECTOR(pitch,double);
    MAL_VECTOR(roll,double);

    struct trunk_t & operator=(const trunk_t &aTS);

    void reset();

    trunk_t();
  };

  //State of the feet on the ground
  struct supportfoot_t
  {
    double x,y,theta,StartTime;
    int SupportFoot;
  };

  /// Absolute reference.
  struct reference_t
  {
    struct frame_t
    {
      /// \brief Constant reference
      double X, Y, Yaw;

      /// \brief Reference vectors
      MAL_VECTOR(X_vec,double);
      MAL_VECTOR(Y_vec,double);
      MAL_VECTOR(Yaw_vec,double);

      frame_t();
      frame_t(const frame_t &);
    };

    frame_t Global, Local;

    reference_t();
    reference_t(const reference_t &);
  };

  /// \brief Convex hull
  struct convex_hull_t
  {

    /// \brief Edges
    std::vector<double> X_vec, Y_vec, Z_vec;
    /// \brief Inequalities A_vec(i)*x+B_vec(i)y+C_vec(i)z+D_vec(i) > 0
    std::vector<double> A_vec, B_vec, C_vec, D_vec;

    /// \brief Rotate the points around the origin of the hull
    ///
    /// \param[in] axis
    /// \param[in] angle
    void rotate( axis_e axis, double angle );

    /// \brief Resize members to the desired number of points
    /// \param[in] nbVert
    /// \param[in] nbIneq
    void resize( unsigned nbVert, unsigned nbIneq = 0 );

    /// \brief Set the polyhedron vertices from arrays
    ///
    /// \param[in] X_a
    /// \param[in] Y_a
    /// \param[in] Z_a
    void set_vertices( const double * X_a, const double * Y_a, const double * Z_a );
    /// \brief Set the polygon vectors from arrays
    ///
    /// \param[in] X_a
    /// \param[in] Y_a
    void set_vertices( const double * X_a, const double * Y_a );
    /// \brief Set polyhedral inequalities from arrays
    ///
    /// \param[in] A_a
    /// \param[in] B_a
    /// \param[in] C_a
    /// \param[in] D_a
    void set_inequalities( const double * A_a, const double * B_a, const double * C_a, const double * D_a );

    /// \brief Set all points to zero
    void clear();

    /// \brief Print
    void cout();

    /// \brief Constructor
    ///
    /// \param[in] nbVert Number vertices
    /// \param[in] nbIneq Number inequalities
    convex_hull_t( unsigned nbVert = 0, unsigned nbIneq = 0 );

  private:

    /// \brief Number inequalities
    unsigned nbIneq_;

    /// \brief Number vertices
    unsigned nbVert_;

  };


  /// \brief Linear inequalities set
  struct linear_inequality_t
  {
    struct coordinate_t
    {
      boost_ublas::compressed_matrix<double, boost_ublas::row_major> X_mat;
      boost_ublas::compressed_matrix<double, boost_ublas::row_major> Y_mat;
      boost_ublas::compressed_matrix<double, boost_ublas::row_major> Z_mat;
    };
    struct coordinate_t D;

    boost_ublas::vector<double> Dc_vec;

    /// \brief Classifier
    int type;

    /// \brief Fill all elements with zeros
    void clear();

    /// \brief Resize all elements
    void resize( int NbRows, int NbCols, bool Preserve );
  };

  /// \brief Support state of the robot at a certain point in time
  struct support_state_t
  {

    /// \brief Support phase
    PhaseType Phase;
    /// \brief Support foot
    foot_type_e Foot;
    /// \brief Number steps left before double support
    unsigned int NbStepsLeft;
    /// \brief Number of step previewed
    unsigned int StepNumber;
    /// \brief Number of samplings passed in this phase
    unsigned int NbInstants;

    /// \brief Time until StateChanged == true
    double TimeLimit;
    /// \brief start time
    double StartTime;
    /// \brief Position and orientation on a plane
    double X,Y,Yaw;

    /// \brief (true) -> New single support state
    bool StateChanged;

    struct support_state_t & operator = (const support_state_t &aSS);

    void reset();

    support_state_t();
  };

  /// \brief Solution
  struct solution_t
  {

    /// \brief Size of the solution array
    unsigned int NbVariables;

    /// \brief Number of constraints (lagrange multipliers)
    unsigned int NbConstraints;

    /// \brief SHOWS THE TERMINATION REASON. (QLD)
    ///   IFAIL = 0 :   SUCCESSFUL RETURN.
    ///   IFAIL = 1 :   TOO MANY ITERATIONS (MORE THAN 40*(N+M)).
    ///   IFAIL = 2 :   ACCURACY INSUFFICIENT TO SATISFY CONVERGENCE
    ///                 CRITERION.
    ///   IFAIL = 5 :   LENGTH OF A WORKING ARRAY IS TOO SHORT.
    ///   IFAIL > 10 :  THE CONSTRAINTS ARE INCONSISTENT.
    int Fail;

    /// \brief OUTPUT CONTROL.
    ///   IPRINT = 0 :  NO OUTPUT OF QL0001.
    ///   IPRINT > 0 :  BRIEF OUTPUT IN ERROR CASES.
    int Print;

    /// \brief True if you want to use warmstart (only with LSSOL)
    bool useWarmStart ;

    /// \name Solution vectors
    /// \{
    /// \brief QP solution vector
    boost_ublas::vector<double> Solution_vec;
    /// \brief QP initial solution vector
    boost_ublas::vector<double> initialSolution;
    /// \brief QP initial constraint vector
    boost_ublas::vector<int>  initialConstraint;
    /// \brief Previewed support orientations
    std::deque<double> SupportOrientations_deq;
    /// \brief Previewed trunk orientations (only yaw as for now)
    std::deque<double> TrunkOrientations_deq;
    /// \brief Previewed support states
    std::deque<support_state_t> SupportStates_deq;
    /// \}

    /// \name{
    /// \{
    /// \brief Lagrange multipliers of the constraints
    boost_ublas::vector<double> ConstrLagr_vec;
    /// \brief Lagrange multipliers of the lower bounds
    boost_ublas::vector<double> LBoundsLagr_vec;
    /// \brief Lagrange multipliers of the upper bounds
    boost_ublas::vector<double> UBoundsLagr_vec;
    /// \}

    /// \brief Reset
    void reset();

    /// \brief Resize solution containers
    void resize( unsigned int NbVariables, unsigned int NbConstraints );

    /// \brief Dump solution
    /// \param Filename
    void dump( const char * Filename );
    /// \brief Print_ solution
    /// \param aos
    void print( std::ostream & aos);

    solution_t();

  };

  /// \}

}

#endif /* _PATTERN_GENERATOR_INTERNAL_PRIVATE_H_ */
