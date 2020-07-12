export function ExecutionTimeLogger() {
    return function decorator(target: any, functionName: string, descriptor: PropertyDescriptor) {
        const baseFunction = descriptor.value;
        if (typeof baseFunction === 'function') {
            descriptor.value = function (...args) {
                try {
                    let start = new Date();
                    const result: any = baseFunction.apply(this, args);
                    return Promise.resolve(result).then(val => {
                        let end = new Date()
                        let executionTime: number = end.getTime() - start.getTime();
                        console.log(`${target.name} - ${functionName} execution time: ${executionTime}ms`)
                        return val
                    });
                } catch (e) {
                    console.log(`Error: ${e}`);
                    throw e;
                }
            }
        }
        return descriptor;
    }
}