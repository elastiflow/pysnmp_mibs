# SNMP MIB module (JUNIPER-CHASSIS-FWDD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-CHASSIS-FWDD-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:48:42 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxFwdd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxFwddProcess_ObjectIdentity = ObjectIdentity
jnxFwddProcess = _JnxFwddProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 34, 1)
)
_JnxFwddMicroKernelCPUUsage_Type = Gauge32
_JnxFwddMicroKernelCPUUsage_Object = MibScalar
jnxFwddMicroKernelCPUUsage = _JnxFwddMicroKernelCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 1),
    _JnxFwddMicroKernelCPUUsage_Type()
)
jnxFwddMicroKernelCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFwddMicroKernelCPUUsage.setStatus("current")
_JnxFwddRtThreadsCPUUsage_Type = Gauge32
_JnxFwddRtThreadsCPUUsage_Object = MibScalar
jnxFwddRtThreadsCPUUsage = _JnxFwddRtThreadsCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 2),
    _JnxFwddRtThreadsCPUUsage_Type()
)
jnxFwddRtThreadsCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFwddRtThreadsCPUUsage.setStatus("current")
_JnxFwddHeapUsage_Type = Gauge32
_JnxFwddHeapUsage_Object = MibScalar
jnxFwddHeapUsage = _JnxFwddHeapUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 3),
    _JnxFwddHeapUsage_Type()
)
jnxFwddHeapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFwddHeapUsage.setStatus("current")
_JnxFwddDmaMemUsage_Type = Gauge32
_JnxFwddDmaMemUsage_Object = MibScalar
jnxFwddDmaMemUsage = _JnxFwddDmaMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 4),
    _JnxFwddDmaMemUsage_Type()
)
jnxFwddDmaMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFwddDmaMemUsage.setStatus("current")
_JnxFwddUpTime_Type = Integer32
_JnxFwddUpTime_Object = MibScalar
jnxFwddUpTime = _JnxFwddUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 5),
    _JnxFwddUpTime_Type()
)
jnxFwddUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFwddUpTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxFwddUpTime.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-CHASSIS-FWDD-MIB",
    **{"jnxFwdd": jnxFwdd,
       "jnxFwddProcess": jnxFwddProcess,
       "jnxFwddMicroKernelCPUUsage": jnxFwddMicroKernelCPUUsage,
       "jnxFwddRtThreadsCPUUsage": jnxFwddRtThreadsCPUUsage,
       "jnxFwddHeapUsage": jnxFwddHeapUsage,
       "jnxFwddDmaMemUsage": jnxFwddDmaMemUsage,
       "jnxFwddUpTime": jnxFwddUpTime}
)
