package polimorfizm.inclusion;

public class Main {
    public static void main(String[] args) {
        Image[] images = new Image[2];
        images[0] = new PNG();
        images[1] = new JPG();

        for (Image image : images) {
            displayImage(image);
        }
    }

    public static void displayImage(Image image) {
        image.display();
    }
}
