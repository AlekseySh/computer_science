module Demo where

doubleFact :: Integer -> Integer
doubleFact 0 = 1
doubleFact 1 = 1
doubleFact n = n * doubleFact (n - 2)


fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)


helper n prev acc
    | n <= 0    = acc
    | otherwise = helper (n - 1) acc (prev + acc)


fib2 :: Integer -> Integer
fib2 0 = 0
fib2 1 = 1
fib2 n = helper n 1 0



fibonacci :: Integer -> Integer
fibonacci n
    | n >= 0 = fib2 n
    | n < 0 = ((-1) ^ (1 - n)) * fib2 (-n)


class Printable a where
    toString :: a -> [Char]


instance Printable Bool where
    toString True = "true"
    toString False = "false"


instance Printable () where
    toString () = "unit type"

instance (Printable a, Printable b) => Printable (a, b) where
    toString (a, b) = "(" ++ (toString a) ++ "," ++ (toString b) ++ ")"


class KnownToGork a where
    stomp :: a -> a
    doesEnrageGork :: a -> Bool

class KnownToMork a where
    stab :: a -> a
    doesEnrageMork :: a -> Bool

class (KnownToGork a, KnownToMork a) => KnownToGorkAndMork a where
    stompOrStab :: a -> a
    stompOrStab x
        | doesEnrageMork x && doesEnrageGork x = stomp $ stab x
        | doesEnrageMork x = stomp x
        | doesEnrageGork x = stab x
        | otherwise = x




class (Eq a, Enum a, Bounded a) => SafeEnum a where
    ssucc :: a -> a
    ssucc x = if x == maxBound then minBound else succ x

    spred :: a -> a
    spred x = if x == minBound then maxBound else pred x


nTimes:: a -> Int -> [a]
nTimes x n
    | n <= 0 = []
    | otherwise = x : nTimes x (n - 1)


oddsOnly :: Integral a => [a] -> [a]
oddsOnly [] = []
oddsOnly (x:xs)
    | odd x = x : oddsOnly xs
    | otherwise = oddsOnly xs


sum2 :: Num a => [a] -> [a] -> [a]
sum2 x          []    = x
sum2 []         x     = x
sum2 (a:as) (b:bs)    = (a + b) : sum2 as bs

sum3 :: Num a => [a] -> [a] -> [a] -> [a]
sum3 x y z = sum2 x $ sum2 y z


groupElems :: Eq a => [a] -> [[a]]
groupElems [] = []
groupElems (x: xs) = group : groupElems residual
    where
        s = span (== x) xs
        group = x : fst s
        residual = snd s
        

filterDisj :: (a -> Bool) -> (a -> Bool) -> [a] -> [a]
filterDisj p1 p2 x = filter p12 x
    where
        p12 y = or [p1 y, p2 y]


qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort x = qsort (filter (< x0) x) ++ (filter (== x0) x) ++ qsort (filter (> x0) x) 
    where x0 = head x


squares'n'cubes :: Num a => [a] -> [a]
squares'n'cubes = concat . map (\x -> [x^2, x^3])


perms :: [a] -> [[a]]
perms [] = [[]]
perms (x:xs) = concatMap (insertAll x) (perms xs)


insertAll :: a -> [a] -> [[a]]
insertAll x xs = map ins $ zip [0..n] $ nTimes' xs n
    where
        n = 1 + length xs
        ins pair = insertAt x (fst pair) (snd pair)


nTimes' :: a -> Int -> [a]
nTimes' x 0 = []
nTimes' x 1 = [x]
nTimes' x n = x : nTimes' x (n - 1)


insertAt :: a -> Int -> [a] -> [a]
insertAt x i xs = left ++ [x] ++ right
    where
        (left, right) = splitAt i xs




coins :: (Num a) => [a]
coins = [3, 8]

change 0 = [[]]
change s = [x:xs | x <- coins, s - x >= 0, xs <- change(s -x)]




meanList :: [Double] -> Double
meanList = mean_func . foldr (\x (s,n) -> (s + x, n + 1)) (0, 0)
    where
        mean_func (s,n)
            | n > 0   = s / n
            | n == 0  = 0


integration :: (Double -> Double) -> Double -> Double -> Double
integration f a b = step * ((f a + f b) / 2 + accfunc (n - 1))
    where
        n = 1000
        step = (b - a) / n
        accfunc 0 = 0
        accfunc n = accfunc (n - 1) + f (a + n * step)


integration' :: (Double -> Double) -> Double -> Double -> Double
integration' f a b = step * (bounds + (sum $ map f grid))
    where
        bounds = (f a + f b) / 2
        grid = [a + step, a + 2 * step .. (b - step)]
        step = (b - a) / 100



data LogLevel = Error | Warning | Info

cmp :: LogLevel -> LogLevel -> Ordering
cmp Error Error = EQ
cmp Warning Warning = EQ
cmp Info Info = EQ
cmp Error _ = GT
cmp Info _ = LT
cmp Warning Error = LT
cmp Warning Info = GT



data Result = Fail | Success

doSomeWork:: a -> (Result, Int)
doSomeWork _     = (Fail, 10)

processData :: a -> String
processData x = let (r, i) = doSomeWork x
    in case r of
        Success -> "Success"
        Fail -> "Fail: " ++ show i




data Coord a = Coord a a deriving Show

distance :: Coord Double -> Coord Double -> Double
distance (Coord x y) (Coord x' y') = sqrt $ (x - x')^2 + (y - y')^2

manhDistance :: Coord Int -> Coord Int -> Int
manhDistance (Coord x y) (Coord x' y') = abs (x - x') + abs (y - y')



getCenter :: Double -> Coord Int -> Coord Double
getCenter d (Coord x y) = Coord (convert x) (convert y)
    where
        convert z =  d / 2 + d * toEnum z


getCell :: Double -> Coord Double -> Coord Int
getCell d (Coord x y) = Coord (convert x) (convert y)
    where
        convert z = round $ (z - d / 2) / d





data List a = Nil | Cons a (List a) deriving Show

fromList :: List a -> [a]
fromList Nil = []
fromList (Cons x xs) = x : fromList xs

toList :: [a] -> List a
toList [] = Nil
toList (x:xs) = Cons x (toList xs)




data Nat = Zero | Suc Nat deriving Show

fromNat :: Nat -> Integer
fromNat Zero = 0
fromNat (Suc n) = 1 + fromNat n

add :: Nat -> Nat -> Nat
add Zero    Zero = Zero
add Zero    a    = a
add a       Zero = a
add (Suc a) b    = Suc (add a b)

{-
a * b = b + (a - 1) * b
-}
mul :: Nat -> Nat -> Nat
mul Zero    _    = Zero
mul _       Zero = Zero
mul (Suc a) b    = b `add` (mul a b)

{-
a! = (a - 1)! * a   
-}
fac :: Nat -> Nat
fac Zero    = Suc Zero
fac (Suc a) = (fac a) `mul` (Suc a)



data Tree a = Leaf a | Node (Tree a) (Tree a)

height :: Tree a -> Int
height (Leaf _)     = 0
height (Node lt rt) = 1 + max (height lt) (height rt)

size :: Tree a -> Int
size (Leaf _ )    = 1
size (Node lt rt) = 1 + (size lt) + (size rt)  

avg :: Tree Int -> Int
avg t =
    let (c,s) = go t
    in s `div` c
  where
    go :: Tree Int -> (Int,Int)
    go (Leaf x)     = (1, x)
    go (Node lt rt) = (cl + cr, sl + sr)
        where
            (cl, sl) = go lt
            (cr, sr) = go rt








