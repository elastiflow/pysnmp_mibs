# SNMP MIB module (BELAIR-IEEE802DOT11) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-IEEE802DOT11.mib
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

(belairInterfaces,
 belairModules) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairInterfaces",
    "belairModules")

(BelAirAdminState,
 BelAirAuthenType,
 BelAirEncryptionKey,
 BelAirEncryptionType,
 BelAirRowStatus,
 BelAirSsidIndex,
 BelAirVlanIdOrZero) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState",
    "BelAirAuthenType",
    "BelAirEncryptionKey",
    "BelAirEncryptionType",
    "BelAirRowStatus",
    "BelAirSsidIndex",
    "BelAirVlanIdOrZero")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

belairIeeeDot11Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 1, 5)
)
if mibBuilder.loadTexts:
    belairIeeeDot11Module.setRevisions(
        ("2009-04-30 14:25",
         "2008-12-12 11:15",
         "2008-09-02 17:05",
         "2007-12-06 10:00",
         "2007-10-25 10:00",
         "2005-08-01 17:57",
         "2005-07-26 15:51",
         "2005-04-01 09:50",
         "2005-01-27 14:00",
         "2004-11-23 18:15",
         "2004-10-01 17:45")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairDot11Objects_ObjectIdentity = ObjectIdentity
belairDot11Objects = _BelairDot11Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1)
)
if mibBuilder.loadTexts:
    belairDot11Objects.setStatus("current")
_BelairDot11StaConfigTable_Object = MibTable
belairDot11StaConfigTable = _BelairDot11StaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1)
)
if mibBuilder.loadTexts:
    belairDot11StaConfigTable.setStatus("current")
_BelairDot11StaConfigEntry_Object = MibTableRow
belairDot11StaConfigEntry = _BelairDot11StaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1)
)
belairDot11StaConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    belairDot11StaConfigEntry.setStatus("current")


class _BelairDot11StaConfigMode_Type(Integer32):
    """Custom type belairDot11StaConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 1),
          ("backhaulAp", 2),
          ("backhaulClient", 3),
          ("disable", 4),
          ("notApplicable", 5))
    )


_BelairDot11StaConfigMode_Type.__name__ = "Integer32"
_BelairDot11StaConfigMode_Object = MibTableColumn
belairDot11StaConfigMode = _BelairDot11StaConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 1),
    _BelairDot11StaConfigMode_Type()
)
belairDot11StaConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaConfigMode.setStatus("current")
_BelairDot11StaMaxAssociated_Type = Integer32
_BelairDot11StaMaxAssociated_Object = MibTableColumn
belairDot11StaMaxAssociated = _BelairDot11StaMaxAssociated_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 2),
    _BelairDot11StaMaxAssociated_Type()
)
belairDot11StaMaxAssociated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaMaxAssociated.setStatus("current")
_BelairDot11StaConfigPeerMac_Type = MacAddress
_BelairDot11StaConfigPeerMac_Object = MibTableColumn
belairDot11StaConfigPeerMac = _BelairDot11StaConfigPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 3),
    _BelairDot11StaConfigPeerMac_Type()
)
belairDot11StaConfigPeerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaConfigPeerMac.setStatus("current")
_BelairDot11StaConfigAssociatedMac_Type = MacAddress
_BelairDot11StaConfigAssociatedMac_Object = MibTableColumn
belairDot11StaConfigAssociatedMac = _BelairDot11StaConfigAssociatedMac_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 4),
    _BelairDot11StaConfigAssociatedMac_Type()
)
belairDot11StaConfigAssociatedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11StaConfigAssociatedMac.setStatus("current")
_BelairDot11StaConfigWirelessBridgeEnable_Type = TruthValue
_BelairDot11StaConfigWirelessBridgeEnable_Object = MibTableColumn
belairDot11StaConfigWirelessBridgeEnable = _BelairDot11StaConfigWirelessBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 5),
    _BelairDot11StaConfigWirelessBridgeEnable_Type()
)
belairDot11StaConfigWirelessBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaConfigWirelessBridgeEnable.setStatus("current")
_BelairDot11StaConfigAclEnable_Type = TruthValue
_BelairDot11StaConfigAclEnable_Object = MibTableColumn
belairDot11StaConfigAclEnable = _BelairDot11StaConfigAclEnable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 6),
    _BelairDot11StaConfigAclEnable_Type()
)
belairDot11StaConfigAclEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaConfigAclEnable.setStatus("current")
_BelairDot11StaConfigRssi_Type = Integer32
_BelairDot11StaConfigRssi_Object = MibTableColumn
belairDot11StaConfigRssi = _BelairDot11StaConfigRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 7),
    _BelairDot11StaConfigRssi_Type()
)
belairDot11StaConfigRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11StaConfigRssi.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11StaConfigRssi.setUnits("dBm")
_BelairDot11StaCurrentAssociated_Type = Integer32
_BelairDot11StaCurrentAssociated_Object = MibTableColumn
belairDot11StaCurrentAssociated = _BelairDot11StaCurrentAssociated_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 8),
    _BelairDot11StaCurrentAssociated_Type()
)
belairDot11StaCurrentAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11StaCurrentAssociated.setStatus("current")
_BelairDot11StaConfigStationIdEnable_Type = TruthValue
_BelairDot11StaConfigStationIdEnable_Object = MibTableColumn
belairDot11StaConfigStationIdEnable = _BelairDot11StaConfigStationIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 9),
    _BelairDot11StaConfigStationIdEnable_Type()
)
belairDot11StaConfigStationIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaConfigStationIdEnable.setStatus("current")
_BelairDot11StaConfigAcctSessionIdEnable_Type = TruthValue
_BelairDot11StaConfigAcctSessionIdEnable_Object = MibTableColumn
belairDot11StaConfigAcctSessionIdEnable = _BelairDot11StaConfigAcctSessionIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 10),
    _BelairDot11StaConfigAcctSessionIdEnable_Type()
)
belairDot11StaConfigAcctSessionIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaConfigAcctSessionIdEnable.setStatus("current")
_BelairDot11StaConfigNasIdentifier_Type = OctetString
_BelairDot11StaConfigNasIdentifier_Object = MibTableColumn
belairDot11StaConfigNasIdentifier = _BelairDot11StaConfigNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 11),
    _BelairDot11StaConfigNasIdentifier_Type()
)
belairDot11StaConfigNasIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaConfigNasIdentifier.setStatus("current")
_BelairDot11StaConfigRadAcctEnable_Type = TruthValue
_BelairDot11StaConfigRadAcctEnable_Object = MibTableColumn
belairDot11StaConfigRadAcctEnable = _BelairDot11StaConfigRadAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 12),
    _BelairDot11StaConfigRadAcctEnable_Type()
)
belairDot11StaConfigRadAcctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11StaConfigRadAcctEnable.setStatus("current")
_BelairDot11StaLastSpoofedSecureMac_Type = MacAddress
_BelairDot11StaLastSpoofedSecureMac_Object = MibTableColumn
belairDot11StaLastSpoofedSecureMac = _BelairDot11StaLastSpoofedSecureMac_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 1, 1, 13),
    _BelairDot11StaLastSpoofedSecureMac_Type()
)
belairDot11StaLastSpoofedSecureMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    belairDot11StaLastSpoofedSecureMac.setStatus("current")
_BelairDot11SsidTable_Object = MibTable
belairDot11SsidTable = _BelairDot11SsidTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 2)
)
if mibBuilder.loadTexts:
    belairDot11SsidTable.setStatus("current")
_BelairDot11SsidEntry_Object = MibTableRow
belairDot11SsidEntry = _BelairDot11SsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 2, 1)
)
belairDot11SsidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-IEEE802DOT11", "belairDot11SsidIndex"),
)
if mibBuilder.loadTexts:
    belairDot11SsidEntry.setStatus("current")
_BelairDot11SsidIndex_Type = BelAirSsidIndex
_BelairDot11SsidIndex_Object = MibTableColumn
belairDot11SsidIndex = _BelairDot11SsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 2, 1, 1),
    _BelairDot11SsidIndex_Type()
)
belairDot11SsidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairDot11SsidIndex.setStatus("current")


class _BelairDot11SsidName_Type(OctetString):
    """Custom type belairDot11SsidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BelairDot11SsidName_Type.__name__ = "OctetString"
_BelairDot11SsidName_Object = MibTableColumn
belairDot11SsidName = _BelairDot11SsidName_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 2, 1, 2),
    _BelairDot11SsidName_Type()
)
belairDot11SsidName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairDot11SsidName.setStatus("current")


class _BelairDot11SsidVlanId_Type(BelAirVlanIdOrZero):
    """Custom type belairDot11SsidVlanId based on BelAirVlanIdOrZero"""
    defaultValue = 0


_BelairDot11SsidVlanId_Type.__name__ = "BelAirVlanIdOrZero"
_BelairDot11SsidVlanId_Object = MibTableColumn
belairDot11SsidVlanId = _BelairDot11SsidVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 2, 1, 3),
    _BelairDot11SsidVlanId_Type()
)
belairDot11SsidVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairDot11SsidVlanId.setStatus("current")
_BelairDot11SsidIfIndex_Type = Integer32
_BelairDot11SsidIfIndex_Object = MibTableColumn
belairDot11SsidIfIndex = _BelairDot11SsidIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 2, 1, 4),
    _BelairDot11SsidIfIndex_Type()
)
belairDot11SsidIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11SsidIfIndex.setStatus("current")
_BelairDot11SsidRowStatus_Type = BelAirRowStatus
_BelairDot11SsidRowStatus_Object = MibTableColumn
belairDot11SsidRowStatus = _BelairDot11SsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 2, 1, 5),
    _BelairDot11SsidRowStatus_Type()
)
belairDot11SsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairDot11SsidRowStatus.setStatus("current")
_BelairDot11SecuConfigTable_Object = MibTable
belairDot11SecuConfigTable = _BelairDot11SecuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3)
)
if mibBuilder.loadTexts:
    belairDot11SecuConfigTable.setStatus("current")
_BelairDot11SecuConfigEntry_Object = MibTableRow
belairDot11SecuConfigEntry = _BelairDot11SecuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1)
)
belairDot11SecuConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-IEEE802DOT11", "belairDot11SecuConfigIndex"),
)
if mibBuilder.loadTexts:
    belairDot11SecuConfigEntry.setStatus("current")


class _BelairDot11SecuConfigIndex_Type(Integer32):
    """Custom type belairDot11SecuConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BelairDot11SecuConfigIndex_Type.__name__ = "Integer32"
_BelairDot11SecuConfigIndex_Object = MibTableColumn
belairDot11SecuConfigIndex = _BelairDot11SecuConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 1),
    _BelairDot11SecuConfigIndex_Type()
)
belairDot11SecuConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairDot11SecuConfigIndex.setStatus("current")
_BelairDot11SecuConfigAuthenType_Type = BelAirAuthenType
_BelairDot11SecuConfigAuthenType_Object = MibTableColumn
belairDot11SecuConfigAuthenType = _BelairDot11SecuConfigAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 2),
    _BelairDot11SecuConfigAuthenType_Type()
)
belairDot11SecuConfigAuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigAuthenType.setStatus("current")


class _BelairDot11SecuConfigKeyLen_Type(Integer32):
    """Custom type belairDot11SecuConfigKeyLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 16),
    )


_BelairDot11SecuConfigKeyLen_Type.__name__ = "Integer32"
_BelairDot11SecuConfigKeyLen_Object = MibTableColumn
belairDot11SecuConfigKeyLen = _BelairDot11SecuConfigKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 3),
    _BelairDot11SecuConfigKeyLen_Type()
)
belairDot11SecuConfigKeyLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigKeyLen.setStatus("current")
_BelairDot11SecuConfigKeyValue_Type = BelAirEncryptionKey
_BelairDot11SecuConfigKeyValue_Object = MibTableColumn
belairDot11SecuConfigKeyValue = _BelairDot11SecuConfigKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 4),
    _BelairDot11SecuConfigKeyValue_Type()
)
belairDot11SecuConfigKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigKeyValue.setStatus("current")


class _BelairDot11SecuConfigRekeyType_Type(Integer32):
    """Custom type belairDot11SecuConfigRekeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRekey", 1),
          ("byTime", 2),
          ("byPacket", 3))
    )


_BelairDot11SecuConfigRekeyType_Type.__name__ = "Integer32"
_BelairDot11SecuConfigRekeyType_Object = MibTableColumn
belairDot11SecuConfigRekeyType = _BelairDot11SecuConfigRekeyType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 5),
    _BelairDot11SecuConfigRekeyType_Type()
)
belairDot11SecuConfigRekeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigRekeyType.setStatus("current")
_BelairDot11SecuConfigRekeyPkts_Type = Integer32
_BelairDot11SecuConfigRekeyPkts_Object = MibTableColumn
belairDot11SecuConfigRekeyPkts = _BelairDot11SecuConfigRekeyPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 6),
    _BelairDot11SecuConfigRekeyPkts_Type()
)
belairDot11SecuConfigRekeyPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigRekeyPkts.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11SecuConfigRekeyPkts.setUnits("packets")
_BelairDot11SecuConfigRekeyInterval_Type = Integer32
_BelairDot11SecuConfigRekeyInterval_Object = MibTableColumn
belairDot11SecuConfigRekeyInterval = _BelairDot11SecuConfigRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 7),
    _BelairDot11SecuConfigRekeyInterval_Type()
)
belairDot11SecuConfigRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigRekeyInterval.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11SecuConfigRekeyInterval.setUnits("seconds")
_BelairDot11SecuConfigKeyUpdate_Type = TruthValue
_BelairDot11SecuConfigKeyUpdate_Object = MibTableColumn
belairDot11SecuConfigKeyUpdate = _BelairDot11SecuConfigKeyUpdate_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 9),
    _BelairDot11SecuConfigKeyUpdate_Type()
)
belairDot11SecuConfigKeyUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigKeyUpdate.setStatus("current")
_BelairDot11SecuConfigCipherType_Type = BelAirEncryptionType
_BelairDot11SecuConfigCipherType_Object = MibTableColumn
belairDot11SecuConfigCipherType = _BelairDot11SecuConfigCipherType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 10),
    _BelairDot11SecuConfigCipherType_Type()
)
belairDot11SecuConfigCipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigCipherType.setStatus("current")
_BelairDot11SecuConfigEnable_Type = TruthValue
_BelairDot11SecuConfigEnable_Object = MibTableColumn
belairDot11SecuConfigEnable = _BelairDot11SecuConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 3, 1, 11),
    _BelairDot11SecuConfigEnable_Type()
)
belairDot11SecuConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11SecuConfigEnable.setStatus("current")
_BelairDot11AclTable_Object = MibTable
belairDot11AclTable = _BelairDot11AclTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 5)
)
if mibBuilder.loadTexts:
    belairDot11AclTable.setStatus("current")
_BelairDot11AclEntry_Object = MibTableRow
belairDot11AclEntry = _BelairDot11AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 5, 1)
)
belairDot11AclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-IEEE802DOT11", "belairDot11AclIndex"),
)
if mibBuilder.loadTexts:
    belairDot11AclEntry.setStatus("current")


class _BelairDot11AclIndex_Type(Integer32):
    """Custom type belairDot11AclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BelairDot11AclIndex_Type.__name__ = "Integer32"
_BelairDot11AclIndex_Object = MibTableColumn
belairDot11AclIndex = _BelairDot11AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 5, 1, 1),
    _BelairDot11AclIndex_Type()
)
belairDot11AclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairDot11AclIndex.setStatus("current")
_BelairDot11AclMacAddress_Type = MacAddress
_BelairDot11AclMacAddress_Object = MibTableColumn
belairDot11AclMacAddress = _BelairDot11AclMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 5, 1, 2),
    _BelairDot11AclMacAddress_Type()
)
belairDot11AclMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairDot11AclMacAddress.setStatus("current")
_BelairDot11AclRowStatus_Type = BelAirRowStatus
_BelairDot11AclRowStatus_Object = MibTableColumn
belairDot11AclRowStatus = _BelairDot11AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 5, 1, 3),
    _BelairDot11AclRowStatus_Type()
)
belairDot11AclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairDot11AclRowStatus.setStatus("current")
_BelairDot11ApSurveyTable_Object = MibTable
belairDot11ApSurveyTable = _BelairDot11ApSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6)
)
if mibBuilder.loadTexts:
    belairDot11ApSurveyTable.setStatus("current")
_BelairDot11ApSurveyEntry_Object = MibTableRow
belairDot11ApSurveyEntry = _BelairDot11ApSurveyEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6, 1)
)
belairDot11ApSurveyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-IEEE802DOT11", "belairDot11ApSurveyMacAddress"),
)
if mibBuilder.loadTexts:
    belairDot11ApSurveyEntry.setStatus("current")
_BelairDot11ApSurveyMacAddress_Type = MacAddress
_BelairDot11ApSurveyMacAddress_Object = MibTableColumn
belairDot11ApSurveyMacAddress = _BelairDot11ApSurveyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6, 1, 1),
    _BelairDot11ApSurveyMacAddress_Type()
)
belairDot11ApSurveyMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairDot11ApSurveyMacAddress.setStatus("current")


class _BelairDot11ApSurveyBssType_Type(Integer32):
    """Custom type belairDot11ApSurveyBssType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("infrastructure", 0),
          ("adhoc", 1))
    )


_BelairDot11ApSurveyBssType_Type.__name__ = "Integer32"
_BelairDot11ApSurveyBssType_Object = MibTableColumn
belairDot11ApSurveyBssType = _BelairDot11ApSurveyBssType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6, 1, 2),
    _BelairDot11ApSurveyBssType_Type()
)
belairDot11ApSurveyBssType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ApSurveyBssType.setStatus("current")


class _BelairDot11ApSurveySsid_Type(OctetString):
    """Custom type belairDot11ApSurveySsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BelairDot11ApSurveySsid_Type.__name__ = "OctetString"
_BelairDot11ApSurveySsid_Object = MibTableColumn
belairDot11ApSurveySsid = _BelairDot11ApSurveySsid_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6, 1, 3),
    _BelairDot11ApSurveySsid_Type()
)
belairDot11ApSurveySsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ApSurveySsid.setStatus("current")
_BelairDot11ApSurveyChannel_Type = Integer32
_BelairDot11ApSurveyChannel_Object = MibTableColumn
belairDot11ApSurveyChannel = _BelairDot11ApSurveyChannel_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6, 1, 4),
    _BelairDot11ApSurveyChannel_Type()
)
belairDot11ApSurveyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ApSurveyChannel.setStatus("current")
_BelairDot11ApSurveyPrivacy_Type = TruthValue
_BelairDot11ApSurveyPrivacy_Object = MibTableColumn
belairDot11ApSurveyPrivacy = _BelairDot11ApSurveyPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6, 1, 5),
    _BelairDot11ApSurveyPrivacy_Type()
)
belairDot11ApSurveyPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ApSurveyPrivacy.setStatus("current")
_BelairDot11ApSurveyRssi_Type = Integer32
_BelairDot11ApSurveyRssi_Object = MibTableColumn
belairDot11ApSurveyRssi = _BelairDot11ApSurveyRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6, 1, 6),
    _BelairDot11ApSurveyRssi_Type()
)
belairDot11ApSurveyRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ApSurveyRssi.setStatus("current")
_BelairDot11ApSurveySecsSinceLastSeen_Type = Integer32
_BelairDot11ApSurveySecsSinceLastSeen_Object = MibTableColumn
belairDot11ApSurveySecsSinceLastSeen = _BelairDot11ApSurveySecsSinceLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 6, 1, 7),
    _BelairDot11ApSurveySecsSinceLastSeen_Type()
)
belairDot11ApSurveySecsSinceLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ApSurveySecsSinceLastSeen.setStatus("current")
_BelairDot11PhyChannelTable_Object = MibTable
belairDot11PhyChannelTable = _BelairDot11PhyChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7)
)
if mibBuilder.loadTexts:
    belairDot11PhyChannelTable.setStatus("current")
_BelairDot11PhyChannelEntry_Object = MibTableRow
belairDot11PhyChannelEntry = _BelairDot11PhyChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1)
)
belairDot11PhyChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    belairDot11PhyChannelEntry.setStatus("current")
_BelairDot11PhyChannelPrimary_Type = Integer32
_BelairDot11PhyChannelPrimary_Object = MibTableColumn
belairDot11PhyChannelPrimary = _BelairDot11PhyChannelPrimary_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 1),
    _BelairDot11PhyChannelPrimary_Type()
)
belairDot11PhyChannelPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyChannelPrimary.setStatus("current")
_BelairDot11PhyChannelSecondary_Type = Integer32
_BelairDot11PhyChannelSecondary_Object = MibTableColumn
belairDot11PhyChannelSecondary = _BelairDot11PhyChannelSecondary_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 2),
    _BelairDot11PhyChannelSecondary_Type()
)
belairDot11PhyChannelSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyChannelSecondary.setStatus("current")
_BelairDot11PhyChannelAutomatic_Type = TruthValue
_BelairDot11PhyChannelAutomatic_Object = MibTableColumn
belairDot11PhyChannelAutomatic = _BelairDot11PhyChannelAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 3),
    _BelairDot11PhyChannelAutomatic_Type()
)
belairDot11PhyChannelAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyChannelAutomatic.setStatus("current")
_BelairDot11PhyChannelBandwidth_Type = Integer32
_BelairDot11PhyChannelBandwidth_Object = MibTableColumn
belairDot11PhyChannelBandwidth = _BelairDot11PhyChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 4),
    _BelairDot11PhyChannelBandwidth_Type()
)
belairDot11PhyChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyChannelBandwidth.setUnits("Mhz")


class _BelairDot11PhyChannelFrqBand_Type(Integer32):
    """Custom type belairDot11PhyChannelFrqBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("b2400Mhz", 1),
          ("b4900Mhz", 2),
          ("b5000Mhz", 3),
          ("b5900Mhz", 4),
          ("b2300Mhz", 5),
          ("b2500Mhz", 6),
          ("b4400Mhz", 7),
          ("b4900MhzJP", 8),
          ("b5000MhzJP", 9),
          ("b4900bMhz", 10))
    )


_BelairDot11PhyChannelFrqBand_Type.__name__ = "Integer32"
_BelairDot11PhyChannelFrqBand_Object = MibTableColumn
belairDot11PhyChannelFrqBand = _BelairDot11PhyChannelFrqBand_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 5),
    _BelairDot11PhyChannelFrqBand_Type()
)
belairDot11PhyChannelFrqBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyChannelFrqBand.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyChannelFrqBand.setUnits("Mhz")
_BelairDot11PhyChannelCurrent_Type = Integer32
_BelairDot11PhyChannelCurrent_Object = MibTableColumn
belairDot11PhyChannelCurrent = _BelairDot11PhyChannelCurrent_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 6),
    _BelairDot11PhyChannelCurrent_Type()
)
belairDot11PhyChannelCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11PhyChannelCurrent.setStatus("current")


class _BelairDot11PhyChannelScanList_Type(Integer32):
    """Custom type belairDot11PhyChannelScanList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BelairDot11PhyChannelScanList_Type.__name__ = "Integer32"
_BelairDot11PhyChannelScanList_Object = MibTableColumn
belairDot11PhyChannelScanList = _BelairDot11PhyChannelScanList_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 7),
    _BelairDot11PhyChannelScanList_Type()
)
belairDot11PhyChannelScanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyChannelScanList.setStatus("current")
_BelairDot11PhyChannelScan_Type = TruthValue
_BelairDot11PhyChannelScan_Object = MibTableColumn
belairDot11PhyChannelScan = _BelairDot11PhyChannelScan_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 8),
    _BelairDot11PhyChannelScan_Type()
)
belairDot11PhyChannelScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyChannelScan.setStatus("current")


class _BelairDot11PhyChannelScanStatus_Type(Integer32):
    """Custom type belairDot11PhyChannelScanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pending", 1),
          ("scanning", 2),
          ("completed", 3))
    )


_BelairDot11PhyChannelScanStatus_Type.__name__ = "Integer32"
_BelairDot11PhyChannelScanStatus_Object = MibTableColumn
belairDot11PhyChannelScanStatus = _BelairDot11PhyChannelScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 9),
    _BelairDot11PhyChannelScanStatus_Type()
)
belairDot11PhyChannelScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11PhyChannelScanStatus.setStatus("current")
_BelairDot11PhyChannelLastScanTime_Type = TimeStamp
_BelairDot11PhyChannelLastScanTime_Object = MibTableColumn
belairDot11PhyChannelLastScanTime = _BelairDot11PhyChannelLastScanTime_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 7, 1, 10),
    _BelairDot11PhyChannelLastScanTime_Type()
)
belairDot11PhyChannelLastScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11PhyChannelLastScanTime.setStatus("current")
_BelairDot11PhyAntennaTable_Object = MibTable
belairDot11PhyAntennaTable = _BelairDot11PhyAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 8)
)
if mibBuilder.loadTexts:
    belairDot11PhyAntennaTable.setStatus("current")
_BelairDot11PhyAntennaEntry_Object = MibTableRow
belairDot11PhyAntennaEntry = _BelairDot11PhyAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 8, 1)
)
belairDot11PhyAntennaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    belairDot11PhyAntennaEntry.setStatus("current")


class _BelairDot11PhyAntennaLocation_Type(Integer32):
    """Custom type belairDot11PhyAntennaLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_BelairDot11PhyAntennaLocation_Type.__name__ = "Integer32"
_BelairDot11PhyAntennaLocation_Object = MibTableColumn
belairDot11PhyAntennaLocation = _BelairDot11PhyAntennaLocation_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 8, 1, 1),
    _BelairDot11PhyAntennaLocation_Type()
)
belairDot11PhyAntennaLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyAntennaLocation.setStatus("current")


class _BelairDot11PhyAntennaNumber_Type(Integer32):
    """Custom type belairDot11PhyAntennaNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BelairDot11PhyAntennaNumber_Type.__name__ = "Integer32"
_BelairDot11PhyAntennaNumber_Object = MibTableColumn
belairDot11PhyAntennaNumber = _BelairDot11PhyAntennaNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 8, 1, 2),
    _BelairDot11PhyAntennaNumber_Type()
)
belairDot11PhyAntennaNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyAntennaNumber.setStatus("current")
_BelairDot11PhyAntennaGain_Type = Integer32
_BelairDot11PhyAntennaGain_Object = MibTableColumn
belairDot11PhyAntennaGain = _BelairDot11PhyAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 8, 1, 3),
    _BelairDot11PhyAntennaGain_Type()
)
belairDot11PhyAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyAntennaGain.setUnits("dbi")
_BelairDot11PhyLinkDistance_Type = Integer32
_BelairDot11PhyLinkDistance_Object = MibTableColumn
belairDot11PhyLinkDistance = _BelairDot11PhyLinkDistance_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 8, 1, 4),
    _BelairDot11PhyLinkDistance_Type()
)
belairDot11PhyLinkDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyLinkDistance.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyLinkDistance.setUnits("km")


class _BelairDot11PhyAntennaGainSupported_Type(OctetString):
    """Custom type belairDot11PhyAntennaGainSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BelairDot11PhyAntennaGainSupported_Type.__name__ = "OctetString"
_BelairDot11PhyAntennaGainSupported_Object = MibTableColumn
belairDot11PhyAntennaGainSupported = _BelairDot11PhyAntennaGainSupported_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 8, 1, 5),
    _BelairDot11PhyAntennaGainSupported_Type()
)
belairDot11PhyAntennaGainSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11PhyAntennaGainSupported.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyAntennaGainSupported.setUnits("dbi")


class _BelairDot11PhyEnergyDetectThresh_Type(Integer32):
    """Custom type belairDot11PhyEnergyDetectThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 45),
    )


_BelairDot11PhyEnergyDetectThresh_Type.__name__ = "Integer32"
_BelairDot11PhyEnergyDetectThresh_Object = MibTableColumn
belairDot11PhyEnergyDetectThresh = _BelairDot11PhyEnergyDetectThresh_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 8, 1, 6),
    _BelairDot11PhyEnergyDetectThresh_Type()
)
belairDot11PhyEnergyDetectThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyEnergyDetectThresh.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyEnergyDetectThresh.setUnits("db")
_BelairDot11PhyTxPowerTable_Object = MibTable
belairDot11PhyTxPowerTable = _BelairDot11PhyTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9)
)
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerTable.setStatus("current")
_BelairDot11PhyTxPowerEntry_Object = MibTableRow
belairDot11PhyTxPowerEntry = _BelairDot11PhyTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9, 1)
)
belairDot11PhyTxPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerEntry.setStatus("current")
_BelairDot11PhyTxPowerLevel_Type = Integer32
_BelairDot11PhyTxPowerLevel_Object = MibTableColumn
belairDot11PhyTxPowerLevel = _BelairDot11PhyTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9, 1, 1),
    _BelairDot11PhyTxPowerLevel_Type()
)
belairDot11PhyTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerLevel.setUnits("dbm")
_BelairDot11PhyTxPowerAuto_Type = TruthValue
_BelairDot11PhyTxPowerAuto_Object = MibTableColumn
belairDot11PhyTxPowerAuto = _BelairDot11PhyTxPowerAuto_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9, 1, 2),
    _BelairDot11PhyTxPowerAuto_Type()
)
belairDot11PhyTxPowerAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerAuto.setStatus("current")


class _BelairDot11PhyTxPowerTargetRssi_Type(Integer32):
    """Custom type belairDot11PhyTxPowerTargetRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_BelairDot11PhyTxPowerTargetRssi_Type.__name__ = "Integer32"
_BelairDot11PhyTxPowerTargetRssi_Object = MibTableColumn
belairDot11PhyTxPowerTargetRssi = _BelairDot11PhyTxPowerTargetRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9, 1, 3),
    _BelairDot11PhyTxPowerTargetRssi_Type()
)
belairDot11PhyTxPowerTargetRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerTargetRssi.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerTargetRssi.setUnits("dbm")
_BelairDot11PhyTxPowerAutoMaximum_Type = Integer32
_BelairDot11PhyTxPowerAutoMaximum_Object = MibTableColumn
belairDot11PhyTxPowerAutoMaximum = _BelairDot11PhyTxPowerAutoMaximum_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9, 1, 4),
    _BelairDot11PhyTxPowerAutoMaximum_Type()
)
belairDot11PhyTxPowerAutoMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerAutoMaximum.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerAutoMaximum.setUnits("dbm")
_BelairDot11PhyTxPowerMinimum_Type = Integer32
_BelairDot11PhyTxPowerMinimum_Object = MibTableColumn
belairDot11PhyTxPowerMinimum = _BelairDot11PhyTxPowerMinimum_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9, 1, 5),
    _BelairDot11PhyTxPowerMinimum_Type()
)
belairDot11PhyTxPowerMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerMinimum.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerMinimum.setUnits("dbm")
_BelairDot11PhyTxPowerMaximum_Type = Integer32
_BelairDot11PhyTxPowerMaximum_Object = MibTableColumn
belairDot11PhyTxPowerMaximum = _BelairDot11PhyTxPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9, 1, 6),
    _BelairDot11PhyTxPowerMaximum_Type()
)
belairDot11PhyTxPowerMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerMaximum.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerMaximum.setUnits("dbm")
_BelairDot11PhyTxPowerActual_Type = Integer32
_BelairDot11PhyTxPowerActual_Object = MibTableColumn
belairDot11PhyTxPowerActual = _BelairDot11PhyTxPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 9, 1, 7),
    _BelairDot11PhyTxPowerActual_Type()
)
belairDot11PhyTxPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerActual.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11PhyTxPowerActual.setUnits("dbm")
_BelairDot11ConfigTable_Object = MibTable
belairDot11ConfigTable = _BelairDot11ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10)
)
if mibBuilder.loadTexts:
    belairDot11ConfigTable.setStatus("current")
_BelairDot11ConfigEntry_Object = MibTableRow
belairDot11ConfigEntry = _BelairDot11ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1)
)
belairDot11ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    belairDot11ConfigEntry.setStatus("current")
_BelairDot11ApAdminState_Type = BelAirAdminState
_BelairDot11ApAdminState_Object = MibTableColumn
belairDot11ApAdminState = _BelairDot11ApAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 1),
    _BelairDot11ApAdminState_Type()
)
belairDot11ApAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11ApAdminState.setStatus("current")
_BelairDot11QosWMM_Type = TruthValue
_BelairDot11QosWMM_Object = MibTableColumn
belairDot11QosWMM = _BelairDot11QosWMM_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 2),
    _BelairDot11QosWMM_Type()
)
belairDot11QosWMM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11QosWMM.setStatus("current")
_BelairDot11QosUAPSD_Type = TruthValue
_BelairDot11QosUAPSD_Object = MibTableColumn
belairDot11QosUAPSD = _BelairDot11QosUAPSD_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 3),
    _BelairDot11QosUAPSD_Type()
)
belairDot11QosUAPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11QosUAPSD.setStatus("current")


class _BelairDot11QosMapping_Type(Integer32):
    """Custom type belairDot11QosMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qosMappingUP", 1),
          ("qosMappingDSCP", 2),
          ("qosMappingBOTH", 3))
    )


_BelairDot11QosMapping_Type.__name__ = "Integer32"
_BelairDot11QosMapping_Object = MibTableColumn
belairDot11QosMapping = _BelairDot11QosMapping_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 4),
    _BelairDot11QosMapping_Type()
)
belairDot11QosMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11QosMapping.setStatus("current")


class _BelairDot11QosSchedule_Type(Integer32):
    """Custom type belairDot11QosSchedule based on Integer32"""
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
        *(("qosScheduleEDCA", 1),
          ("qosScheduleSPQ", 2),
          ("qosScheduleLSPQ", 3),
          ("qosScheduleT1", 4))
    )


_BelairDot11QosSchedule_Type.__name__ = "Integer32"
_BelairDot11QosSchedule_Object = MibTableColumn
belairDot11QosSchedule = _BelairDot11QosSchedule_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 5),
    _BelairDot11QosSchedule_Type()
)
belairDot11QosSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11QosSchedule.setStatus("current")
_BelairDot11AdvColllisionCtrl_Type = TruthValue
_BelairDot11AdvColllisionCtrl_Object = MibTableColumn
belairDot11AdvColllisionCtrl = _BelairDot11AdvColllisionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 6),
    _BelairDot11AdvColllisionCtrl_Type()
)
belairDot11AdvColllisionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11AdvColllisionCtrl.setStatus("current")
_BelairDot11RateAwareFairness_Type = TruthValue
_BelairDot11RateAwareFairness_Object = MibTableColumn
belairDot11RateAwareFairness = _BelairDot11RateAwareFairness_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 7),
    _BelairDot11RateAwareFairness_Type()
)
belairDot11RateAwareFairness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11RateAwareFairness.setStatus("current")
_BelairDot11DeauthDos_Type = TruthValue
_BelairDot11DeauthDos_Object = MibTableColumn
belairDot11DeauthDos = _BelairDot11DeauthDos_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 8),
    _BelairDot11DeauthDos_Type()
)
belairDot11DeauthDos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11DeauthDos.setStatus("current")
_BelairDot11NavDos_Type = TruthValue
_BelairDot11NavDos_Object = MibTableColumn
belairDot11NavDos = _BelairDot11NavDos_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 9),
    _BelairDot11NavDos_Type()
)
belairDot11NavDos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11NavDos.setStatus("current")


class _BelairDot11NavDosLimit_Type(Integer32):
    """Custom type belairDot11NavDosLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(320, 32767),
    )


_BelairDot11NavDosLimit_Type.__name__ = "Integer32"
_BelairDot11NavDosLimit_Object = MibTableColumn
belairDot11NavDosLimit = _BelairDot11NavDosLimit_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 10),
    _BelairDot11NavDosLimit_Type()
)
belairDot11NavDosLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11NavDosLimit.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11NavDosLimit.setUnits("uSecs")
_BelairDot11DhcpUnicast_Type = TruthValue
_BelairDot11DhcpUnicast_Object = MibTableColumn
belairDot11DhcpUnicast = _BelairDot11DhcpUnicast_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 11),
    _BelairDot11DhcpUnicast_Type()
)
belairDot11DhcpUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11DhcpUnicast.setStatus("current")
_BelairDot11ClientAuthTrap_Type = TruthValue
_BelairDot11ClientAuthTrap_Object = MibTableColumn
belairDot11ClientAuthTrap = _BelairDot11ClientAuthTrap_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 12),
    _BelairDot11ClientAuthTrap_Type()
)
belairDot11ClientAuthTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11ClientAuthTrap.setStatus("current")


class _BelairDot11RtsCtsThresh_Type(Integer32):
    """Custom type belairDot11RtsCtsThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2347),
    )


_BelairDot11RtsCtsThresh_Type.__name__ = "Integer32"
_BelairDot11RtsCtsThresh_Object = MibTableColumn
belairDot11RtsCtsThresh = _BelairDot11RtsCtsThresh_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 1, 10, 1, 13),
    _BelairDot11RtsCtsThresh_Type()
)
belairDot11RtsCtsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairDot11RtsCtsThresh.setStatus("current")
_BelairDot11Traps_ObjectIdentity = ObjectIdentity
belairDot11Traps = _BelairDot11Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 2)
)
if mibBuilder.loadTexts:
    belairDot11Traps.setStatus("current")
_BelairDot11TrapsV2_ObjectIdentity = ObjectIdentity
belairDot11TrapsV2 = _BelairDot11TrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 2, 0)
)
if mibBuilder.loadTexts:
    belairDot11TrapsV2.setStatus("current")
_BelairDot11Conformance_ObjectIdentity = ObjectIdentity
belairDot11Conformance = _BelairDot11Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 3)
)
if mibBuilder.loadTexts:
    belairDot11Conformance.setStatus("current")

# Managed Objects groups

belairDot11ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 3, 1)
)
belairDot11ObjectGroup.setObjects(
      *(("BELAIR-IEEE802DOT11", "belairDot11StaConfigMode"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaMaxAssociated"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigPeerMac"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigAssociatedMac"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigWirelessBridgeEnable"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigAclEnable"),
        ("BELAIR-IEEE802DOT11", "belairDot11SsidName"),
        ("BELAIR-IEEE802DOT11", "belairDot11SsidVlanId"),
        ("BELAIR-IEEE802DOT11", "belairDot11SsidIfIndex"),
        ("BELAIR-IEEE802DOT11", "belairDot11SsidRowStatus"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigAuthenType"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigKeyLen"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigKeyValue"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigRekeyType"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigRekeyPkts"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigRekeyInterval"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigKeyUpdate"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigCipherType"),
        ("BELAIR-IEEE802DOT11", "belairDot11SecuConfigEnable"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaCurrentAssociated"),
        ("BELAIR-IEEE802DOT11", "belairDot11AclRowStatus"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigStationIdEnable"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigAcctSessionIdEnable"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigNasIdentifier"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigRadAcctEnable"),
        ("BELAIR-IEEE802DOT11", "belairDot11ApSurveyBssType"),
        ("BELAIR-IEEE802DOT11", "belairDot11ApSurveySsid"),
        ("BELAIR-IEEE802DOT11", "belairDot11ApSurveyChannel"),
        ("BELAIR-IEEE802DOT11", "belairDot11ApSurveyPrivacy"),
        ("BELAIR-IEEE802DOT11", "belairDot11ApSurveyRssi"),
        ("BELAIR-IEEE802DOT11", "belairDot11ApSurveySecsSinceLastSeen"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaLastSpoofedSecureMac"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyTxPowerActual"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyTxPowerMaximum"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyTxPowerMinimum"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyTxPowerAutoMaximum"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyTxPowerTargetRssi"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyTxPowerAuto"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyTxPowerLevel"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyLinkDistance"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyAntennaGain"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyAntennaNumber"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyAntennaLocation"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelFrqBand"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelScanList"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelCurrent"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelAutomatic"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelSecondary"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelPrimary"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelBandwidth"),
        ("BELAIR-IEEE802DOT11", "belairDot11ApAdminState"),
        ("BELAIR-IEEE802DOT11", "belairDot11RtsCtsThresh"),
        ("BELAIR-IEEE802DOT11", "belairDot11ClientAuthTrap"),
        ("BELAIR-IEEE802DOT11", "belairDot11DhcpUnicast"),
        ("BELAIR-IEEE802DOT11", "belairDot11NavDosLimit"),
        ("BELAIR-IEEE802DOT11", "belairDot11NavDos"),
        ("BELAIR-IEEE802DOT11", "belairDot11DeauthDos"),
        ("BELAIR-IEEE802DOT11", "belairDot11RateAwareFairness"),
        ("BELAIR-IEEE802DOT11", "belairDot11AdvColllisionCtrl"),
        ("BELAIR-IEEE802DOT11", "belairDot11QosSchedule"),
        ("BELAIR-IEEE802DOT11", "belairDot11QosMapping"),
        ("BELAIR-IEEE802DOT11", "belairDot11QosUAPSD"),
        ("BELAIR-IEEE802DOT11", "belairDot11QosWMM"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyEnergyDetectThresh"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelLastScanTime"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelScan"),
        ("BELAIR-IEEE802DOT11", "belairDot11AclMacAddress"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaConfigRssi"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyAntennaGainSupported"),
        ("BELAIR-IEEE802DOT11", "belairDot11PhyChannelScanStatus"))
)
if mibBuilder.loadTexts:
    belairDot11ObjectGroup.setStatus("current")


# Notification objects

belairDot11SecureMacSpoofed = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 4, 2, 0, 1)
)
belairDot11SecureMacSpoofed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BELAIR-IEEE802DOT11", "belairDot11StaLastSpoofedSecureMac"))
)
if mibBuilder.loadTexts:
    belairDot11SecureMacSpoofed.setStatus(
        "current"
    )

belairDot11DhcpAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 4, 2, 0, 2)
)
belairDot11DhcpAttack.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    belairDot11DhcpAttack.setStatus(
        "current"
    )


# Notifications groups

belairDot11TrapObjectGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 3, 2)
)
belairDot11TrapObjectGroup.setObjects(
      *(("BELAIR-IEEE802DOT11", "belairDot11SecureMacSpoofed"),
        ("BELAIR-IEEE802DOT11", "belairDot11DhcpAttack"))
)
if mibBuilder.loadTexts:
    belairDot11TrapObjectGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-IEEE802DOT11",
    **{"belairIeeeDot11Module": belairIeeeDot11Module,
       "belairDot11Objects": belairDot11Objects,
       "belairDot11StaConfigTable": belairDot11StaConfigTable,
       "belairDot11StaConfigEntry": belairDot11StaConfigEntry,
       "belairDot11StaConfigMode": belairDot11StaConfigMode,
       "belairDot11StaMaxAssociated": belairDot11StaMaxAssociated,
       "belairDot11StaConfigPeerMac": belairDot11StaConfigPeerMac,
       "belairDot11StaConfigAssociatedMac": belairDot11StaConfigAssociatedMac,
       "belairDot11StaConfigWirelessBridgeEnable": belairDot11StaConfigWirelessBridgeEnable,
       "belairDot11StaConfigAclEnable": belairDot11StaConfigAclEnable,
       "belairDot11StaConfigRssi": belairDot11StaConfigRssi,
       "belairDot11StaCurrentAssociated": belairDot11StaCurrentAssociated,
       "belairDot11StaConfigStationIdEnable": belairDot11StaConfigStationIdEnable,
       "belairDot11StaConfigAcctSessionIdEnable": belairDot11StaConfigAcctSessionIdEnable,
       "belairDot11StaConfigNasIdentifier": belairDot11StaConfigNasIdentifier,
       "belairDot11StaConfigRadAcctEnable": belairDot11StaConfigRadAcctEnable,
       "belairDot11StaLastSpoofedSecureMac": belairDot11StaLastSpoofedSecureMac,
       "belairDot11SsidTable": belairDot11SsidTable,
       "belairDot11SsidEntry": belairDot11SsidEntry,
       "belairDot11SsidIndex": belairDot11SsidIndex,
       "belairDot11SsidName": belairDot11SsidName,
       "belairDot11SsidVlanId": belairDot11SsidVlanId,
       "belairDot11SsidIfIndex": belairDot11SsidIfIndex,
       "belairDot11SsidRowStatus": belairDot11SsidRowStatus,
       "belairDot11SecuConfigTable": belairDot11SecuConfigTable,
       "belairDot11SecuConfigEntry": belairDot11SecuConfigEntry,
       "belairDot11SecuConfigIndex": belairDot11SecuConfigIndex,
       "belairDot11SecuConfigAuthenType": belairDot11SecuConfigAuthenType,
       "belairDot11SecuConfigKeyLen": belairDot11SecuConfigKeyLen,
       "belairDot11SecuConfigKeyValue": belairDot11SecuConfigKeyValue,
       "belairDot11SecuConfigRekeyType": belairDot11SecuConfigRekeyType,
       "belairDot11SecuConfigRekeyPkts": belairDot11SecuConfigRekeyPkts,
       "belairDot11SecuConfigRekeyInterval": belairDot11SecuConfigRekeyInterval,
       "belairDot11SecuConfigKeyUpdate": belairDot11SecuConfigKeyUpdate,
       "belairDot11SecuConfigCipherType": belairDot11SecuConfigCipherType,
       "belairDot11SecuConfigEnable": belairDot11SecuConfigEnable,
       "belairDot11AclTable": belairDot11AclTable,
       "belairDot11AclEntry": belairDot11AclEntry,
       "belairDot11AclIndex": belairDot11AclIndex,
       "belairDot11AclMacAddress": belairDot11AclMacAddress,
       "belairDot11AclRowStatus": belairDot11AclRowStatus,
       "belairDot11ApSurveyTable": belairDot11ApSurveyTable,
       "belairDot11ApSurveyEntry": belairDot11ApSurveyEntry,
       "belairDot11ApSurveyMacAddress": belairDot11ApSurveyMacAddress,
       "belairDot11ApSurveyBssType": belairDot11ApSurveyBssType,
       "belairDot11ApSurveySsid": belairDot11ApSurveySsid,
       "belairDot11ApSurveyChannel": belairDot11ApSurveyChannel,
       "belairDot11ApSurveyPrivacy": belairDot11ApSurveyPrivacy,
       "belairDot11ApSurveyRssi": belairDot11ApSurveyRssi,
       "belairDot11ApSurveySecsSinceLastSeen": belairDot11ApSurveySecsSinceLastSeen,
       "belairDot11PhyChannelTable": belairDot11PhyChannelTable,
       "belairDot11PhyChannelEntry": belairDot11PhyChannelEntry,
       "belairDot11PhyChannelPrimary": belairDot11PhyChannelPrimary,
       "belairDot11PhyChannelSecondary": belairDot11PhyChannelSecondary,
       "belairDot11PhyChannelAutomatic": belairDot11PhyChannelAutomatic,
       "belairDot11PhyChannelBandwidth": belairDot11PhyChannelBandwidth,
       "belairDot11PhyChannelFrqBand": belairDot11PhyChannelFrqBand,
       "belairDot11PhyChannelCurrent": belairDot11PhyChannelCurrent,
       "belairDot11PhyChannelScanList": belairDot11PhyChannelScanList,
       "belairDot11PhyChannelScan": belairDot11PhyChannelScan,
       "belairDot11PhyChannelScanStatus": belairDot11PhyChannelScanStatus,
       "belairDot11PhyChannelLastScanTime": belairDot11PhyChannelLastScanTime,
       "belairDot11PhyAntennaTable": belairDot11PhyAntennaTable,
       "belairDot11PhyAntennaEntry": belairDot11PhyAntennaEntry,
       "belairDot11PhyAntennaLocation": belairDot11PhyAntennaLocation,
       "belairDot11PhyAntennaNumber": belairDot11PhyAntennaNumber,
       "belairDot11PhyAntennaGain": belairDot11PhyAntennaGain,
       "belairDot11PhyLinkDistance": belairDot11PhyLinkDistance,
       "belairDot11PhyAntennaGainSupported": belairDot11PhyAntennaGainSupported,
       "belairDot11PhyEnergyDetectThresh": belairDot11PhyEnergyDetectThresh,
       "belairDot11PhyTxPowerTable": belairDot11PhyTxPowerTable,
       "belairDot11PhyTxPowerEntry": belairDot11PhyTxPowerEntry,
       "belairDot11PhyTxPowerLevel": belairDot11PhyTxPowerLevel,
       "belairDot11PhyTxPowerAuto": belairDot11PhyTxPowerAuto,
       "belairDot11PhyTxPowerTargetRssi": belairDot11PhyTxPowerTargetRssi,
       "belairDot11PhyTxPowerAutoMaximum": belairDot11PhyTxPowerAutoMaximum,
       "belairDot11PhyTxPowerMinimum": belairDot11PhyTxPowerMinimum,
       "belairDot11PhyTxPowerMaximum": belairDot11PhyTxPowerMaximum,
       "belairDot11PhyTxPowerActual": belairDot11PhyTxPowerActual,
       "belairDot11ConfigTable": belairDot11ConfigTable,
       "belairDot11ConfigEntry": belairDot11ConfigEntry,
       "belairDot11ApAdminState": belairDot11ApAdminState,
       "belairDot11QosWMM": belairDot11QosWMM,
       "belairDot11QosUAPSD": belairDot11QosUAPSD,
       "belairDot11QosMapping": belairDot11QosMapping,
       "belairDot11QosSchedule": belairDot11QosSchedule,
       "belairDot11AdvColllisionCtrl": belairDot11AdvColllisionCtrl,
       "belairDot11RateAwareFairness": belairDot11RateAwareFairness,
       "belairDot11DeauthDos": belairDot11DeauthDos,
       "belairDot11NavDos": belairDot11NavDos,
       "belairDot11NavDosLimit": belairDot11NavDosLimit,
       "belairDot11DhcpUnicast": belairDot11DhcpUnicast,
       "belairDot11ClientAuthTrap": belairDot11ClientAuthTrap,
       "belairDot11RtsCtsThresh": belairDot11RtsCtsThresh,
       "belairDot11Traps": belairDot11Traps,
       "belairDot11TrapsV2": belairDot11TrapsV2,
       "belairDot11SecureMacSpoofed": belairDot11SecureMacSpoofed,
       "belairDot11DhcpAttack": belairDot11DhcpAttack,
       "belairDot11Conformance": belairDot11Conformance,
       "belairDot11ObjectGroup": belairDot11ObjectGroup,
       "belairDot11TrapObjectGroup": belairDot11TrapObjectGroup}
)
