class MyThread extends Thread {
  override def run() : Unit = {
    println("Thread " + Thread.currentThread().getName() + " is running.")
  }
}

object MyObject {
  // Main method
  def main(args: Array[String]) : Unit = {
    for (x <- 1 to 5) {
      var th = new MyThread()
      th.setName(x.toString())
      th.start()
    }
  } 
}