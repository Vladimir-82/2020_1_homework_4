cal=6000
step=43
step_count=0
while cal>3400:
    cal=cal-step
    step_count=step_count+1
    print(f"Шаг{step_count},калорий{cal}")


print(f"Шагов сделано:{step_count}")
