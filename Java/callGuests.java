public class callGuests {

    public static int callGuests(int n) {
        if(n<=1){
            return 1;
        }
        //call Single
        int way1 = callGuests(n-1);

        //call in Pair
        int way2 = (n-1) * callGuests(n-2);

        return way1 + way2;
    }

    public static void main(String[] args) {
        int n=4;
        System.out.println(callGuests(n));
    }
}
