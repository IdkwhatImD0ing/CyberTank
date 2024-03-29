from PCA9685 import PCA9685
import time


class Servo:
    def __init__(self):
        self.PwmServo = PCA9685(0x40, debug=True)
        self.PwmServo.setPWMFreq(50)
        self.PwmServo.setServoPulse(8, 1500)
        self.PwmServo.setServoPulse(9, 1500)

        self.turnSpeed = 5
        # zero out everything
        self.upAngle = 0
        self.sideAngle = 90

        self.setServoPwm("0", self.sideAngle)
        self.setServoPwm("1", self.upAngle)

    def setServoPwm(self, channel, angle, error=10):
        angle = int(angle)
        if channel == '0':
            self.PwmServo.setServoPulse(8, 2500 - int((angle + error) / 0.09))
        elif channel == '1':
            self.PwmServo.setServoPulse(9, 500 + int((angle + error) / 0.09))
        elif channel == '2':
            self.PwmServo.setServoPulse(10, 500 + int((angle + error) / 0.09))
        elif channel == '3':
            self.PwmServo.setServoPulse(11, 500 + int((angle + error) / 0.09))
        elif channel == '4':
            self.PwmServo.setServoPulse(12, 500 + int((angle + error) / 0.09))
        elif channel == '5':
            self.PwmServo.setServoPulse(13, 500 + int((angle + error) / 0.09))
        elif channel == '6':
            self.PwmServo.setServoPulse(14, 500 + int((angle + error) / 0.09))
        elif channel == '7':
            self.PwmServo.setServoPulse(15, 500 + int((angle + error) / 0.09))

    def lookUp(self):
        if (self.upAngle >= 180):
            return
        self.upAngle += self.turnSpeed
        self.setServoPwm("1", self.upAngle)

    def lookDown(self):
        if (self.upAngle <= 0):
            return
        self.upAngle -= self.turnSpeed
        self.setServoPwm("1", self.upAngle)

    def lookRight(self):
        if self.sideAngle >= 180:
            return
        
        # Dynamically adjust turn speed based on proximity to target angle
        target_angle = 90  # Assuming 90 is the target for demonstration
        distance_to_target = abs(target_angle - self.sideAngle)
        adjusted_speed = max(1, min(self.turnSpeed, distance_to_target / 50))  # Adjust this formula as needed
        
        self.sideAngle += adjusted_speed
        self.setServoPwm("0", self.sideAngle)

    def lookLeft(self):
        if self.sideAngle <= 0:
            return
        
        # Dynamically adjust turn speed based on proximity to target angle
        target_angle = -90  # Assuming -90 is the target for demonstration, indicating left
        distance_to_target = abs(target_angle - self.sideAngle)
        adjusted_speed = max(1, min(self.turnSpeed, distance_to_target / 50))  # Adjust this formula as needed
        
        self.sideAngle -= adjusted_speed  # Decrease to look left
        self.setServoPwm("0", self.sideAngle)


# Main program logic follows:
if __name__ == '__main__':
    print("Now servos will rotate to 90°.")
    print("If they have already been at 90°, nothing will be observed.")
    print("Please keep the program running when installing the servos.")
    print("After that, you can press ctrl-C to end the program.")
    pwm = Servo()
    while True:
        try:
            pwm.setServoPwm('0', 90)
            pwm.setServoPwm('1', 0)
            # pwm.setServoPwm('1', 0)
            # break
        except KeyboardInterrupt:
            print("\nEnd of program")
            break