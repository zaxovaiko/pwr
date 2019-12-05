class Time(private var h: Int) {
    if (h < 0) h = 0

    def hour: Int = h

    def hour_= (newHour: Int) : Unit = {
        if (newHour < 0) h = 0
        else h = newHour
    }
}

object Time {
    def apply(hour: Int) = new Time(hour)
}

var c = Time(-9)
print(c.hour)