# SNMP MIB module (RUIJIE-ROUTER-WIFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ROUTER-WIFI-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieWifiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133)
)
if mibBuilder.loadTexts:
    ruijieWifiMIB.setRevisions(
        ("2014-12-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieEableType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



class RuijieWlanType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("station", 2))
    )



class RuijieIsolateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isolate", 1),
          ("noisolate", 2))
    )



class RuijieAuthenticationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("share-key", 2))
    )



class RuijieWapPskCiphersType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("tkip", 2),
          ("auto", 3))
    )



class RuijieWifiChanWidthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twenty", 1),
          ("forty", 2))
    )



class RuijieWifiSlotType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("long", 2))
    )



class RuijieWifiFreChanelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("two-point-four", 1),
          ("five", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RuijieWifiMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWifiMIBObjects = _RuijieWifiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1)
)
_RuijieWifiDot11radioSupportObjects_ObjectIdentity = ObjectIdentity
ruijieWifiDot11radioSupportObjects = _RuijieWifiDot11radioSupportObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 1)
)
_RuijieWifiDot11radioSupportTable_Object = MibTable
ruijieWifiDot11radioSupportTable = _RuijieWifiDot11radioSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWifiDot11radioSupportTable.setStatus("current")
_RuijieWifiDot11radioSupportEntry_Object = MibTableRow
ruijieWifiDot11radioSupportEntry = _RuijieWifiDot11radioSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 1, 1, 1)
)
ruijieWifiDot11radioSupportEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-WIFI-MIB", "ruijieWifiDot11radioIndex"),
)
if mibBuilder.loadTexts:
    ruijieWifiDot11radioSupportEntry.setStatus("current")
_RuijieWifiDot11radioIndex_Type = Integer32
_RuijieWifiDot11radioIndex_Object = MibTableColumn
ruijieWifiDot11radioIndex = _RuijieWifiDot11radioIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 1, 1, 1, 1),
    _RuijieWifiDot11radioIndex_Type()
)
ruijieWifiDot11radioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIndex.setStatus("current")
_RuijieWifiDot11radioApMaxCnt_Type = Integer32
_RuijieWifiDot11radioApMaxCnt_Object = MibTableColumn
ruijieWifiDot11radioApMaxCnt = _RuijieWifiDot11radioApMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 1, 1, 1, 2),
    _RuijieWifiDot11radioApMaxCnt_Type()
)
ruijieWifiDot11radioApMaxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioApMaxCnt.setStatus("current")
_RuijieWifiDot11radioStationMaxCnt_Type = Integer32
_RuijieWifiDot11radioStationMaxCnt_Object = MibTableColumn
ruijieWifiDot11radioStationMaxCnt = _RuijieWifiDot11radioStationMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 1, 1, 1, 3),
    _RuijieWifiDot11radioStationMaxCnt_Type()
)
ruijieWifiDot11radioStationMaxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioStationMaxCnt.setStatus("current")
_RuijieWifiWlanObjects_ObjectIdentity = ObjectIdentity
ruijieWifiWlanObjects = _RuijieWifiWlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2)
)
_RuijieWifiWlanIndexNext_Type = Integer32
_RuijieWifiWlanIndexNext_Object = MibScalar
ruijieWifiWlanIndexNext = _RuijieWifiWlanIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 1),
    _RuijieWifiWlanIndexNext_Type()
)
ruijieWifiWlanIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanIndexNext.setStatus("current")
_RuijieWifiVlanIndexNext_Type = Integer32
_RuijieWifiVlanIndexNext_Object = MibScalar
ruijieWifiVlanIndexNext = _RuijieWifiVlanIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 2),
    _RuijieWifiVlanIndexNext_Type()
)
ruijieWifiVlanIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiVlanIndexNext.setStatus("current")
_RuijieWifiWlanTable_Object = MibTable
ruijieWifiWlanTable = _RuijieWifiWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieWifiWlanTable.setStatus("current")
_RuijieWifiWlanEntry_Object = MibTableRow
ruijieWifiWlanEntry = _RuijieWifiWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1)
)
ruijieWifiWlanEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-WIFI-MIB", "ruijieWifiWlanIndex"),
)
if mibBuilder.loadTexts:
    ruijieWifiWlanEntry.setStatus("current")


class _RuijieWifiWlanIndex_Type(Integer32):
    """Custom type ruijieWifiWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiWlanIndex_Type.__name__ = "Integer32"
_RuijieWifiWlanIndex_Object = MibTableColumn
ruijieWifiWlanIndex = _RuijieWifiWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 1),
    _RuijieWifiWlanIndex_Type()
)
ruijieWifiWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanIndex.setStatus("current")
_RuijieWifiWlanType_Type = RuijieWlanType
_RuijieWifiWlanType_Object = MibTableColumn
ruijieWifiWlanType = _RuijieWifiWlanType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 2),
    _RuijieWifiWlanType_Type()
)
ruijieWifiWlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanType.setStatus("current")


class _RuijieWifiWlanSsidName_Type(DisplayString):
    """Custom type ruijieWifiWlanSsidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieWifiWlanSsidName_Type.__name__ = "DisplayString"
_RuijieWifiWlanSsidName_Object = MibTableColumn
ruijieWifiWlanSsidName = _RuijieWifiWlanSsidName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 3),
    _RuijieWifiWlanSsidName_Type()
)
ruijieWifiWlanSsidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanSsidName.setStatus("current")


class _RuijieWifiWlanVlanId_Type(Integer32):
    """Custom type ruijieWifiWlanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RuijieWifiWlanVlanId_Type.__name__ = "Integer32"
_RuijieWifiWlanVlanId_Object = MibTableColumn
ruijieWifiWlanVlanId = _RuijieWifiWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 4),
    _RuijieWifiWlanVlanId_Type()
)
ruijieWifiWlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanVlanId.setStatus("current")
_RuijieWifiWlanRowStatus_Type = RowStatus
_RuijieWifiWlanRowStatus_Object = MibTableColumn
ruijieWifiWlanRowStatus = _RuijieWifiWlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 5),
    _RuijieWifiWlanRowStatus_Type()
)
ruijieWifiWlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanRowStatus.setStatus("current")
_RuijieWifiWlanBroadcastSsid_Type = RuijieEableType
_RuijieWifiWlanBroadcastSsid_Object = MibTableColumn
ruijieWifiWlanBroadcastSsid = _RuijieWifiWlanBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 6),
    _RuijieWifiWlanBroadcastSsid_Type()
)
ruijieWifiWlanBroadcastSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanBroadcastSsid.setStatus("current")
_RuijieWifiWlanIsolate_Type = RuijieIsolateType
_RuijieWifiWlanIsolate_Object = MibTableColumn
ruijieWifiWlanIsolate = _RuijieWifiWlanIsolate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 7),
    _RuijieWifiWlanIsolate_Type()
)
ruijieWifiWlanIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanIsolate.setStatus("current")
_RuijieWifiWlanBssStaLimit_Type = Integer32
_RuijieWifiWlanBssStaLimit_Object = MibTableColumn
ruijieWifiWlanBssStaLimit = _RuijieWifiWlanBssStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 8),
    _RuijieWifiWlanBssStaLimit_Type()
)
ruijieWifiWlanBssStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanBssStaLimit.setStatus("current")


class _RujieWifiWlanSecurityType_Type(Bits):
    """Custom type rujieWifiWlanSecurityType based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("wep", 1),
          ("wpa-psk", 2),
          ("wpa2-psk", 3))
    )

_RujieWifiWlanSecurityType_Type.__name__ = "Bits"
_RujieWifiWlanSecurityType_Object = MibTableColumn
rujieWifiWlanSecurityType = _RujieWifiWlanSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 9),
    _RujieWifiWlanSecurityType_Type()
)
rujieWifiWlanSecurityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rujieWifiWlanSecurityType.setStatus("current")
_RuijieWifiWlanAuthenticationSetKey_Type = DisplayString
_RuijieWifiWlanAuthenticationSetKey_Object = MibTableColumn
ruijieWifiWlanAuthenticationSetKey = _RuijieWifiWlanAuthenticationSetKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 10),
    _RuijieWifiWlanAuthenticationSetKey_Type()
)
ruijieWifiWlanAuthenticationSetKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanAuthenticationSetKey.setStatus("current")
_RuijieWifiWlanWepAuthenticationType_Type = RuijieAuthenticationType
_RuijieWifiWlanWepAuthenticationType_Object = MibTableColumn
ruijieWifiWlanWepAuthenticationType = _RuijieWifiWlanWepAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 11),
    _RuijieWifiWlanWepAuthenticationType_Type()
)
ruijieWifiWlanWepAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanWepAuthenticationType.setStatus("current")
_RuijieWifiWlanWpaPskCiphersType_Type = RuijieWapPskCiphersType
_RuijieWifiWlanWpaPskCiphersType_Object = MibTableColumn
ruijieWifiWlanWpaPskCiphersType = _RuijieWifiWlanWpaPskCiphersType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 12),
    _RuijieWifiWlanWpaPskCiphersType_Type()
)
ruijieWifiWlanWpaPskCiphersType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanWpaPskCiphersType.setStatus("current")
_RuijieWifiWlanPassphrase_Type = DisplayString
_RuijieWifiWlanPassphrase_Object = MibTableColumn
ruijieWifiWlanPassphrase = _RuijieWifiWlanPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 13),
    _RuijieWifiWlanPassphrase_Type()
)
ruijieWifiWlanPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiWlanPassphrase.setStatus("current")
_RuijieWifiWlanDot11RadioIfindex_Type = Integer32
_RuijieWifiWlanDot11RadioIfindex_Object = MibTableColumn
ruijieWifiWlanDot11RadioIfindex = _RuijieWifiWlanDot11RadioIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 14),
    _RuijieWifiWlanDot11RadioIfindex_Type()
)
ruijieWifiWlanDot11RadioIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanDot11RadioIfindex.setStatus("current")
_RuijieWifiWlanDot11RadioSubIfindex_Type = Integer32
_RuijieWifiWlanDot11RadioSubIfindex_Object = MibTableColumn
ruijieWifiWlanDot11RadioSubIfindex = _RuijieWifiWlanDot11RadioSubIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 2, 3, 1, 15),
    _RuijieWifiWlanDot11RadioSubIfindex_Type()
)
ruijieWifiWlanDot11RadioSubIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanDot11RadioSubIfindex.setStatus("current")
_RuijieWifiDot11radioIfConfigObjects_ObjectIdentity = ObjectIdentity
ruijieWifiDot11radioIfConfigObjects = _RuijieWifiDot11radioIfConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3)
)
_RuijieWifiDot11radioIfConfigTable_Object = MibTable
ruijieWifiDot11radioIfConfigTable = _RuijieWifiDot11radioIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigTable.setStatus("current")
_RuijieWifiDot11radioIfConfigEntry_Object = MibTableRow
ruijieWifiDot11radioIfConfigEntry = _RuijieWifiDot11radioIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1)
)
ruijieWifiDot11radioIfConfigEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-WIFI-MIB", "ruijieWifiDot11radioIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEntry.setStatus("current")
_RuijieWifiDot11radioIfConfigIfIndex_Type = Integer32
_RuijieWifiDot11radioIfConfigIfIndex_Object = MibTableColumn
ruijieWifiDot11radioIfConfigIfIndex = _RuijieWifiDot11radioIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 1),
    _RuijieWifiDot11radioIfConfigIfIndex_Type()
)
ruijieWifiDot11radioIfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigIfIndex.setStatus("current")
_RuijieWifiDot11radioIfConfigRowStatus_Type = RowStatus
_RuijieWifiDot11radioIfConfigRowStatus_Object = MibTableColumn
ruijieWifiDot11radioIfConfigRowStatus = _RuijieWifiDot11radioIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 2),
    _RuijieWifiDot11radioIfConfigRowStatus_Type()
)
ruijieWifiDot11radioIfConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigRowStatus.setStatus("current")
_RuijieWifiDot11radioIfConfigFreBand_Type = RuijieWifiFreChanelType
_RuijieWifiDot11radioIfConfigFreBand_Object = MibTableColumn
ruijieWifiDot11radioIfConfigFreBand = _RuijieWifiDot11radioIfConfigFreBand_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 3),
    _RuijieWifiDot11radioIfConfigFreBand_Type()
)
ruijieWifiDot11radioIfConfigFreBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigFreBand.setStatus("current")
_RuijieWifiDot11radioIfConfigChannel_Type = Integer32
_RuijieWifiDot11radioIfConfigChannel_Object = MibTableColumn
ruijieWifiDot11radioIfConfigChannel = _RuijieWifiDot11radioIfConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 4),
    _RuijieWifiDot11radioIfConfigChannel_Type()
)
ruijieWifiDot11radioIfConfigChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigChannel.setStatus("current")
_RuijieWifiDot11radioIfConfigChanWidth_Type = RuijieWifiChanWidthType
_RuijieWifiDot11radioIfConfigChanWidth_Object = MibTableColumn
ruijieWifiDot11radioIfConfigChanWidth = _RuijieWifiDot11radioIfConfigChanWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 5),
    _RuijieWifiDot11radioIfConfigChanWidth_Type()
)
ruijieWifiDot11radioIfConfigChanWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigChanWidth.setStatus("current")
_RuijieWifiDot11radioIfConfigCountryCode_Type = DisplayString
_RuijieWifiDot11radioIfConfigCountryCode_Object = MibTableColumn
ruijieWifiDot11radioIfConfigCountryCode = _RuijieWifiDot11radioIfConfigCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 6),
    _RuijieWifiDot11radioIfConfigCountryCode_Type()
)
ruijieWifiDot11radioIfConfigCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigCountryCode.setStatus("current")


class _RuijieWifiDot11radioIfConfigPowerLocal_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigPowerLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieWifiDot11radioIfConfigPowerLocal_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigPowerLocal_Object = MibTableColumn
ruijieWifiDot11radioIfConfigPowerLocal = _RuijieWifiDot11radioIfConfigPowerLocal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 7),
    _RuijieWifiDot11radioIfConfigPowerLocal_Type()
)
ruijieWifiDot11radioIfConfigPowerLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigPowerLocal.setStatus("current")


class _RuijieWifiDot11radioIfConfigWirelessProSupport_Type(Bits):
    """Custom type ruijieWifiDot11radioIfConfigWirelessProSupport based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("b", 1),
          ("g", 2),
          ("n", 3))
    )

_RuijieWifiDot11radioIfConfigWirelessProSupport_Type.__name__ = "Bits"
_RuijieWifiDot11radioIfConfigWirelessProSupport_Object = MibTableColumn
ruijieWifiDot11radioIfConfigWirelessProSupport = _RuijieWifiDot11radioIfConfigWirelessProSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 8),
    _RuijieWifiDot11radioIfConfigWirelessProSupport_Type()
)
ruijieWifiDot11radioIfConfigWirelessProSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigWirelessProSupport.setStatus("current")


class _RuijieWifiDot11radioIfConfigStaLimit_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigStaLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RuijieWifiDot11radioIfConfigStaLimit_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigStaLimit_Object = MibTableColumn
ruijieWifiDot11radioIfConfigStaLimit = _RuijieWifiDot11radioIfConfigStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 9),
    _RuijieWifiDot11radioIfConfigStaLimit_Type()
)
ruijieWifiDot11radioIfConfigStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigStaLimit.setStatus("current")
_RuijieWifiDot11radioIfConfig20ShortGiEnable_Type = RuijieEableType
_RuijieWifiDot11radioIfConfig20ShortGiEnable_Object = MibTableColumn
ruijieWifiDot11radioIfConfig20ShortGiEnable = _RuijieWifiDot11radioIfConfig20ShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 10),
    _RuijieWifiDot11radioIfConfig20ShortGiEnable_Type()
)
ruijieWifiDot11radioIfConfig20ShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfig20ShortGiEnable.setStatus("current")
_RuijieWifiDot11radioIfConfig40ShortGiEnable_Type = RuijieEableType
_RuijieWifiDot11radioIfConfig40ShortGiEnable_Object = MibTableColumn
ruijieWifiDot11radioIfConfig40ShortGiEnable = _RuijieWifiDot11radioIfConfig40ShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 11),
    _RuijieWifiDot11radioIfConfig40ShortGiEnable_Type()
)
ruijieWifiDot11radioIfConfig40ShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfig40ShortGiEnable.setStatus("current")
_RuijieWifiDot11radioIfConfigShortPreambleEnable_Type = RuijieEableType
_RuijieWifiDot11radioIfConfigShortPreambleEnable_Object = MibTableColumn
ruijieWifiDot11radioIfConfigShortPreambleEnable = _RuijieWifiDot11radioIfConfigShortPreambleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 12),
    _RuijieWifiDot11radioIfConfigShortPreambleEnable_Type()
)
ruijieWifiDot11radioIfConfigShortPreambleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigShortPreambleEnable.setStatus("current")
_RuijieWifiDot11radioIfConfigSlottime_Type = RuijieWifiSlotType
_RuijieWifiDot11radioIfConfigSlottime_Object = MibTableColumn
ruijieWifiDot11radioIfConfigSlottime = _RuijieWifiDot11radioIfConfigSlottime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 13),
    _RuijieWifiDot11radioIfConfigSlottime_Type()
)
ruijieWifiDot11radioIfConfigSlottime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigSlottime.setStatus("current")


class _RuijieWifiDot11radioIfConfigRtsThreshold_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigRtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(257, 2347),
    )


_RuijieWifiDot11radioIfConfigRtsThreshold_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigRtsThreshold_Object = MibTableColumn
ruijieWifiDot11radioIfConfigRtsThreshold = _RuijieWifiDot11radioIfConfigRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 14),
    _RuijieWifiDot11radioIfConfigRtsThreshold_Type()
)
ruijieWifiDot11radioIfConfigRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigRtsThreshold.setStatus("current")


class _RuijieWifiDot11radioIfConfigFragmentThreshold_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigFragmentThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_RuijieWifiDot11radioIfConfigFragmentThreshold_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigFragmentThreshold_Object = MibTableColumn
ruijieWifiDot11radioIfConfigFragmentThreshold = _RuijieWifiDot11radioIfConfigFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 15),
    _RuijieWifiDot11radioIfConfigFragmentThreshold_Type()
)
ruijieWifiDot11radioIfConfigFragmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigFragmentThreshold.setStatus("current")


class _RuijieWifiDot11radioIfConfigResponseRssi_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigResponseRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieWifiDot11radioIfConfigResponseRssi_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigResponseRssi_Object = MibTableColumn
ruijieWifiDot11radioIfConfigResponseRssi = _RuijieWifiDot11radioIfConfigResponseRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 16),
    _RuijieWifiDot11radioIfConfigResponseRssi_Type()
)
ruijieWifiDot11radioIfConfigResponseRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigResponseRssi.setStatus("current")
_RuijieWifiDot11radioIfConfigEnableQos_Type = RuijieEableType
_RuijieWifiDot11radioIfConfigEnableQos_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEnableQos = _RuijieWifiDot11radioIfConfigEnableQos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 17),
    _RuijieWifiDot11radioIfConfigEnableQos_Type()
)
ruijieWifiDot11radioIfConfigEnableQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEnableQos.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientBgAifsn_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientBgAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientBgAifsn_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientBgAifsn_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientBgAifsn = _RuijieWifiDot11radioIfConfigEdcaClientBgAifsn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 18),
    _RuijieWifiDot11radioIfConfigEdcaClientBgAifsn_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientBgAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientBgAifsn.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientBgCwmin_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientBgCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientBgCwmin_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientBgCwmin_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientBgCwmin = _RuijieWifiDot11radioIfConfigEdcaClientBgCwmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 19),
    _RuijieWifiDot11radioIfConfigEdcaClientBgCwmin_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientBgCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientBgCwmin.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientBgCwmax_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientBgCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientBgCwmax_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientBgCwmax_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientBgCwmax = _RuijieWifiDot11radioIfConfigEdcaClientBgCwmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 20),
    _RuijieWifiDot11radioIfConfigEdcaClientBgCwmax_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientBgCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientBgCwmax.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientBgTxop_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientBgTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWifiDot11radioIfConfigEdcaClientBgTxop_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientBgTxop_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientBgTxop = _RuijieWifiDot11radioIfConfigEdcaClientBgTxop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 21),
    _RuijieWifiDot11radioIfConfigEdcaClientBgTxop_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientBgTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientBgTxop.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientBeAifsn_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientBeAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientBeAifsn_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientBeAifsn_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientBeAifsn = _RuijieWifiDot11radioIfConfigEdcaClientBeAifsn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 22),
    _RuijieWifiDot11radioIfConfigEdcaClientBeAifsn_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientBeAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientBeAifsn.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientBeCwmin_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientBeCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientBeCwmin_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientBeCwmin_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientBeCwmin = _RuijieWifiDot11radioIfConfigEdcaClientBeCwmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 23),
    _RuijieWifiDot11radioIfConfigEdcaClientBeCwmin_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientBeCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientBeCwmin.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientBeCwmax_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientBeCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientBeCwmax_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientBeCwmax_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientBeCwmax = _RuijieWifiDot11radioIfConfigEdcaClientBeCwmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 24),
    _RuijieWifiDot11radioIfConfigEdcaClientBeCwmax_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientBeCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientBeCwmax.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientBeTxop_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientBeTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWifiDot11radioIfConfigEdcaClientBeTxop_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientBeTxop_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientBeTxop = _RuijieWifiDot11radioIfConfigEdcaClientBeTxop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 25),
    _RuijieWifiDot11radioIfConfigEdcaClientBeTxop_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientBeTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientBeTxop.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientViAifsn_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientViAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientViAifsn_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientViAifsn_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientViAifsn = _RuijieWifiDot11radioIfConfigEdcaClientViAifsn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 26),
    _RuijieWifiDot11radioIfConfigEdcaClientViAifsn_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientViAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientViAifsn.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientViCwmin_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientViCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientViCwmin_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientViCwmin_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientViCwmin = _RuijieWifiDot11radioIfConfigEdcaClientViCwmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 27),
    _RuijieWifiDot11radioIfConfigEdcaClientViCwmin_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientViCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientViCwmin.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientViCwmax_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientViCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientViCwmax_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientViCwmax_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientViCwmax = _RuijieWifiDot11radioIfConfigEdcaClientViCwmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 28),
    _RuijieWifiDot11radioIfConfigEdcaClientViCwmax_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientViCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientViCwmax.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientViTxop_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientViTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWifiDot11radioIfConfigEdcaClientViTxop_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientViTxop_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientViTxop = _RuijieWifiDot11radioIfConfigEdcaClientViTxop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 29),
    _RuijieWifiDot11radioIfConfigEdcaClientViTxop_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientViTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientViTxop.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientVoAifsn_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientVoAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientVoAifsn_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientVoAifsn_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientVoAifsn = _RuijieWifiDot11radioIfConfigEdcaClientVoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 30),
    _RuijieWifiDot11radioIfConfigEdcaClientVoAifsn_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientVoAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientVoAifsn.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientVoCwmin_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientVoCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientVoCwmin_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientVoCwmin_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientVoCwmin = _RuijieWifiDot11radioIfConfigEdcaClientVoCwmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 31),
    _RuijieWifiDot11radioIfConfigEdcaClientVoCwmin_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientVoCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientVoCwmin.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientVoCwmax_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientVoCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaClientVoCwmax_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientVoCwmax_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientVoCwmax = _RuijieWifiDot11radioIfConfigEdcaClientVoCwmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 32),
    _RuijieWifiDot11radioIfConfigEdcaClientVoCwmax_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientVoCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientVoCwmax.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaClientVoTxop_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaClientVoTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWifiDot11radioIfConfigEdcaClientVoTxop_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaClientVoTxop_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaClientVoTxop = _RuijieWifiDot11radioIfConfigEdcaClientVoTxop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 33),
    _RuijieWifiDot11radioIfConfigEdcaClientVoTxop_Type()
)
ruijieWifiDot11radioIfConfigEdcaClientVoTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaClientVoTxop.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioBgAifsn_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioBgAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioBgAifsn_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioBgAifsn_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioBgAifsn = _RuijieWifiDot11radioIfConfigEdcaRadioBgAifsn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 34),
    _RuijieWifiDot11radioIfConfigEdcaRadioBgAifsn_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioBgAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioBgAifsn.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioBgCwmin_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioBgCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioBgCwmin_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioBgCwmin_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioBgCwmin = _RuijieWifiDot11radioIfConfigEdcaRadioBgCwmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 35),
    _RuijieWifiDot11radioIfConfigEdcaRadioBgCwmin_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioBgCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioBgCwmin.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioBgCwmax_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioBgCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioBgCwmax_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioBgCwmax_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioBgCwmax = _RuijieWifiDot11radioIfConfigEdcaRadioBgCwmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 36),
    _RuijieWifiDot11radioIfConfigEdcaRadioBgCwmax_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioBgCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioBgCwmax.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioBgTxop_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioBgTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioBgTxop_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioBgTxop_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioBgTxop = _RuijieWifiDot11radioIfConfigEdcaRadioBgTxop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 37),
    _RuijieWifiDot11radioIfConfigEdcaRadioBgTxop_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioBgTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioBgTxop.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioBeAifsn_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioBeAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioBeAifsn_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioBeAifsn_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioBeAifsn = _RuijieWifiDot11radioIfConfigEdcaRadioBeAifsn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 38),
    _RuijieWifiDot11radioIfConfigEdcaRadioBeAifsn_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioBeAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioBeAifsn.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioBeCwmin_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioBeCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioBeCwmin_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioBeCwmin_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioBeCwmin = _RuijieWifiDot11radioIfConfigEdcaRadioBeCwmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 39),
    _RuijieWifiDot11radioIfConfigEdcaRadioBeCwmin_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioBeCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioBeCwmin.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioBeCwmax_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioBeCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioBeCwmax_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioBeCwmax_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioBeCwmax = _RuijieWifiDot11radioIfConfigEdcaRadioBeCwmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 40),
    _RuijieWifiDot11radioIfConfigEdcaRadioBeCwmax_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioBeCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioBeCwmax.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioBeTxop_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioBeTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioBeTxop_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioBeTxop_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioBeTxop = _RuijieWifiDot11radioIfConfigEdcaRadioBeTxop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 41),
    _RuijieWifiDot11radioIfConfigEdcaRadioBeTxop_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioBeTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioBeTxop.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioViAifsn_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioViAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioViAifsn_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioViAifsn_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioViAifsn = _RuijieWifiDot11radioIfConfigEdcaRadioViAifsn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 42),
    _RuijieWifiDot11radioIfConfigEdcaRadioViAifsn_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioViAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioViAifsn.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioViCwmin_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioViCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioViCwmin_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioViCwmin_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioViCwmin = _RuijieWifiDot11radioIfConfigEdcaRadioViCwmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 43),
    _RuijieWifiDot11radioIfConfigEdcaRadioViCwmin_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioViCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioViCwmin.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioViCwmax_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioViCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioViCwmax_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioViCwmax_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioViCwmax = _RuijieWifiDot11radioIfConfigEdcaRadioViCwmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 44),
    _RuijieWifiDot11radioIfConfigEdcaRadioViCwmax_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioViCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioViCwmax.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioViTxop_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioViTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioViTxop_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioViTxop_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioViTxop = _RuijieWifiDot11radioIfConfigEdcaRadioViTxop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 45),
    _RuijieWifiDot11radioIfConfigEdcaRadioViTxop_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioViTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioViTxop.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioVoAifsn_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioVoAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioVoAifsn_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioVoAifsn_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioVoAifsn = _RuijieWifiDot11radioIfConfigEdcaRadioVoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 46),
    _RuijieWifiDot11radioIfConfigEdcaRadioVoAifsn_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioVoAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioVoAifsn.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioVoCwmin_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioVoCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioVoCwmin_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioVoCwmin_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioVoCwmin = _RuijieWifiDot11radioIfConfigEdcaRadioVoCwmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 47),
    _RuijieWifiDot11radioIfConfigEdcaRadioVoCwmin_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioVoCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioVoCwmin.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioVoCwmax_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioVoCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioVoCwmax_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioVoCwmax_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioVoCwmax = _RuijieWifiDot11radioIfConfigEdcaRadioVoCwmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 48),
    _RuijieWifiDot11radioIfConfigEdcaRadioVoCwmax_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioVoCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioVoCwmax.setStatus("current")


class _RuijieWifiDot11radioIfConfigEdcaRadioVoTxop_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigEdcaRadioVoTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWifiDot11radioIfConfigEdcaRadioVoTxop_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigEdcaRadioVoTxop_Object = MibTableColumn
ruijieWifiDot11radioIfConfigEdcaRadioVoTxop = _RuijieWifiDot11radioIfConfigEdcaRadioVoTxop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 49),
    _RuijieWifiDot11radioIfConfigEdcaRadioVoTxop_Type()
)
ruijieWifiDot11radioIfConfigEdcaRadioVoTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigEdcaRadioVoTxop.setStatus("current")


class _RuijieWifiDot11radioIfConfigAntennaTransChainmask_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigAntennaTransChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RuijieWifiDot11radioIfConfigAntennaTransChainmask_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigAntennaTransChainmask_Object = MibTableColumn
ruijieWifiDot11radioIfConfigAntennaTransChainmask = _RuijieWifiDot11radioIfConfigAntennaTransChainmask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 50),
    _RuijieWifiDot11radioIfConfigAntennaTransChainmask_Type()
)
ruijieWifiDot11radioIfConfigAntennaTransChainmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigAntennaTransChainmask.setStatus("current")


class _RuijieWifiDot11radioIfConfigAntennaReceiveChainmask_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigAntennaReceiveChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RuijieWifiDot11radioIfConfigAntennaReceiveChainmask_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigAntennaReceiveChainmask_Object = MibTableColumn
ruijieWifiDot11radioIfConfigAntennaReceiveChainmask = _RuijieWifiDot11radioIfConfigAntennaReceiveChainmask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 51),
    _RuijieWifiDot11radioIfConfigAntennaReceiveChainmask_Type()
)
ruijieWifiDot11radioIfConfigAntennaReceiveChainmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigAntennaReceiveChainmask.setStatus("current")


class _RuijieWifiDot11radioIfConfigBeaconDtimPeriod_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigBeaconDtimPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieWifiDot11radioIfConfigBeaconDtimPeriod_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigBeaconDtimPeriod_Object = MibTableColumn
ruijieWifiDot11radioIfConfigBeaconDtimPeriod = _RuijieWifiDot11radioIfConfigBeaconDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 52),
    _RuijieWifiDot11radioIfConfigBeaconDtimPeriod_Type()
)
ruijieWifiDot11radioIfConfigBeaconDtimPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigBeaconDtimPeriod.setStatus("current")


class _RuijieWifiDot11radioIfConfigBeaconPeriod_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_RuijieWifiDot11radioIfConfigBeaconPeriod_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigBeaconPeriod_Object = MibTableColumn
ruijieWifiDot11radioIfConfigBeaconPeriod = _RuijieWifiDot11radioIfConfigBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 53),
    _RuijieWifiDot11radioIfConfigBeaconPeriod_Type()
)
ruijieWifiDot11radioIfConfigBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigBeaconPeriod.setStatus("current")


class _RuijieWifiDot11radioIfConfigRetrieShortTime_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigRetrieShortTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RuijieWifiDot11radioIfConfigRetrieShortTime_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigRetrieShortTime_Object = MibTableColumn
ruijieWifiDot11radioIfConfigRetrieShortTime = _RuijieWifiDot11radioIfConfigRetrieShortTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 54),
    _RuijieWifiDot11radioIfConfigRetrieShortTime_Type()
)
ruijieWifiDot11radioIfConfigRetrieShortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigRetrieShortTime.setStatus("current")


class _RuijieWifiDot11radioIfConfigRetrieLongTime_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigRetrieLongTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuijieWifiDot11radioIfConfigRetrieLongTime_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigRetrieLongTime_Object = MibTableColumn
ruijieWifiDot11radioIfConfigRetrieLongTime = _RuijieWifiDot11radioIfConfigRetrieLongTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 55),
    _RuijieWifiDot11radioIfConfigRetrieLongTime_Type()
)
ruijieWifiDot11radioIfConfigRetrieLongTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigRetrieLongTime.setStatus("current")


class _RuijieWifiDot11radioIfConfigStaIdleTimeout_Type(Integer32):
    """Custom type ruijieWifiDot11radioIfConfigStaIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_RuijieWifiDot11radioIfConfigStaIdleTimeout_Type.__name__ = "Integer32"
_RuijieWifiDot11radioIfConfigStaIdleTimeout_Object = MibTableColumn
ruijieWifiDot11radioIfConfigStaIdleTimeout = _RuijieWifiDot11radioIfConfigStaIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 56),
    _RuijieWifiDot11radioIfConfigStaIdleTimeout_Type()
)
ruijieWifiDot11radioIfConfigStaIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigStaIdleTimeout.setStatus("current")


class _RuijieWifiDot11radioIfConfigWlanIdList_Type(Bits):
    """Custom type ruijieWifiDot11radioIfConfigWlanIdList based on Bits"""
    namedValues = NamedValues(
        *(("w0", 0),
          ("w1", 1),
          ("w2", 2),
          ("w3", 3),
          ("w4", 4),
          ("w5", 5),
          ("w6", 6),
          ("w7", 7),
          ("w8", 8),
          ("w9", 9),
          ("w10", 10),
          ("w11", 11),
          ("w12", 12),
          ("w13", 13),
          ("w14", 14),
          ("w15", 15))
    )

_RuijieWifiDot11radioIfConfigWlanIdList_Type.__name__ = "Bits"
_RuijieWifiDot11radioIfConfigWlanIdList_Object = MibTableColumn
ruijieWifiDot11radioIfConfigWlanIdList = _RuijieWifiDot11radioIfConfigWlanIdList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 3, 1, 1, 57),
    _RuijieWifiDot11radioIfConfigWlanIdList_Type()
)
ruijieWifiDot11radioIfConfigWlanIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWifiDot11radioIfConfigWlanIdList.setStatus("current")
_RuijieWifiWlanAssociateObjects_ObjectIdentity = ObjectIdentity
ruijieWifiWlanAssociateObjects = _RuijieWifiWlanAssociateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4)
)
_RuijieWifiWlanAssociateTable_Object = MibTable
ruijieWifiWlanAssociateTable = _RuijieWifiWlanAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateTable.setStatus("current")
_RuijieWifiWlanAssociateEntry_Object = MibTableRow
ruijieWifiWlanAssociateEntry = _RuijieWifiWlanAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1)
)
ruijieWifiWlanAssociateEntry.setIndexNames(
    (0, "RUIJIE-ROUTER-WIFI-MIB", "ruijieWifiWlanAssociateWlanId"),
    (0, "RUIJIE-ROUTER-WIFI-MIB", "ruijieWifiWlanAssociateStaMacAdress"),
)
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateEntry.setStatus("current")
_RuijieWifiWlanAssociateWlanId_Type = Integer32
_RuijieWifiWlanAssociateWlanId_Object = MibTableColumn
ruijieWifiWlanAssociateWlanId = _RuijieWifiWlanAssociateWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 1),
    _RuijieWifiWlanAssociateWlanId_Type()
)
ruijieWifiWlanAssociateWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateWlanId.setStatus("current")
_RuijieWifiWlanAssociateStaMacAdress_Type = DisplayString
_RuijieWifiWlanAssociateStaMacAdress_Object = MibTableColumn
ruijieWifiWlanAssociateStaMacAdress = _RuijieWifiWlanAssociateStaMacAdress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 2),
    _RuijieWifiWlanAssociateStaMacAdress_Type()
)
ruijieWifiWlanAssociateStaMacAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateStaMacAdress.setStatus("current")
_RuijieWifiWlanAssociateSsidName_Type = DisplayString
_RuijieWifiWlanAssociateSsidName_Object = MibTableColumn
ruijieWifiWlanAssociateSsidName = _RuijieWifiWlanAssociateSsidName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 3),
    _RuijieWifiWlanAssociateSsidName_Type()
)
ruijieWifiWlanAssociateSsidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateSsidName.setStatus("current")
_RuijieWifiWlanAssociateStaIpAdress_Type = IpAddress
_RuijieWifiWlanAssociateStaIpAdress_Object = MibTableColumn
ruijieWifiWlanAssociateStaIpAdress = _RuijieWifiWlanAssociateStaIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 4),
    _RuijieWifiWlanAssociateStaIpAdress_Type()
)
ruijieWifiWlanAssociateStaIpAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateStaIpAdress.setStatus("current")
_RuijieWifiWlanAssociateStaMaskAdress_Type = IpAddress
_RuijieWifiWlanAssociateStaMaskAdress_Object = MibTableColumn
ruijieWifiWlanAssociateStaMaskAdress = _RuijieWifiWlanAssociateStaMaskAdress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 5),
    _RuijieWifiWlanAssociateStaMaskAdress_Type()
)
ruijieWifiWlanAssociateStaMaskAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateStaMaskAdress.setStatus("current")
_RuijieWifiWlanAssociateStaSigalStrength_Type = Integer32
_RuijieWifiWlanAssociateStaSigalStrength_Object = MibTableColumn
ruijieWifiWlanAssociateStaSigalStrength = _RuijieWifiWlanAssociateStaSigalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 6),
    _RuijieWifiWlanAssociateStaSigalStrength_Type()
)
ruijieWifiWlanAssociateStaSigalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateStaSigalStrength.setStatus("current")
_RuijieWifiWlanAssociateStaConnectTime_Type = DisplayString
_RuijieWifiWlanAssociateStaConnectTime_Object = MibTableColumn
ruijieWifiWlanAssociateStaConnectTime = _RuijieWifiWlanAssociateStaConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 7),
    _RuijieWifiWlanAssociateStaConnectTime_Type()
)
ruijieWifiWlanAssociateStaConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateStaConnectTime.setStatus("current")
_RuijieWifiWlanAssociateStaConnectTimeLength_Type = DisplayString
_RuijieWifiWlanAssociateStaConnectTimeLength_Object = MibTableColumn
ruijieWifiWlanAssociateStaConnectTimeLength = _RuijieWifiWlanAssociateStaConnectTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 8),
    _RuijieWifiWlanAssociateStaConnectTimeLength_Type()
)
ruijieWifiWlanAssociateStaConnectTimeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateStaConnectTimeLength.setStatus("current")
_RuijieWifiWlanAssociateStaGate_Type = IpAddress
_RuijieWifiWlanAssociateStaGate_Object = MibTableColumn
ruijieWifiWlanAssociateStaGate = _RuijieWifiWlanAssociateStaGate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 9),
    _RuijieWifiWlanAssociateStaGate_Type()
)
ruijieWifiWlanAssociateStaGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateStaGate.setStatus("current")
_RuijieWifiWlanAssociateStaDns_Type = IpAddress
_RuijieWifiWlanAssociateStaDns_Object = MibTableColumn
ruijieWifiWlanAssociateStaDns = _RuijieWifiWlanAssociateStaDns_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 133, 1, 4, 1, 1, 10),
    _RuijieWifiWlanAssociateStaDns_Type()
)
ruijieWifiWlanAssociateStaDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWifiWlanAssociateStaDns.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ROUTER-WIFI-MIB",
    **{"RuijieEableType": RuijieEableType,
       "RuijieWlanType": RuijieWlanType,
       "RuijieIsolateType": RuijieIsolateType,
       "RuijieAuthenticationType": RuijieAuthenticationType,
       "RuijieWapPskCiphersType": RuijieWapPskCiphersType,
       "RuijieWifiChanWidthType": RuijieWifiChanWidthType,
       "RuijieWifiSlotType": RuijieWifiSlotType,
       "RuijieWifiFreChanelType": RuijieWifiFreChanelType,
       "ruijieWifiMIB": ruijieWifiMIB,
       "ruijieWifiMIBObjects": ruijieWifiMIBObjects,
       "ruijieWifiDot11radioSupportObjects": ruijieWifiDot11radioSupportObjects,
       "ruijieWifiDot11radioSupportTable": ruijieWifiDot11radioSupportTable,
       "ruijieWifiDot11radioSupportEntry": ruijieWifiDot11radioSupportEntry,
       "ruijieWifiDot11radioIndex": ruijieWifiDot11radioIndex,
       "ruijieWifiDot11radioApMaxCnt": ruijieWifiDot11radioApMaxCnt,
       "ruijieWifiDot11radioStationMaxCnt": ruijieWifiDot11radioStationMaxCnt,
       "ruijieWifiWlanObjects": ruijieWifiWlanObjects,
       "ruijieWifiWlanIndexNext": ruijieWifiWlanIndexNext,
       "ruijieWifiVlanIndexNext": ruijieWifiVlanIndexNext,
       "ruijieWifiWlanTable": ruijieWifiWlanTable,
       "ruijieWifiWlanEntry": ruijieWifiWlanEntry,
       "ruijieWifiWlanIndex": ruijieWifiWlanIndex,
       "ruijieWifiWlanType": ruijieWifiWlanType,
       "ruijieWifiWlanSsidName": ruijieWifiWlanSsidName,
       "ruijieWifiWlanVlanId": ruijieWifiWlanVlanId,
       "ruijieWifiWlanRowStatus": ruijieWifiWlanRowStatus,
       "ruijieWifiWlanBroadcastSsid": ruijieWifiWlanBroadcastSsid,
       "ruijieWifiWlanIsolate": ruijieWifiWlanIsolate,
       "ruijieWifiWlanBssStaLimit": ruijieWifiWlanBssStaLimit,
       "rujieWifiWlanSecurityType": rujieWifiWlanSecurityType,
       "ruijieWifiWlanAuthenticationSetKey": ruijieWifiWlanAuthenticationSetKey,
       "ruijieWifiWlanWepAuthenticationType": ruijieWifiWlanWepAuthenticationType,
       "ruijieWifiWlanWpaPskCiphersType": ruijieWifiWlanWpaPskCiphersType,
       "ruijieWifiWlanPassphrase": ruijieWifiWlanPassphrase,
       "ruijieWifiWlanDot11RadioIfindex": ruijieWifiWlanDot11RadioIfindex,
       "ruijieWifiWlanDot11RadioSubIfindex": ruijieWifiWlanDot11RadioSubIfindex,
       "ruijieWifiDot11radioIfConfigObjects": ruijieWifiDot11radioIfConfigObjects,
       "ruijieWifiDot11radioIfConfigTable": ruijieWifiDot11radioIfConfigTable,
       "ruijieWifiDot11radioIfConfigEntry": ruijieWifiDot11radioIfConfigEntry,
       "ruijieWifiDot11radioIfConfigIfIndex": ruijieWifiDot11radioIfConfigIfIndex,
       "ruijieWifiDot11radioIfConfigRowStatus": ruijieWifiDot11radioIfConfigRowStatus,
       "ruijieWifiDot11radioIfConfigFreBand": ruijieWifiDot11radioIfConfigFreBand,
       "ruijieWifiDot11radioIfConfigChannel": ruijieWifiDot11radioIfConfigChannel,
       "ruijieWifiDot11radioIfConfigChanWidth": ruijieWifiDot11radioIfConfigChanWidth,
       "ruijieWifiDot11radioIfConfigCountryCode": ruijieWifiDot11radioIfConfigCountryCode,
       "ruijieWifiDot11radioIfConfigPowerLocal": ruijieWifiDot11radioIfConfigPowerLocal,
       "ruijieWifiDot11radioIfConfigWirelessProSupport": ruijieWifiDot11radioIfConfigWirelessProSupport,
       "ruijieWifiDot11radioIfConfigStaLimit": ruijieWifiDot11radioIfConfigStaLimit,
       "ruijieWifiDot11radioIfConfig20ShortGiEnable": ruijieWifiDot11radioIfConfig20ShortGiEnable,
       "ruijieWifiDot11radioIfConfig40ShortGiEnable": ruijieWifiDot11radioIfConfig40ShortGiEnable,
       "ruijieWifiDot11radioIfConfigShortPreambleEnable": ruijieWifiDot11radioIfConfigShortPreambleEnable,
       "ruijieWifiDot11radioIfConfigSlottime": ruijieWifiDot11radioIfConfigSlottime,
       "ruijieWifiDot11radioIfConfigRtsThreshold": ruijieWifiDot11radioIfConfigRtsThreshold,
       "ruijieWifiDot11radioIfConfigFragmentThreshold": ruijieWifiDot11radioIfConfigFragmentThreshold,
       "ruijieWifiDot11radioIfConfigResponseRssi": ruijieWifiDot11radioIfConfigResponseRssi,
       "ruijieWifiDot11radioIfConfigEnableQos": ruijieWifiDot11radioIfConfigEnableQos,
       "ruijieWifiDot11radioIfConfigEdcaClientBgAifsn": ruijieWifiDot11radioIfConfigEdcaClientBgAifsn,
       "ruijieWifiDot11radioIfConfigEdcaClientBgCwmin": ruijieWifiDot11radioIfConfigEdcaClientBgCwmin,
       "ruijieWifiDot11radioIfConfigEdcaClientBgCwmax": ruijieWifiDot11radioIfConfigEdcaClientBgCwmax,
       "ruijieWifiDot11radioIfConfigEdcaClientBgTxop": ruijieWifiDot11radioIfConfigEdcaClientBgTxop,
       "ruijieWifiDot11radioIfConfigEdcaClientBeAifsn": ruijieWifiDot11radioIfConfigEdcaClientBeAifsn,
       "ruijieWifiDot11radioIfConfigEdcaClientBeCwmin": ruijieWifiDot11radioIfConfigEdcaClientBeCwmin,
       "ruijieWifiDot11radioIfConfigEdcaClientBeCwmax": ruijieWifiDot11radioIfConfigEdcaClientBeCwmax,
       "ruijieWifiDot11radioIfConfigEdcaClientBeTxop": ruijieWifiDot11radioIfConfigEdcaClientBeTxop,
       "ruijieWifiDot11radioIfConfigEdcaClientViAifsn": ruijieWifiDot11radioIfConfigEdcaClientViAifsn,
       "ruijieWifiDot11radioIfConfigEdcaClientViCwmin": ruijieWifiDot11radioIfConfigEdcaClientViCwmin,
       "ruijieWifiDot11radioIfConfigEdcaClientViCwmax": ruijieWifiDot11radioIfConfigEdcaClientViCwmax,
       "ruijieWifiDot11radioIfConfigEdcaClientViTxop": ruijieWifiDot11radioIfConfigEdcaClientViTxop,
       "ruijieWifiDot11radioIfConfigEdcaClientVoAifsn": ruijieWifiDot11radioIfConfigEdcaClientVoAifsn,
       "ruijieWifiDot11radioIfConfigEdcaClientVoCwmin": ruijieWifiDot11radioIfConfigEdcaClientVoCwmin,
       "ruijieWifiDot11radioIfConfigEdcaClientVoCwmax": ruijieWifiDot11radioIfConfigEdcaClientVoCwmax,
       "ruijieWifiDot11radioIfConfigEdcaClientVoTxop": ruijieWifiDot11radioIfConfigEdcaClientVoTxop,
       "ruijieWifiDot11radioIfConfigEdcaRadioBgAifsn": ruijieWifiDot11radioIfConfigEdcaRadioBgAifsn,
       "ruijieWifiDot11radioIfConfigEdcaRadioBgCwmin": ruijieWifiDot11radioIfConfigEdcaRadioBgCwmin,
       "ruijieWifiDot11radioIfConfigEdcaRadioBgCwmax": ruijieWifiDot11radioIfConfigEdcaRadioBgCwmax,
       "ruijieWifiDot11radioIfConfigEdcaRadioBgTxop": ruijieWifiDot11radioIfConfigEdcaRadioBgTxop,
       "ruijieWifiDot11radioIfConfigEdcaRadioBeAifsn": ruijieWifiDot11radioIfConfigEdcaRadioBeAifsn,
       "ruijieWifiDot11radioIfConfigEdcaRadioBeCwmin": ruijieWifiDot11radioIfConfigEdcaRadioBeCwmin,
       "ruijieWifiDot11radioIfConfigEdcaRadioBeCwmax": ruijieWifiDot11radioIfConfigEdcaRadioBeCwmax,
       "ruijieWifiDot11radioIfConfigEdcaRadioBeTxop": ruijieWifiDot11radioIfConfigEdcaRadioBeTxop,
       "ruijieWifiDot11radioIfConfigEdcaRadioViAifsn": ruijieWifiDot11radioIfConfigEdcaRadioViAifsn,
       "ruijieWifiDot11radioIfConfigEdcaRadioViCwmin": ruijieWifiDot11radioIfConfigEdcaRadioViCwmin,
       "ruijieWifiDot11radioIfConfigEdcaRadioViCwmax": ruijieWifiDot11radioIfConfigEdcaRadioViCwmax,
       "ruijieWifiDot11radioIfConfigEdcaRadioViTxop": ruijieWifiDot11radioIfConfigEdcaRadioViTxop,
       "ruijieWifiDot11radioIfConfigEdcaRadioVoAifsn": ruijieWifiDot11radioIfConfigEdcaRadioVoAifsn,
       "ruijieWifiDot11radioIfConfigEdcaRadioVoCwmin": ruijieWifiDot11radioIfConfigEdcaRadioVoCwmin,
       "ruijieWifiDot11radioIfConfigEdcaRadioVoCwmax": ruijieWifiDot11radioIfConfigEdcaRadioVoCwmax,
       "ruijieWifiDot11radioIfConfigEdcaRadioVoTxop": ruijieWifiDot11radioIfConfigEdcaRadioVoTxop,
       "ruijieWifiDot11radioIfConfigAntennaTransChainmask": ruijieWifiDot11radioIfConfigAntennaTransChainmask,
       "ruijieWifiDot11radioIfConfigAntennaReceiveChainmask": ruijieWifiDot11radioIfConfigAntennaReceiveChainmask,
       "ruijieWifiDot11radioIfConfigBeaconDtimPeriod": ruijieWifiDot11radioIfConfigBeaconDtimPeriod,
       "ruijieWifiDot11radioIfConfigBeaconPeriod": ruijieWifiDot11radioIfConfigBeaconPeriod,
       "ruijieWifiDot11radioIfConfigRetrieShortTime": ruijieWifiDot11radioIfConfigRetrieShortTime,
       "ruijieWifiDot11radioIfConfigRetrieLongTime": ruijieWifiDot11radioIfConfigRetrieLongTime,
       "ruijieWifiDot11radioIfConfigStaIdleTimeout": ruijieWifiDot11radioIfConfigStaIdleTimeout,
       "ruijieWifiDot11radioIfConfigWlanIdList": ruijieWifiDot11radioIfConfigWlanIdList,
       "ruijieWifiWlanAssociateObjects": ruijieWifiWlanAssociateObjects,
       "ruijieWifiWlanAssociateTable": ruijieWifiWlanAssociateTable,
       "ruijieWifiWlanAssociateEntry": ruijieWifiWlanAssociateEntry,
       "ruijieWifiWlanAssociateWlanId": ruijieWifiWlanAssociateWlanId,
       "ruijieWifiWlanAssociateStaMacAdress": ruijieWifiWlanAssociateStaMacAdress,
       "ruijieWifiWlanAssociateSsidName": ruijieWifiWlanAssociateSsidName,
       "ruijieWifiWlanAssociateStaIpAdress": ruijieWifiWlanAssociateStaIpAdress,
       "ruijieWifiWlanAssociateStaMaskAdress": ruijieWifiWlanAssociateStaMaskAdress,
       "ruijieWifiWlanAssociateStaSigalStrength": ruijieWifiWlanAssociateStaSigalStrength,
       "ruijieWifiWlanAssociateStaConnectTime": ruijieWifiWlanAssociateStaConnectTime,
       "ruijieWifiWlanAssociateStaConnectTimeLength": ruijieWifiWlanAssociateStaConnectTimeLength,
       "ruijieWifiWlanAssociateStaGate": ruijieWifiWlanAssociateStaGate,
       "ruijieWifiWlanAssociateStaDns": ruijieWifiWlanAssociateStaDns}
)
