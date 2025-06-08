# SNMP MIB module (BELAIR-CM-OEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-CM-OEM.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairApplications,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairApplications")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

belairCmOemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 5)
)
if mibBuilder.loadTexts:
    belairCmOemMib.setRevisions(
        ("2008-07-28 10:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairCmOemObjects_ObjectIdentity = ObjectIdentity
belairCmOemObjects = _BelairCmOemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 5, 1)
)
_BelairCmSystemReboot_Type = TruthValue
_BelairCmSystemReboot_Object = MibScalar
belairCmSystemReboot = _BelairCmSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 5, 1, 1),
    _BelairCmSystemReboot_Type()
)
belairCmSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCmSystemReboot.setStatus("current")
_BelairCmOemConformance_ObjectIdentity = ObjectIdentity
belairCmOemConformance = _BelairCmOemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 5, 3)
)

# Managed Objects groups

belairCmOemObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 6, 5, 3, 1)
)
belairCmOemObjectsGroup.setObjects(
    ("BELAIR-CM-OEM", "belairCmSystemReboot")
)
if mibBuilder.loadTexts:
    belairCmOemObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-CM-OEM",
    **{"belairCmOemMib": belairCmOemMib,
       "belairCmOemObjects": belairCmOemObjects,
       "belairCmSystemReboot": belairCmSystemReboot,
       "belairCmOemConformance": belairCmOemConformance,
       "belairCmOemObjectsGroup": belairCmOemObjectsGroup}
)
