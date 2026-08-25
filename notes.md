# MRO (Method Resolution Order)

```
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, name="Shiftling",  creature_type="Normal")
        TransformCapability.__init__(self)

```

when we use super().__init__() with multiple inheritance, python creates a specific linear lookup chain and follows this path which is called called MRO.

We can inspect this chain in python by running (at the root of the repository): print(creatures.Shiftling.__mro__)

if parent classes don't also use super(), the chain breaks and the second parent's __init__ might be skipped.

by explicitly writing TransformCapabilty.__init__(self) after Creature.__init__(self, ...), we guarantee that self.is_transformed = False gets created successfully.

## The single inheritance scenario

if you only inherit from one class (class CadetCreature(Creature):), the MRO looks like this:

(<class '__main__.CadetCreature'>, <class 'ex0.creature.Creature'>, <class 'abc.ABC'>, <class 'object'>)
CadetCreature -> Creature -> ABC -> object

1. CadetCreature uses super().__init__() and passes the token to Creature
2. creature.__init__ runs, setting up name and creature_type.
3. Creature drop the token since it does not have a super() to call
4. The chain stops but who cares? the only things left in the chain were ABC and object. and neither of them needs to create any variables to store any data.

> The Trap
The trap only snaps shut when we have multiple inheritance and more than one parent has variables to set up (like TransformCapability needing to set self.is_transformed = False)

if one parent drops the token before the other parent gets its turn to set up its variables, the code crashes the moment we try to use those variables.

## The multiple inheritance scenario

(<class '__main__.TranscenderCreature'>, <class 'ex0.creature.Creature'>, <class 'ex1.capabilities.TransformCapability'>, <class 'abc.ABC'>, <class 'object'>)
TranscenderCreature -> Creature (Creature class doesn't have a super() the chain breaks here) -> TransformCapability -> ABC -> object
