# SNMP MIB module (ARUBAWIRED-PORTVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hpe_47196/ARUBAWIRED-PORTVLAN-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 22:01:36 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

arubaWiredPortVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18)
)
if mibBuilder.loadTexts:
    arubaWiredPortVlanMIB.setRevisions(
        ("2021-10-14 00:00",
         "2020-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VidList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixedLength = 512



# MIB Managed Objects in the order of their OIDs

_ArubaWiredPortVlanNotifications_ObjectIdentity = ObjectIdentity
arubaWiredPortVlanNotifications = _ArubaWiredPortVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 0)
)
_ArubaWiredPortVlanObjects_ObjectIdentity = ObjectIdentity
arubaWiredPortVlanObjects = _ArubaWiredPortVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1)
)
_ArubaWiredPortVlanConfig_ObjectIdentity = ObjectIdentity
arubaWiredPortVlanConfig = _ArubaWiredPortVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 0)
)
_ArubaWiredPortVlanStatus_ObjectIdentity = ObjectIdentity
arubaWiredPortVlanStatus = _ArubaWiredPortVlanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1)
)
_ArubaWiredPortVlanMemberTable_Object = MibTable
arubaWiredPortVlanMemberTable = _ArubaWiredPortVlanMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPortVlanMemberTable.setStatus("current")
_ArubaWiredPortVlanMemberEntry_Object = MibTableRow
arubaWiredPortVlanMemberEntry = _ArubaWiredPortVlanMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1, 1)
)
arubaWiredPortVlanMemberEntry.setIndexNames(
    (0, "ARUBAWIRED-PORTVLAN-MIB", "arubaWiredPortVlanMemberIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredPortVlanMemberEntry.setStatus("current")
_ArubaWiredPortVlanMemberIndex_Type = InterfaceIndex
_ArubaWiredPortVlanMemberIndex_Object = MibTableColumn
arubaWiredPortVlanMemberIndex = _ArubaWiredPortVlanMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1, 1, 1),
    _ArubaWiredPortVlanMemberIndex_Type()
)
arubaWiredPortVlanMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPortVlanMemberIndex.setStatus("current")


class _ArubaWiredPortVlanMemberMode_Type(Integer32):
    """Custom type arubaWiredPortVlanMemberMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trunk", 1),
          ("access", 2))
    )


_ArubaWiredPortVlanMemberMode_Type.__name__ = "Integer32"
_ArubaWiredPortVlanMemberMode_Object = MibTableColumn
arubaWiredPortVlanMemberMode = _ArubaWiredPortVlanMemberMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1, 1, 2),
    _ArubaWiredPortVlanMemberMode_Type()
)
arubaWiredPortVlanMemberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPortVlanMemberMode.setStatus("current")
_ArubaWiredPortVlanMemberVid_Type = VidList
_ArubaWiredPortVlanMemberVid_Object = MibTableColumn
arubaWiredPortVlanMemberVid = _ArubaWiredPortVlanMemberVid_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 1, 1, 1, 1, 3),
    _ArubaWiredPortVlanMemberVid_Type()
)
arubaWiredPortVlanMemberVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPortVlanMemberVid.setStatus("current")
_ArubaWiredPortVlanConformance_ObjectIdentity = ObjectIdentity
arubaWiredPortVlanConformance = _ArubaWiredPortVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2)
)
_ArubaWiredPortVlanCompliances_ObjectIdentity = ObjectIdentity
arubaWiredPortVlanCompliances = _ArubaWiredPortVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2, 1)
)
_ArubaWiredPortVlanGroups_ObjectIdentity = ObjectIdentity
arubaWiredPortVlanGroups = _ArubaWiredPortVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2, 2)
)

# Managed Objects groups

arubaWiredPortVlanMemberTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2, 2, 1)
)
arubaWiredPortVlanMemberTableGroup.setObjects(
      *(("ARUBAWIRED-PORTVLAN-MIB", "arubaWiredPortVlanMemberMode"),
        ("ARUBAWIRED-PORTVLAN-MIB", "arubaWiredPortVlanMemberVid"))
)
if mibBuilder.loadTexts:
    arubaWiredPortVlanMemberTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredPortVlanMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18, 2, 1, 1)
)
arubaWiredPortVlanMibCompliance.setObjects(
    ("ARUBAWIRED-PORTVLAN-MIB", "arubaWiredPortVlanMemberTableGroup")
)
if mibBuilder.loadTexts:
    arubaWiredPortVlanMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-PORTVLAN-MIB",
    **{"VidList": VidList,
       "arubaWiredPortVlanMIB": arubaWiredPortVlanMIB,
       "arubaWiredPortVlanNotifications": arubaWiredPortVlanNotifications,
       "arubaWiredPortVlanObjects": arubaWiredPortVlanObjects,
       "arubaWiredPortVlanConfig": arubaWiredPortVlanConfig,
       "arubaWiredPortVlanStatus": arubaWiredPortVlanStatus,
       "arubaWiredPortVlanMemberTable": arubaWiredPortVlanMemberTable,
       "arubaWiredPortVlanMemberEntry": arubaWiredPortVlanMemberEntry,
       "arubaWiredPortVlanMemberIndex": arubaWiredPortVlanMemberIndex,
       "arubaWiredPortVlanMemberMode": arubaWiredPortVlanMemberMode,
       "arubaWiredPortVlanMemberVid": arubaWiredPortVlanMemberVid,
       "arubaWiredPortVlanConformance": arubaWiredPortVlanConformance,
       "arubaWiredPortVlanCompliances": arubaWiredPortVlanCompliances,
       "arubaWiredPortVlanMibCompliance": arubaWiredPortVlanMibCompliance,
       "arubaWiredPortVlanGroups": arubaWiredPortVlanGroups,
       "arubaWiredPortVlanMemberTableGroup": arubaWiredPortVlanMemberTableGroup}
)
