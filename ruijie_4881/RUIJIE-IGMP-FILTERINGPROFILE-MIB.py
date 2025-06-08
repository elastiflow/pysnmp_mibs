# SNMP MIB module (RUIJIE-IGMP-FILTERINGPROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IGMP-FILTERINGPROFILE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:22 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieIgmpFilteringProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37)
)
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileMIB.setRevisions(
        ("2003-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieIgmpFilteringProfileMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIgmpFilteringProfileMIBObjects = _RuijieIgmpFilteringProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1)
)
_RuijieIgmpFilteringMaxProfiles_Type = Unsigned32
_RuijieIgmpFilteringMaxProfiles_Object = MibScalar
ruijieIgmpFilteringMaxProfiles = _RuijieIgmpFilteringMaxProfiles_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 1),
    _RuijieIgmpFilteringMaxProfiles_Type()
)
ruijieIgmpFilteringMaxProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpFilteringMaxProfiles.setStatus("current")
_RuijieIgmpFilteringProfileActionTable_Object = MibTable
ruijieIgmpFilteringProfileActionTable = _RuijieIgmpFilteringProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileActionTable.setStatus("current")
_RuijieIgmpFilteringProfileActionEntry_Object = MibTableRow
ruijieIgmpFilteringProfileActionEntry = _RuijieIgmpFilteringProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2, 1)
)
ruijieIgmpFilteringProfileActionEntry.setIndexNames(
    (0, "RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfileIndex"),
)
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileActionEntry.setStatus("current")
_RuijieIgmpFilteringProfileIndex_Type = Unsigned32
_RuijieIgmpFilteringProfileIndex_Object = MibTableColumn
ruijieIgmpFilteringProfileIndex = _RuijieIgmpFilteringProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2, 1, 1),
    _RuijieIgmpFilteringProfileIndex_Type()
)
ruijieIgmpFilteringProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileIndex.setStatus("current")


class _RuijieIgmpFilteringProfileAction_Type(Integer32):
    """Custom type ruijieIgmpFilteringProfileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RuijieIgmpFilteringProfileAction_Type.__name__ = "Integer32"
_RuijieIgmpFilteringProfileAction_Object = MibTableColumn
ruijieIgmpFilteringProfileAction = _RuijieIgmpFilteringProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2, 1, 2),
    _RuijieIgmpFilteringProfileAction_Type()
)
ruijieIgmpFilteringProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileAction.setStatus("current")


class _RuijieIgmpFilteringProfileStatus_Type(Integer32):
    """Custom type ruijieIgmpFilteringProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RuijieIgmpFilteringProfileStatus_Type.__name__ = "Integer32"
_RuijieIgmpFilteringProfileStatus_Object = MibTableColumn
ruijieIgmpFilteringProfileStatus = _RuijieIgmpFilteringProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2, 1, 3),
    _RuijieIgmpFilteringProfileStatus_Type()
)
ruijieIgmpFilteringProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileStatus.setStatus("current")
_RuijieIgmpFilteringProfileRangeTable_Object = MibTable
ruijieIgmpFilteringProfileRangeTable = _RuijieIgmpFilteringProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileRangeTable.setStatus("current")
_RuijieIgmpFilteringProfileRangeEntry_Object = MibTableRow
ruijieIgmpFilteringProfileRangeEntry = _RuijieIgmpFilteringProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1)
)
ruijieIgmpFilteringProfileRangeEntry.setIndexNames(
    (0, "RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfileRangeIndex"),
    (0, "RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfieRangeRuijieAddress"),
)
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileRangeEntry.setStatus("current")
_RuijieIgmpFilteringProfileRangeIndex_Type = Unsigned32
_RuijieIgmpFilteringProfileRangeIndex_Object = MibTableColumn
ruijieIgmpFilteringProfileRangeIndex = _RuijieIgmpFilteringProfileRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1, 1),
    _RuijieIgmpFilteringProfileRangeIndex_Type()
)
ruijieIgmpFilteringProfileRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileRangeIndex.setStatus("current")
_RuijieIgmpFilteringProfieRangeRuijieAddress_Type = IpAddress
_RuijieIgmpFilteringProfieRangeRuijieAddress_Object = MibTableColumn
ruijieIgmpFilteringProfieRangeRuijieAddress = _RuijieIgmpFilteringProfieRangeRuijieAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1, 2),
    _RuijieIgmpFilteringProfieRangeRuijieAddress_Type()
)
ruijieIgmpFilteringProfieRangeRuijieAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfieRangeRuijieAddress.setStatus("current")
_RuijieIgmpFilteringProfieRangeEndAddress_Type = IpAddress
_RuijieIgmpFilteringProfieRangeEndAddress_Object = MibTableColumn
ruijieIgmpFilteringProfieRangeEndAddress = _RuijieIgmpFilteringProfieRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1, 3),
    _RuijieIgmpFilteringProfieRangeEndAddress_Type()
)
ruijieIgmpFilteringProfieRangeEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfieRangeEndAddress.setStatus("current")
_RuijieIgmpFilteringProfileRangeStatus_Type = RowStatus
_RuijieIgmpFilteringProfileRangeStatus_Object = MibTableColumn
ruijieIgmpFilteringProfileRangeStatus = _RuijieIgmpFilteringProfileRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1, 4),
    _RuijieIgmpFilteringProfileRangeStatus_Type()
)
ruijieIgmpFilteringProfileRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileRangeStatus.setStatus("current")
_RuijieIgmpFilteringProfileMIBConformance_ObjectIdentity = ObjectIdentity
ruijieIgmpFilteringProfileMIBConformance = _RuijieIgmpFilteringProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2)
)
_RuijieIgmpFilteringProfileMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieIgmpFilteringProfileMIBCompliances = _RuijieIgmpFilteringProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2, 1)
)
_RuijieIgmpFilteringProfileMIBGroups_ObjectIdentity = ObjectIdentity
ruijieIgmpFilteringProfileMIBGroups = _RuijieIgmpFilteringProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2, 2)
)

# Managed Objects groups

ruijieIgmpFilteringProfileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2, 2, 1)
)
ruijieIgmpFilteringProfileMIBGroup.setObjects(
      *(("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringMaxProfiles"),
        ("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfileIndex"),
        ("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfileAction"),
        ("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfileStatus"),
        ("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfileRangeIndex"),
        ("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfieRangeRuijieAddress"),
        ("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfieRangeEndAddress"),
        ("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfileRangeStatus"))
)
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieIgmpFilteringProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2, 1, 1)
)
ruijieIgmpFilteringProfileMIBCompliance.setObjects(
    ("RUIJIE-IGMP-FILTERINGPROFILE-MIB", "ruijieIgmpFilteringProfileMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieIgmpFilteringProfileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IGMP-FILTERINGPROFILE-MIB",
    **{"ruijieIgmpFilteringProfileMIB": ruijieIgmpFilteringProfileMIB,
       "ruijieIgmpFilteringProfileMIBObjects": ruijieIgmpFilteringProfileMIBObjects,
       "ruijieIgmpFilteringMaxProfiles": ruijieIgmpFilteringMaxProfiles,
       "ruijieIgmpFilteringProfileActionTable": ruijieIgmpFilteringProfileActionTable,
       "ruijieIgmpFilteringProfileActionEntry": ruijieIgmpFilteringProfileActionEntry,
       "ruijieIgmpFilteringProfileIndex": ruijieIgmpFilteringProfileIndex,
       "ruijieIgmpFilteringProfileAction": ruijieIgmpFilteringProfileAction,
       "ruijieIgmpFilteringProfileStatus": ruijieIgmpFilteringProfileStatus,
       "ruijieIgmpFilteringProfileRangeTable": ruijieIgmpFilteringProfileRangeTable,
       "ruijieIgmpFilteringProfileRangeEntry": ruijieIgmpFilteringProfileRangeEntry,
       "ruijieIgmpFilteringProfileRangeIndex": ruijieIgmpFilteringProfileRangeIndex,
       "ruijieIgmpFilteringProfieRangeRuijieAddress": ruijieIgmpFilteringProfieRangeRuijieAddress,
       "ruijieIgmpFilteringProfieRangeEndAddress": ruijieIgmpFilteringProfieRangeEndAddress,
       "ruijieIgmpFilteringProfileRangeStatus": ruijieIgmpFilteringProfileRangeStatus,
       "ruijieIgmpFilteringProfileMIBConformance": ruijieIgmpFilteringProfileMIBConformance,
       "ruijieIgmpFilteringProfileMIBCompliances": ruijieIgmpFilteringProfileMIBCompliances,
       "ruijieIgmpFilteringProfileMIBCompliance": ruijieIgmpFilteringProfileMIBCompliance,
       "ruijieIgmpFilteringProfileMIBGroups": ruijieIgmpFilteringProfileMIBGroups,
       "ruijieIgmpFilteringProfileMIBGroup": ruijieIgmpFilteringProfileMIBGroup}
)
