import Prelude hiding (lookup)
import qualified Data.List as L


class MapLike m where
    empty :: m k v
    lookup :: Ord k => k -> m k v -> Maybe v
    insert :: Ord k => k -> v -> m k v -> m k v
    delete :: Ord k => k -> m k v -> m k v

    fromList :: Ord k => [(k,v)] -> m k v
    fromList [] = empty
    fromList ((k,v):xs) = insert k v (fromList xs)


newtype ListMap k v = ListMap { getListMap :: [(k,v)] }
    deriving (Eq,Show)

instance MapLike ListMap where
    empty = ListMap []

    lookup k0 (ListMap []) = Nothing
    lookup k0 (ListMap ((k,v):xs)) = if k0 == k then (Just v) else lookup k0 (ListMap xs)

    insert k0 v0 m = ListMap $ (k0, v0):(getListMap (delete k0 m))

    delete k0 (ListMap m) = ListMap $ filter (\(k, _) -> (k0 /= k)) m
