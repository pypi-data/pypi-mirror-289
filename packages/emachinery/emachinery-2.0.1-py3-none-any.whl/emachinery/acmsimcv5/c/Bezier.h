#ifndef BEZIER_C
#define BEZIER_C

#include "typedef.h"
#include "brentq.h"
#include "pid_regulator.h"
#include <stdio.h>
typedef struct
{
    REAL x;
    REAL y;
} Point;

typedef struct
{
    Point points[10];
    int terminal;
} BezierController;

int Comb(int n, int m);

Point bezier(const REAL *t, const BezierController *BziController);

REAL bezier_x(const REAL *t, const BezierController *BziController);

REAL bezier_y(const REAL *t, const BezierController *BziController);

REAL bezier_x_diff(REAL t, void *params);

REAL find_t_for_given_x(const REAL x, const BezierController *BziController);

REAL find_y_for_given_x(const REAL x, const BezierController *BziController);

void set_points(BezierController *BziController);

void control_output(st_pid_regulator *r, BezierController *BzController);

#endif