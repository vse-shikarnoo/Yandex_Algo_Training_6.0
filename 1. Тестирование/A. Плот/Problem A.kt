fun main(){
    
    //x1,y1,x2,y2,x,y
    val params = mutableListOf<Int>()
    
    for(i in 0 until 6){
        params.add(readLine()!!.toInt())
    }
    //println(params)
    
    val ch = checkHorizontal(params[4],params[0],params[2])
    val cv = checkVertical(params[5],params[1],params[3])
    
    //println("$ch $cv")
    
    var res=""
    
    when{
        ch==0 && cv==0 -> res="SW"
        ch==0 && cv==1 -> res="W"
        ch==0 && cv==2 -> res="NW"
        ch==1 && cv==0 -> res="S"
        ch==1 && cv==2 -> res="N"
        ch==2 && cv==0 -> res="SE"
        ch==2 && cv==1 -> res="E"
        ch==2 && cv==2 -> res="NE"
        else -> res = "ERROR"
    }
    println(res)
}


//0 1 2
fun checkHorizontal(x:Int,x1:Int,x2:Int):Int{
    //println("x=$x x1=$x1 x2=$x2")
    if(x<=x1) return 0
    if(x>=x2) return 2

    return 1
}

//2
//1
//0

fun checkVertical(y:Int,y1:Int,y2:Int):Int{
    //println("y=$y y1=$y1 y2=$y2")
    if(y<=y1) return 0
    if(y>=y2) return 2

    return 1
}