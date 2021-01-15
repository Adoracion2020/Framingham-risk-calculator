import pandas as pd


def points_framingham_10year_risk(sex, age, total_cholesterol, systolic_blood_pressure, smoker,
                                  blood_pressure_med_treatment):

    if sex == 1:
        sex = "male"
    else:
        sex = "female"
    if smoker == 1:
        smoker = True
    else:
        smoker = False
    if int(blood_pressure_med_treatment) == 1:
        blood_pressure_med_treatment = True
    else:
        blood_pressure_med_treatment = False

    # intialize variables -----------------------------------------------------
    points = 0
    age = int(age)
    total_cholesterol = int(total_cholesterol)
    hdl_cholesterol = 39 if (sex == 'male') else 43
    systolic_blood_pressure = int(systolic_blood_pressure)

    # Process males -----------------------------------------------------------
    if sex.lower() == "male":

        # Age - male
        if 20 <= age <= 34:
            points -= 9
        if 35 <= age <= 39:
            points -= 4
        if 40 <= age <= 44:
            points -= 0
        if 45 <= age <= 49:
            points += 3
        if 50 <= age <= 54:
            points += 6
        if 55 <= age <= 59:
            points += 8
        if 60 <= age <= 64:
            points += 10
        if 65 <= age <= 69:
            points += 12
        if 70 <= age <= 74:
            points += 14
        if 75 <= age <= 79:
            points += 16

        # Total cholesterol, mg/dL - Male ------------------------
        if 20 <= age <= 39:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 4
            if 200 <= total_cholesterol <= 239:
                points += 7
            if 240 <= total_cholesterol <= 279:
                points += 9
            if total_cholesterol > 289:
                points += 11
        if 40 <= age <= 49:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 3
            if 200 <= total_cholesterol <= 239:
                points += 5
            if 240 <= total_cholesterol <= 279:
                points += 6
            if total_cholesterol > 289:
                points += 8
        if 50 <= age <= 59:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 2
            if 200 <= total_cholesterol <= 239:
                points += 3
            if 240 <= total_cholesterol <= 279:
                points += 4
            if total_cholesterol > 289:
                points += 5
        if 60 <= age <= 69:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 1
            if 200 <= total_cholesterol <= 239:
                points += 1
            if 240 <= total_cholesterol <= 279:
                points += 2
            if total_cholesterol > 289:
                points += 3
        if 70 <= age <= 79:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 0
            if 200 <= total_cholesterol <= 239:
                points += 0
            if 240 <= total_cholesterol <= 279:
                points += 1
            if total_cholesterol > 289:
                points += 1
        # smoking - male
        if smoker:
            if 20 <= age <= 39:
                points += 8
            if 40 <= age <= 49:
                points += 5
            if 50 <= age <= 59:
                points += 3
            if 60 <= age <= 69:
                points += 1
            if 70 <= age <= 79:
                points += 1
        else:  # nonsmoker
            points += 0

        # hdl cholesterol
        if hdl_cholesterol > 60:
            points -= 1
        if 50 <= hdl_cholesterol <= 59:
            points += 0
        if 40 <= hdl_cholesterol <= 49:
            points += 1
        if hdl_cholesterol < 40:
            points += 2

        # systolic blood pressure
        if not blood_pressure_med_treatment:
            if systolic_blood_pressure < 120:
                points += 0
            if 120 <= systolic_blood_pressure <= 129:
                points += 0
            if 130 <= systolic_blood_pressure <= 139:
                points += 1
            if 140 <= systolic_blood_pressure <= 159:
                points += 1
            if systolic_blood_pressure >= 160:
                points += 2
        else:  # if the patient is on blood pressure meds
            if systolic_blood_pressure < 120:
                points += 0
            if 120 <= systolic_blood_pressure <= 129:
                points += 1
            if 130 <= systolic_blood_pressure <= 139:
                points += 1
            if 140 <= systolic_blood_pressure <= 159:
                points += 2
            if systolic_blood_pressure >= 160:
                points += 3

    # process females ----------------------------------------------------------
    elif sex.lower() == "female":
        # Age - female
        if 20 <= age <= 34:
            points -= 7
        if 35 <= age <= 39:
            points -= 3
        if 40 <= age <= 44:
            points -= 0
        if 45 <= age <= 49:
            points += 3
        if 50 <= age <= 54:
            points += 6
        if 55 <= age <= 59:
            points += 8
        if 60 <= age <= 64:
            points += 10
        if 65 <= age <= 69:
            points += 12
        if 70 <= age <= 74:
            points += 14
        if 75 <= age <= 79:
            points += 16

        # Total cholesterol, mg/dL - Female ------------------------
        if 20 <= age <= 39:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 4
            if 200 <= total_cholesterol <= 239:
                points += 8
            if 240 <= total_cholesterol <= 279:
                points += 11
            if total_cholesterol > 289:
                points += 13
        if 40 <= age <= 49:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 3
            if 200 <= total_cholesterol <= 239:
                points += 6
            if 240 <= total_cholesterol <= 279:
                points += 8
            if total_cholesterol > 289:
                points += 10
        if 50 <= age <= 59:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 2
            if 200 <= total_cholesterol <= 239:
                points += 4
            if 240 <= total_cholesterol <= 279:
                points += 5
            if total_cholesterol > 289:
                points += 7
        if 60 <= age <= 69:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 1
            if 200 <= total_cholesterol <= 239:
                points += 2
            if 240 <= total_cholesterol <= 279:
                points += 3
            if total_cholesterol > 289:
                points += 4
        if 70 <= age <= 79:
            if total_cholesterol < 160:
                points += 0
            if 160 <= total_cholesterol <= 199:
                points += 1
            if 200 <= total_cholesterol <= 239:
                points += 1
            if 240 <= total_cholesterol <= 279:
                points += 2
            if total_cholesterol > 289:
                points += 2
        # smoking - female
        if smoker:
            if 20 <= age <= 39:
                points += 9
            if 40 <= age <= 49:
                points += 7
            if 50 <= age <= 59:
                points += 4
            if 60 <= age <= 69:
                points += 2
            if 70 <= age <= 79:
                points += 1
        else:  # nonsmoker
            points += 0

        # hdl cholesterol - female
        if hdl_cholesterol > 60:
            points -= 1
        if 50 <= hdl_cholesterol <= 59:
            points += 0
        if 40 <= hdl_cholesterol <= 49:
            points += 1
        if hdl_cholesterol < 40:
            points += 2

        # systolic blood pressure
        if not blood_pressure_med_treatment:  # untreated
            if systolic_blood_pressure < 120:
                points += 0
            if 120 <= systolic_blood_pressure <= 129:
                points += 1
            if 130 <= systolic_blood_pressure <= 139:
                points += 2
            if 140 <= systolic_blood_pressure <= 159:
                points += 3
            if systolic_blood_pressure >= 160:
                points += 4
        else:  # if the patient is on blood pressure meds
            if systolic_blood_pressure < 120:
                points += 0
            if 120 <= systolic_blood_pressure <= 129:
                points += 3
            if 130 <= systolic_blood_pressure <= 139:
                points += 4
            if 140 <= systolic_blood_pressure <= 159:
                points += 5
            if systolic_blood_pressure >= 160:
                points += 6

    return points


def percentage_risk(sex, points):

    percent_risk = "0%"
    # Process males -----------------------------------------------------------
    if sex == 1:
        # calulate % risk for males
        if points <= 0:
            percent_risk = "<1%"
        elif points == 1:
            percent_risk = "1%"

        elif points == 2:
            percent_risk = "1%"

        elif points == 3:
            percent_risk = "1%"

        elif points == 4:
            percent_risk = "1%"

        elif points == 5:
            percent_risk = "2%"

        elif points == 6:
            percent_risk = "2%"

        elif points == 7:
            percent_risk = "2%"

        elif points == 8:
            percent_risk = "2%"

        elif points == 9:
            percent_risk = "5%"

        elif points == 10:
            percent_risk = "6%"

        elif points == 11:
            percent_risk = "8%"

        elif points == 12:
            percent_risk = "10%"

        elif points == 13:
            percent_risk = "12%"

        elif points == 14:
            percent_risk = "16%"

        elif points == 15:
            percent_risk = "20%"

        elif points == 16:
            percent_risk = "25%"

        elif points >= 17:
            percent_risk = ">30%"

    # process females ----------------------------------------------------------

    elif sex == 0:
        # calulate % risk for females
        if points <= 9:
            percent_risk = "<1%"

        elif 9 <= points <= 12:
            percent_risk = "1%"

        elif 13 <= points <= 14:
            percent_risk = "2%"

        elif points == 15:
            percent_risk = "3%"

        elif points == 16:
            percent_risk = "4%"

        elif points == 17:
            percent_risk = "5%"

        elif points == 18:
            percent_risk = "6%"

        elif points == 19:
            percent_risk = "8%"

        elif points == 20:
            percent_risk = "11%"

        elif points == 21:
            percent_risk = "14%"

        elif points == 22:
            percent_risk = "17%"

        elif points == 23:
            percent_risk = "22%"

        elif points == 24:
            percent_risk = "27%"

        elif points >= 25:
            percent_risk = "30%"

    return percent_risk


def add_diabetes(sex, diabetes, points):
    if sex == 1:
        if diabetes == 1:
            points += 2
    if sex == 0:
        if diabetes == 1:
            points += 4
    return points


if __name__ == "__main__":

    data = pd.read_csv("**RUTA**/framingham.csv")

    # rename columns
    df_new = data.rename(columns={'male': 'sex', 'totChol': 'total_cholesterol', 'sysBP': 'systolic_blood_pressure',
                                  'currentSmoker': 'smoker', 'BPMeds': 'blood_pressure_med_treatment'})
    # drop unusued columns
    df_1 = df_new.drop(
        columns=['education', 'BMI', 'cigsPerDay', 'prevalentStroke', 'prevalentHyp', 'diaBP', 'heartRate',
                 'glucose'])
    # Preview the first 5 lines of the loaded data
    print(df_1.head)

    # remove missing values
    df3 = df_1.dropna()

    pd.options.mode.chained_assignment = None  # default='warn'

    # (sex, age, total_cholesterol, systolic_blood_pressure, smoker, blood_pressure_med_treatment):
    df3['baseline_score'] = df3.apply(lambda x: points_framingham_10year_risk(x[0], x[1], x[5], x[6], x[2], x[3]),
                                      axis=1)

    df3['baseline_risk'] = df3.apply(lambda x: percentage_risk(x[0], x[8]), axis=1)

    df3['enhanced_score'] = df3.apply(lambda x: add_diabetes(x[0], x[4], x[8]), axis=1)

    df3['enhanced_risk'] = df3.apply(lambda x: percentage_risk(x[0], x[10]), axis=1)

    print(len(df3.index))

    df3.to_csv('**RUTA**/risk_score.csv')

    df4 = df3[df3["diabetes"] == 1].drop(columns=['age', 'sex', 'total_cholesterol', 'systolic_blood_pressure',
                                                  'smoker', 'blood_pressure_med_treatment', 'diabetes', 'baseline_score'
                                                  , 'enhanced_score'])

    df4.to_csv('**RUTA**/baseline_vs_enhanced.csv')


