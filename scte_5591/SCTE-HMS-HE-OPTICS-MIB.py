# SNMP MIB module (SCTE-HMS-HE-OPTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-OPTICS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:48 2025
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

(heOptics,) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "heOptics")

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

heOpticsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeOpticalTransmitterGroup_ObjectIdentity = ObjectIdentity
heOpticalTransmitterGroup = _HeOpticalTransmitterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    heOpticalTransmitterGroup.setStatus("current")
_HeOpticalReceiverGroup_ObjectIdentity = ObjectIdentity
heOpticalReceiverGroup = _HeOpticalReceiverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    heOpticalReceiverGroup.setStatus("current")
_HeOpticalAmplifierGroup_ObjectIdentity = ObjectIdentity
heOpticalAmplifierGroup = _HeOpticalAmplifierGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    heOpticalAmplifierGroup.setStatus("current")
_HeOpticalSwitchGroup_ObjectIdentity = ObjectIdentity
heOpticalSwitchGroup = _HeOpticalSwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4)
)
if mibBuilder.loadTexts:
    heOpticalSwitchGroup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-OPTICS-MIB",
    **{"heOpticsMib": heOpticsMib,
       "heOpticalTransmitterGroup": heOpticalTransmitterGroup,
       "heOpticalReceiverGroup": heOpticalReceiverGroup,
       "heOpticalAmplifierGroup": heOpticalAmplifierGroup,
       "heOpticalSwitchGroup": heOpticalSwitchGroup}
)
