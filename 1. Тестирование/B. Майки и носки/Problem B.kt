fun main(){
    
    test2()
}

fun test2(){

    
    val a = readLine()!!.toInt()
    val b = readLine()!!.toInt()
    val c = readLine()!!.toInt()
    val d = readLine()!!.toInt()
    
    val ans = mutableListOf<Pair<Int,Int>>()
    
    if(a!=0 && c!=0){
        if(b!=0 && d!=0){
            ans.add(Pair(b+1,d+1))
            ans.add(Pair(maxOf(a,b)+1,1))
            ans.add(Pair(1,maxOf(c,d)+1))
        }else if (b!=0 && d==0) ans.add(Pair(b+1,1))
        else if (b==0 && d!=0) ans.add(Pair(1,d+1))
        else ans.add(Pair(1,1))
    }
    if(b!=0 && d!=0){
        if(a!=0 && c!=0) ans.add(Pair(a+1,c+1))
        else if (a!=0 && c==0) ans.add(Pair(a+1,1))
        else if (a==0 && c!=0) ans.add(Pair(1,c+1))
        else ans.add(Pair(1,1))
    }
    
    
    val res = ans.minBy{
        it.first+it.second
    }
    
    println("${res.first} ${res.second}")
    
}