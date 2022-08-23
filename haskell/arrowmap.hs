import Prelude hiding (lookup)

class MapLike m where
    empty :: m k v
    lookup :: Ord k => k -> m k v -> Maybe v
    insert :: Ord k => k -> v -> m k v -> m k v
    delete :: Ord k => k -> m k v -> m k v

    fromList :: Ord k => [(k,v)] -> m k v
    fromList [] = empty
    fromList ((k,v):xs) = insert k v (fromList xs)


newtype ArrowMap k v = ArrowMap { getArrowMap :: k -> Maybe v }


instance MapLike ArrowMap where
    empty = ArrowMap (\_ -> Nothing)

    lookup k0 (ArrowMap f) = f k0


    insert k0 v0 (ArrowMap f) = ArrowMap f'
        where
            f' = (\k -> if k == k0 then Just v0 else f k)
    
    delete k0 (ArrowMap f) = ArrowMap f'
        where
            f' = (\k -> if k == k0 then Nothing else f k) 




