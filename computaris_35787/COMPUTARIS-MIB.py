# SNMP MIB module (COMPUTARIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/computaris_35787/COMPUTARIS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:02:15 2025
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

ctsRegMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35787)
)
if mibBuilder.loadTexts:
    ctsRegMIB.setRevisions(
        ("2013-09-25 07:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtsObjects_ObjectIdentity = ObjectIdentity
ctsObjects = _CtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 1)
)
_CtsEvents_ObjectIdentity = ObjectIdentity
ctsEvents = _CtsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 2)
)
_CtsConf_ObjectIdentity = ObjectIdentity
ctsConf = _CtsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 3)
)
_CtsGroups_ObjectIdentity = ObjectIdentity
ctsGroups = _CtsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 3, 1)
)
_CtsCompls_ObjectIdentity = ObjectIdentity
ctsCompls = _CtsCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35787, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMPUTARIS-MIB",
    **{"ctsRegMIB": ctsRegMIB,
       "ctsObjects": ctsObjects,
       "ctsEvents": ctsEvents,
       "ctsConf": ctsConf,
       "ctsGroups": ctsGroups,
       "ctsCompls": ctsCompls}
)
