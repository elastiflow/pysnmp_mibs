# SNMP MIB module (EXAML-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/applied_micro_47182/EXAML-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:25:51 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netSnmpExamples = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47182)
)
if mibBuilder.loadTexts:
    netSnmpExamples.setRevisions(
        ("2004-06-15 00:00",
         "2002-02-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetSnmpExampleScalars_ObjectIdentity = ObjectIdentity
netSnmpExampleScalars = _NetSnmpExampleScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47182, 1)
)


class _NetSnmpExampleInteger_Type(DisplayString):
    """Custom type netSnmpExampleInteger based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_NetSnmpExampleInteger_Type.__name__ = "DisplayString"
_NetSnmpExampleInteger_Object = MibScalar
netSnmpExampleInteger = _NetSnmpExampleInteger_Object(
    (1, 3, 6, 1, 4, 1, 47182, 1, 1),
    _NetSnmpExampleInteger_Type()
)
netSnmpExampleInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSnmpExampleInteger.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXAML-MIB",
    **{"netSnmpExamples": netSnmpExamples,
       "netSnmpExampleScalars": netSnmpExampleScalars,
       "netSnmpExampleInteger": netSnmpExampleInteger}
)
