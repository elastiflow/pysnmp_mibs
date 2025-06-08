# SNMP MIB module (CISCO-MGX82XX-CARD-FEATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-MGX82XX-CARD-FEATURE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:12:02 2025
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

(cardSpecific,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cardSpecific")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoMgx82xxCardFeatureMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 74)
)
if mibBuilder.loadTexts:
    ciscoMgx82xxCardFeatureMIB.setRevisions(
        ("2003-05-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AscFeatures_ObjectIdentity = ObjectIdentity
ascFeatures = _AscFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 5)
)


class _RedundancyAllowed_Type(Integer32):
    """Custom type redundancyAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redNotAllowed", 1),
          ("redAllowed", 2))
    )


_RedundancyAllowed_Type.__name__ = "Integer32"
_RedundancyAllowed_Object = MibScalar
redundancyAllowed = _RedundancyAllowed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 5, 1),
    _RedundancyAllowed_Type()
)
redundancyAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyAllowed.setStatus("current")
_PxmFeatures_ObjectIdentity = ObjectIdentity
pxmFeatures = _PxmFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 15)
)


class _VsiControllersAllowed_Type(Integer32):
    """Custom type vsiControllersAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VsiControllersAllowed_Type.__name__ = "Integer32"
_VsiControllersAllowed_Object = MibScalar
vsiControllersAllowed = _VsiControllersAllowed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 1),
    _VsiControllersAllowed_Type()
)
vsiControllersAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsiControllersAllowed.setStatus("current")


class _ApsCardAttributes_Type(Integer32):
    """Custom type apsCardAttributes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApsCardAttributes_Type.__name__ = "Integer32"
_ApsCardAttributes_Object = MibScalar
apsCardAttributes = _ApsCardAttributes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 2),
    _ApsCardAttributes_Type()
)
apsCardAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsCardAttributes.setStatus("current")


class _TrkCACEnable_Type(Integer32):
    """Custom type trkCACEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TrkCACEnable_Type.__name__ = "Integer32"
_TrkCACEnable_Object = MibScalar
trkCACEnable = _TrkCACEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 3),
    _TrkCACEnable_Type()
)
trkCACEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkCACEnable.setStatus("current")


class _PxmCardCacMode_Type(Integer32):
    """Custom type pxmCardCacMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pcrBasedCac", 1),
          ("scrBasedCac", 2))
    )


_PxmCardCacMode_Type.__name__ = "Integer32"
_PxmCardCacMode_Object = MibScalar
pxmCardCacMode = _PxmCardCacMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 4),
    _PxmCardCacMode_Type()
)
pxmCardCacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmCardCacMode.setStatus("current")
_CoreCardCommands_ObjectIdentity = ObjectIdentity
coreCardCommands = _CoreCardCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 20)
)


class _SwitchCoreCard_Type(Integer32):
    """Custom type switchCoreCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("doswitchcc", 2),
          ("instswitchcc", 3),
          ("fallbackswitchcc", 4))
    )


_SwitchCoreCard_Type.__name__ = "Integer32"
_SwitchCoreCard_Object = MibScalar
switchCoreCard = _SwitchCoreCard_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 20, 1),
    _SwitchCoreCard_Type()
)
switchCoreCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchCoreCard.setStatus("current")
_CmCardFeatureMIBConformance_ObjectIdentity = ObjectIdentity
cmCardFeatureMIBConformance = _CmCardFeatureMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 74, 2)
)
_CmCardFeatureMIBGroups_ObjectIdentity = ObjectIdentity
cmCardFeatureMIBGroups = _CmCardFeatureMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1)
)
_CmCardFeatureMIBCompliances_ObjectIdentity = ObjectIdentity
cmCardFeatureMIBCompliances = _CmCardFeatureMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 2)
)

# Managed Objects groups

cmPxmCardFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 1)
)
cmPxmCardFeatureGroup.setObjects(
      *(("CISCO-MGX82XX-CARD-FEATURE-MIB", "vsiControllersAllowed"),
        ("CISCO-MGX82XX-CARD-FEATURE-MIB", "apsCardAttributes"),
        ("CISCO-MGX82XX-CARD-FEATURE-MIB", "trkCACEnable"),
        ("CISCO-MGX82XX-CARD-FEATURE-MIB", "pxmCardCacMode"))
)
if mibBuilder.loadTexts:
    cmPxmCardFeatureGroup.setStatus("current")

cmAscCardFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 2)
)
cmAscCardFeatureGroup.setObjects(
    ("CISCO-MGX82XX-CARD-FEATURE-MIB", "redundancyAllowed")
)
if mibBuilder.loadTexts:
    cmAscCardFeatureGroup.setStatus("current")

cmCoreCardFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 3)
)
cmCoreCardFeatureGroup.setObjects(
    ("CISCO-MGX82XX-CARD-FEATURE-MIB", "switchCoreCard")
)
if mibBuilder.loadTexts:
    cmCoreCardFeatureGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmCardFeatureCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 2, 1)
)
cmCardFeatureCompliance.setObjects(
      *(("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmPxmCardFeatureGroup"),
        ("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmAscCardFeatureGroup"),
        ("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmCoreCardFeatureGroup"))
)
if mibBuilder.loadTexts:
    cmCardFeatureCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-CARD-FEATURE-MIB",
    **{"ascFeatures": ascFeatures,
       "redundancyAllowed": redundancyAllowed,
       "pxmFeatures": pxmFeatures,
       "vsiControllersAllowed": vsiControllersAllowed,
       "apsCardAttributes": apsCardAttributes,
       "trkCACEnable": trkCACEnable,
       "pxmCardCacMode": pxmCardCacMode,
       "coreCardCommands": coreCardCommands,
       "switchCoreCard": switchCoreCard,
       "ciscoMgx82xxCardFeatureMIB": ciscoMgx82xxCardFeatureMIB,
       "cmCardFeatureMIBConformance": cmCardFeatureMIBConformance,
       "cmCardFeatureMIBGroups": cmCardFeatureMIBGroups,
       "cmPxmCardFeatureGroup": cmPxmCardFeatureGroup,
       "cmAscCardFeatureGroup": cmAscCardFeatureGroup,
       "cmCoreCardFeatureGroup": cmCoreCardFeatureGroup,
       "cmCardFeatureMIBCompliances": cmCardFeatureMIBCompliances,
       "cmCardFeatureCompliance": cmCardFeatureCompliance}
)
