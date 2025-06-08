# SNMP MIB module (CISCOSB-SCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-SCT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:12:47 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSctMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlSctCpuRateEnabled_Type = TruthValue
_RlSctCpuRateEnabled_Object = MibScalar
rlSctCpuRateEnabled = _RlSctCpuRateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203, 1),
    _RlSctCpuRateEnabled_Type()
)
rlSctCpuRateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSctCpuRateEnabled.setStatus("current")
_RlSctCpuRate_Type = Counter32
_RlSctCpuRate_Object = MibScalar
rlSctCpuRate = _RlSctCpuRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203, 2),
    _RlSctCpuRate_Type()
)
rlSctCpuRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSctCpuRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SCT-MIB",
    **{"rlSctMib": rlSctMib,
       "rlSctCpuRateEnabled": rlSctCpuRateEnabled,
       "rlSctCpuRate": rlSctCpuRate}
)
