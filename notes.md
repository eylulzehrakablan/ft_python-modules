# MRO (Method Resolution Order)

```
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, name="Shiftling",  creature_type="Normal")
        TransformCapability.__init__(self)

```

when we use super().__init__() with multiple inheritance, python follwos a complex path called mro. if parent classes don't also use super(), the chain breaks and the second parent't __init__ might be skipped.

by explicitly writing TransformCapabilty.__init__(self) after Creature.__init__(self, ...), we guarantee that self.is_transformed = False gets created successfully.