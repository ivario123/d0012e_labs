fn smallest_three_incremental(L: Vec<i16>) -> Vec<i16> {
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

fn smallest_three_divide(L:Vec<i16>) -> Vec<i16>{
  let len = L.len() as i16;
  if L.len() <=1{
    return L;
  }
  let mut mid : i16 = len/2 as i16;
  let mut left : Vec<i16> = smallest_three_divide(L[0..mid]);
  let mut right : Vec<i16> = smallest_three_divide(L[mid..L.len]);
  let max_value : i16 =  if len > 3 {3} else { len};
  let mut ret = Vec![];
  for i in 0..max_value{
    if left.len() == 0{
      while ret.len() < max_value{
        ret.append(right[0]);
        right.erase(right.begin());
      }
      return ret;
    }
    else if right.len() == 0{
      while ret.len() < max_value{
        ret.append(left[0]);
        left.erase(left.begin());
      }
      return ret;

    }
    if left[0]<right[0]{
       ret.append(left[0]);
       left.erase(left.begin());
    }
    else{
      ret.append(right[0]);
      right.erase(right.begin());
    }
  }  
  return ret;
}




fn main(){
  let vec :Vec<i16> = [1,2,3,5,6,-2,-100,-5,-6].to_vec();
  println!("{:?}",smallest_three_incremental(vec));
  println!("{:?}",smallest_three_divide(vec));
}