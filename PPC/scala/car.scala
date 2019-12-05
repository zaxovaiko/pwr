class Pojazd (val producent: String, val model: String, val rok: Int = -1, var rejestracja: String = "") {
    def this(producent: String, model: String, rejestracja: String) {
        this(producent, model, -1, rejestracja)
    }
}

new Pojazd("BMW", "x6", 2030, "AB123")
new Pojazd("BMW", "x6", 2030)
new Pojazd("BMW", "x6", "AB123")
new Pojazd("BMW", "x6")