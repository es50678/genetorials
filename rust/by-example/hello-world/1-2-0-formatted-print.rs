fn main() {
    // fmt_print();
    // debug();
}

fn fmt_print() { // https://doc.rust-lang.org/stable/rust-by-example/hello/print.html
    println!("{} days", 31); // by default, 31 is inferred as i32
    // specifying type requires a suffix, quite ugly
    println!("{} days", 31i16);

    // positional args
    println!("{0}, {1}, {1}, {0}", "alice", "bob");

    // named args
    println!("{subject} {verb} {object}", object = "the dog", subject = "the brown fox", verb = "jumps over");

    // special formatting
    println!("{} of {:b} people k now binary, the other half doesn't", 1, 2);

    // formatting with padding
    println!("{number:>width$}", number = 1, width = 6);
    println!("{number:>0width$}", number = 1, width = 6); // padding with 0s

    println!("My name is {0}, {1} {0}", "Bond", "James");

    let pi = 3.141592;

    println!("Pi is roughly {:.3}", pi); // https://doc.rust-lang.org/std/fmt/
}

fn debug() { // https://doc.rust-lang.org/stable/rust-by-example/hello/print/print_debug.html
    #[derive(Debug)]
    struct DebugPrintable(i32);

    #[derive(Debug)]
    struct Deep(DebugPrintable);

    // struct Unprintable(i32);
    // #[derive(Debug)]
    // struct DeepTest(Unprintable); // will throw compiler error bc Unprintable doesn't derive from Debug

    println!("{:?} months in a year", 12);

    println!("{1:?} {0:?} is the {actor:?} name", "Slater", "Christian", actor = "actor's");

    println!("Now {:?} will print", DebugPrintable(332));

    // deriving debug doesn't allow controlling how the results look
    println!("Now {:?} will print", Deep(DebugPrintable(7)));
    // --> Now Deep(DebugPrintable(7)) will print
    // this is a problem if you want it formatted in a certain way

    #[derive(Debug)]
    struct Person<'a> {
        name: &'a str,
        age: u8,
    }

    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Pretty print, you still need to derive Debug for this
    println!("{:#?}", Deep(DebugPrintable(7)));
    println!("{:#?}", peter);
}
