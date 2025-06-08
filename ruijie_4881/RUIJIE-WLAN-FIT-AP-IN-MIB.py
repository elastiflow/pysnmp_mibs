# SNMP MIB module (RUIJIE-WLAN-FIT-AP-IN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WLAN-FIT-AP-IN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:52:30 2025
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

(ruijieApApName,
 ruijieApCfgRadioId,
 ruijieApMacAddr,
 ruijieApgWlanId,
 ruijieStaMacAddr) = mibBuilder.importSymbols(
    "RUIJIE-AC-MGMT-MIB",
    "ruijieApApName",
    "ruijieApCfgRadioId",
    "ruijieApMacAddr",
    "ruijieApgWlanId",
    "ruijieStaMacAddr")

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

ruijieFitApMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83)
)
if mibBuilder.loadTexts:
    ruijieFitApMibModule.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieAlarmTraps_ObjectIdentity = ObjectIdentity
ruijieAlarmTraps = _RuijieAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 0)
)
_RuijieSystemInfoConfigObjects_ObjectIdentity = ObjectIdentity
ruijieSystemInfoConfigObjects = _RuijieSystemInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1)
)
_RuijieDomain_Type = DisplayString
_RuijieDomain_Object = MibScalar
ruijieDomain = _RuijieDomain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 1),
    _RuijieDomain_Type()
)
ruijieDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDomain.setStatus("current")


class _RuijiePhySeparatedEnable_Type(Integer32):
    """Custom type ruijiePhySeparatedEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RuijiePhySeparatedEnable_Type.__name__ = "Integer32"
_RuijiePhySeparatedEnable_Object = MibScalar
ruijiePhySeparatedEnable = _RuijiePhySeparatedEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 2),
    _RuijiePhySeparatedEnable_Type()
)
ruijiePhySeparatedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePhySeparatedEnable.setStatus("current")


class _RuijieForfendDosAttackEnable_Type(Integer32):
    """Custom type ruijieForfendDosAttackEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RuijieForfendDosAttackEnable_Type.__name__ = "Integer32"
_RuijieForfendDosAttackEnable_Object = MibScalar
ruijieForfendDosAttackEnable = _RuijieForfendDosAttackEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 3),
    _RuijieForfendDosAttackEnable_Type()
)
ruijieForfendDosAttackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieForfendDosAttackEnable.setStatus("current")
_RuijieAcTrafficLoadBalancing_Type = TruthValue
_RuijieAcTrafficLoadBalancing_Object = MibScalar
ruijieAcTrafficLoadBalancing = _RuijieAcTrafficLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 4),
    _RuijieAcTrafficLoadBalancing_Type()
)
ruijieAcTrafficLoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcTrafficLoadBalancing.setStatus("current")
_RuijieAcTrafficLoadBalanceThreshold_Type = Integer32
_RuijieAcTrafficLoadBalanceThreshold_Object = MibScalar
ruijieAcTrafficLoadBalanceThreshold = _RuijieAcTrafficLoadBalanceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 5),
    _RuijieAcTrafficLoadBalanceThreshold_Type()
)
ruijieAcTrafficLoadBalanceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcTrafficLoadBalanceThreshold.setStatus("current")
_RuijieAcTrafficOtherAPThresholdValue_Type = Integer32
_RuijieAcTrafficOtherAPThresholdValue_Object = MibScalar
ruijieAcTrafficOtherAPThresholdValue = _RuijieAcTrafficOtherAPThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 6),
    _RuijieAcTrafficOtherAPThresholdValue_Type()
)
ruijieAcTrafficOtherAPThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcTrafficOtherAPThresholdValue.setStatus("current")
_RuijieAcAPWIDSScanningMode_Type = Integer32
_RuijieAcAPWIDSScanningMode_Object = MibScalar
ruijieAcAPWIDSScanningMode = _RuijieAcAPWIDSScanningMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 7),
    _RuijieAcAPWIDSScanningMode_Type()
)
ruijieAcAPWIDSScanningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcAPWIDSScanningMode.setStatus("current")
_RuijieAcAPLegitimateMode_Type = Integer32
_RuijieAcAPLegitimateMode_Object = MibScalar
ruijieAcAPLegitimateMode = _RuijieAcAPLegitimateMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 8),
    _RuijieAcAPLegitimateMode_Type()
)
ruijieAcAPLegitimateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAPLegitimateMode.setStatus("current")
_RuijieAcAPTreatMode_Type = Integer32
_RuijieAcAPTreatMode_Object = MibScalar
ruijieAcAPTreatMode = _RuijieAcAPTreatMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 9),
    _RuijieAcAPTreatMode_Type()
)
ruijieAcAPTreatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAPTreatMode.setStatus("current")
_RuijieAcAssociationFailureTotalTimes_Type = Counter32
_RuijieAcAssociationFailureTotalTimes_Object = MibScalar
ruijieAcAssociationFailureTotalTimes = _RuijieAcAssociationFailureTotalTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 10),
    _RuijieAcAssociationFailureTotalTimes_Type()
)
ruijieAcAssociationFailureTotalTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAssociationFailureTotalTimes.setStatus("current")
_RuijieAcAirIfRxTotalDataFrams_Type = Counter32
_RuijieAcAirIfRxTotalDataFrams_Object = MibScalar
ruijieAcAirIfRxTotalDataFrams = _RuijieAcAirIfRxTotalDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 11),
    _RuijieAcAirIfRxTotalDataFrams_Type()
)
ruijieAcAirIfRxTotalDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirIfRxTotalDataFrams.setStatus("current")
_RuijieAcAirIfTxTotalDataFrams_Type = Counter32
_RuijieAcAirIfTxTotalDataFrams_Object = MibScalar
ruijieAcAirIfTxTotalDataFrams = _RuijieAcAirIfTxTotalDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 12),
    _RuijieAcAirIfTxTotalDataFrams_Type()
)
ruijieAcAirIfTxTotalDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirIfTxTotalDataFrams.setStatus("current")
_RuijieAcAirIfTxTotalLostFrams_Type = Counter32
_RuijieAcAirIfTxTotalLostFrams_Object = MibScalar
ruijieAcAirIfTxTotalLostFrams = _RuijieAcAirIfTxTotalLostFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 13),
    _RuijieAcAirIfTxTotalLostFrams_Type()
)
ruijieAcAirIfTxTotalLostFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirIfTxTotalLostFrams.setStatus("current")
_RuijieAcAirIfTxAssociateFrams_Type = Counter32
_RuijieAcAirIfTxAssociateFrams_Object = MibScalar
ruijieAcAirIfTxAssociateFrams = _RuijieAcAirIfTxAssociateFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 14),
    _RuijieAcAirIfTxAssociateFrams_Type()
)
ruijieAcAirIfTxAssociateFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirIfTxAssociateFrams.setStatus("current")
_RuijieAcAirIfRxAssociateFrams_Type = Counter32
_RuijieAcAirIfRxAssociateFrams_Object = MibScalar
ruijieAcAirIfRxAssociateFrams = _RuijieAcAirIfRxAssociateFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 15),
    _RuijieAcAirIfRxAssociateFrams_Type()
)
ruijieAcAirIfRxAssociateFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirIfRxAssociateFrams.setStatus("current")
_RuijieAcAirIfBeaconTotalFrams_Type = Counter32
_RuijieAcAirIfBeaconTotalFrams_Object = MibScalar
ruijieAcAirIfBeaconTotalFrams = _RuijieAcAirIfBeaconTotalFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 16),
    _RuijieAcAirIfBeaconTotalFrams_Type()
)
ruijieAcAirIfBeaconTotalFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirIfBeaconTotalFrams.setStatus("current")
_RuijieAcAirIfRxTotalDataBytes_Type = Counter32
_RuijieAcAirIfRxTotalDataBytes_Object = MibScalar
ruijieAcAirIfRxTotalDataBytes = _RuijieAcAirIfRxTotalDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 17),
    _RuijieAcAirIfRxTotalDataBytes_Type()
)
ruijieAcAirIfRxTotalDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirIfRxTotalDataBytes.setStatus("current")
_RuijieAcAirIfTxTotalDataBytes_Type = Counter32
_RuijieAcAirIfTxTotalDataBytes_Object = MibScalar
ruijieAcAirIfTxTotalDataBytes = _RuijieAcAirIfTxTotalDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 18),
    _RuijieAcAirIfTxTotalDataBytes_Type()
)
ruijieAcAirIfTxTotalDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirIfTxTotalDataBytes.setStatus("current")
_RuijieAcAirRxFlux_Type = Integer32
_RuijieAcAirRxFlux_Object = MibScalar
ruijieAcAirRxFlux = _RuijieAcAirRxFlux_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 19),
    _RuijieAcAirRxFlux_Type()
)
ruijieAcAirRxFlux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirRxFlux.setStatus("current")
_RuijieAcAirTxFlux_Type = Integer32
_RuijieAcAirTxFlux_Object = MibScalar
ruijieAcAirTxFlux = _RuijieAcAirTxFlux_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 1, 20),
    _RuijieAcAirTxFlux_Type()
)
ruijieAcAirTxFlux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAirTxFlux.setStatus("current")
_RuijieInfoConfigObjects_ObjectIdentity = ObjectIdentity
ruijieInfoConfigObjects = _RuijieInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 2)
)
_RuijieInfoConfigTable_Object = MibTable
ruijieInfoConfigTable = _RuijieInfoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieInfoConfigTable.setStatus("current")
_RuijieInfoConfigTableEntry_Object = MibTableRow
ruijieInfoConfigTableEntry = _RuijieInfoConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 2, 1, 1)
)
ruijieInfoConfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieInfoConfigTableEntry.setStatus("current")
_RuijieAcAPWIDSWorkMode_Type = Integer32
_RuijieAcAPWIDSWorkMode_Object = MibTableColumn
ruijieAcAPWIDSWorkMode = _RuijieAcAPWIDSWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 2, 1, 1, 1),
    _RuijieAcAPWIDSWorkMode_Type()
)
ruijieAcAPWIDSWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcAPWIDSWorkMode.setStatus("current")
_RuijieStationConfigObjects_ObjectIdentity = ObjectIdentity
ruijieStationConfigObjects = _RuijieStationConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 4)
)
_RuijieConfigStaInfoTable_Object = MibTable
ruijieConfigStaInfoTable = _RuijieConfigStaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieConfigStaInfoTable.setStatus("current")
_RuijieConfigStaInfoTableEntry_Object = MibTableRow
ruijieConfigStaInfoTableEntry = _RuijieConfigStaInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 4, 1, 1)
)
ruijieConfigStaInfoTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieStaMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieConfigStaInfoTableEntry.setStatus("current")
_RuijieACconfigAPBandwith_Type = Integer32
_RuijieACconfigAPBandwith_Object = MibTableColumn
ruijieACconfigAPBandwith = _RuijieACconfigAPBandwith_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 4, 1, 1, 1),
    _RuijieACconfigAPBandwith_Type()
)
ruijieACconfigAPBandwith.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieACconfigAPBandwith.setStatus("current")
_RuijieAirIfStatisticsObjects_ObjectIdentity = ObjectIdentity
ruijieAirIfStatisticsObjects = _RuijieAirIfStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6)
)
_RuijieAirIfInfoStatisticsTable_Object = MibTable
ruijieAirIfInfoStatisticsTable = _RuijieAirIfInfoStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1)
)
if mibBuilder.loadTexts:
    ruijieAirIfInfoStatisticsTable.setStatus("current")
_RuijieAirIfInfoStatisticsTableEntry_Object = MibTableRow
ruijieAirIfInfoStatisticsTableEntry = _RuijieAirIfInfoStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1)
)
ruijieAirIfInfoStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieAirIfInfoStatisticsTableEntry.setStatus("current")
_RuijieRxTotalDataFrams_Type = Counter32
_RuijieRxTotalDataFrams_Object = MibTableColumn
ruijieRxTotalDataFrams = _RuijieRxTotalDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 1),
    _RuijieRxTotalDataFrams_Type()
)
ruijieRxTotalDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRxTotalDataFrams.setStatus("current")
_RuijieTxTotalDataFrams_Type = Counter32
_RuijieTxTotalDataFrams_Object = MibTableColumn
ruijieTxTotalDataFrams = _RuijieTxTotalDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 2),
    _RuijieTxTotalDataFrams_Type()
)
ruijieTxTotalDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTxTotalDataFrams.setStatus("current")
_RuijieTxLostDataFrams_Type = Counter32
_RuijieTxLostDataFrams_Object = MibTableColumn
ruijieTxLostDataFrams = _RuijieTxLostDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 3),
    _RuijieTxLostDataFrams_Type()
)
ruijieTxLostDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTxLostDataFrams.setStatus("current")
_RuijieTxAssociateFrams_Type = Counter32
_RuijieTxAssociateFrams_Object = MibTableColumn
ruijieTxAssociateFrams = _RuijieTxAssociateFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 4),
    _RuijieTxAssociateFrams_Type()
)
ruijieTxAssociateFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTxAssociateFrams.setStatus("current")
_RuijieRxAssociateFrams_Type = Counter32
_RuijieRxAssociateFrams_Object = MibTableColumn
ruijieRxAssociateFrams = _RuijieRxAssociateFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 5),
    _RuijieRxAssociateFrams_Type()
)
ruijieRxAssociateFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRxAssociateFrams.setStatus("current")
_RuijieBeaconFrams_Type = Counter32
_RuijieBeaconFrams_Object = MibTableColumn
ruijieBeaconFrams = _RuijieBeaconFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 6),
    _RuijieBeaconFrams_Type()
)
ruijieBeaconFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBeaconFrams.setStatus("current")
_RuijieRxTotalDataBytes_Type = Counter32
_RuijieRxTotalDataBytes_Object = MibTableColumn
ruijieRxTotalDataBytes = _RuijieRxTotalDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 7),
    _RuijieRxTotalDataBytes_Type()
)
ruijieRxTotalDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRxTotalDataBytes.setStatus("current")
_RuijieTxTotalDataBytes_Type = Counter32
_RuijieTxTotalDataBytes_Object = MibTableColumn
ruijieTxTotalDataBytes = _RuijieTxTotalDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 8),
    _RuijieTxTotalDataBytes_Type()
)
ruijieTxTotalDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTxTotalDataBytes.setStatus("current")
_RuijieRESUtilization_Type = Integer32
_RuijieRESUtilization_Object = MibTableColumn
ruijieRESUtilization = _RuijieRESUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 1, 1, 9),
    _RuijieRESUtilization_Type()
)
ruijieRESUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRESUtilization.setStatus("current")
_RuijieAirIfTxResendDataTable_Object = MibTable
ruijieAirIfTxResendDataTable = _RuijieAirIfTxResendDataTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 2)
)
if mibBuilder.loadTexts:
    ruijieAirIfTxResendDataTable.setStatus("current")
_RuijieAirIfTxResendDataTableEntry_Object = MibTableRow
ruijieAirIfTxResendDataTableEntry = _RuijieAirIfTxResendDataTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 2, 1)
)
ruijieAirIfTxResendDataTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieStaMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieAirIfTxResendDataTableEntry.setStatus("current")
_RuijieStaResendDataFrams_Type = Counter32
_RuijieStaResendDataFrams_Object = MibTableColumn
ruijieStaResendDataFrams = _RuijieStaResendDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 6, 2, 1, 1),
    _RuijieStaResendDataFrams_Type()
)
ruijieStaResendDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaResendDataFrams.setStatus("current")
_RuijieTermServiceStatistics_ObjectIdentity = ObjectIdentity
ruijieTermServiceStatistics = _RuijieTermServiceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7)
)
_RuijieTermServiceStatisticsWithSSID_ObjectIdentity = ObjectIdentity
ruijieTermServiceStatisticsWithSSID = _RuijieTermServiceStatisticsWithSSID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1)
)
_RuijieTermServiceStaticWithSSIDTable_Object = MibTable
ruijieTermServiceStaticWithSSIDTable = _RuijieTermServiceStaticWithSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieTermServiceStaticWithSSIDTable.setStatus("current")
_RuijieTermServiceStaticWithSSIDTableEntry_Object = MibTableRow
ruijieTermServiceStaticWithSSIDTableEntry = _RuijieTermServiceStaticWithSSIDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1)
)
ruijieTermServiceStaticWithSSIDTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ruijieTermServiceStaticWithSSIDTableEntry.setStatus("current")
_RuijieTotalUserNum_Type = Integer32
_RuijieTotalUserNum_Object = MibTableColumn
ruijieTotalUserNum = _RuijieTotalUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 1),
    _RuijieTotalUserNum_Type()
)
ruijieTotalUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalUserNum.setStatus("current")
_RuijieCurrentUserNum_Type = Integer32
_RuijieCurrentUserNum_Object = MibTableColumn
ruijieCurrentUserNum = _RuijieCurrentUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 2),
    _RuijieCurrentUserNum_Type()
)
ruijieCurrentUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCurrentUserNum.setStatus("current")
_RuijieStaReqAccessTimes_Type = Integer32
_RuijieStaReqAccessTimes_Object = MibTableColumn
ruijieStaReqAccessTimes = _RuijieStaReqAccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 3),
    _RuijieStaReqAccessTimes_Type()
)
ruijieStaReqAccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaReqAccessTimes.setStatus("current")
_RuijieRspStaAccessReqTimes_Type = Integer32
_RuijieRspStaAccessReqTimes_Object = MibTableColumn
ruijieRspStaAccessReqTimes = _RuijieRspStaAccessReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 4),
    _RuijieRspStaAccessReqTimes_Type()
)
ruijieRspStaAccessReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRspStaAccessReqTimes.setStatus("current")
_RuijieStaAccessSucessTimes_Type = Integer32
_RuijieStaAccessSucessTimes_Object = MibTableColumn
ruijieStaAccessSucessTimes = _RuijieStaAccessSucessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 5),
    _RuijieStaAccessSucessTimes_Type()
)
ruijieStaAccessSucessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAccessSucessTimes.setStatus("current")
_RuijieIneffiLinkVerifyFailTime_Type = Integer32
_RuijieIneffiLinkVerifyFailTime_Object = MibTableColumn
ruijieIneffiLinkVerifyFailTime = _RuijieIneffiLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 6),
    _RuijieIneffiLinkVerifyFailTime_Type()
)
ruijieIneffiLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIneffiLinkVerifyFailTime.setStatus("current")
_RuijieTimeoutLinkVerifyFailTime_Type = Integer32
_RuijieTimeoutLinkVerifyFailTime_Object = MibTableColumn
ruijieTimeoutLinkVerifyFailTime = _RuijieTimeoutLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 7),
    _RuijieTimeoutLinkVerifyFailTime_Type()
)
ruijieTimeoutLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeoutLinkVerifyFailTime.setStatus("current")
_RuijieInefficiencyLinkVerifyFailTime_Type = Integer32
_RuijieInefficiencyLinkVerifyFailTime_Object = MibTableColumn
ruijieInefficiencyLinkVerifyFailTime = _RuijieInefficiencyLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 8),
    _RuijieInefficiencyLinkVerifyFailTime_Type()
)
ruijieInefficiencyLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyLinkVerifyFailTime.setStatus("current")
_RuijieOtherReasonLinkVerifyFailTime_Type = Integer32
_RuijieOtherReasonLinkVerifyFailTime_Object = MibTableColumn
ruijieOtherReasonLinkVerifyFailTime = _RuijieOtherReasonLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 9),
    _RuijieOtherReasonLinkVerifyFailTime_Type()
)
ruijieOtherReasonLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonLinkVerifyFailTime.setStatus("current")
_RuijieIneffiAssociationFailTime_Type = Integer32
_RuijieIneffiAssociationFailTime_Object = MibTableColumn
ruijieIneffiAssociationFailTime = _RuijieIneffiAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 10),
    _RuijieIneffiAssociationFailTime_Type()
)
ruijieIneffiAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIneffiAssociationFailTime.setStatus("current")
_RuijieTimeoutAssociationFailTime_Type = Integer32
_RuijieTimeoutAssociationFailTime_Object = MibTableColumn
ruijieTimeoutAssociationFailTime = _RuijieTimeoutAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 11),
    _RuijieTimeoutAssociationFailTime_Type()
)
ruijieTimeoutAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeoutAssociationFailTime.setStatus("current")
_RuijieInefficiencyAssociationFailTime_Type = Integer32
_RuijieInefficiencyAssociationFailTime_Object = MibTableColumn
ruijieInefficiencyAssociationFailTime = _RuijieInefficiencyAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 12),
    _RuijieInefficiencyAssociationFailTime_Type()
)
ruijieInefficiencyAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyAssociationFailTime.setStatus("current")
_RuijieOtherReasonAssociationFailTime_Type = Integer32
_RuijieOtherReasonAssociationFailTime_Object = MibTableColumn
ruijieOtherReasonAssociationFailTime = _RuijieOtherReasonAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 13),
    _RuijieOtherReasonAssociationFailTime_Type()
)
ruijieOtherReasonAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonAssociationFailTime.setStatus("current")
_RuijieTotalReassociationAtmptTimes_Type = Integer32
_RuijieTotalReassociationAtmptTimes_Object = MibTableColumn
ruijieTotalReassociationAtmptTimes = _RuijieTotalReassociationAtmptTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 14),
    _RuijieTotalReassociationAtmptTimes_Type()
)
ruijieTotalReassociationAtmptTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalReassociationAtmptTimes.setStatus("current")
_RuijieTotalReassociationSuccessTimes_Type = Integer32
_RuijieTotalReassociationSuccessTimes_Object = MibTableColumn
ruijieTotalReassociationSuccessTimes = _RuijieTotalReassociationSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 15),
    _RuijieTotalReassociationSuccessTimes_Type()
)
ruijieTotalReassociationSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalReassociationSuccessTimes.setStatus("current")
_RuijieIneffiReassociationFailTime_Type = Integer32
_RuijieIneffiReassociationFailTime_Object = MibTableColumn
ruijieIneffiReassociationFailTime = _RuijieIneffiReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 16),
    _RuijieIneffiReassociationFailTime_Type()
)
ruijieIneffiReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIneffiReassociationFailTime.setStatus("current")
_RuijieTimeoutReassociationFailTime_Type = Integer32
_RuijieTimeoutReassociationFailTime_Object = MibTableColumn
ruijieTimeoutReassociationFailTime = _RuijieTimeoutReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 17),
    _RuijieTimeoutReassociationFailTime_Type()
)
ruijieTimeoutReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeoutReassociationFailTime.setStatus("current")
_RuijieInefficiencyReassociationFailTime_Type = Integer32
_RuijieInefficiencyReassociationFailTime_Object = MibTableColumn
ruijieInefficiencyReassociationFailTime = _RuijieInefficiencyReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 18),
    _RuijieInefficiencyReassociationFailTime_Type()
)
ruijieInefficiencyReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyReassociationFailTime.setStatus("current")
_RuijieOtherReasonReassociationFailTime_Type = Integer32
_RuijieOtherReasonReassociationFailTime_Object = MibTableColumn
ruijieOtherReasonReassociationFailTime = _RuijieOtherReasonReassociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 19),
    _RuijieOtherReasonReassociationFailTime_Type()
)
ruijieOtherReasonReassociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonReassociationFailTime.setStatus("current")
_RuijieTotalIdentificationAtmptTimes_Type = Integer32
_RuijieTotalIdentificationAtmptTimes_Object = MibTableColumn
ruijieTotalIdentificationAtmptTimes = _RuijieTotalIdentificationAtmptTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 20),
    _RuijieTotalIdentificationAtmptTimes_Type()
)
ruijieTotalIdentificationAtmptTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalIdentificationAtmptTimes.setStatus("current")
_RuijieTotalIdentificationSuccessTimes_Type = Integer32
_RuijieTotalIdentificationSuccessTimes_Object = MibTableColumn
ruijieTotalIdentificationSuccessTimes = _RuijieTotalIdentificationSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 21),
    _RuijieTotalIdentificationSuccessTimes_Type()
)
ruijieTotalIdentificationSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalIdentificationSuccessTimes.setStatus("current")
_RuijiePwdErrorIdentifyFailTime_Type = Integer32
_RuijiePwdErrorIdentifyFailTime_Object = MibTableColumn
ruijiePwdErrorIdentifyFailTime = _RuijiePwdErrorIdentifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 22),
    _RuijiePwdErrorIdentifyFailTime_Type()
)
ruijiePwdErrorIdentifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePwdErrorIdentifyFailTime.setStatus("current")
_RuijieIneffiIdentificationFailTime_Type = Integer32
_RuijieIneffiIdentificationFailTime_Object = MibTableColumn
ruijieIneffiIdentificationFailTime = _RuijieIneffiIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 23),
    _RuijieIneffiIdentificationFailTime_Type()
)
ruijieIneffiIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIneffiIdentificationFailTime.setStatus("current")
_RuijieTimeoutIdentificationFailTime_Type = Integer32
_RuijieTimeoutIdentificationFailTime_Object = MibTableColumn
ruijieTimeoutIdentificationFailTime = _RuijieTimeoutIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 24),
    _RuijieTimeoutIdentificationFailTime_Type()
)
ruijieTimeoutIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeoutIdentificationFailTime.setStatus("current")
_RuijieInefficiencyIdentificationFailTime_Type = Integer32
_RuijieInefficiencyIdentificationFailTime_Object = MibTableColumn
ruijieInefficiencyIdentificationFailTime = _RuijieInefficiencyIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 25),
    _RuijieInefficiencyIdentificationFailTime_Type()
)
ruijieInefficiencyIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyIdentificationFailTime.setStatus("current")
_RuijieOtherReasonIdentificationFailTime_Type = Integer32
_RuijieOtherReasonIdentificationFailTime_Object = MibTableColumn
ruijieOtherReasonIdentificationFailTime = _RuijieOtherReasonIdentificationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 26),
    _RuijieOtherReasonIdentificationFailTime_Type()
)
ruijieOtherReasonIdentificationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonIdentificationFailTime.setStatus("current")
_RuijieTotalRemoveLinkVerifyFailTimes_Type = Integer32
_RuijieTotalRemoveLinkVerifyFailTimes_Object = MibTableColumn
ruijieTotalRemoveLinkVerifyFailTimes = _RuijieTotalRemoveLinkVerifyFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 27),
    _RuijieTotalRemoveLinkVerifyFailTimes_Type()
)
ruijieTotalRemoveLinkVerifyFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalRemoveLinkVerifyFailTimes.setStatus("current")
_RuijieLeaveAPCoverageRemoveLinkVerifyFailTimes_Type = Integer32
_RuijieLeaveAPCoverageRemoveLinkVerifyFailTimes_Object = MibTableColumn
ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes = _RuijieLeaveAPCoverageRemoveLinkVerifyFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 28),
    _RuijieLeaveAPCoverageRemoveLinkVerifyFailTimes_Type()
)
ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes.setStatus("current")
_RuijieInefficiencyRemoveLinkVerifyFailTime_Type = Integer32
_RuijieInefficiencyRemoveLinkVerifyFailTime_Object = MibTableColumn
ruijieInefficiencyRemoveLinkVerifyFailTime = _RuijieInefficiencyRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 29),
    _RuijieInefficiencyRemoveLinkVerifyFailTime_Type()
)
ruijieInefficiencyRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyRemoveLinkVerifyFailTime.setStatus("current")
_RuijieLinkVerifyFailRemoveLinkVerifyFailTime_Type = Integer32
_RuijieLinkVerifyFailRemoveLinkVerifyFailTime_Object = MibTableColumn
ruijieLinkVerifyFailRemoveLinkVerifyFailTime = _RuijieLinkVerifyFailRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 30),
    _RuijieLinkVerifyFailRemoveLinkVerifyFailTime_Type()
)
ruijieLinkVerifyFailRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLinkVerifyFailRemoveLinkVerifyFailTime.setStatus("current")
_RuijieOtherReasonRemoveLinkVerifyFailTime_Type = Integer32
_RuijieOtherReasonRemoveLinkVerifyFailTime_Object = MibTableColumn
ruijieOtherReasonRemoveLinkVerifyFailTime = _RuijieOtherReasonRemoveLinkVerifyFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 31),
    _RuijieOtherReasonRemoveLinkVerifyFailTime_Type()
)
ruijieOtherReasonRemoveLinkVerifyFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonRemoveLinkVerifyFailTime.setStatus("current")
_RuijieTotalRemoveLinkAssociationTimes_Type = Integer32
_RuijieTotalRemoveLinkAssociationTimes_Object = MibTableColumn
ruijieTotalRemoveLinkAssociationTimes = _RuijieTotalRemoveLinkAssociationTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 32),
    _RuijieTotalRemoveLinkAssociationTimes_Type()
)
ruijieTotalRemoveLinkAssociationTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTotalRemoveLinkAssociationTimes.setStatus("current")
_RuijieLeaveAPCoverageRemoveAssociationFailTimes_Type = Integer32
_RuijieLeaveAPCoverageRemoveAssociationFailTimes_Object = MibTableColumn
ruijieLeaveAPCoverageRemoveAssociationFailTimes = _RuijieLeaveAPCoverageRemoveAssociationFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 33),
    _RuijieLeaveAPCoverageRemoveAssociationFailTimes_Type()
)
ruijieLeaveAPCoverageRemoveAssociationFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLeaveAPCoverageRemoveAssociationFailTimes.setStatus("current")
_RuijieInefficiencyRemoveAssociationFailTime_Type = Integer32
_RuijieInefficiencyRemoveAssociationFailTime_Object = MibTableColumn
ruijieInefficiencyRemoveAssociationFailTime = _RuijieInefficiencyRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 34),
    _RuijieInefficiencyRemoveAssociationFailTime_Type()
)
ruijieInefficiencyRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInefficiencyRemoveAssociationFailTime.setStatus("current")
_RuijieAssociationFailRemoveAssociationFailTime_Type = Integer32
_RuijieAssociationFailRemoveAssociationFailTime_Object = MibTableColumn
ruijieAssociationFailRemoveAssociationFailTime = _RuijieAssociationFailRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 35),
    _RuijieAssociationFailRemoveAssociationFailTime_Type()
)
ruijieAssociationFailRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssociationFailRemoveAssociationFailTime.setStatus("current")
_RuijieOtherReasonRemoveAssociationFailTime_Type = Integer32
_RuijieOtherReasonRemoveAssociationFailTime_Object = MibTableColumn
ruijieOtherReasonRemoveAssociationFailTime = _RuijieOtherReasonRemoveAssociationFailTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 1, 1, 1, 36),
    _RuijieOtherReasonRemoveAssociationFailTime_Type()
)
ruijieOtherReasonRemoveAssociationFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOtherReasonRemoveAssociationFailTime.setStatus("current")
_RuijieTermServiceStatisticsWithAP_ObjectIdentity = ObjectIdentity
ruijieTermServiceStatisticsWithAP = _RuijieTermServiceStatisticsWithAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 2)
)
_RuijieTermServiceStaticWithAPTable_Object = MibTable
ruijieTermServiceStaticWithAPTable = _RuijieTermServiceStaticWithAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieTermServiceStaticWithAPTable.setStatus("current")
_RuijieTermServiceStaticWithAPTableEntry_Object = MibTableRow
ruijieTermServiceStaticWithAPTableEntry = _RuijieTermServiceStaticWithAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 2, 1, 1)
)
ruijieTermServiceStaticWithAPTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieTermServiceStaticWithAPTableEntry.setStatus("current")
_RuijieUserAccumulateTime_Type = Counter32
_RuijieUserAccumulateTime_Object = MibTableColumn
ruijieUserAccumulateTime = _RuijieUserAccumulateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 2, 1, 1, 1),
    _RuijieUserAccumulateTime_Type()
)
ruijieUserAccumulateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUserAccumulateTime.setStatus("current")
_RuijieAssociaFailTimes_Type = Counter32
_RuijieAssociaFailTimes_Object = MibTableColumn
ruijieAssociaFailTimes = _RuijieAssociaFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 2, 1, 1, 2),
    _RuijieAssociaFailTimes_Type()
)
ruijieAssociaFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssociaFailTimes.setStatus("current")
_RuijieTermServiceSTatisticsWithStation_ObjectIdentity = ObjectIdentity
ruijieTermServiceSTatisticsWithStation = _RuijieTermServiceSTatisticsWithStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3)
)
_RuijieTermServiceStationWithStationTable_Object = MibTable
ruijieTermServiceStationWithStationTable = _RuijieTermServiceStationWithStationTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieTermServiceStationWithStationTable.setStatus("current")
_RuijieTermServiceStationWithStationTableEntry_Object = MibTableRow
ruijieTermServiceStationWithStationTableEntry = _RuijieTermServiceStationWithStationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1)
)
ruijieTermServiceStationWithStationTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieStaMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieTermServiceStationWithStationTableEntry.setStatus("current")
_RuijieStaAssociateTime_Type = Counter32
_RuijieStaAssociateTime_Object = MibTableColumn
ruijieStaAssociateTime = _RuijieStaAssociateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 2),
    _RuijieStaAssociateTime_Type()
)
ruijieStaAssociateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssociateTime.setStatus("current")
_RuijieRxStaDataFrams_Type = Counter32
_RuijieRxStaDataFrams_Object = MibTableColumn
ruijieRxStaDataFrams = _RuijieRxStaDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 3),
    _RuijieRxStaDataFrams_Type()
)
ruijieRxStaDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRxStaDataFrams.setStatus("current")
_RuijieRXStaErrorFrams_Type = Counter32
_RuijieRXStaErrorFrams_Object = MibTableColumn
ruijieRXStaErrorFrams = _RuijieRXStaErrorFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 4),
    _RuijieRXStaErrorFrams_Type()
)
ruijieRXStaErrorFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRXStaErrorFrams.setStatus("current")
_RuijieTxStaDataFrams_Type = Counter32
_RuijieTxStaDataFrams_Object = MibTableColumn
ruijieTxStaDataFrams = _RuijieTxStaDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 5),
    _RuijieTxStaDataFrams_Type()
)
ruijieTxStaDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTxStaDataFrams.setStatus("current")
_RuijieReSendDataFrams_Type = Counter32
_RuijieReSendDataFrams_Object = MibTableColumn
ruijieReSendDataFrams = _RuijieReSendDataFrams_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 6),
    _RuijieReSendDataFrams_Type()
)
ruijieReSendDataFrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieReSendDataFrams.setStatus("current")
_RuijieStaRxAvgSpeed_Type = Integer32
_RuijieStaRxAvgSpeed_Object = MibTableColumn
ruijieStaRxAvgSpeed = _RuijieStaRxAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 7),
    _RuijieStaRxAvgSpeed_Type()
)
ruijieStaRxAvgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaRxAvgSpeed.setStatus("current")
_RuijieStaTxAvgSpeed_Type = Integer32
_RuijieStaTxAvgSpeed_Object = MibTableColumn
ruijieStaTxAvgSpeed = _RuijieStaTxAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 8),
    _RuijieStaTxAvgSpeed_Type()
)
ruijieStaTxAvgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTxAvgSpeed.setStatus("current")
_RuijieStaThroughput_Type = Integer32
_RuijieStaThroughput_Object = MibTableColumn
ruijieStaThroughput = _RuijieStaThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 9),
    _RuijieStaThroughput_Type()
)
ruijieStaThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaThroughput.setStatus("current")
_RuijieStaSignalStrength_Type = Integer32
_RuijieStaSignalStrength_Object = MibTableColumn
ruijieStaSignalStrength = _RuijieStaSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 10),
    _RuijieStaSignalStrength_Type()
)
ruijieStaSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaSignalStrength.setStatus("current")
_RuijieStaSignalNoise_Type = Integer32
_RuijieStaSignalNoise_Object = MibTableColumn
ruijieStaSignalNoise = _RuijieStaSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 7, 3, 1, 1, 11),
    _RuijieStaSignalNoise_Type()
)
ruijieStaSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaSignalNoise.setStatus("current")
_RuijieDOT11WIDSParamObjects_ObjectIdentity = ObjectIdentity
ruijieDOT11WIDSParamObjects = _RuijieDOT11WIDSParamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8)
)
_RuijieDot11WIDSInfoTable_Object = MibTable
ruijieDot11WIDSInfoTable = _RuijieDot11WIDSInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1)
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSInfoTable.setStatus("current")
_RuijieDot11WIDSInfoEntry_Object = MibTableRow
ruijieDot11WIDSInfoEntry = _RuijieDot11WIDSInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1)
)
ruijieDot11WIDSInfoEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieDot11WIDSLocalIndex"),
)
if mibBuilder.loadTexts:
    ruijieDot11WIDSInfoEntry.setStatus("current")
_RuijieDot11WIDSLocalIndex_Type = Integer32
_RuijieDot11WIDSLocalIndex_Object = MibTableColumn
ruijieDot11WIDSLocalIndex = _RuijieDot11WIDSLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 1),
    _RuijieDot11WIDSLocalIndex_Type()
)
ruijieDot11WIDSLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDot11WIDSLocalIndex.setStatus("current")
_RuijieDot11WIDSpermittedSSID_Type = DisplayString
_RuijieDot11WIDSpermittedSSID_Object = MibTableColumn
ruijieDot11WIDSpermittedSSID = _RuijieDot11WIDSpermittedSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 2),
    _RuijieDot11WIDSpermittedSSID_Type()
)
ruijieDot11WIDSpermittedSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSpermittedSSID.setStatus("current")
_RuijieDot11WIDSpermitBSSID_Type = MacAddress
_RuijieDot11WIDSpermitBSSID_Object = MibTableColumn
ruijieDot11WIDSpermitBSSID = _RuijieDot11WIDSpermitBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 3),
    _RuijieDot11WIDSpermitBSSID_Type()
)
ruijieDot11WIDSpermitBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSpermitBSSID.setStatus("current")
_RuijieDot11WIDSDeviceOUI_Type = DisplayString
_RuijieDot11WIDSDeviceOUI_Object = MibTableColumn
ruijieDot11WIDSDeviceOUI = _RuijieDot11WIDSDeviceOUI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 4),
    _RuijieDot11WIDSDeviceOUI_Type()
)
ruijieDot11WIDSDeviceOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSDeviceOUI.setStatus("current")
_RuijieDot11WIDSSuspiciousAPBSS_Type = MacAddress
_RuijieDot11WIDSSuspiciousAPBSS_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPBSS = _RuijieDot11WIDSSuspiciousAPBSS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 5),
    _RuijieDot11WIDSSuspiciousAPBSS_Type()
)
ruijieDot11WIDSSuspiciousAPBSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPBSS.setStatus("current")
_RuijieDot11WIDSSuspiciousAPCount_Type = Integer32
_RuijieDot11WIDSSuspiciousAPCount_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPCount = _RuijieDot11WIDSSuspiciousAPCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 6),
    _RuijieDot11WIDSSuspiciousAPCount_Type()
)
ruijieDot11WIDSSuspiciousAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPCount.setStatus("current")
_RuijieDot11WIDSMomentFirstTimeDetectedSusAP_Type = TimeTicks
_RuijieDot11WIDSMomentFirstTimeDetectedSusAP_Object = MibTableColumn
ruijieDot11WIDSMomentFirstTimeDetectedSusAP = _RuijieDot11WIDSMomentFirstTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 7),
    _RuijieDot11WIDSMomentFirstTimeDetectedSusAP_Type()
)
ruijieDot11WIDSMomentFirstTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSMomentFirstTimeDetectedSusAP.setStatus("current")
_RuijieDot11WIDSMomentLastTimeDetectedSusAP_Type = TimeTicks
_RuijieDot11WIDSMomentLastTimeDetectedSusAP_Object = MibTableColumn
ruijieDot11WIDSMomentLastTimeDetectedSusAP = _RuijieDot11WIDSMomentLastTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 8),
    _RuijieDot11WIDSMomentLastTimeDetectedSusAP_Type()
)
ruijieDot11WIDSMomentLastTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSMomentLastTimeDetectedSusAP.setStatus("current")
_RuijieDot11WIDSSuspiciousAPSSID_Type = DisplayString
_RuijieDot11WIDSSuspiciousAPSSID_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPSSID = _RuijieDot11WIDSSuspiciousAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 9),
    _RuijieDot11WIDSSuspiciousAPSSID_Type()
)
ruijieDot11WIDSSuspiciousAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPSSID.setStatus("current")
_RuijieDot11WIDSSuspiciousAPMaxSignalStrength_Type = Integer32
_RuijieDot11WIDSSuspiciousAPMaxSignalStrength_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPMaxSignalStrength = _RuijieDot11WIDSSuspiciousAPMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 10),
    _RuijieDot11WIDSSuspiciousAPMaxSignalStrength_Type()
)
ruijieDot11WIDSSuspiciousAPMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPMaxSignalStrength.setStatus("current")
_RuijieDot11WIDSSuspiciousAPUsingChannel_Type = Integer32
_RuijieDot11WIDSSuspiciousAPUsingChannel_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPUsingChannel = _RuijieDot11WIDSSuspiciousAPUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 11),
    _RuijieDot11WIDSSuspiciousAPUsingChannel_Type()
)
ruijieDot11WIDSSuspiciousAPUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPUsingChannel.setStatus("current")
_RuijieDot11WIDSSuspiciousAPFrameEncrption_Type = Integer32
_RuijieDot11WIDSSuspiciousAPFrameEncrption_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPFrameEncrption = _RuijieDot11WIDSSuspiciousAPFrameEncrption_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 12),
    _RuijieDot11WIDSSuspiciousAPFrameEncrption_Type()
)
ruijieDot11WIDSSuspiciousAPFrameEncrption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPFrameEncrption.setStatus("current")
_RuijieDot11WIDSSuspiciousAPNeedsDealingTag_Type = TruthValue
_RuijieDot11WIDSSuspiciousAPNeedsDealingTag_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPNeedsDealingTag = _RuijieDot11WIDSSuspiciousAPNeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 13),
    _RuijieDot11WIDSSuspiciousAPNeedsDealingTag_Type()
)
ruijieDot11WIDSSuspiciousAPNeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPNeedsDealingTag.setStatus("current")
_RuijieDot11WIDSSuspiciousAPIgnoredTag_Type = TruthValue
_RuijieDot11WIDSSuspiciousAPIgnoredTag_Object = MibTableColumn
ruijieDot11WIDSSuspiciousAPIgnoredTag = _RuijieDot11WIDSSuspiciousAPIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 14),
    _RuijieDot11WIDSSuspiciousAPIgnoredTag_Type()
)
ruijieDot11WIDSSuspiciousAPIgnoredTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousAPIgnoredTag.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAMAC_Type = MacAddress
_RuijieDot11WIDSSuspiciousSTAMAC_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAMAC = _RuijieDot11WIDSSuspiciousSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 15),
    _RuijieDot11WIDSSuspiciousSTAMAC_Type()
)
ruijieDot11WIDSSuspiciousSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAMAC.setStatus("current")
_RuijieDot11WIDSAPCountDetectingSuspiciousSTA_Type = Integer32
_RuijieDot11WIDSAPCountDetectingSuspiciousSTA_Object = MibTableColumn
ruijieDot11WIDSAPCountDetectingSuspiciousSTA = _RuijieDot11WIDSAPCountDetectingSuspiciousSTA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 16),
    _RuijieDot11WIDSAPCountDetectingSuspiciousSTA_Type()
)
ruijieDot11WIDSAPCountDetectingSuspiciousSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSAPCountDetectingSuspiciousSTA.setStatus("current")
_RuijieDot11WIDSMomentFirstTimeDetectedSusSTA_Type = TimeTicks
_RuijieDot11WIDSMomentFirstTimeDetectedSusSTA_Object = MibTableColumn
ruijieDot11WIDSMomentFirstTimeDetectedSusSTA = _RuijieDot11WIDSMomentFirstTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 17),
    _RuijieDot11WIDSMomentFirstTimeDetectedSusSTA_Type()
)
ruijieDot11WIDSMomentFirstTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSMomentFirstTimeDetectedSusSTA.setStatus("current")
_RuijieDot11WIDSMomentLastTimeDetectedSusSTA_Type = TimeTicks
_RuijieDot11WIDSMomentLastTimeDetectedSusSTA_Object = MibTableColumn
ruijieDot11WIDSMomentLastTimeDetectedSusSTA = _RuijieDot11WIDSMomentLastTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 18),
    _RuijieDot11WIDSMomentLastTimeDetectedSusSTA_Type()
)
ruijieDot11WIDSMomentLastTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSMomentLastTimeDetectedSusSTA.setStatus("current")
_RuijieDot11WIDSBSSIDSuspiciousSTAAccessing_Type = MacAddress
_RuijieDot11WIDSBSSIDSuspiciousSTAAccessing_Object = MibTableColumn
ruijieDot11WIDSBSSIDSuspiciousSTAAccessing = _RuijieDot11WIDSBSSIDSuspiciousSTAAccessing_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 19),
    _RuijieDot11WIDSBSSIDSuspiciousSTAAccessing_Type()
)
ruijieDot11WIDSBSSIDSuspiciousSTAAccessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSBSSIDSuspiciousSTAAccessing.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAMaxSignalStrength_Type = Integer32
_RuijieDot11WIDSSuspiciousSTAMaxSignalStrength_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAMaxSignalStrength = _RuijieDot11WIDSSuspiciousSTAMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 20),
    _RuijieDot11WIDSSuspiciousSTAMaxSignalStrength_Type()
)
ruijieDot11WIDSSuspiciousSTAMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAMaxSignalStrength.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAUsingChannel_Type = Integer32
_RuijieDot11WIDSSuspiciousSTAUsingChannel_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAUsingChannel = _RuijieDot11WIDSSuspiciousSTAUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 21),
    _RuijieDot11WIDSSuspiciousSTAUsingChannel_Type()
)
ruijieDot11WIDSSuspiciousSTAUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAUsingChannel.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAWorksInAdhocMode_Type = TruthValue
_RuijieDot11WIDSSuspiciousSTAWorksInAdhocMode_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode = _RuijieDot11WIDSSuspiciousSTAWorksInAdhocMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 22),
    _RuijieDot11WIDSSuspiciousSTAWorksInAdhocMode_Type()
)
ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode.setStatus("current")
_RuijieDot11WIDSSuspiciousSTANeedsDealingTag_Type = TruthValue
_RuijieDot11WIDSSuspiciousSTANeedsDealingTag_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTANeedsDealingTag = _RuijieDot11WIDSSuspiciousSTANeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 23),
    _RuijieDot11WIDSSuspiciousSTANeedsDealingTag_Type()
)
ruijieDot11WIDSSuspiciousSTANeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTANeedsDealingTag.setStatus("current")
_RuijieDot11WIDSSuspiciousSTAIgnoredTag_Type = TruthValue
_RuijieDot11WIDSSuspiciousSTAIgnoredTag_Object = MibTableColumn
ruijieDot11WIDSSuspiciousSTAIgnoredTag = _RuijieDot11WIDSSuspiciousSTAIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 24),
    _RuijieDot11WIDSSuspiciousSTAIgnoredTag_Type()
)
ruijieDot11WIDSSuspiciousSTAIgnoredTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSuspiciousSTAIgnoredTag.setStatus("current")
_RuijieDot11WIDSFloodAttackDetectSwitch_Type = TruthValue
_RuijieDot11WIDSFloodAttackDetectSwitch_Object = MibTableColumn
ruijieDot11WIDSFloodAttackDetectSwitch = _RuijieDot11WIDSFloodAttackDetectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 25),
    _RuijieDot11WIDSFloodAttackDetectSwitch_Type()
)
ruijieDot11WIDSFloodAttackDetectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSFloodAttackDetectSwitch.setStatus("current")
_RuijieDot11WIDSSpoofAttackDetectSwitch_Type = TruthValue
_RuijieDot11WIDSSpoofAttackDetectSwitch_Object = MibTableColumn
ruijieDot11WIDSSpoofAttackDetectSwitch = _RuijieDot11WIDSSpoofAttackDetectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 26),
    _RuijieDot11WIDSSpoofAttackDetectSwitch_Type()
)
ruijieDot11WIDSSpoofAttackDetectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSSpoofAttackDetectSwitch.setStatus("current")
_RuijieDot11WIDSWeakIVDetectSwitch_Type = TruthValue
_RuijieDot11WIDSWeakIVDetectSwitch_Object = MibTableColumn
ruijieDot11WIDSWeakIVDetectSwitch = _RuijieDot11WIDSWeakIVDetectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 27),
    _RuijieDot11WIDSWeakIVDetectSwitch_Type()
)
ruijieDot11WIDSWeakIVDetectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSWeakIVDetectSwitch.setStatus("current")
_RuijieDot11WIDSClearIllegalEquipmentHistroyTag_Type = TruthValue
_RuijieDot11WIDSClearIllegalEquipmentHistroyTag_Object = MibTableColumn
ruijieDot11WIDSClearIllegalEquipmentHistroyTag = _RuijieDot11WIDSClearIllegalEquipmentHistroyTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 28),
    _RuijieDot11WIDSClearIllegalEquipmentHistroyTag_Type()
)
ruijieDot11WIDSClearIllegalEquipmentHistroyTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSClearIllegalEquipmentHistroyTag.setStatus("current")
_RuijieDot11WIDSClearAttackDetectionHistroyTag_Type = TruthValue
_RuijieDot11WIDSClearAttackDetectionHistroyTag_Object = MibTableColumn
ruijieDot11WIDSClearAttackDetectionHistroyTag = _RuijieDot11WIDSClearAttackDetectionHistroyTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 29),
    _RuijieDot11WIDSClearAttackDetectionHistroyTag_Type()
)
ruijieDot11WIDSClearAttackDetectionHistroyTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSClearAttackDetectionHistroyTag.setStatus("current")
_RuijieDot11WIDSClearAttackDetectionStaticsTag_Type = TruthValue
_RuijieDot11WIDSClearAttackDetectionStaticsTag_Object = MibTableColumn
ruijieDot11WIDSClearAttackDetectionStaticsTag = _RuijieDot11WIDSClearAttackDetectionStaticsTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 1, 1, 30),
    _RuijieDot11WIDSClearAttackDetectionStaticsTag_Type()
)
ruijieDot11WIDSClearAttackDetectionStaticsTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDot11WIDSClearAttackDetectionStaticsTag.setStatus("current")
_RuijieDot11LawlessApInfoTable_Object = MibTable
ruijieDot11LawlessApInfoTable = _RuijieDot11LawlessApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2)
)
if mibBuilder.loadTexts:
    ruijieDot11LawlessApInfoTable.setStatus("current")
_RuijieDot11LawlessApInfoTableEntry_Object = MibTableRow
ruijieDot11LawlessApInfoTableEntry = _RuijieDot11LawlessApInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2, 1)
)
ruijieDot11LawlessApInfoTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieLawlessAPIndex"),
)
if mibBuilder.loadTexts:
    ruijieDot11LawlessApInfoTableEntry.setStatus("current")
_RuijieLawlessAPIndex_Type = Integer32
_RuijieLawlessAPIndex_Object = MibTableColumn
ruijieLawlessAPIndex = _RuijieLawlessAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2, 1, 1),
    _RuijieLawlessAPIndex_Type()
)
ruijieLawlessAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieLawlessAPIndex.setStatus("current")
_RuijieLawlessAPSignalStrength_Type = Integer32
_RuijieLawlessAPSignalStrength_Object = MibTableColumn
ruijieLawlessAPSignalStrength = _RuijieLawlessAPSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2, 1, 2),
    _RuijieLawlessAPSignalStrength_Type()
)
ruijieLawlessAPSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLawlessAPSignalStrength.setStatus("current")
_RuijieLawlessAPSignalSNR_Type = Integer32
_RuijieLawlessAPSignalSNR_Object = MibTableColumn
ruijieLawlessAPSignalSNR = _RuijieLawlessAPSignalSNR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2, 1, 3),
    _RuijieLawlessAPSignalSNR_Type()
)
ruijieLawlessAPSignalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLawlessAPSignalSNR.setStatus("current")
_RuijieLawlessAPChannelNum_Type = Integer32
_RuijieLawlessAPChannelNum_Object = MibTableColumn
ruijieLawlessAPChannelNum = _RuijieLawlessAPChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2, 1, 4),
    _RuijieLawlessAPChannelNum_Type()
)
ruijieLawlessAPChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLawlessAPChannelNum.setStatus("current")
_RuijieLawlessAPSSIDName_Type = DisplayString
_RuijieLawlessAPSSIDName_Object = MibTableColumn
ruijieLawlessAPSSIDName = _RuijieLawlessAPSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2, 1, 5),
    _RuijieLawlessAPSSIDName_Type()
)
ruijieLawlessAPSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLawlessAPSSIDName.setStatus("current")
_RuijieLawlessAPMacaddr_Type = MacAddress
_RuijieLawlessAPMacaddr_Object = MibTableColumn
ruijieLawlessAPMacaddr = _RuijieLawlessAPMacaddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2, 1, 6),
    _RuijieLawlessAPMacaddr_Type()
)
ruijieLawlessAPMacaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLawlessAPMacaddr.setStatus("current")
_RuijieLawlessAPTreatMode_Type = Integer32
_RuijieLawlessAPTreatMode_Object = MibTableColumn
ruijieLawlessAPTreatMode = _RuijieLawlessAPTreatMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 2, 1, 7),
    _RuijieLawlessAPTreatMode_Type()
)
ruijieLawlessAPTreatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLawlessAPTreatMode.setStatus("current")
_RuijieDot11UndefinedApInfoTable_Object = MibTable
ruijieDot11UndefinedApInfoTable = _RuijieDot11UndefinedApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3)
)
if mibBuilder.loadTexts:
    ruijieDot11UndefinedApInfoTable.setStatus("current")
_RuijieDot11UndefinedApInfoTableEntry_Object = MibTableRow
ruijieDot11UndefinedApInfoTableEntry = _RuijieDot11UndefinedApInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3, 1)
)
ruijieDot11UndefinedApInfoTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieUndefinedAPIndex"),
)
if mibBuilder.loadTexts:
    ruijieDot11UndefinedApInfoTableEntry.setStatus("current")
_RuijieUndefinedAPIndex_Type = Integer32
_RuijieUndefinedAPIndex_Object = MibTableColumn
ruijieUndefinedAPIndex = _RuijieUndefinedAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3, 1, 1),
    _RuijieUndefinedAPIndex_Type()
)
ruijieUndefinedAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieUndefinedAPIndex.setStatus("current")
_RuijieUndefinedAPSignalStrength_Type = Integer32
_RuijieUndefinedAPSignalStrength_Object = MibTableColumn
ruijieUndefinedAPSignalStrength = _RuijieUndefinedAPSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3, 1, 2),
    _RuijieUndefinedAPSignalStrength_Type()
)
ruijieUndefinedAPSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUndefinedAPSignalStrength.setStatus("current")
_RuijieUndefinedAPSignalSNR_Type = Integer32
_RuijieUndefinedAPSignalSNR_Object = MibTableColumn
ruijieUndefinedAPSignalSNR = _RuijieUndefinedAPSignalSNR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3, 1, 3),
    _RuijieUndefinedAPSignalSNR_Type()
)
ruijieUndefinedAPSignalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUndefinedAPSignalSNR.setStatus("current")
_RuijieUndefinedAPChannelNum_Type = Integer32
_RuijieUndefinedAPChannelNum_Object = MibTableColumn
ruijieUndefinedAPChannelNum = _RuijieUndefinedAPChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3, 1, 4),
    _RuijieUndefinedAPChannelNum_Type()
)
ruijieUndefinedAPChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUndefinedAPChannelNum.setStatus("current")
_RuijieUndefinedAPSSIDName_Type = DisplayString
_RuijieUndefinedAPSSIDName_Object = MibTableColumn
ruijieUndefinedAPSSIDName = _RuijieUndefinedAPSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3, 1, 5),
    _RuijieUndefinedAPSSIDName_Type()
)
ruijieUndefinedAPSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUndefinedAPSSIDName.setStatus("current")
_RuijieUndefinedAPMacaddr_Type = MacAddress
_RuijieUndefinedAPMacaddr_Object = MibTableColumn
ruijieUndefinedAPMacaddr = _RuijieUndefinedAPMacaddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3, 1, 6),
    _RuijieUndefinedAPMacaddr_Type()
)
ruijieUndefinedAPMacaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUndefinedAPMacaddr.setStatus("current")
_RuijieUndefinedAPTreatMode_Type = Integer32
_RuijieUndefinedAPTreatMode_Object = MibTableColumn
ruijieUndefinedAPTreatMode = _RuijieUndefinedAPTreatMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 3, 1, 7),
    _RuijieUndefinedAPTreatMode_Type()
)
ruijieUndefinedAPTreatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUndefinedAPTreatMode.setStatus("current")
_RuijieDot11LegalityApInfoTable_Object = MibTable
ruijieDot11LegalityApInfoTable = _RuijieDot11LegalityApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4)
)
if mibBuilder.loadTexts:
    ruijieDot11LegalityApInfoTable.setStatus("current")
_RuijieDot11LegalityApInfoTableEntry_Object = MibTableRow
ruijieDot11LegalityApInfoTableEntry = _RuijieDot11LegalityApInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4, 1)
)
ruijieDot11LegalityApInfoTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieLegalityAPIndex"),
)
if mibBuilder.loadTexts:
    ruijieDot11LegalityApInfoTableEntry.setStatus("current")
_RuijieLegalityAPIndex_Type = Integer32
_RuijieLegalityAPIndex_Object = MibTableColumn
ruijieLegalityAPIndex = _RuijieLegalityAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4, 1, 1),
    _RuijieLegalityAPIndex_Type()
)
ruijieLegalityAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieLegalityAPIndex.setStatus("current")
_RuijieLegalityAPSignalStrength_Type = Integer32
_RuijieLegalityAPSignalStrength_Object = MibTableColumn
ruijieLegalityAPSignalStrength = _RuijieLegalityAPSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4, 1, 2),
    _RuijieLegalityAPSignalStrength_Type()
)
ruijieLegalityAPSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLegalityAPSignalStrength.setStatus("current")
_RuijieLegalityAPSignalSNR_Type = Integer32
_RuijieLegalityAPSignalSNR_Object = MibTableColumn
ruijieLegalityAPSignalSNR = _RuijieLegalityAPSignalSNR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4, 1, 3),
    _RuijieLegalityAPSignalSNR_Type()
)
ruijieLegalityAPSignalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLegalityAPSignalSNR.setStatus("current")
_RuijieLegalityAPChannelNum_Type = Integer32
_RuijieLegalityAPChannelNum_Object = MibTableColumn
ruijieLegalityAPChannelNum = _RuijieLegalityAPChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4, 1, 4),
    _RuijieLegalityAPChannelNum_Type()
)
ruijieLegalityAPChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLegalityAPChannelNum.setStatus("current")
_RuijieLegalityAPSSIDName_Type = DisplayString
_RuijieLegalityAPSSIDName_Object = MibTableColumn
ruijieLegalityAPSSIDName = _RuijieLegalityAPSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4, 1, 5),
    _RuijieLegalityAPSSIDName_Type()
)
ruijieLegalityAPSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLegalityAPSSIDName.setStatus("current")
_RuijieLegalityAPMacaddr_Type = MacAddress
_RuijieLegalityAPMacaddr_Object = MibTableColumn
ruijieLegalityAPMacaddr = _RuijieLegalityAPMacaddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4, 1, 6),
    _RuijieLegalityAPMacaddr_Type()
)
ruijieLegalityAPMacaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLegalityAPMacaddr.setStatus("current")
_RuijieLegalityAPTreatMode_Type = Integer32
_RuijieLegalityAPTreatMode_Object = MibTableColumn
ruijieLegalityAPTreatMode = _RuijieLegalityAPTreatMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 8, 4, 1, 7),
    _RuijieLegalityAPTreatMode_Type()
)
ruijieLegalityAPTreatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLegalityAPTreatMode.setStatus("current")
_RuijieAlarmTrapsObjects_ObjectIdentity = ObjectIdentity
ruijieAlarmTrapsObjects = _RuijieAlarmTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10)
)


class _RuijieWIDSSuspiciousType_Type(DisplayString):
    """Custom type ruijieWIDSSuspiciousType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RuijieWIDSSuspiciousType_Type.__name__ = "DisplayString"
_RuijieWIDSSuspiciousType_Object = MibScalar
ruijieWIDSSuspiciousType = _RuijieWIDSSuspiciousType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10, 1),
    _RuijieWIDSSuspiciousType_Type()
)
ruijieWIDSSuspiciousType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWIDSSuspiciousType.setStatus("current")
_RuijieWIDSSuspiciousDeviceMac_Type = MacAddress
_RuijieWIDSSuspiciousDeviceMac_Object = MibScalar
ruijieWIDSSuspiciousDeviceMac = _RuijieWIDSSuspiciousDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10, 2),
    _RuijieWIDSSuspiciousDeviceMac_Type()
)
ruijieWIDSSuspiciousDeviceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWIDSSuspiciousDeviceMac.setStatus("current")


class _RuijieWIDSSuspiciousDeviceExtensionInfo_Type(DisplayString):
    """Custom type ruijieWIDSSuspiciousDeviceExtensionInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RuijieWIDSSuspiciousDeviceExtensionInfo_Type.__name__ = "DisplayString"
_RuijieWIDSSuspiciousDeviceExtensionInfo_Object = MibScalar
ruijieWIDSSuspiciousDeviceExtensionInfo = _RuijieWIDSSuspiciousDeviceExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10, 3),
    _RuijieWIDSSuspiciousDeviceExtensionInfo_Type()
)
ruijieWIDSSuspiciousDeviceExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWIDSSuspiciousDeviceExtensionInfo.setStatus("current")


class _RuijieAPCurrentPMMode_Type(DisplayString):
    """Custom type ruijieAPCurrentPMMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RuijieAPCurrentPMMode_Type.__name__ = "DisplayString"
_RuijieAPCurrentPMMode_Object = MibScalar
ruijieAPCurrentPMMode = _RuijieAPCurrentPMMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10, 4),
    _RuijieAPCurrentPMMode_Type()
)
ruijieAPCurrentPMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPCurrentPMMode.setStatus("current")
_RuijieChgWorkModeAPMac_Type = MacAddress
_RuijieChgWorkModeAPMac_Object = MibScalar
ruijieChgWorkModeAPMac = _RuijieChgWorkModeAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10, 7),
    _RuijieChgWorkModeAPMac_Type()
)
ruijieChgWorkModeAPMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieChgWorkModeAPMac.setStatus("current")


class _RuijieAttackType_Type(DisplayString):
    """Custom type ruijieAttackType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RuijieAttackType_Type.__name__ = "DisplayString"
_RuijieAttackType_Object = MibScalar
ruijieAttackType = _RuijieAttackType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10, 8),
    _RuijieAttackType_Type()
)
ruijieAttackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAttackType.setStatus("current")
_RuijieAttackCilentIP_Type = IpAddress
_RuijieAttackCilentIP_Object = MibScalar
ruijieAttackCilentIP = _RuijieAttackCilentIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10, 9),
    _RuijieAttackCilentIP_Type()
)
ruijieAttackCilentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAttackCilentIP.setStatus("current")


class _RuijieAttackCilentExternInfo_Type(DisplayString):
    """Custom type ruijieAttackCilentExternInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RuijieAttackCilentExternInfo_Type.__name__ = "DisplayString"
_RuijieAttackCilentExternInfo_Object = MibScalar
ruijieAttackCilentExternInfo = _RuijieAttackCilentExternInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 10, 10),
    _RuijieAttackCilentExternInfo_Type()
)
ruijieAttackCilentExternInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAttackCilentExternInfo.setStatus("current")

# Managed Objects groups


# Notification objects

ruijieWIDSIllegalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 0, 1)
)
ruijieWIDSIllegalAlarmTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieWIDSSuspiciousType"),
        ("RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieWIDSSuspiciousDeviceMac"),
        ("RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieWIDSSuspiciousDeviceExtensionInfo"))
)
if mibBuilder.loadTexts:
    ruijieWIDSIllegalAlarmTrap.setStatus(
        "current"
    )

ruijieTelMtWorkModeChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 0, 2)
)
ruijieTelMtWorkModeChgTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieAPCurrentPMMode"),
        ("RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieChgWorkModeAPMac"))
)
if mibBuilder.loadTexts:
    ruijieTelMtWorkModeChgTrap.setStatus(
        "current"
    )

ruijieAttackAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 83, 0, 4)
)
ruijieAttackAlarm.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieAttackType"),
        ("RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieAttackCilentIP"),
        ("RUIJIE-WLAN-FIT-AP-IN-MIB", "ruijieAttackCilentExternInfo"))
)
if mibBuilder.loadTexts:
    ruijieAttackAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WLAN-FIT-AP-IN-MIB",
    **{"ruijieFitApMibModule": ruijieFitApMibModule,
       "ruijieAlarmTraps": ruijieAlarmTraps,
       "ruijieWIDSIllegalAlarmTrap": ruijieWIDSIllegalAlarmTrap,
       "ruijieTelMtWorkModeChgTrap": ruijieTelMtWorkModeChgTrap,
       "ruijieAttackAlarm": ruijieAttackAlarm,
       "ruijieSystemInfoConfigObjects": ruijieSystemInfoConfigObjects,
       "ruijieDomain": ruijieDomain,
       "ruijiePhySeparatedEnable": ruijiePhySeparatedEnable,
       "ruijieForfendDosAttackEnable": ruijieForfendDosAttackEnable,
       "ruijieAcTrafficLoadBalancing": ruijieAcTrafficLoadBalancing,
       "ruijieAcTrafficLoadBalanceThreshold": ruijieAcTrafficLoadBalanceThreshold,
       "ruijieAcTrafficOtherAPThresholdValue": ruijieAcTrafficOtherAPThresholdValue,
       "ruijieAcAPWIDSScanningMode": ruijieAcAPWIDSScanningMode,
       "ruijieAcAPLegitimateMode": ruijieAcAPLegitimateMode,
       "ruijieAcAPTreatMode": ruijieAcAPTreatMode,
       "ruijieAcAssociationFailureTotalTimes": ruijieAcAssociationFailureTotalTimes,
       "ruijieAcAirIfRxTotalDataFrams": ruijieAcAirIfRxTotalDataFrams,
       "ruijieAcAirIfTxTotalDataFrams": ruijieAcAirIfTxTotalDataFrams,
       "ruijieAcAirIfTxTotalLostFrams": ruijieAcAirIfTxTotalLostFrams,
       "ruijieAcAirIfTxAssociateFrams": ruijieAcAirIfTxAssociateFrams,
       "ruijieAcAirIfRxAssociateFrams": ruijieAcAirIfRxAssociateFrams,
       "ruijieAcAirIfBeaconTotalFrams": ruijieAcAirIfBeaconTotalFrams,
       "ruijieAcAirIfRxTotalDataBytes": ruijieAcAirIfRxTotalDataBytes,
       "ruijieAcAirIfTxTotalDataBytes": ruijieAcAirIfTxTotalDataBytes,
       "ruijieAcAirRxFlux": ruijieAcAirRxFlux,
       "ruijieAcAirTxFlux": ruijieAcAirTxFlux,
       "ruijieInfoConfigObjects": ruijieInfoConfigObjects,
       "ruijieInfoConfigTable": ruijieInfoConfigTable,
       "ruijieInfoConfigTableEntry": ruijieInfoConfigTableEntry,
       "ruijieAcAPWIDSWorkMode": ruijieAcAPWIDSWorkMode,
       "ruijieStationConfigObjects": ruijieStationConfigObjects,
       "ruijieConfigStaInfoTable": ruijieConfigStaInfoTable,
       "ruijieConfigStaInfoTableEntry": ruijieConfigStaInfoTableEntry,
       "ruijieACconfigAPBandwith": ruijieACconfigAPBandwith,
       "ruijieAirIfStatisticsObjects": ruijieAirIfStatisticsObjects,
       "ruijieAirIfInfoStatisticsTable": ruijieAirIfInfoStatisticsTable,
       "ruijieAirIfInfoStatisticsTableEntry": ruijieAirIfInfoStatisticsTableEntry,
       "ruijieRxTotalDataFrams": ruijieRxTotalDataFrams,
       "ruijieTxTotalDataFrams": ruijieTxTotalDataFrams,
       "ruijieTxLostDataFrams": ruijieTxLostDataFrams,
       "ruijieTxAssociateFrams": ruijieTxAssociateFrams,
       "ruijieRxAssociateFrams": ruijieRxAssociateFrams,
       "ruijieBeaconFrams": ruijieBeaconFrams,
       "ruijieRxTotalDataBytes": ruijieRxTotalDataBytes,
       "ruijieTxTotalDataBytes": ruijieTxTotalDataBytes,
       "ruijieRESUtilization": ruijieRESUtilization,
       "ruijieAirIfTxResendDataTable": ruijieAirIfTxResendDataTable,
       "ruijieAirIfTxResendDataTableEntry": ruijieAirIfTxResendDataTableEntry,
       "ruijieStaResendDataFrams": ruijieStaResendDataFrams,
       "ruijieTermServiceStatistics": ruijieTermServiceStatistics,
       "ruijieTermServiceStatisticsWithSSID": ruijieTermServiceStatisticsWithSSID,
       "ruijieTermServiceStaticWithSSIDTable": ruijieTermServiceStaticWithSSIDTable,
       "ruijieTermServiceStaticWithSSIDTableEntry": ruijieTermServiceStaticWithSSIDTableEntry,
       "ruijieTotalUserNum": ruijieTotalUserNum,
       "ruijieCurrentUserNum": ruijieCurrentUserNum,
       "ruijieStaReqAccessTimes": ruijieStaReqAccessTimes,
       "ruijieRspStaAccessReqTimes": ruijieRspStaAccessReqTimes,
       "ruijieStaAccessSucessTimes": ruijieStaAccessSucessTimes,
       "ruijieIneffiLinkVerifyFailTime": ruijieIneffiLinkVerifyFailTime,
       "ruijieTimeoutLinkVerifyFailTime": ruijieTimeoutLinkVerifyFailTime,
       "ruijieInefficiencyLinkVerifyFailTime": ruijieInefficiencyLinkVerifyFailTime,
       "ruijieOtherReasonLinkVerifyFailTime": ruijieOtherReasonLinkVerifyFailTime,
       "ruijieIneffiAssociationFailTime": ruijieIneffiAssociationFailTime,
       "ruijieTimeoutAssociationFailTime": ruijieTimeoutAssociationFailTime,
       "ruijieInefficiencyAssociationFailTime": ruijieInefficiencyAssociationFailTime,
       "ruijieOtherReasonAssociationFailTime": ruijieOtherReasonAssociationFailTime,
       "ruijieTotalReassociationAtmptTimes": ruijieTotalReassociationAtmptTimes,
       "ruijieTotalReassociationSuccessTimes": ruijieTotalReassociationSuccessTimes,
       "ruijieIneffiReassociationFailTime": ruijieIneffiReassociationFailTime,
       "ruijieTimeoutReassociationFailTime": ruijieTimeoutReassociationFailTime,
       "ruijieInefficiencyReassociationFailTime": ruijieInefficiencyReassociationFailTime,
       "ruijieOtherReasonReassociationFailTime": ruijieOtherReasonReassociationFailTime,
       "ruijieTotalIdentificationAtmptTimes": ruijieTotalIdentificationAtmptTimes,
       "ruijieTotalIdentificationSuccessTimes": ruijieTotalIdentificationSuccessTimes,
       "ruijiePwdErrorIdentifyFailTime": ruijiePwdErrorIdentifyFailTime,
       "ruijieIneffiIdentificationFailTime": ruijieIneffiIdentificationFailTime,
       "ruijieTimeoutIdentificationFailTime": ruijieTimeoutIdentificationFailTime,
       "ruijieInefficiencyIdentificationFailTime": ruijieInefficiencyIdentificationFailTime,
       "ruijieOtherReasonIdentificationFailTime": ruijieOtherReasonIdentificationFailTime,
       "ruijieTotalRemoveLinkVerifyFailTimes": ruijieTotalRemoveLinkVerifyFailTimes,
       "ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes": ruijieLeaveAPCoverageRemoveLinkVerifyFailTimes,
       "ruijieInefficiencyRemoveLinkVerifyFailTime": ruijieInefficiencyRemoveLinkVerifyFailTime,
       "ruijieLinkVerifyFailRemoveLinkVerifyFailTime": ruijieLinkVerifyFailRemoveLinkVerifyFailTime,
       "ruijieOtherReasonRemoveLinkVerifyFailTime": ruijieOtherReasonRemoveLinkVerifyFailTime,
       "ruijieTotalRemoveLinkAssociationTimes": ruijieTotalRemoveLinkAssociationTimes,
       "ruijieLeaveAPCoverageRemoveAssociationFailTimes": ruijieLeaveAPCoverageRemoveAssociationFailTimes,
       "ruijieInefficiencyRemoveAssociationFailTime": ruijieInefficiencyRemoveAssociationFailTime,
       "ruijieAssociationFailRemoveAssociationFailTime": ruijieAssociationFailRemoveAssociationFailTime,
       "ruijieOtherReasonRemoveAssociationFailTime": ruijieOtherReasonRemoveAssociationFailTime,
       "ruijieTermServiceStatisticsWithAP": ruijieTermServiceStatisticsWithAP,
       "ruijieTermServiceStaticWithAPTable": ruijieTermServiceStaticWithAPTable,
       "ruijieTermServiceStaticWithAPTableEntry": ruijieTermServiceStaticWithAPTableEntry,
       "ruijieUserAccumulateTime": ruijieUserAccumulateTime,
       "ruijieAssociaFailTimes": ruijieAssociaFailTimes,
       "ruijieTermServiceSTatisticsWithStation": ruijieTermServiceSTatisticsWithStation,
       "ruijieTermServiceStationWithStationTable": ruijieTermServiceStationWithStationTable,
       "ruijieTermServiceStationWithStationTableEntry": ruijieTermServiceStationWithStationTableEntry,
       "ruijieStaAssociateTime": ruijieStaAssociateTime,
       "ruijieRxStaDataFrams": ruijieRxStaDataFrams,
       "ruijieRXStaErrorFrams": ruijieRXStaErrorFrams,
       "ruijieTxStaDataFrams": ruijieTxStaDataFrams,
       "ruijieReSendDataFrams": ruijieReSendDataFrams,
       "ruijieStaRxAvgSpeed": ruijieStaRxAvgSpeed,
       "ruijieStaTxAvgSpeed": ruijieStaTxAvgSpeed,
       "ruijieStaThroughput": ruijieStaThroughput,
       "ruijieStaSignalStrength": ruijieStaSignalStrength,
       "ruijieStaSignalNoise": ruijieStaSignalNoise,
       "ruijieDOT11WIDSParamObjects": ruijieDOT11WIDSParamObjects,
       "ruijieDot11WIDSInfoTable": ruijieDot11WIDSInfoTable,
       "ruijieDot11WIDSInfoEntry": ruijieDot11WIDSInfoEntry,
       "ruijieDot11WIDSLocalIndex": ruijieDot11WIDSLocalIndex,
       "ruijieDot11WIDSpermittedSSID": ruijieDot11WIDSpermittedSSID,
       "ruijieDot11WIDSpermitBSSID": ruijieDot11WIDSpermitBSSID,
       "ruijieDot11WIDSDeviceOUI": ruijieDot11WIDSDeviceOUI,
       "ruijieDot11WIDSSuspiciousAPBSS": ruijieDot11WIDSSuspiciousAPBSS,
       "ruijieDot11WIDSSuspiciousAPCount": ruijieDot11WIDSSuspiciousAPCount,
       "ruijieDot11WIDSMomentFirstTimeDetectedSusAP": ruijieDot11WIDSMomentFirstTimeDetectedSusAP,
       "ruijieDot11WIDSMomentLastTimeDetectedSusAP": ruijieDot11WIDSMomentLastTimeDetectedSusAP,
       "ruijieDot11WIDSSuspiciousAPSSID": ruijieDot11WIDSSuspiciousAPSSID,
       "ruijieDot11WIDSSuspiciousAPMaxSignalStrength": ruijieDot11WIDSSuspiciousAPMaxSignalStrength,
       "ruijieDot11WIDSSuspiciousAPUsingChannel": ruijieDot11WIDSSuspiciousAPUsingChannel,
       "ruijieDot11WIDSSuspiciousAPFrameEncrption": ruijieDot11WIDSSuspiciousAPFrameEncrption,
       "ruijieDot11WIDSSuspiciousAPNeedsDealingTag": ruijieDot11WIDSSuspiciousAPNeedsDealingTag,
       "ruijieDot11WIDSSuspiciousAPIgnoredTag": ruijieDot11WIDSSuspiciousAPIgnoredTag,
       "ruijieDot11WIDSSuspiciousSTAMAC": ruijieDot11WIDSSuspiciousSTAMAC,
       "ruijieDot11WIDSAPCountDetectingSuspiciousSTA": ruijieDot11WIDSAPCountDetectingSuspiciousSTA,
       "ruijieDot11WIDSMomentFirstTimeDetectedSusSTA": ruijieDot11WIDSMomentFirstTimeDetectedSusSTA,
       "ruijieDot11WIDSMomentLastTimeDetectedSusSTA": ruijieDot11WIDSMomentLastTimeDetectedSusSTA,
       "ruijieDot11WIDSBSSIDSuspiciousSTAAccessing": ruijieDot11WIDSBSSIDSuspiciousSTAAccessing,
       "ruijieDot11WIDSSuspiciousSTAMaxSignalStrength": ruijieDot11WIDSSuspiciousSTAMaxSignalStrength,
       "ruijieDot11WIDSSuspiciousSTAUsingChannel": ruijieDot11WIDSSuspiciousSTAUsingChannel,
       "ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode": ruijieDot11WIDSSuspiciousSTAWorksInAdhocMode,
       "ruijieDot11WIDSSuspiciousSTANeedsDealingTag": ruijieDot11WIDSSuspiciousSTANeedsDealingTag,
       "ruijieDot11WIDSSuspiciousSTAIgnoredTag": ruijieDot11WIDSSuspiciousSTAIgnoredTag,
       "ruijieDot11WIDSFloodAttackDetectSwitch": ruijieDot11WIDSFloodAttackDetectSwitch,
       "ruijieDot11WIDSSpoofAttackDetectSwitch": ruijieDot11WIDSSpoofAttackDetectSwitch,
       "ruijieDot11WIDSWeakIVDetectSwitch": ruijieDot11WIDSWeakIVDetectSwitch,
       "ruijieDot11WIDSClearIllegalEquipmentHistroyTag": ruijieDot11WIDSClearIllegalEquipmentHistroyTag,
       "ruijieDot11WIDSClearAttackDetectionHistroyTag": ruijieDot11WIDSClearAttackDetectionHistroyTag,
       "ruijieDot11WIDSClearAttackDetectionStaticsTag": ruijieDot11WIDSClearAttackDetectionStaticsTag,
       "ruijieDot11LawlessApInfoTable": ruijieDot11LawlessApInfoTable,
       "ruijieDot11LawlessApInfoTableEntry": ruijieDot11LawlessApInfoTableEntry,
       "ruijieLawlessAPIndex": ruijieLawlessAPIndex,
       "ruijieLawlessAPSignalStrength": ruijieLawlessAPSignalStrength,
       "ruijieLawlessAPSignalSNR": ruijieLawlessAPSignalSNR,
       "ruijieLawlessAPChannelNum": ruijieLawlessAPChannelNum,
       "ruijieLawlessAPSSIDName": ruijieLawlessAPSSIDName,
       "ruijieLawlessAPMacaddr": ruijieLawlessAPMacaddr,
       "ruijieLawlessAPTreatMode": ruijieLawlessAPTreatMode,
       "ruijieDot11UndefinedApInfoTable": ruijieDot11UndefinedApInfoTable,
       "ruijieDot11UndefinedApInfoTableEntry": ruijieDot11UndefinedApInfoTableEntry,
       "ruijieUndefinedAPIndex": ruijieUndefinedAPIndex,
       "ruijieUndefinedAPSignalStrength": ruijieUndefinedAPSignalStrength,
       "ruijieUndefinedAPSignalSNR": ruijieUndefinedAPSignalSNR,
       "ruijieUndefinedAPChannelNum": ruijieUndefinedAPChannelNum,
       "ruijieUndefinedAPSSIDName": ruijieUndefinedAPSSIDName,
       "ruijieUndefinedAPMacaddr": ruijieUndefinedAPMacaddr,
       "ruijieUndefinedAPTreatMode": ruijieUndefinedAPTreatMode,
       "ruijieDot11LegalityApInfoTable": ruijieDot11LegalityApInfoTable,
       "ruijieDot11LegalityApInfoTableEntry": ruijieDot11LegalityApInfoTableEntry,
       "ruijieLegalityAPIndex": ruijieLegalityAPIndex,
       "ruijieLegalityAPSignalStrength": ruijieLegalityAPSignalStrength,
       "ruijieLegalityAPSignalSNR": ruijieLegalityAPSignalSNR,
       "ruijieLegalityAPChannelNum": ruijieLegalityAPChannelNum,
       "ruijieLegalityAPSSIDName": ruijieLegalityAPSSIDName,
       "ruijieLegalityAPMacaddr": ruijieLegalityAPMacaddr,
       "ruijieLegalityAPTreatMode": ruijieLegalityAPTreatMode,
       "ruijieAlarmTrapsObjects": ruijieAlarmTrapsObjects,
       "ruijieWIDSSuspiciousType": ruijieWIDSSuspiciousType,
       "ruijieWIDSSuspiciousDeviceMac": ruijieWIDSSuspiciousDeviceMac,
       "ruijieWIDSSuspiciousDeviceExtensionInfo": ruijieWIDSSuspiciousDeviceExtensionInfo,
       "ruijieAPCurrentPMMode": ruijieAPCurrentPMMode,
       "ruijieChgWorkModeAPMac": ruijieChgWorkModeAPMac,
       "ruijieAttackType": ruijieAttackType,
       "ruijieAttackCilentIP": ruijieAttackCilentIP,
       "ruijieAttackCilentExternInfo": ruijieAttackCilentExternInfo}
)
