import Data.List


revRange :: (Char,Char) -> [Char]
revRange (a, b) = unfoldr (\x -> if x < a then Nothing else Just (x, pred x)) b
