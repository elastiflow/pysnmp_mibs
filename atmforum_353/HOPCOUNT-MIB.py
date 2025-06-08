# SNMP MIB module (HOPCOUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/HOPCOUNT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:04:44 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atmfHopCountMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1)
)
if mibBuilder.loadTexts:
    atmfHopCountMIB.setRevisions(
        ("2001-11-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfSignalling_ObjectIdentity = ObjectIdentity
atmfSignalling = _AtmfSignalling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9)
)
_AtmfHopCount_ObjectIdentity = ObjectIdentity
atmfHopCount = _AtmfHopCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4)
)
_HopCountMIBObjects_ObjectIdentity = ObjectIdentity
hopCountMIBObjects = _HopCountMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 1)
)


class _AtmSwHopCountGen_Type(TruthValue):
    """Custom type atmSwHopCountGen based on TruthValue"""
    defaultValue = 1


_AtmSwHopCountGen_Type.__name__ = "TruthValue"
_AtmSwHopCountGen_Object = MibScalar
atmSwHopCountGen = _AtmSwHopCountGen_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 1, 1),
    _AtmSwHopCountGen_Type()
)
atmSwHopCountGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwHopCountGen.setStatus("current")


class _AtmSwHopCountMax_Type(Integer32):
    """Custom type atmSwHopCountMax based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmSwHopCountMax_Type.__name__ = "Integer32"
_AtmSwHopCountMax_Object = MibScalar
atmSwHopCountMax = _AtmSwHopCountMax_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 1, 2),
    _AtmSwHopCountMax_Type()
)
atmSwHopCountMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSwHopCountMax.setStatus("current")
_AtmIfHopCountGenTable_Object = MibTable
atmIfHopCountGenTable = _AtmIfHopCountGenTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmIfHopCountGenTable.setStatus("current")
_AtmIfHopCountGenEntry_Object = MibTableRow
atmIfHopCountGenEntry = _AtmIfHopCountGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 1, 3, 1)
)
atmIfHopCountGenEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmIfHopCountGenEntry.setStatus("current")


class _AtmIfHopCountGen_Type(TruthValue):
    """Custom type atmIfHopCountGen based on TruthValue"""
    defaultValue = 1


_AtmIfHopCountGen_Type.__name__ = "TruthValue"
_AtmIfHopCountGen_Object = MibTableColumn
atmIfHopCountGen = _AtmIfHopCountGen_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 1, 3, 1, 1),
    _AtmIfHopCountGen_Type()
)
atmIfHopCountGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfHopCountGen.setStatus("current")
_HopCountMIBConformance_ObjectIdentity = ObjectIdentity
hopCountMIBConformance = _HopCountMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 2)
)
_HopCountMIBCompliances_ObjectIdentity = ObjectIdentity
hopCountMIBCompliances = _HopCountMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 2, 1)
)
_HopCountMIBGroups_ObjectIdentity = ObjectIdentity
hopCountMIBGroups = _HopCountMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 2, 2)
)

# Managed Objects groups

hopCountSwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 2, 2, 1)
)
hopCountSwGroup.setObjects(
      *(("HOPCOUNT-MIB", "atmSwHopCountGen"),
        ("HOPCOUNT-MIB", "atmSwHopCountMax"))
)
if mibBuilder.loadTexts:
    hopCountSwGroup.setStatus("current")

hopCountIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 2, 2, 2)
)
hopCountIfGroup.setObjects(
    ("HOPCOUNT-MIB", "atmIfHopCountGen")
)
if mibBuilder.loadTexts:
    hopCountIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hopCountMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 4, 1, 2, 1, 1)
)
hopCountMIBCompliance.setObjects(
      *(("HOPCOUNT-MIB", "hopCountSwGroup"),
        ("HOPCOUNT-MIB", "hopCountIfGroup"))
)
if mibBuilder.loadTexts:
    hopCountMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HOPCOUNT-MIB",
    **{"atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfSignalling": atmfSignalling,
       "atmfHopCount": atmfHopCount,
       "atmfHopCountMIB": atmfHopCountMIB,
       "hopCountMIBObjects": hopCountMIBObjects,
       "atmSwHopCountGen": atmSwHopCountGen,
       "atmSwHopCountMax": atmSwHopCountMax,
       "atmIfHopCountGenTable": atmIfHopCountGenTable,
       "atmIfHopCountGenEntry": atmIfHopCountGenEntry,
       "atmIfHopCountGen": atmIfHopCountGen,
       "hopCountMIBConformance": hopCountMIBConformance,
       "hopCountMIBCompliances": hopCountMIBCompliances,
       "hopCountMIBCompliance": hopCountMIBCompliance,
       "hopCountMIBGroups": hopCountMIBGroups,
       "hopCountSwGroup": hopCountSwGroup,
       "hopCountIfGroup": hopCountIfGroup}
)
