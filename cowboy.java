import java.util.*;
/**
 * Author :- Jayspray
 * Team :- Dillusioners
 * Program topic :- Cowboy
 * SuperB special events
 * This program helps the user to find in which village a certain number of cowboys exist
 */
class cowboy{
    public static void welcome(){
        //Just a print method to print the heading
        System.out.println("#################### Welcome to cowboy searcher ####################");
        System.out.println("Find the village using the number of cowboys in it");
    }
    public static void solve(HashMap<Long,Integer> g_map, long search){
        //Checking if key exists
        Long myNum = (long)(search);
        //If key exists we print the value which is the village index
        if(g_map.containsKey(myNum)){
            int answer = g_map.get(myNum);
            System.out.println(search + " villagers exist in village " + answer);
        }
        //else we let the user know that village doesnt exist
        else{
            System.out.println("Village doesn't exist!");
        }
    }
    public static void main(String[] args) {
        //Invoking welcome function
        welcome();
        Scanner sc = new Scanner(System.in);
        HashMap<Long, Integer> map = new HashMap<>();

        //Taking the number of villages as input

        System.out.println("Enter the number of villages");
        long villages = sc.nextLong();

        //Appending village cowboys in a hashmap
        for(int i = 1; i <= villages; i++){
            System.out.println("Enter number of cowboys in village " + i);
            long cowboys = sc.nextLong();
            map.put(cowboys, i);
        }
        //Asking for number of cowboys to see which village has that many cowboys
        System.out.println("Enter the number of cowboys you wanna search : ");
        long search = sc.nextLong();

        //Invoking solve method
        solve(map,search);
        sc.close();
    }
}
