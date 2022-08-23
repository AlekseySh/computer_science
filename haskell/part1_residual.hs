helper n prev_prev prev acc
    | n <= 2    = acc
    | otherwise = helper (n - 1) prev acc (acc + prev - 2 * prev_prev) 


seqA :: Integer -> Integer
seqA 0 = 1
seqA 1 = 2
seqA 2 = 3
seqA n = helper n 1 2 3


data Odd = Odd Integer deriving (Eq, Show)

instance Enum Odd where
  succ (Odd x) = Odd $ x + 2
  pred (Odd x) = Odd $ x - 2
  toEnum x = Odd $ toInteger x * 2 + 1
  fromEnum (Odd x) = quot (fromInteger x - 1) 2
  enumFrom = iterate succ
  enumFromThen (Odd x) (Odd y) = map Odd [x, y ..]
  enumFromTo (Odd x) (Odd y) = map Odd [x, x + 2 .. y]
  enumFromThenTo (Odd x) (Odd y) (Odd z) = map Odd [x , y .. z]


newtype Maybe' a = Maybe' { getMaybe :: Maybe a } deriving (Eq,Show)

instance Monoid a => Monoid (Maybe' a) where
    mempty = Maybe' $ Just mempty
    mappend _ (Maybe' (Nothing)) = Maybe' $ Nothing
    mappend (Maybe' (Nothing)) _ = Maybe' $ Nothing
    mappend (Maybe' x) (Maybe' y) = Maybe' $ mappend x y
    