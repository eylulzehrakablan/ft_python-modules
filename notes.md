# MRO (Method Resolution Order)

```python
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



# Static Type Checking and identity
## 42 Campus Analogy ======

to understand how static analyzers think, imagine walking to the security desk at the 42 campus. to enter the cluster, you must be a *human* and an active *Cadet*.

the security guard (selahattin abi a.k.a. the static analyzer) looks at you. you are clearly a human in real life (at runtime). however, you forgot your physical 42 Cadet ID card (the type annotation) at home. even thought the guard might know you, they cannot officially verify you as a cadet at that exact moment. the guard refuse you entry. the guard doesnt care about your actual physical abilities, he only care about the credentials you can present to them right now.

===========================

Static analyzers do not execute our code. instead, they read the type annotations (the 'credentials') of a variable to determine what methods are legally available. 

> **Note:** in our development workflow, we are dealing with two statuc analyzers:
1. vscode's Pylance (or pyright): this is the analyzer running live insode vscode. it reads to code as we type, highlights lines and autocomplete menus.
2. mypy: this is the standalone command-line tool we run to strictly audit our code

if a function accepts a creature: Creature, the analyzer only grants access to Creature methods like .attack(). it strictly forbids calling .transform(). even if the underlying object at runtime possesses that capability.

if we attempt to overwrite the variable's type using typing.cast():
`creature = typing.cast(TransformCapability, creature)`

we effectively strip the Creature credential and replace it entirely with the TransfrmCapability credential. the analyzer will now permit .transform() but it will instantly flad .attack() as an error because it forgot the original type which was 'Creature' before.

## solution

to satisfy the static anaylzer without modifying runtime behaviour, we assign the cast to a secondary variable. this creates two distinct "credentials" that point to the exact same object in memory.

```python
class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, ex1.TransformCapability)

    def act(self, creature: Creature):
        if self.is_valid(creature):
            transformer = typing.cast(ex1.TransformCapability, creature)
            print(transformer.transform())
            print(creature.attack())
            print(transformer.revert())
```

typing.cast() performs no operations at runtime. it is erased when python executes the script.

we can prove that both variables refer to the exact same memory address using python's built-in id() function and the is operator.

```python
def act(self, creature: Creature):
        if self.is_valid(creature):
            transformer = typing.cast(ex1.TransformCapability, creature)
            
            print(creature is transformer)
            # Output: True

            print(id(creature) == id(transformer))
            # Output: Ture
```

because both variables point to the exact same physical instance, triggering transformer.transform() correctly updates the internal state (self.is_transformed = True), which creature.attack() then reads successfully on the next line.
