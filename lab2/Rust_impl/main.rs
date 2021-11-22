fn smallest_three_incremental(L: Vec<i16>) -> Vec<i16> {
  /// Finds the smalles three elements in an array using an incremental aproach
  if L.len() < 3{
    return L;
  }
  let mut ret : Vec<i16> = vec![i16::MAX,i16::MAX, i16::MAX];
  for x in L{
    if x < ret[0] {
      ret = vec![x,ret[0],ret[1]];
    }
    else if x < ret[1]{
      ret = vec![ret[0],x,ret[1]];
    }
    else if x < ret[2]{
      ret = vec![ret[0],ret[1],x];
    }
  }
  return ret;
}

fn smallest_three_divide(L:Vec<i16>) -> Veck<i16>{
  if L.len() ==1
    return L;
  
}




fn main(){
  let vec :Vec<i16> = [1,2,3,5,6,-2,-100,-5,-6].to_vec();
  println!("{:?}",smallest_three_incremental(vec));
}