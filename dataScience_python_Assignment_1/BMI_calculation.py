def bmi_calculation(weight,height):
    bmi=weight/height**2
    if bmi<18.5:
        return bmi,'UNDERWEIGHT'
    elif 18.5<=bmi<25:
        return bmi,'NORMAL'
    elif 25<=bmi<30:
        return bmi,'OVERWEIGHT'
    else:
        return bmi,'VERY-OVERWEIGHT'        
Name=input("enter your name")
weight=float(input("enter your weight in kgs"))
height_choice=input("enter your preferred choice of height:Type 'M' or 'F':")
if height_choice=="M":
    height=float(input("enter your height in meters:"))
if height_choice=="F":
    feet=float(input("enter your height in feet:"))
    inches=float(input("enter your height in inches:"))
    feet_meters=feet/3.2808
    inches_meters=inches*0.0254
    height=feet_meters+inches_meters
calculated_bmi,Result=bmi_calculation(weight, height)
print('your bmi is {:.2f} and you are {}'.format(calculated_bmi,Result))
    
    