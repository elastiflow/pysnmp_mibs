# SNMP MIB module (RUIJIE-WLAN-FIT-AP-CF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WLAN-FIT-AP-CF-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81)
)
if mibBuilder.loadTexts:
    ruijieFitApMibModule.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApRuijieAlarmTraps_ObjectIdentity = ObjectIdentity
apRuijieAlarmTraps = _ApRuijieAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0)
)
_ApSystemAlarmTraps_ObjectIdentity = ObjectIdentity
apSystemAlarmTraps = _ApSystemAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1)
)
_ApWirelessAlarmTraps_ObjectIdentity = ObjectIdentity
apWirelessAlarmTraps = _ApWirelessAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2)
)
_ApStaAnnounceTraps_ObjectIdentity = ObjectIdentity
apStaAnnounceTraps = _ApStaAnnounceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 3)
)
_ApWAPISecurityAlarmTraps_ObjectIdentity = ObjectIdentity
apWAPISecurityAlarmTraps = _ApWAPISecurityAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 4)
)
_ApEgAnnounceTraps_ObjectIdentity = ObjectIdentity
apEgAnnounceTraps = _ApEgAnnounceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 5)
)
_ApSystemInfoConfigObjects_ObjectIdentity = ObjectIdentity
apSystemInfoConfigObjects = _ApSystemInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1)
)
_ApGeneralInfoConfigObjects_ObjectIdentity = ObjectIdentity
apGeneralInfoConfigObjects = _ApGeneralInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1)
)
_ApGeneralInfoConfigTable_Object = MibTable
apGeneralInfoConfigTable = _ApGeneralInfoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1)
)
if mibBuilder.loadTexts:
    apGeneralInfoConfigTable.setStatus("current")
_ApGeneralInfoConfigTableEntry_Object = MibTableRow
apGeneralInfoConfigTableEntry = _ApGeneralInfoConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1, 1)
)
apGeneralInfoConfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    apGeneralInfoConfigTableEntry.setStatus("current")


class _ApSysNEId_Type(DisplayString):
    """Custom type apSysNEId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApSysNEId_Type.__name__ = "DisplayString"
_ApSysNEId_Object = MibTableColumn
apSysNEId = _ApSysNEId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1, 1, 1),
    _ApSysNEId_Type()
)
apSysNEId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysNEId.setStatus("current")


class _ApSysName_Type(DisplayString):
    """Custom type apSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ApSysName_Type.__name__ = "DisplayString"
_ApSysName_Object = MibTableColumn
apSysName = _ApSysName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1, 1, 2),
    _ApSysName_Type()
)
apSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysName.setStatus("current")
_ApStatWindowTime_Type = TimeTicks
_ApStatWindowTime_Object = MibTableColumn
apStatWindowTime = _ApStatWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1, 1, 3),
    _ApStatWindowTime_Type()
)
apStatWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apStatWindowTime.setStatus("current")
_ApSampleTime_Type = Counter32
_ApSampleTime_Object = MibTableColumn
apSampleTime = _ApSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1, 1, 4),
    _ApSampleTime_Type()
)
apSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSampleTime.setStatus("current")


class _ApRtCollectOnoff_Type(Integer32):
    """Custom type apRtCollectOnoff based on Integer32"""
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


_ApRtCollectOnoff_Type.__name__ = "Integer32"
_ApRtCollectOnoff_Object = MibTableColumn
apRtCollectOnoff = _ApRtCollectOnoff_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1, 1, 5),
    _ApRtCollectOnoff_Type()
)
apRtCollectOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRtCollectOnoff.setStatus("current")


class _ApSysRestart_Type(Integer32):
    """Custom type apSysRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("restart", 1))
    )


_ApSysRestart_Type.__name__ = "Integer32"
_ApSysRestart_Object = MibTableColumn
apSysRestart = _ApSysRestart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1, 1, 6),
    _ApSysRestart_Type()
)
apSysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysRestart.setStatus("current")


class _ApSysReset_Type(Integer32):
    """Custom type apSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_ApSysReset_Type.__name__ = "Integer32"
_ApSysReset_Object = MibTableColumn
apSysReset = _ApSysReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 1, 1, 1, 7),
    _ApSysReset_Type()
)
apSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSysReset.setStatus("current")
_ApGeneralInfoReadObjects_ObjectIdentity = ObjectIdentity
apGeneralInfoReadObjects = _ApGeneralInfoReadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2)
)
_ApGeneralCfgInfoReadTable_Object = MibTable
apGeneralCfgInfoReadTable = _ApGeneralCfgInfoReadTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apGeneralCfgInfoReadTable.setStatus("current")
_ApGeneralCfgInfoReadTableEntry_Object = MibTableRow
apGeneralCfgInfoReadTableEntry = _ApGeneralCfgInfoReadTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1)
)
apGeneralCfgInfoReadTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    apGeneralCfgInfoReadTableEntry.setStatus("current")


class _ApSysDescr_Type(DisplayString):
    """Custom type apSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysDescr_Type.__name__ = "DisplayString"
_ApSysDescr_Object = MibTableColumn
apSysDescr = _ApSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 1),
    _ApSysDescr_Type()
)
apSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysDescr.setStatus("current")


class _ApSysManufacture_Type(DisplayString):
    """Custom type apSysManufacture based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysManufacture_Type.__name__ = "DisplayString"
_ApSysManufacture_Object = MibTableColumn
apSysManufacture = _ApSysManufacture_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 2),
    _ApSysManufacture_Type()
)
apSysManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysManufacture.setStatus("current")


class _ApSerialNumber_Type(DisplayString):
    """Custom type apSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSerialNumber_Type.__name__ = "DisplayString"
_ApSerialNumber_Object = MibTableColumn
apSerialNumber = _ApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 3),
    _ApSerialNumber_Type()
)
apSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSerialNumber.setStatus("current")


class _ApSysModel_Type(DisplayString):
    """Custom type apSysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysModel_Type.__name__ = "DisplayString"
_ApSysModel_Object = MibTableColumn
apSysModel = _ApSysModel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 4),
    _ApSysModel_Type()
)
apSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysModel.setStatus("current")
_ApSysUpTime_Type = Counter32
_ApSysUpTime_Object = MibTableColumn
apSysUpTime = _ApSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 5),
    _ApSysUpTime_Type()
)
apSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysUpTime.setStatus("current")
_ApSysOnlineTime_Type = Counter32
_ApSysOnlineTime_Object = MibTableColumn
apSysOnlineTime = _ApSysOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 6),
    _ApSysOnlineTime_Type()
)
apSysOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysOnlineTime.setStatus("current")
_ApSysIPAddress_Type = IpAddress
_ApSysIPAddress_Object = MibTableColumn
apSysIPAddress = _ApSysIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 7),
    _ApSysIPAddress_Type()
)
apSysIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysIPAddress.setStatus("current")
_ApSysIPNetMask_Type = IpAddress
_ApSysIPNetMask_Object = MibTableColumn
apSysIPNetMask = _ApSysIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 8),
    _ApSysIPNetMask_Type()
)
apSysIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysIPNetMask.setStatus("current")
_ApSysGateWayAddr_Type = IpAddress
_ApSysGateWayAddr_Object = MibTableColumn
apSysGateWayAddr = _ApSysGateWayAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 9),
    _ApSysGateWayAddr_Type()
)
apSysGateWayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysGateWayAddr.setStatus("current")
_ApSysMacAddrConnectToAC_Type = MacAddress
_ApSysMacAddrConnectToAC_Object = MibTableColumn
apSysMacAddrConnectToAC = _ApSysMacAddrConnectToAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 10),
    _ApSysMacAddrConnectToAC_Type()
)
apSysMacAddrConnectToAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMacAddrConnectToAC.setStatus("current")
_ApSoftwareName_Type = DisplayString
_ApSoftwareName_Object = MibTableColumn
apSoftwareName = _ApSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 11),
    _ApSoftwareName_Type()
)
apSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareName.setStatus("current")
_ApSoftwareVersion_Type = DisplayString
_ApSoftwareVersion_Object = MibTableColumn
apSoftwareVersion = _ApSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 12),
    _ApSoftwareVersion_Type()
)
apSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareVersion.setStatus("current")
_ApSoftwareVendor_Type = DisplayString
_ApSoftwareVendor_Object = MibTableColumn
apSoftwareVendor = _ApSoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 13),
    _ApSoftwareVendor_Type()
)
apSoftwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareVendor.setStatus("current")
_ApCPUType_Type = DisplayString
_ApCPUType_Object = MibTableColumn
apCPUType = _ApCPUType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 14),
    _ApCPUType_Type()
)
apCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCPUType.setStatus("current")
_ApMemoryType_Type = DisplayString
_ApMemoryType_Object = MibTableColumn
apMemoryType = _ApMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 15),
    _ApMemoryType_Type()
)
apMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMemoryType.setStatus("current")
_ApMemorySize_Type = OctetString
_ApMemorySize_Object = MibTableColumn
apMemorySize = _ApMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 17),
    _ApMemorySize_Type()
)
apMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMemorySize.setStatus("current")
_ApFlashSize_Type = OctetString
_ApFlashSize_Object = MibTableColumn
apFlashSize = _ApFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 2, 1, 1, 18),
    _ApFlashSize_Type()
)
apFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlashSize.setStatus("current")
_ApGeneralStatusCFGObjects_ObjectIdentity = ObjectIdentity
apGeneralStatusCFGObjects = _ApGeneralStatusCFGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3)
)
_ApGeneralStatusCFGTable_Object = MibTable
apGeneralStatusCFGTable = _ApGeneralStatusCFGTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1)
)
if mibBuilder.loadTexts:
    apGeneralStatusCFGTable.setStatus("current")
_ApGeneralStatusCFGTableEntry_Object = MibTableRow
apGeneralStatusCFGTableEntry = _ApGeneralStatusCFGTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1)
)
apGeneralStatusCFGTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apAssoStatusAPMac"),
)
if mibBuilder.loadTexts:
    apGeneralStatusCFGTableEntry.setStatus("current")
_ApGeneralStatusCFGAPName_Type = DisplayString
_ApGeneralStatusCFGAPName_Object = MibTableColumn
apGeneralStatusCFGAPName = _ApGeneralStatusCFGAPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 1),
    _ApGeneralStatusCFGAPName_Type()
)
apGeneralStatusCFGAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGAPName.setStatus("current")


class _ApGeneralStatusCFGACAssociateStatus_Type(Integer32):
    """Custom type apGeneralStatusCFGACAssociateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deassociate", 0),
          ("associate", 1))
    )


_ApGeneralStatusCFGACAssociateStatus_Type.__name__ = "Integer32"
_ApGeneralStatusCFGACAssociateStatus_Object = MibTableColumn
apGeneralStatusCFGACAssociateStatus = _ApGeneralStatusCFGACAssociateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 2),
    _ApGeneralStatusCFGACAssociateStatus_Type()
)
apGeneralStatusCFGACAssociateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGACAssociateStatus.setStatus("current")


class _ApGeneralStatusCFGMonitorMode_Type(Integer32):
    """Custom type apGeneralStatusCFGMonitorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("monitor", 1),
          ("semiMonitor", 2))
    )


_ApGeneralStatusCFGMonitorMode_Type.__name__ = "Integer32"
_ApGeneralStatusCFGMonitorMode_Object = MibTableColumn
apGeneralStatusCFGMonitorMode = _ApGeneralStatusCFGMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 3),
    _ApGeneralStatusCFGMonitorMode_Type()
)
apGeneralStatusCFGMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apGeneralStatusCFGMonitorMode.setStatus("current")
_ApGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac_Type = MacAddress
_ApGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac_Object = MibScalar
apGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac = _ApGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 4),
    _ApGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac_Type()
)
apGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac.setStatus("current")


class _ApGeneralStatusCFGACHbAssocStatus_Type(Integer32):
    """Custom type apGeneralStatusCFGACHbAssocStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deassociate", 0),
          ("associate", 1))
    )


_ApGeneralStatusCFGACHbAssocStatus_Type.__name__ = "Integer32"
_ApGeneralStatusCFGACHbAssocStatus_Object = MibTableColumn
apGeneralStatusCFGACHbAssocStatus = _ApGeneralStatusCFGACHbAssocStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 5),
    _ApGeneralStatusCFGACHbAssocStatus_Type()
)
apGeneralStatusCFGACHbAssocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGACHbAssocStatus.setStatus("current")
_ApGeneralStatusCFGScanType_Type = Integer32
_ApGeneralStatusCFGScanType_Object = MibTableColumn
apGeneralStatusCFGScanType = _ApGeneralStatusCFGScanType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 6),
    _ApGeneralStatusCFGScanType_Type()
)
apGeneralStatusCFGScanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apGeneralStatusCFGScanType.setStatus("current")
_ApGeneralStatusCFGAssocTimes_Type = Counter32
_ApGeneralStatusCFGAssocTimes_Object = MibTableColumn
apGeneralStatusCFGAssocTimes = _ApGeneralStatusCFGAssocTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 7),
    _ApGeneralStatusCFGAssocTimes_Type()
)
apGeneralStatusCFGAssocTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGAssocTimes.setStatus("current")
_ApGeneralStatusCFGAssocSuccessTimes_Type = Counter32
_ApGeneralStatusCFGAssocSuccessTimes_Object = MibTableColumn
apGeneralStatusCFGAssocSuccessTimes = _ApGeneralStatusCFGAssocSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 8),
    _ApGeneralStatusCFGAssocSuccessTimes_Type()
)
apGeneralStatusCFGAssocSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGAssocSuccessTimes.setStatus("current")
_ApGeneralStatusCFGAssocFailTimes_Type = Counter32
_ApGeneralStatusCFGAssocFailTimes_Object = MibTableColumn
apGeneralStatusCFGAssocFailTimes = _ApGeneralStatusCFGAssocFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 9),
    _ApGeneralStatusCFGAssocFailTimes_Type()
)
apGeneralStatusCFGAssocFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGAssocFailTimes.setStatus("current")
_ApGeneralStatusCFG24GSignalStrength_Type = Integer32
_ApGeneralStatusCFG24GSignalStrength_Object = MibTableColumn
apGeneralStatusCFG24GSignalStrength = _ApGeneralStatusCFG24GSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 10),
    _ApGeneralStatusCFG24GSignalStrength_Type()
)
apGeneralStatusCFG24GSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFG24GSignalStrength.setStatus("current")
_ApGeneralStatusCFG5GSignalStrength_Type = Integer32
_ApGeneralStatusCFG5GSignalStrength_Object = MibTableColumn
apGeneralStatusCFG5GSignalStrength = _ApGeneralStatusCFG5GSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 11),
    _ApGeneralStatusCFG5GSignalStrength_Type()
)
apGeneralStatusCFG5GSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFG5GSignalStrength.setStatus("current")
_ApGeneralStatusCFGTotalRxBytes_Type = Counter64
_ApGeneralStatusCFGTotalRxBytes_Object = MibTableColumn
apGeneralStatusCFGTotalRxBytes = _ApGeneralStatusCFGTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 12),
    _ApGeneralStatusCFGTotalRxBytes_Type()
)
apGeneralStatusCFGTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGTotalRxBytes.setStatus("current")
_ApGeneralStatusCFGTotalTxBytes_Type = Counter64
_ApGeneralStatusCFGTotalTxBytes_Object = MibTableColumn
apGeneralStatusCFGTotalTxBytes = _ApGeneralStatusCFGTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 1, 3, 1, 1, 13),
    _ApGeneralStatusCFGTotalTxBytes_Type()
)
apGeneralStatusCFGTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGeneralStatusCFGTotalTxBytes.setStatus("current")
_ApInterfaceConfigObjects_ObjectIdentity = ObjectIdentity
apInterfaceConfigObjects = _ApInterfaceConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2)
)
_ApInterfaceNumberObjects_ObjectIdentity = ObjectIdentity
apInterfaceNumberObjects = _ApInterfaceNumberObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 1)
)
_ApInterfaceNumberTable_Object = MibTable
apInterfaceNumberTable = _ApInterfaceNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 1, 1)
)
if mibBuilder.loadTexts:
    apInterfaceNumberTable.setStatus("current")
_ApInterfaceNumberTableEntry_Object = MibTableRow
apInterfaceNumberTableEntry = _ApInterfaceNumberTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 1, 1, 1)
)
apInterfaceNumberTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    apInterfaceNumberTableEntry.setStatus("current")


class _ApIfNumber_Type(Integer32):
    """Custom type apIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApIfNumber_Type.__name__ = "Integer32"
_ApIfNumber_Object = MibTableColumn
apIfNumber = _ApIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 1, 1, 1, 1),
    _ApIfNumber_Type()
)
apIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfNumber.setStatus("current")


class _ApBSSIDNum_Type(Integer32):
    """Custom type apBSSIDNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApBSSIDNum_Type.__name__ = "Integer32"
_ApBSSIDNum_Object = MibTableColumn
apBSSIDNum = _ApBSSIDNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 1, 1, 1, 2),
    _ApBSSIDNum_Type()
)
apBSSIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBSSIDNum.setStatus("current")
_ApInterfaceRGMIIcfgObjects_ObjectIdentity = ObjectIdentity
apInterfaceRGMIIcfgObjects = _ApInterfaceRGMIIcfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2)
)
_ApInterfaceRGMIIconfigTable_Object = MibTable
apInterfaceRGMIIconfigTable = _ApInterfaceRGMIIconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1)
)
if mibBuilder.loadTexts:
    apInterfaceRGMIIconfigTable.setStatus("current")
_ApInterfaceRGMIIconfigTableEntry_Object = MibTableRow
apInterfaceRGMIIconfigTableEntry = _ApInterfaceRGMIIconfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1)
)
apInterfaceRGMIIconfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apIfLocalRGMIINum"),
)
if mibBuilder.loadTexts:
    apInterfaceRGMIIconfigTableEntry.setStatus("current")
_ApIfLocalRGMIINum_Type = Integer32
_ApIfLocalRGMIINum_Object = MibTableColumn
apIfLocalRGMIINum = _ApIfLocalRGMIINum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 1),
    _ApIfLocalRGMIINum_Type()
)
apIfLocalRGMIINum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apIfLocalRGMIINum.setStatus("current")


class _ApIfRGMIIDescr_Type(DisplayString):
    """Custom type apIfRGMIIDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApIfRGMIIDescr_Type.__name__ = "DisplayString"
_ApIfRGMIIDescr_Object = MibTableColumn
apIfRGMIIDescr = _ApIfRGMIIDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 2),
    _ApIfRGMIIDescr_Type()
)
apIfRGMIIDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfRGMIIDescr.setStatus("current")
_ApIfRGMIIType_Type = IANAifType
_ApIfRGMIIType_Object = MibTableColumn
apIfRGMIIType = _ApIfRGMIIType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 3),
    _ApIfRGMIIType_Type()
)
apIfRGMIIType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfRGMIIType.setStatus("current")
_ApIfRGMIIMtu_Type = Integer32
_ApIfRGMIIMtu_Object = MibTableColumn
apIfRGMIIMtu = _ApIfRGMIIMtu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 4),
    _ApIfRGMIIMtu_Type()
)
apIfRGMIIMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfRGMIIMtu.setStatus("current")
_ApIfRGMIISpeed_Type = Integer32
_ApIfRGMIISpeed_Object = MibTableColumn
apIfRGMIISpeed = _ApIfRGMIISpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 5),
    _ApIfRGMIISpeed_Type()
)
apIfRGMIISpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfRGMIISpeed.setStatus("current")
_ApIfRGMIIPhysAddress_Type = MacAddress
_ApIfRGMIIPhysAddress_Object = MibTableColumn
apIfRGMIIPhysAddress = _ApIfRGMIIPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 6),
    _ApIfRGMIIPhysAddress_Type()
)
apIfRGMIIPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfRGMIIPhysAddress.setStatus("current")


class _ApIfRGMIIAdminStatusEnable_Type(Integer32):
    """Custom type apIfRGMIIAdminStatusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("admindown", 0),
          ("up", 1))
    )


_ApIfRGMIIAdminStatusEnable_Type.__name__ = "Integer32"
_ApIfRGMIIAdminStatusEnable_Object = MibTableColumn
apIfRGMIIAdminStatusEnable = _ApIfRGMIIAdminStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 7),
    _ApIfRGMIIAdminStatusEnable_Type()
)
apIfRGMIIAdminStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfRGMIIAdminStatusEnable.setStatus("current")


class _ApIfRGMIIOperStatus_Type(Integer32):
    """Custom type apIfRGMIIOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("admindown", 2))
    )


_ApIfRGMIIOperStatus_Type.__name__ = "Integer32"
_ApIfRGMIIOperStatus_Object = MibTableColumn
apIfRGMIIOperStatus = _ApIfRGMIIOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 8),
    _ApIfRGMIIOperStatus_Type()
)
apIfRGMIIOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfRGMIIOperStatus.setStatus("current")
_ApIfRGMIILastChange_Type = TimeTicks
_ApIfRGMIILastChange_Object = MibTableColumn
apIfRGMIILastChange = _ApIfRGMIILastChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 2, 1, 1, 9),
    _ApIfRGMIILastChange_Type()
)
apIfRGMIILastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfRGMIILastChange.setStatus("current")
_ApInterfaceWirelesscfgObjects_ObjectIdentity = ObjectIdentity
apInterfaceWirelesscfgObjects = _ApInterfaceWirelesscfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3)
)
_ApInterfaceWirelessconfigTable_Object = MibTable
apInterfaceWirelessconfigTable = _ApInterfaceWirelessconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1)
)
if mibBuilder.loadTexts:
    apInterfaceWirelessconfigTable.setStatus("current")
_ApInterfaceWirelessconfigTableEntry_Object = MibTableRow
apInterfaceWirelessconfigTableEntry = _ApInterfaceWirelessconfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1)
)
apInterfaceWirelessconfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apInterfaceWirelessconfigTableEntry.setStatus("current")


class _ApIfWireDescr_Type(DisplayString):
    """Custom type apIfWireDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApIfWireDescr_Type.__name__ = "DisplayString"
_ApIfWireDescr_Object = MibTableColumn
apIfWireDescr = _ApIfWireDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 1),
    _ApIfWireDescr_Type()
)
apIfWireDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireDescr.setStatus("current")
_ApIfWireType_Type = IANAifType
_ApIfWireType_Object = MibTableColumn
apIfWireType = _ApIfWireType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 2),
    _ApIfWireType_Type()
)
apIfWireType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireType.setStatus("current")
_ApIfWireMtu_Type = Integer32
_ApIfWireMtu_Object = MibTableColumn
apIfWireMtu = _ApIfWireMtu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 3),
    _ApIfWireMtu_Type()
)
apIfWireMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireMtu.setStatus("current")
_ApIfWireSpeed_Type = Integer32
_ApIfWireSpeed_Object = MibTableColumn
apIfWireSpeed = _ApIfWireSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 4),
    _ApIfWireSpeed_Type()
)
apIfWireSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireSpeed.setStatus("current")
_ApIfWirePhysAddress_Type = MacAddress
_ApIfWirePhysAddress_Object = MibTableColumn
apIfWirePhysAddress = _ApIfWirePhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 5),
    _ApIfWirePhysAddress_Type()
)
apIfWirePhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWirePhysAddress.setStatus("current")


class _ApIfWireAdminStatusEnable_Type(Integer32):
    """Custom type apIfWireAdminStatusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("admindown", 1))
    )


_ApIfWireAdminStatusEnable_Type.__name__ = "Integer32"
_ApIfWireAdminStatusEnable_Object = MibTableColumn
apIfWireAdminStatusEnable = _ApIfWireAdminStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 6),
    _ApIfWireAdminStatusEnable_Type()
)
apIfWireAdminStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireAdminStatusEnable.setStatus("current")


class _ApIfWireOperStatus_Type(Integer32):
    """Custom type apIfWireOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("admindown", 2))
    )


_ApIfWireOperStatus_Type.__name__ = "Integer32"
_ApIfWireOperStatus_Object = MibTableColumn
apIfWireOperStatus = _ApIfWireOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 7),
    _ApIfWireOperStatus_Type()
)
apIfWireOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireOperStatus.setStatus("current")
_ApIfWireLastChange_Type = TimeTicks
_ApIfWireLastChange_Object = MibTableColumn
apIfWireLastChange = _ApIfWireLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 8),
    _ApIfWireLastChange_Type()
)
apIfWireLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireLastChange.setStatus("current")


class _ApIfWireChannelAutoSelectEnable_Type(Integer32):
    """Custom type apIfWireChannelAutoSelectEnable based on Integer32"""
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


_ApIfWireChannelAutoSelectEnable_Type.__name__ = "Integer32"
_ApIfWireChannelAutoSelectEnable_Object = MibTableColumn
apIfWireChannelAutoSelectEnable = _ApIfWireChannelAutoSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 9),
    _ApIfWireChannelAutoSelectEnable_Type()
)
apIfWireChannelAutoSelectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireChannelAutoSelectEnable.setStatus("current")
_ApIfWireRadioChannelConfig_Type = Integer32
_ApIfWireRadioChannelConfig_Object = MibTableColumn
apIfWireRadioChannelConfig = _ApIfWireRadioChannelConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 10),
    _ApIfWireRadioChannelConfig_Type()
)
apIfWireRadioChannelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireRadioChannelConfig.setStatus("current")
_ApIfWireRadioChannelUsing_Type = Integer32
_ApIfWireRadioChannelUsing_Object = MibTableColumn
apIfWireRadioChannelUsing = _ApIfWireRadioChannelUsing_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 11),
    _ApIfWireRadioChannelUsing_Type()
)
apIfWireRadioChannelUsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireRadioChannelUsing.setStatus("current")
_ApIfWireCurrRadioModeSupport_Type = Counter32
_ApIfWireCurrRadioModeSupport_Object = MibTableColumn
apIfWireCurrRadioModeSupport = _ApIfWireCurrRadioModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 12),
    _ApIfWireCurrRadioModeSupport_Type()
)
apIfWireCurrRadioModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireCurrRadioModeSupport.setStatus("current")
_ApIfWireRadioModeConfig_Type = Counter32
_ApIfWireRadioModeConfig_Object = MibTableColumn
apIfWireRadioModeConfig = _ApIfWireRadioModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 13),
    _ApIfWireRadioModeConfig_Type()
)
apIfWireRadioModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireRadioModeConfig.setStatus("current")


class _ApIfWireTransmitSpeedConfig_Type(DisplayString):
    """Custom type apIfWireTransmitSpeedConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApIfWireTransmitSpeedConfig_Type.__name__ = "DisplayString"
_ApIfWireTransmitSpeedConfig_Object = MibTableColumn
apIfWireTransmitSpeedConfig = _ApIfWireTransmitSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 14),
    _ApIfWireTransmitSpeedConfig_Type()
)
apIfWireTransmitSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireTransmitSpeedConfig.setStatus("current")


class _ApIfWireMaxTxPwrLvl_Type(DisplayString):
    """Custom type apIfWireMaxTxPwrLvl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApIfWireMaxTxPwrLvl_Type.__name__ = "DisplayString"
_ApIfWireMaxTxPwrLvl_Object = MibTableColumn
apIfWireMaxTxPwrLvl = _ApIfWireMaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 15),
    _ApIfWireMaxTxPwrLvl_Type()
)
apIfWireMaxTxPwrLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireMaxTxPwrLvl.setStatus("current")
_ApIfWirePwrAttRange_Type = Integer32
_ApIfWirePwrAttRange_Object = MibTableColumn
apIfWirePwrAttRange = _ApIfWirePwrAttRange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 16),
    _ApIfWirePwrAttRange_Type()
)
apIfWirePwrAttRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWirePwrAttRange.setStatus("current")
_ApIfWirePwrAttValue_Type = Integer32
_ApIfWirePwrAttValue_Object = MibTableColumn
apIfWirePwrAttValue = _ApIfWirePwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 17),
    _ApIfWirePwrAttValue_Type()
)
apIfWirePwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWirePwrAttValue.setStatus("current")
_ApIfWireAntennaGain_Type = Integer32
_ApIfWireAntennaGain_Object = MibTableColumn
apIfWireAntennaGain = _ApIfWireAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 18),
    _ApIfWireAntennaGain_Type()
)
apIfWireAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireAntennaGain.setStatus("current")
_ApIfWirePowerMgmtEnable_Type = TruthValue
_ApIfWirePowerMgmtEnable_Object = MibTableColumn
apIfWirePowerMgmtEnable = _ApIfWirePowerMgmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 19),
    _ApIfWirePowerMgmtEnable_Type()
)
apIfWirePowerMgmtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWirePowerMgmtEnable.setStatus("current")
_ApTxPwr_Type = Integer32
_ApTxPwr_Object = MibTableColumn
apTxPwr = _ApTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 20),
    _ApTxPwr_Type()
)
apTxPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTxPwr.setStatus("current")
_ApIfWireMaxStationNumPermitted_Type = Counter32
_ApIfWireMaxStationNumPermitted_Object = MibTableColumn
apIfWireMaxStationNumPermitted = _ApIfWireMaxStationNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 21),
    _ApIfWireMaxStationNumPermitted_Type()
)
apIfWireMaxStationNumPermitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireMaxStationNumPermitted.setStatus("current")


class _ApIfWireAMPDUEnabled_Type(Integer32):
    """Custom type apIfWireAMPDUEnabled based on Integer32"""
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


_ApIfWireAMPDUEnabled_Type.__name__ = "Integer32"
_ApIfWireAMPDUEnabled_Object = MibTableColumn
apIfWireAMPDUEnabled = _ApIfWireAMPDUEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 22),
    _ApIfWireAMPDUEnabled_Type()
)
apIfWireAMPDUEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireAMPDUEnabled.setStatus("current")


class _ApIfWireBWMode_Type(Integer32):
    """Custom type apIfWireBWMode based on Integer32"""
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


_ApIfWireBWMode_Type.__name__ = "Integer32"
_ApIfWireBWMode_Object = MibTableColumn
apIfWireBWMode = _ApIfWireBWMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 23),
    _ApIfWireBWMode_Type()
)
apIfWireBWMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireBWMode.setStatus("current")


class _ApIfWireShortGIEnabled_Type(Integer32):
    """Custom type apIfWireShortGIEnabled based on Integer32"""
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


_ApIfWireShortGIEnabled_Type.__name__ = "Integer32"
_ApIfWireShortGIEnabled_Object = MibTableColumn
apIfWireShortGIEnabled = _ApIfWireShortGIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 24),
    _ApIfWireShortGIEnabled_Type()
)
apIfWireShortGIEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireShortGIEnabled.setStatus("current")
_ApIfWireIs11nOnly_Type = TruthValue
_ApIfWireIs11nOnly_Object = MibTableColumn
apIfWireIs11nOnly = _ApIfWireIs11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 25),
    _ApIfWireIs11nOnly_Type()
)
apIfWireIs11nOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireIs11nOnly.setStatus("current")
_ApIfWireBeaconIntvl_Type = Integer32
_ApIfWireBeaconIntvl_Object = MibTableColumn
apIfWireBeaconIntvl = _ApIfWireBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 26),
    _ApIfWireBeaconIntvl_Type()
)
apIfWireBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireBeaconIntvl.setStatus("current")
_ApIfWireDtimIntvl_Type = Integer32
_ApIfWireDtimIntvl_Object = MibTableColumn
apIfWireDtimIntvl = _ApIfWireDtimIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 27),
    _ApIfWireDtimIntvl_Type()
)
apIfWireDtimIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireDtimIntvl.setStatus("current")
_ApIfWireRtsThreshold_Type = Integer32
_ApIfWireRtsThreshold_Object = MibTableColumn
apIfWireRtsThreshold = _ApIfWireRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 28),
    _ApIfWireRtsThreshold_Type()
)
apIfWireRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireRtsThreshold.setStatus("current")
_ApIfWireFragThreshlod_Type = Integer32
_ApIfWireFragThreshlod_Object = MibTableColumn
apIfWireFragThreshlod = _ApIfWireFragThreshlod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 29),
    _ApIfWireFragThreshlod_Type()
)
apIfWireFragThreshlod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireFragThreshlod.setStatus("current")


class _ApIfWirePreambleLen_Type(Integer32):
    """Custom type apIfWirePreambleLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 0),
          ("short", 1))
    )


_ApIfWirePreambleLen_Type.__name__ = "Integer32"
_ApIfWirePreambleLen_Object = MibTableColumn
apIfWirePreambleLen = _ApIfWirePreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 30),
    _ApIfWirePreambleLen_Type()
)
apIfWirePreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWirePreambleLen.setStatus("current")
_ApAntennaReceiveMask_Type = Integer32
_ApAntennaReceiveMask_Object = MibTableColumn
apAntennaReceiveMask = _ApAntennaReceiveMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 31),
    _ApAntennaReceiveMask_Type()
)
apAntennaReceiveMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAntennaReceiveMask.setStatus("current")
_ApAntennaTransmitMask_Type = Integer32
_ApAntennaTransmitMask_Object = MibTableColumn
apAntennaTransmitMask = _ApAntennaTransmitMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 32),
    _ApAntennaTransmitMask_Type()
)
apAntennaTransmitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAntennaTransmitMask.setStatus("current")
_ApIfWireAMSDUEnabled_Type = Integer32
_ApIfWireAMSDUEnabled_Object = MibTableColumn
apIfWireAMSDUEnabled = _ApIfWireAMSDUEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 33),
    _ApIfWireAMSDUEnabled_Type()
)
apIfWireAMSDUEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireAMSDUEnabled.setStatus("current")
_ApIfwireMcsSuppIndex_Type = Integer32
_ApIfwireMcsSuppIndex_Object = MibTableColumn
apIfwireMcsSuppIndex = _ApIfwireMcsSuppIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 34),
    _ApIfwireMcsSuppIndex_Type()
)
apIfwireMcsSuppIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfwireMcsSuppIndex.setStatus("current")
_ApIfwireMcsMandIndex_Type = Integer32
_ApIfwireMcsMandIndex_Object = MibTableColumn
apIfwireMcsMandIndex = _ApIfwireMcsMandIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 35),
    _ApIfwireMcsMandIndex_Type()
)
apIfwireMcsMandIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfwireMcsMandIndex.setStatus("current")
_ApIfwire11nSuppEnable_Type = Integer32
_ApIfwire11nSuppEnable_Object = MibTableColumn
apIfwire11nSuppEnable = _ApIfwire11nSuppEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 36),
    _ApIfwire11nSuppEnable_Type()
)
apIfwire11nSuppEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfwire11nSuppEnable.setStatus("current")
_ApShtRetryThld_Type = Integer32
_ApShtRetryThld_Object = MibTableColumn
apShtRetryThld = _ApShtRetryThld_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 37),
    _ApShtRetryThld_Type()
)
apShtRetryThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apShtRetryThld.setStatus("current")
_ApLongRetryThld_Type = Integer32
_ApLongRetryThld_Object = MibTableColumn
apLongRetryThld = _ApLongRetryThld_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 38),
    _ApLongRetryThld_Type()
)
apLongRetryThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLongRetryThld.setStatus("current")
_ApIfWireResponseRssi_Type = Integer32
_ApIfWireResponseRssi_Object = MibTableColumn
apIfWireResponseRssi = _ApIfWireResponseRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 39),
    _ApIfWireResponseRssi_Type()
)
apIfWireResponseRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireResponseRssi.setStatus("current")
_ApIfWireMaxStationLimit_Type = Integer32
_ApIfWireMaxStationLimit_Object = MibTableColumn
apIfWireMaxStationLimit = _ApIfWireMaxStationLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 40),
    _ApIfWireMaxStationLimit_Type()
)
apIfWireMaxStationLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIfWireMaxStationLimit.setStatus("current")
_ApIfWireLinkscan_Type = Integer32
_ApIfWireLinkscan_Object = MibTableColumn
apIfWireLinkscan = _ApIfWireLinkscan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 41),
    _ApIfWireLinkscan_Type()
)
apIfWireLinkscan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireLinkscan.setStatus("current")
_ApIfWireRadioChannelutilization_Type = Integer32
_ApIfWireRadioChannelutilization_Object = MibTableColumn
apIfWireRadioChannelutilization = _ApIfWireRadioChannelutilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 2, 3, 1, 1, 42),
    _ApIfWireRadioChannelutilization_Type()
)
apIfWireRadioChannelutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfWireRadioChannelutilization.setStatus("current")
_ApSSIDConfigObjects_ObjectIdentity = ObjectIdentity
apSSIDConfigObjects = _ApSSIDConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3)
)
_ApSSIDListCreateTable_Object = MibTable
apSSIDListCreateTable = _ApSSIDListCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 1)
)
if mibBuilder.loadTexts:
    apSSIDListCreateTable.setStatus("current")
_ApSSIDListCreateTableEntry_Object = MibTableRow
apSSIDListCreateTableEntry = _ApSSIDListCreateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 1, 1)
)
apSSIDListCreateTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDAPMac"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDRadioId"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apSSIDListCreateTableEntry.setStatus("current")
_ApSSIDAPMac_Type = MacAddress
_ApSSIDAPMac_Object = MibTableColumn
apSSIDAPMac = _ApSSIDAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 1, 1, 1),
    _ApSSIDAPMac_Type()
)
apSSIDAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDAPMac.setStatus("current")
_ApSSIDRadioId_Type = Integer32
_ApSSIDRadioId_Object = MibTableColumn
apSSIDRadioId = _ApSSIDRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 1, 1, 2),
    _ApSSIDRadioId_Type()
)
apSSIDRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDRadioId.setStatus("current")
_ApSSIDListName_Type = DisplayString
_ApSSIDListName_Object = MibTableColumn
apSSIDListName = _ApSSIDListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 1, 1, 3),
    _ApSSIDListName_Type()
)
apSSIDListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDListName.setStatus("current")
_ApListBSSIDAddr_Type = MacAddress
_ApListBSSIDAddr_Object = MibTableColumn
apListBSSIDAddr = _ApListBSSIDAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 1, 1, 4),
    _ApListBSSIDAddr_Type()
)
apListBSSIDAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apListBSSIDAddr.setStatus("current")
_ApSSIDListStatus_Type = RowStatus
_ApSSIDListStatus_Object = MibTableColumn
apSSIDListStatus = _ApSSIDListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 1, 1, 5),
    _ApSSIDListStatus_Type()
)
apSSIDListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDListStatus.setStatus("current")
_ApSSIDConfigTable_Object = MibTable
apSSIDConfigTable = _ApSSIDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2)
)
if mibBuilder.loadTexts:
    apSSIDConfigTable.setStatus("current")
_ApSSIDConfigTableEntry_Object = MibTableRow
apSSIDConfigTableEntry = _ApSSIDConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1)
)
apSSIDConfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apSSIDConfigTableEntry.setStatus("current")


class _ApSSIDName_Type(DisplayString):
    """Custom type apSSIDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSSIDName_Type.__name__ = "DisplayString"
_ApSSIDName_Object = MibTableColumn
apSSIDName = _ApSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 1),
    _ApSSIDName_Type()
)
apSSIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDName.setStatus("current")
_ApSSIDEnabled_Type = TruthValue
_ApSSIDEnabled_Object = MibTableColumn
apSSIDEnabled = _ApSSIDEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 2),
    _ApSSIDEnabled_Type()
)
apSSIDEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDEnabled.setStatus("current")
_ApSSIDHidden_Type = TruthValue
_ApSSIDHidden_Object = MibTableColumn
apSSIDHidden = _ApSSIDHidden_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 3),
    _ApSSIDHidden_Type()
)
apSSIDHidden.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDHidden.setStatus("current")
_ApStaIsolate_Type = TruthValue
_ApStaIsolate_Object = MibTableColumn
apStaIsolate = _ApStaIsolate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 4),
    _ApStaIsolate_Type()
)
apStaIsolate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStaIsolate.setStatus("current")


class _ApDot11Auth_Type(Integer32):
    """Custom type apDot11Auth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1))
    )


_ApDot11Auth_Type.__name__ = "Integer32"
_ApDot11Auth_Object = MibTableColumn
apDot11Auth = _ApDot11Auth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 5),
    _ApDot11Auth_Type()
)
apDot11Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDot11Auth.setStatus("current")


class _ApsecurityMode_Type(Integer32):
    """Custom type apsecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wpa", 1),
          ("wpa2", 2),
          ("wapi", 3))
    )


_ApsecurityMode_Type.__name__ = "Integer32"
_ApsecurityMode_Object = MibTableColumn
apsecurityMode = _ApsecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 6),
    _ApsecurityMode_Type()
)
apsecurityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsecurityMode.setStatus("current")


class _ApAuthenMode_Type(Integer32):
    """Custom type apAuthenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("psk", 1),
          ("radius", 2),
          ("wapicer", 3),
          ("web", 4),
          ("psk-web", 5),
          ("wapicer-web", 6),
          ("wapipsk", 7))
    )


_ApAuthenMode_Type.__name__ = "Integer32"
_ApAuthenMode_Object = MibTableColumn
apAuthenMode = _ApAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 7),
    _ApAuthenMode_Type()
)
apAuthenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAuthenMode.setStatus("current")


class _ApSecurityCiphers_Type(Integer32):
    """Custom type apSecurityCiphers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wep40", 1),
          ("wep104", 2),
          ("tkip", 3),
          ("aesccmp", 4),
          ("wapisms4", 5))
    )


_ApSecurityCiphers_Type.__name__ = "Integer32"
_ApSecurityCiphers_Object = MibTableColumn
apSecurityCiphers = _ApSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 8),
    _ApSecurityCiphers_Type()
)
apSecurityCiphers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurityCiphers.setStatus("current")
_ApVlanId_Type = Integer32
_ApVlanId_Object = MibTableColumn
apVlanId = _ApVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 9),
    _ApVlanId_Type()
)
apVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apVlanId.setStatus("current")
_ApVlanIpAddr_Type = IpAddress
_ApVlanIpAddr_Object = MibTableColumn
apVlanIpAddr = _ApVlanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 10),
    _ApVlanIpAddr_Type()
)
apVlanIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apVlanIpAddr.setStatus("current")
_ApMaxSimultUsers_Type = Counter32
_ApMaxSimultUsers_Object = MibTableColumn
apMaxSimultUsers = _ApMaxSimultUsers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 11),
    _ApMaxSimultUsers_Type()
)
apMaxSimultUsers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apMaxSimultUsers.setStatus("current")
_ApStaUplinkMaxRate_Type = Counter32
_ApStaUplinkMaxRate_Object = MibTableColumn
apStaUplinkMaxRate = _ApStaUplinkMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 12),
    _ApStaUplinkMaxRate_Type()
)
apStaUplinkMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStaUplinkMaxRate.setStatus("current")
_ApStaDwlinkMaxRate_Type = Counter32
_ApStaDwlinkMaxRate_Object = MibTableColumn
apStaDwlinkMaxRate = _ApStaDwlinkMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 13),
    _ApStaDwlinkMaxRate_Type()
)
apStaDwlinkMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStaDwlinkMaxRate.setStatus("current")
_ApSSIDCfgStatus_Type = RowStatus
_ApSSIDCfgStatus_Object = MibTableColumn
apSSIDCfgStatus = _ApSSIDCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 3, 2, 1, 14),
    _ApSSIDCfgStatus_Type()
)
apSSIDCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSSIDCfgStatus.setStatus("current")
_ApSecurityConfigObjects_ObjectIdentity = ObjectIdentity
apSecurityConfigObjects = _ApSecurityConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4)
)
_ApSecurityConfigTable_Object = MibTable
apSecurityConfigTable = _ApSecurityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1)
)
if mibBuilder.loadTexts:
    apSecurityConfigTable.setStatus("current")
_ApSecurityConfigTableEntry_Object = MibTableRow
apSecurityConfigTableEntry = _ApSecurityConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1)
)
apSecurityConfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apSecurityConfigTableEntry.setStatus("current")
_ApWEPCipherKeyIndex_Type = Integer32
_ApWEPCipherKeyIndex_Object = MibTableColumn
apWEPCipherKeyIndex = _ApWEPCipherKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1, 1),
    _ApWEPCipherKeyIndex_Type()
)
apWEPCipherKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPCipherKeyIndex.setStatus("current")
_ApWEPCipherKeyValue_Type = DisplayString
_ApWEPCipherKeyValue_Object = MibTableColumn
apWEPCipherKeyValue = _ApWEPCipherKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1, 2),
    _ApWEPCipherKeyValue_Type()
)
apWEPCipherKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPCipherKeyValue.setStatus("current")


class _ApWEPCipherKeyCharType_Type(Integer32):
    """Custom type apWEPCipherKeyCharType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hex", 0),
          ("char", 1))
    )


_ApWEPCipherKeyCharType_Type.__name__ = "Integer32"
_ApWEPCipherKeyCharType_Object = MibTableColumn
apWEPCipherKeyCharType = _ApWEPCipherKeyCharType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1, 3),
    _ApWEPCipherKeyCharType_Type()
)
apWEPCipherKeyCharType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPCipherKeyCharType.setStatus("current")
_ApPSKCipherKeyValue_Type = DisplayString
_ApPSKCipherKeyValue_Object = MibTableColumn
apPSKCipherKeyValue = _ApPSKCipherKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1, 4),
    _ApPSKCipherKeyValue_Type()
)
apPSKCipherKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPSKCipherKeyValue.setStatus("current")


class _ApPSKCipherKeyCharType_Type(Integer32):
    """Custom type apPSKCipherKeyCharType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hex", 0),
          ("char", 1))
    )


_ApPSKCipherKeyCharType_Type.__name__ = "Integer32"
_ApPSKCipherKeyCharType_Object = MibTableColumn
apPSKCipherKeyCharType = _ApPSKCipherKeyCharType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1, 5),
    _ApPSKCipherKeyCharType_Type()
)
apPSKCipherKeyCharType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPSKCipherKeyCharType.setStatus("current")
_ApWAPIAuthModeEnable_Type = TruthValue
_ApWAPIAuthModeEnable_Object = MibTableColumn
apWAPIAuthModeEnable = _ApWAPIAuthModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1, 6),
    _ApWAPIAuthModeEnable_Type()
)
apWAPIAuthModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIAuthModeEnable.setStatus("current")
_ApWAPIASIPAddress_Type = IpAddress
_ApWAPIASIPAddress_Object = MibTableColumn
apWAPIASIPAddress = _ApWAPIASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1, 7),
    _ApWAPIASIPAddress_Type()
)
apWAPIASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIASIPAddress.setStatus("current")
_ApWAPIIsInstalledCer_Type = TruthValue
_ApWAPIIsInstalledCer_Object = MibTableColumn
apWAPIIsInstalledCer = _ApWAPIIsInstalledCer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 1, 1, 8),
    _ApWAPIIsInstalledCer_Type()
)
apWAPIIsInstalledCer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIIsInstalledCer.setStatus("current")
_ApWlanSecurityTable_Object = MibTable
apWlanSecurityTable = _ApWlanSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 2)
)
if mibBuilder.loadTexts:
    apWlanSecurityTable.setStatus("current")
_ApWlanSecurityTableEntry_Object = MibTableRow
apWlanSecurityTableEntry = _ApWlanSecurityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 2, 1)
)
apWlanSecurityTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanSecurityAPMac"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanSecurityRadioId"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanSecurityWlanId"),
)
if mibBuilder.loadTexts:
    apWlanSecurityTableEntry.setStatus("current")
_ApWlanSecurityAPMac_Type = MacAddress
_ApWlanSecurityAPMac_Object = MibTableColumn
apWlanSecurityAPMac = _ApWlanSecurityAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 2, 1, 1),
    _ApWlanSecurityAPMac_Type()
)
apWlanSecurityAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanSecurityAPMac.setStatus("current")
_ApWlanSecurityRadioId_Type = Integer32
_ApWlanSecurityRadioId_Object = MibTableColumn
apWlanSecurityRadioId = _ApWlanSecurityRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 2, 1, 2),
    _ApWlanSecurityRadioId_Type()
)
apWlanSecurityRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanSecurityRadioId.setStatus("current")
_ApWlanSecurityWlanId_Type = Integer32
_ApWlanSecurityWlanId_Object = MibTableColumn
apWlanSecurityWlanId = _ApWlanSecurityWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 2, 1, 3),
    _ApWlanSecurityWlanId_Type()
)
apWlanSecurityWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanSecurityWlanId.setStatus("current")
_ApWlanSecurityAuthenMode_Type = Integer32
_ApWlanSecurityAuthenMode_Object = MibTableColumn
apWlanSecurityAuthenMode = _ApWlanSecurityAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 4, 2, 1, 4),
    _ApWlanSecurityAuthenMode_Type()
)
apWlanSecurityAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanSecurityAuthenMode.setStatus("current")
_ApWAPIExternInfoConfigObjects_ObjectIdentity = ObjectIdentity
apWAPIExternInfoConfigObjects = _ApWAPIExternInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5)
)
_ApWAPIExternInfoConfigTable_Object = MibTable
apWAPIExternInfoConfigTable = _ApWAPIExternInfoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1)
)
if mibBuilder.loadTexts:
    apWAPIExternInfoConfigTable.setStatus("current")
_ApWAPIExternInfoConfigTableEntry_Object = MibTableRow
apWAPIExternInfoConfigTableEntry = _ApWAPIExternInfoConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1)
)
apWAPIExternInfoConfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apWAPIExternInfoConfigTableEntry.setStatus("current")
_ApWAPIConfigVersion_Type = Integer32
_ApWAPIConfigVersion_Object = MibTableColumn
apWAPIConfigVersion = _ApWAPIConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 1),
    _ApWAPIConfigVersion_Type()
)
apWAPIConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIConfigVersion.setStatus("current")
_ApWAPIControlledAuthControl_Type = TruthValue
_ApWAPIControlledAuthControl_Object = MibTableColumn
apWAPIControlledAuthControl = _ApWAPIControlledAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 2),
    _ApWAPIControlledAuthControl_Type()
)
apWAPIControlledAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIControlledAuthControl.setStatus("current")
_ApWAPIControlledPortControl_Type = Integer32
_ApWAPIControlledPortControl_Object = MibTableColumn
apWAPIControlledPortControl = _ApWAPIControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 3),
    _ApWAPIControlledPortControl_Type()
)
apWAPIControlledPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIControlledPortControl.setStatus("current")
_ApWAPIOptionImplemented_Type = TruthValue
_ApWAPIOptionImplemented_Object = MibTableColumn
apWAPIOptionImplemented = _ApWAPIOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 4),
    _ApWAPIOptionImplemented_Type()
)
apWAPIOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIOptionImplemented.setStatus("current")
_ApWAPIPreauthenticationImplemented_Type = TruthValue
_ApWAPIPreauthenticationImplemented_Object = MibTableColumn
apWAPIPreauthenticationImplemented = _ApWAPIPreauthenticationImplemented_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 5),
    _ApWAPIPreauthenticationImplemented_Type()
)
apWAPIPreauthenticationImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIPreauthenticationImplemented.setStatus("current")
_ApWAPIEnabled_Type = TruthValue
_ApWAPIEnabled_Object = MibTableColumn
apWAPIEnabled = _ApWAPIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 6),
    _ApWAPIEnabled_Type()
)
apWAPIEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIEnabled.setStatus("current")
_ApWAPIPreauthEnabled_Type = TruthValue
_ApWAPIPreauthEnabled_Object = MibTableColumn
apWAPIPreauthEnabled = _ApWAPIPreauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 7),
    _ApWAPIPreauthEnabled_Type()
)
apWAPIPreauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIPreauthEnabled.setStatus("current")
_ApWAPIUnicastKeysSupported_Type = Unsigned32
_ApWAPIUnicastKeysSupported_Object = MibTableColumn
apWAPIUnicastKeysSupported = _ApWAPIUnicastKeysSupported_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 8),
    _ApWAPIUnicastKeysSupported_Type()
)
apWAPIUnicastKeysSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIUnicastKeysSupported.setStatus("current")


class _ApWAPIUnicastRekeyMethod_Type(Integer32):
    """Custom type apWAPIUnicastRekeyMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("timeBased", 1),
          ("packetBased", 2),
          ("timepacket-Based", 3))
    )


_ApWAPIUnicastRekeyMethod_Type.__name__ = "Integer32"
_ApWAPIUnicastRekeyMethod_Object = MibTableColumn
apWAPIUnicastRekeyMethod = _ApWAPIUnicastRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 9),
    _ApWAPIUnicastRekeyMethod_Type()
)
apWAPIUnicastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIUnicastRekeyMethod.setStatus("current")


class _ApWAPIUnicastRekeyTime_Type(Unsigned32):
    """Custom type apWAPIUnicastRekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPIUnicastRekeyTime_Type.__name__ = "Unsigned32"
_ApWAPIUnicastRekeyTime_Object = MibTableColumn
apWAPIUnicastRekeyTime = _ApWAPIUnicastRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 10),
    _ApWAPIUnicastRekeyTime_Type()
)
apWAPIUnicastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIUnicastRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    apWAPIUnicastRekeyTime.setUnits("second")


class _ApWAPIUnicastRekeyPackets_Type(Unsigned32):
    """Custom type apWAPIUnicastRekeyPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPIUnicastRekeyPackets_Type.__name__ = "Unsigned32"
_ApWAPIUnicastRekeyPackets_Object = MibTableColumn
apWAPIUnicastRekeyPackets = _ApWAPIUnicastRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 11),
    _ApWAPIUnicastRekeyPackets_Type()
)
apWAPIUnicastRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIUnicastRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    apWAPIUnicastRekeyPackets.setUnits("1000 packets")


class _ApWAPIMulticastCipher_Type(OctetString):
    """Custom type apWAPIMulticastCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ApWAPIMulticastCipher_Type.__name__ = "OctetString"
_ApWAPIMulticastCipher_Object = MibTableColumn
apWAPIMulticastCipher = _ApWAPIMulticastCipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 12),
    _ApWAPIMulticastCipher_Type()
)
apWAPIMulticastCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIMulticastCipher.setStatus("current")


class _ApWAPIMulticastRekeyMethod_Type(Integer32):
    """Custom type apWAPIMulticastRekeyMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("timeBased", 1),
          ("packetBased", 2),
          ("timepacket-Based", 3))
    )


_ApWAPIMulticastRekeyMethod_Type.__name__ = "Integer32"
_ApWAPIMulticastRekeyMethod_Object = MibTableColumn
apWAPIMulticastRekeyMethod = _ApWAPIMulticastRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 13),
    _ApWAPIMulticastRekeyMethod_Type()
)
apWAPIMulticastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIMulticastRekeyMethod.setStatus("current")


class _ApWAPIMulticastRekeyTime_Type(Unsigned32):
    """Custom type apWAPIMulticastRekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPIMulticastRekeyTime_Type.__name__ = "Unsigned32"
_ApWAPIMulticastRekeyTime_Object = MibTableColumn
apWAPIMulticastRekeyTime = _ApWAPIMulticastRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 14),
    _ApWAPIMulticastRekeyTime_Type()
)
apWAPIMulticastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIMulticastRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    apWAPIMulticastRekeyTime.setUnits("second")


class _ApWAPIMulticastRekeyPackets_Type(Unsigned32):
    """Custom type apWAPIMulticastRekeyPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPIMulticastRekeyPackets_Type.__name__ = "Unsigned32"
_ApWAPIMulticastRekeyPackets_Object = MibTableColumn
apWAPIMulticastRekeyPackets = _ApWAPIMulticastRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 15),
    _ApWAPIMulticastRekeyPackets_Type()
)
apWAPIMulticastRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIMulticastRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    apWAPIMulticastRekeyPackets.setUnits("1000 packets")
_ApWAPIMulticastRekeyStrict_Type = TruthValue
_ApWAPIMulticastRekeyStrict_Object = MibTableColumn
apWAPIMulticastRekeyStrict = _ApWAPIMulticastRekeyStrict_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 16),
    _ApWAPIMulticastRekeyStrict_Type()
)
apWAPIMulticastRekeyStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIMulticastRekeyStrict.setStatus("current")


class _ApWAPIPSKValue_Type(OctetString):
    """Custom type apWAPIPSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_ApWAPIPSKValue_Type.__name__ = "OctetString"
_ApWAPIPSKValue_Object = MibTableColumn
apWAPIPSKValue = _ApWAPIPSKValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 17),
    _ApWAPIPSKValue_Type()
)
apWAPIPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIPSKValue.setStatus("current")
_ApWAPIPSKPassPhrase_Type = DisplayString
_ApWAPIPSKPassPhrase_Object = MibTableColumn
apWAPIPSKPassPhrase = _ApWAPIPSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 18),
    _ApWAPIPSKPassPhrase_Type()
)
apWAPIPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIPSKPassPhrase.setStatus("current")


class _ApWAPICertificateUpdateCount_Type(Unsigned32):
    """Custom type apWAPICertificateUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPICertificateUpdateCount_Type.__name__ = "Unsigned32"
_ApWAPICertificateUpdateCount_Object = MibTableColumn
apWAPICertificateUpdateCount = _ApWAPICertificateUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 19),
    _ApWAPICertificateUpdateCount_Type()
)
apWAPICertificateUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPICertificateUpdateCount.setStatus("current")


class _ApWAPIMulticastUpdateCount_Type(Unsigned32):
    """Custom type apWAPIMulticastUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPIMulticastUpdateCount_Type.__name__ = "Unsigned32"
_ApWAPIMulticastUpdateCount_Object = MibTableColumn
apWAPIMulticastUpdateCount = _ApWAPIMulticastUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 20),
    _ApWAPIMulticastUpdateCount_Type()
)
apWAPIMulticastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIMulticastUpdateCount.setStatus("current")


class _ApWAPIUnicastUpdateCount_Type(Unsigned32):
    """Custom type apWAPIUnicastUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPIUnicastUpdateCount_Type.__name__ = "Unsigned32"
_ApWAPIUnicastUpdateCount_Object = MibTableColumn
apWAPIUnicastUpdateCount = _ApWAPIUnicastUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 21),
    _ApWAPIUnicastUpdateCount_Type()
)
apWAPIUnicastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIUnicastUpdateCount.setStatus("current")


class _ApWAPIMulticastCipherSize_Type(Unsigned32):
    """Custom type apWAPIMulticastCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ApWAPIMulticastCipherSize_Type.__name__ = "Unsigned32"
_ApWAPIMulticastCipherSize_Object = MibTableColumn
apWAPIMulticastCipherSize = _ApWAPIMulticastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 22),
    _ApWAPIMulticastCipherSize_Type()
)
apWAPIMulticastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIMulticastCipherSize.setStatus("current")


class _ApWAPIBKLifetime_Type(Unsigned32):
    """Custom type apWAPIBKLifetime based on Unsigned32"""
    defaultValue = 43200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPIBKLifetime_Type.__name__ = "Unsigned32"
_ApWAPIBKLifetime_Object = MibTableColumn
apWAPIBKLifetime = _ApWAPIBKLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 23),
    _ApWAPIBKLifetime_Type()
)
apWAPIBKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIBKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    apWAPIBKLifetime.setUnits("second")


class _ApWAPIBKReauthThreshold_Type(Unsigned32):
    """Custom type apWAPIBKReauthThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApWAPIBKReauthThreshold_Type.__name__ = "Unsigned32"
_ApWAPIBKReauthThreshold_Object = MibTableColumn
apWAPIBKReauthThreshold = _ApWAPIBKReauthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 24),
    _ApWAPIBKReauthThreshold_Type()
)
apWAPIBKReauthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIBKReauthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    apWAPIBKReauthThreshold.setUnits("percentage")


class _ApWAPISATimeout_Type(Unsigned32):
    """Custom type apWAPISATimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApWAPISATimeout_Type.__name__ = "Unsigned32"
_ApWAPISATimeout_Object = MibTableColumn
apWAPISATimeout = _ApWAPISATimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 25),
    _ApWAPISATimeout_Type()
)
apWAPISATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPISATimeout.setStatus("current")
if mibBuilder.loadTexts:
    apWAPISATimeout.setUnits("second")


class _ApWAPIAuthSuiteSelected_Type(OctetString):
    """Custom type apWAPIAuthSuiteSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ApWAPIAuthSuiteSelected_Type.__name__ = "OctetString"
_ApWAPIAuthSuiteSelected_Object = MibTableColumn
apWAPIAuthSuiteSelected = _ApWAPIAuthSuiteSelected_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 26),
    _ApWAPIAuthSuiteSelected_Type()
)
apWAPIAuthSuiteSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIAuthSuiteSelected.setStatus("current")


class _ApWAPIUnicastCipherSelected_Type(OctetString):
    """Custom type apWAPIUnicastCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ApWAPIUnicastCipherSelected_Type.__name__ = "OctetString"
_ApWAPIUnicastCipherSelected_Object = MibTableColumn
apWAPIUnicastCipherSelected = _ApWAPIUnicastCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 27),
    _ApWAPIUnicastCipherSelected_Type()
)
apWAPIUnicastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIUnicastCipherSelected.setStatus("current")


class _ApWAPIMulticastCipherSelected_Type(OctetString):
    """Custom type apWAPIMulticastCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ApWAPIMulticastCipherSelected_Type.__name__ = "OctetString"
_ApWAPIMulticastCipherSelected_Object = MibTableColumn
apWAPIMulticastCipherSelected = _ApWAPIMulticastCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 28),
    _ApWAPIMulticastCipherSelected_Type()
)
apWAPIMulticastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIMulticastCipherSelected.setStatus("current")


class _ApWAPIBKIDUsed_Type(OctetString):
    """Custom type apWAPIBKIDUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ApWAPIBKIDUsed_Type.__name__ = "OctetString"
_ApWAPIBKIDUsed_Object = MibTableColumn
apWAPIBKIDUsed = _ApWAPIBKIDUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 29),
    _ApWAPIBKIDUsed_Type()
)
apWAPIBKIDUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIBKIDUsed.setStatus("current")


class _ApWAPIAuthSuiteRequested_Type(OctetString):
    """Custom type apWAPIAuthSuiteRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ApWAPIAuthSuiteRequested_Type.__name__ = "OctetString"
_ApWAPIAuthSuiteRequested_Object = MibTableColumn
apWAPIAuthSuiteRequested = _ApWAPIAuthSuiteRequested_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 30),
    _ApWAPIAuthSuiteRequested_Type()
)
apWAPIAuthSuiteRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIAuthSuiteRequested.setStatus("current")


class _ApWAPIUnicastCipherRequested_Type(OctetString):
    """Custom type apWAPIUnicastCipherRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ApWAPIUnicastCipherRequested_Type.__name__ = "OctetString"
_ApWAPIUnicastCipherRequested_Object = MibTableColumn
apWAPIUnicastCipherRequested = _ApWAPIUnicastCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 31),
    _ApWAPIUnicastCipherRequested_Type()
)
apWAPIUnicastCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIUnicastCipherRequested.setStatus("current")


class _ApWAPIMulticastCipherRequested_Type(OctetString):
    """Custom type apWAPIMulticastCipherRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ApWAPIMulticastCipherRequested_Type.__name__ = "OctetString"
_ApWAPIMulticastCipherRequested_Object = MibTableColumn
apWAPIMulticastCipherRequested = _ApWAPIMulticastCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 32),
    _ApWAPIMulticastCipherRequested_Type()
)
apWAPIMulticastCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIMulticastCipherRequested.setStatus("current")
_ApWAPIUnicastCipher_Type = OctetString
_ApWAPIUnicastCipher_Object = MibTableColumn
apWAPIUnicastCipher = _ApWAPIUnicastCipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 33),
    _ApWAPIUnicastCipher_Type()
)
apWAPIUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIUnicastCipher.setStatus("current")
_ApWAPIUnicastCipherEnabled_Type = TruthValue
_ApWAPIUnicastCipherEnabled_Object = MibTableColumn
apWAPIUnicastCipherEnabled = _ApWAPIUnicastCipherEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 34),
    _ApWAPIUnicastCipherEnabled_Type()
)
apWAPIUnicastCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIUnicastCipherEnabled.setStatus("current")
_ApWAPIUnicastCipherSize_Type = Unsigned32
_ApWAPIUnicastCipherSize_Object = MibTableColumn
apWAPIUnicastCipherSize = _ApWAPIUnicastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 35),
    _ApWAPIUnicastCipherSize_Type()
)
apWAPIUnicastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIUnicastCipherSize.setStatus("current")
_ApWAPIAuthenticationSuite_Type = OctetString
_ApWAPIAuthenticationSuite_Object = MibTableColumn
apWAPIAuthenticationSuite = _ApWAPIAuthenticationSuite_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 36),
    _ApWAPIAuthenticationSuite_Type()
)
apWAPIAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIAuthenticationSuite.setStatus("current")
_ApWAPIAuthenticationSuiteEnabled_Type = TruthValue
_ApWAPIAuthenticationSuiteEnabled_Object = MibTableColumn
apWAPIAuthenticationSuiteEnabled = _ApWAPIAuthenticationSuiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 37),
    _ApWAPIAuthenticationSuiteEnabled_Type()
)
apWAPIAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIAuthenticationSuiteEnabled.setStatus("current")
_ApWAPIAECertFile_Type = DisplayString
_ApWAPIAECertFile_Object = MibTableColumn
apWAPIAECertFile = _ApWAPIAECertFile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 38),
    _ApWAPIAECertFile_Type()
)
apWAPIAECertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIAECertFile.setStatus("current")
_ApWAPICACertFile_Type = DisplayString
_ApWAPICACertFile_Object = MibTableColumn
apWAPICACertFile = _ApWAPICACertFile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 39),
    _ApWAPICACertFile_Type()
)
apWAPICACertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPICACertFile.setStatus("current")
_ApWAPIASUCertFile_Type = DisplayString
_ApWAPIASUCertFile_Object = MibTableColumn
apWAPIASUCertFile = _ApWAPIASUCertFile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 5, 1, 1, 40),
    _ApWAPIASUCertFile_Type()
)
apWAPIASUCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWAPIASUCertFile.setStatus("current")
_ApStationInfoGetObjects_ObjectIdentity = ObjectIdentity
apStationInfoGetObjects = _ApStationInfoGetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6)
)
_ApStationInfoGetTable_Object = MibTable
apStationInfoGetTable = _ApStationInfoGetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1)
)
if mibBuilder.loadTexts:
    apStationInfoGetTable.setStatus("current")
_ApStationInfoGetTableEntry_Object = MibTableRow
apStationInfoGetTableEntry = _ApStationInfoGetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1)
)
apStationInfoGetTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieStaMacAddr"),
)
if mibBuilder.loadTexts:
    apStationInfoGetTableEntry.setStatus("current")
_ApStaMAC_Type = MacAddress
_ApStaMAC_Object = MibTableColumn
apStaMAC = _ApStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 1),
    _ApStaMAC_Type()
)
apStaMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaMAC.setStatus("current")


class _ApStaWMMAttr_Type(Integer32):
    """Custom type apStaWMMAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonwmmsta", 0),
          ("wmmsta", 1))
    )


_ApStaWMMAttr_Type.__name__ = "Integer32"
_ApStaWMMAttr_Object = MibTableColumn
apStaWMMAttr = _ApStaWMMAttr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 2),
    _ApStaWMMAttr_Type()
)
apStaWMMAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaWMMAttr.setStatus("current")
_ApStaIPAddress_Type = IpAddress
_ApStaIPAddress_Object = MibTableColumn
apStaIPAddress = _ApStaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 3),
    _ApStaIPAddress_Type()
)
apStaIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaIPAddress.setStatus("current")


class _ApStaRadioMode_Type(Integer32):
    """Custom type apStaRadioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 0),
          ("dot11b", 1),
          ("dot11g", 2),
          ("dot11n", 3),
          ("dot11ac", 4),
          ("dot11ax", 5))
    )


_ApStaRadioMode_Type.__name__ = "Integer32"
_ApStaRadioMode_Object = MibTableColumn
apStaRadioMode = _ApStaRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 4),
    _ApStaRadioMode_Type()
)
apStaRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRadioMode.setStatus("current")
_ApStaRadioChannel_Type = Integer32
_ApStaRadioChannel_Object = MibTableColumn
apStaRadioChannel = _ApStaRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 5),
    _ApStaRadioChannel_Type()
)
apStaRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRadioChannel.setStatus("current")
_ApAPTxRates_Type = Integer32
_ApAPTxRates_Object = MibTableColumn
apAPTxRates = _ApAPTxRates_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 6),
    _ApAPTxRates_Type()
)
apAPTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPTxRates.setStatus("current")


class _ApStaPowerSaveMode_Type(Integer32):
    """Custom type apStaPowerSaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("powersave", 1))
    )


_ApStaPowerSaveMode_Type.__name__ = "Integer32"
_ApStaPowerSaveMode_Object = MibTableColumn
apStaPowerSaveMode = _ApStaPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 7),
    _ApStaPowerSaveMode_Type()
)
apStaPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaPowerSaveMode.setStatus("current")
_ApStaVlanId_Type = Counter32
_ApStaVlanId_Object = MibTableColumn
apStaVlanId = _ApStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 8),
    _ApStaVlanId_Type()
)
apStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaVlanId.setStatus("current")
_ApStaSSIDName_Type = DisplayString
_ApStaSSIDName_Object = MibTableColumn
apStaSSIDName = _ApStaSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 9),
    _ApStaSSIDName_Type()
)
apStaSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaSSIDName.setStatus("current")
_ApAPId_Type = Integer32
_ApAPId_Object = MibTableColumn
apAPId = _ApAPId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 10),
    _ApAPId_Type()
)
apAPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPId.setStatus("current")


class _ApStaDot11Auth_Type(Integer32):
    """Custom type apStaDot11Auth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1))
    )


_ApStaDot11Auth_Type.__name__ = "Integer32"
_ApStaDot11Auth_Object = MibTableColumn
apStaDot11Auth = _ApStaDot11Auth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 11),
    _ApStaDot11Auth_Type()
)
apStaDot11Auth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDot11Auth.setStatus("current")


class _Apsecurity_Type(Integer32):
    """Custom type apsecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wpa", 1),
          ("wpa2", 2),
          ("wapi", 3))
    )


_Apsecurity_Type.__name__ = "Integer32"
_Apsecurity_Object = MibTableColumn
apsecurity = _Apsecurity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 12),
    _Apsecurity_Type()
)
apsecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsecurity.setStatus("current")


class _ApStaAuthenMode_Type(Integer32):
    """Custom type apStaAuthenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("psk", 1),
          ("radius", 2),
          ("wapicer", 3),
          ("web", 4),
          ("psk-web", 5),
          ("wapicer-web", 6),
          ("wapipsk", 7))
    )


_ApStaAuthenMode_Type.__name__ = "Integer32"
_ApStaAuthenMode_Object = MibTableColumn
apStaAuthenMode = _ApStaAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 13),
    _ApStaAuthenMode_Type()
)
apStaAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaAuthenMode.setStatus("current")


class _ApStaSecurityCiphers_Type(Integer32):
    """Custom type apStaSecurityCiphers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wep40", 1),
          ("wep104", 2),
          ("tkip", 3),
          ("aesccmp", 4),
          ("wpisms4", 5))
    )


_ApStaSecurityCiphers_Type.__name__ = "Integer32"
_ApStaSecurityCiphers_Object = MibTableColumn
apStaSecurityCiphers = _ApStaSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 14),
    _ApStaSecurityCiphers_Type()
)
apStaSecurityCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaSecurityCiphers.setStatus("current")
_ApAPIdMac_Type = MacAddress
_ApAPIdMac_Object = MibTableColumn
apAPIdMac = _ApAPIdMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 15),
    _ApAPIdMac_Type()
)
apAPIdMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPIdMac.setStatus("current")


class _ApStaMode_Type(Integer32):
    """Custom type apStaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11an", 8),
          ("dot11gn", 16),
          ("dot11ac", 32),
          ("dot11ax", 64))
    )


_ApStaMode_Type.__name__ = "Integer32"
_ApStaMode_Object = MibTableColumn
apStaMode = _ApStaMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 16),
    _ApStaMode_Type()
)
apStaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaMode.setStatus("current")
_ApStaBand_Type = Integer32
_ApStaBand_Object = MibTableColumn
apStaBand = _ApStaBand_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 1, 1, 17),
    _ApStaBand_Type()
)
apStaBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaBand.setStatus("current")
_ApStationRefusedAccessTable_Object = MibTable
apStationRefusedAccessTable = _ApStationRefusedAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 2)
)
if mibBuilder.loadTexts:
    apStationRefusedAccessTable.setStatus("current")
_ApStationRefusedAccessTableEntry_Object = MibTableRow
apStationRefusedAccessTableEntry = _ApStationRefusedAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 2, 1)
)
apStationRefusedAccessTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apRefusedStaMAC"),
)
if mibBuilder.loadTexts:
    apStationRefusedAccessTableEntry.setStatus("current")
_ApRefusedStaMAC_Type = MacAddress
_ApRefusedStaMAC_Object = MibTableColumn
apRefusedStaMAC = _ApRefusedStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 2, 1, 1),
    _ApRefusedStaMAC_Type()
)
apRefusedStaMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRefusedStaMAC.setStatus("current")
_ApFailReason_Type = Integer32
_ApFailReason_Object = MibTableColumn
apFailReason = _ApFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 2, 1, 2),
    _ApFailReason_Type()
)
apFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFailReason.setStatus("current")
_ApRefusedTime_Type = DisplayString
_ApRefusedTime_Object = MibTableColumn
apRefusedTime = _ApRefusedTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 2, 1, 3),
    _ApRefusedTime_Type()
)
apRefusedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRefusedTime.setStatus("current")
_ApRefusedAPMac_Type = MacAddress
_ApRefusedAPMac_Object = MibTableColumn
apRefusedAPMac = _ApRefusedAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 2, 1, 4),
    _ApRefusedAPMac_Type()
)
apRefusedAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRefusedAPMac.setStatus("current")
_ApStationRadiusInfoTable_Object = MibTable
apStationRadiusInfoTable = _ApStationRadiusInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 3)
)
if mibBuilder.loadTexts:
    apStationRadiusInfoTable.setStatus("current")
_ApStationRadiusInfoTableEntry_Object = MibTableRow
apStationRadiusInfoTableEntry = _ApStationRadiusInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 3, 1)
)
apStationRadiusInfoTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apUserMacAddress"),
)
if mibBuilder.loadTexts:
    apStationRadiusInfoTableEntry.setStatus("current")
_ApUserMacAddress_Type = MacAddress
_ApUserMacAddress_Object = MibTableColumn
apUserMacAddress = _ApUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 3, 1, 1),
    _ApUserMacAddress_Type()
)
apUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUserMacAddress.setStatus("current")
_ApUserIpAddress_Type = IpAddress
_ApUserIpAddress_Object = MibTableColumn
apUserIpAddress = _ApUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 3, 1, 2),
    _ApUserIpAddress_Type()
)
apUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUserIpAddress.setStatus("current")
_ApUserLoginName_Type = OctetString
_ApUserLoginName_Object = MibTableColumn
apUserLoginName = _ApUserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 3, 1, 3),
    _ApUserLoginName_Type()
)
apUserLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUserLoginName.setStatus("current")
_ApUserLoginTime_Type = OctetString
_ApUserLoginTime_Object = MibTableColumn
apUserLoginTime = _ApUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 3, 1, 4),
    _ApUserLoginTime_Type()
)
apUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUserLoginTime.setStatus("current")
_ApUserOnlineTime_Type = TimeTicks
_ApUserOnlineTime_Object = MibTableColumn
apUserOnlineTime = _ApUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 3, 1, 5),
    _ApUserOnlineTime_Type()
)
apUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUserOnlineTime.setStatus("current")
_ApStationInfoJsonTable_Object = MibTable
apStationInfoJsonTable = _ApStationInfoJsonTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 4)
)
if mibBuilder.loadTexts:
    apStationInfoJsonTable.setStatus("current")
_ApStationInfoJsonEntry_Object = MibTableRow
apStationInfoJsonEntry = _ApStationInfoJsonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 4, 1)
)
apStationInfoJsonEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apStationInfoJsonMacAddr"),
)
if mibBuilder.loadTexts:
    apStationInfoJsonEntry.setStatus("current")
_ApStationInfoJsonMacAddr_Type = MacAddress
_ApStationInfoJsonMacAddr_Object = MibTableColumn
apStationInfoJsonMacAddr = _ApStationInfoJsonMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 4, 1, 1),
    _ApStationInfoJsonMacAddr_Type()
)
apStationInfoJsonMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInfoJsonMacAddr.setStatus("current")


class _ApStationInfoJsonContent_Type(OctetString):
    """Custom type apStationInfoJsonContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_ApStationInfoJsonContent_Type.__name__ = "OctetString"
_ApStationInfoJsonContent_Object = MibTableColumn
apStationInfoJsonContent = _ApStationInfoJsonContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 6, 4, 1, 2),
    _ApStationInfoJsonContent_Type()
)
apStationInfoJsonContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInfoJsonContent.setStatus("current")
_ApQOSInfoConfigObjects_ObjectIdentity = ObjectIdentity
apQOSInfoConfigObjects = _ApQOSInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7)
)
_ApQOSWirelessConfigObjects_ObjectIdentity = ObjectIdentity
apQOSWirelessConfigObjects = _ApQOSWirelessConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 1)
)
_ApQOSWirelessConfigTable_Object = MibTable
apQOSWirelessConfigTable = _ApQOSWirelessConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 1, 1)
)
if mibBuilder.loadTexts:
    apQOSWirelessConfigTable.setStatus("current")
_ApQOSWirelessConfigTableEntry_Object = MibTableRow
apQOSWirelessConfigTableEntry = _ApQOSWirelessConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 1, 1, 1)
)
apQOSWirelessConfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apWireQoSTrafficClassId"),
)
if mibBuilder.loadTexts:
    apQOSWirelessConfigTableEntry.setStatus("current")


class _ApWireQoSTrafficClassId_Type(Integer32):
    """Custom type apWireQoSTrafficClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 0),
          ("background", 1),
          ("video", 2),
          ("voice", 3))
    )


_ApWireQoSTrafficClassId_Type.__name__ = "Integer32"
_ApWireQoSTrafficClassId_Object = MibTableColumn
apWireQoSTrafficClassId = _ApWireQoSTrafficClassId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 1, 1, 1, 1),
    _ApWireQoSTrafficClassId_Type()
)
apWireQoSTrafficClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWireQoSTrafficClassId.setStatus("current")
_ApWireQosAIFS_Type = Integer32
_ApWireQosAIFS_Object = MibTableColumn
apWireQosAIFS = _ApWireQosAIFS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 1, 1, 1, 2),
    _ApWireQosAIFS_Type()
)
apWireQosAIFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWireQosAIFS.setStatus("current")
_ApWireQoSCWmin_Type = Integer32
_ApWireQoSCWmin_Object = MibTableColumn
apWireQoSCWmin = _ApWireQoSCWmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 1, 1, 1, 3),
    _ApWireQoSCWmin_Type()
)
apWireQoSCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWireQoSCWmin.setStatus("current")
_ApWireQoSCWmax_Type = Integer32
_ApWireQoSCWmax_Object = MibTableColumn
apWireQoSCWmax = _ApWireQoSCWmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 1, 1, 1, 4),
    _ApWireQoSCWmax_Type()
)
apWireQoSCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWireQoSCWmax.setStatus("current")
_ApWireQoSTXOPLim_Type = Integer32
_ApWireQoSTXOPLim_Object = MibTableColumn
apWireQoSTXOPLim = _ApWireQoSTXOPLim_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 1, 1, 1, 5),
    _ApWireQoSTXOPLim_Type()
)
apWireQoSTXOPLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWireQoSTXOPLim.setStatus("current")
_ApQOSBaseInfoConfigObjects_ObjectIdentity = ObjectIdentity
apQOSBaseInfoConfigObjects = _ApQOSBaseInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2)
)
_ApQOSBaseInfoConfigTable_Object = MibTable
apQOSBaseInfoConfigTable = _ApQOSBaseInfoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1)
)
if mibBuilder.loadTexts:
    apQOSBaseInfoConfigTable.setStatus("current")
_ApQOSBaseInfoConfigTableEntry_Object = MibTableRow
apQOSBaseInfoConfigTableEntry = _ApQOSBaseInfoConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1)
)
apQOSBaseInfoConfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSBaseInfoConfigTableEntry.setStatus("current")


class _ApBaseQoSTrafficClass_Type(Integer32):
    """Custom type apBaseQoSTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("background", 0),
          ("bestEffort", 1),
          ("video", 2),
          ("voice", 3))
    )


_ApBaseQoSTrafficClass_Type.__name__ = "Integer32"
_ApBaseQoSTrafficClass_Object = MibTableColumn
apBaseQoSTrafficClass = _ApBaseQoSTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 1),
    _ApBaseQoSTrafficClass_Type()
)
apBaseQoSTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSTrafficClass.setStatus("current")
_ApBaseQoSEnabled_Type = TruthValue
_ApBaseQoSEnabled_Object = MibTableColumn
apBaseQoSEnabled = _ApBaseQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 2),
    _ApBaseQoSEnabled_Type()
)
apBaseQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSEnabled.setStatus("current")
_ApBaseQoSBW_Type = Integer32
_ApBaseQoSBW_Object = MibTableColumn
apBaseQoSBW = _ApBaseQoSBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 3),
    _ApBaseQoSBW_Type()
)
apBaseQoSBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBW.setStatus("current")
_ApBaseQoSResPercent_Type = Integer32
_ApBaseQoSResPercent_Object = MibTableColumn
apBaseQoSResPercent = _ApBaseQoSResPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 4),
    _ApBaseQoSResPercent_Type()
)
apBaseQoSResPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSResPercent.setStatus("current")
_ApBaseQoSsharedBW_Type = Integer32
_ApBaseQoSsharedBW_Object = MibTableColumn
apBaseQoSsharedBW = _ApBaseQoSsharedBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 5),
    _ApBaseQoSsharedBW_Type()
)
apBaseQoSsharedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSsharedBW.setStatus("current")
_ApBaseQoSsharedBWPercent_Type = Integer32
_ApBaseQoSsharedBWPercent_Object = MibTableColumn
apBaseQoSsharedBWPercent = _ApBaseQoSsharedBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 6),
    _ApBaseQoSsharedBWPercent_Type()
)
apBaseQoSsharedBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSsharedBWPercent.setStatus("current")
_ApBaseQoSSchedAlgName_Type = DisplayString
_ApBaseQoSSchedAlgName_Object = MibTableColumn
apBaseQoSSchedAlgName = _ApBaseQoSSchedAlgName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 7),
    _ApBaseQoSSchedAlgName_Type()
)
apBaseQoSSchedAlgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSSchedAlgName.setStatus("current")
_ApBaseQoSResPolicyEnabled_Type = TruthValue
_ApBaseQoSResPolicyEnabled_Object = MibTableColumn
apBaseQoSResPolicyEnabled = _ApBaseQoSResPolicyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 8),
    _ApBaseQoSResPolicyEnabled_Type()
)
apBaseQoSResPolicyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSResPolicyEnabled.setStatus("current")
_ApBaseQoSResPolicyName_Type = DisplayString
_ApBaseQoSResPolicyName_Object = MibTableColumn
apBaseQoSResPolicyName = _ApBaseQoSResPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 9),
    _ApBaseQoSResPolicyName_Type()
)
apBaseQoSResPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSResPolicyName.setStatus("current")
_ApBaseQoSBackgroundSvcAvgSpeed_Type = Integer32
_ApBaseQoSBackgroundSvcAvgSpeed_Object = MibTableColumn
apBaseQoSBackgroundSvcAvgSpeed = _ApBaseQoSBackgroundSvcAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 10),
    _ApBaseQoSBackgroundSvcAvgSpeed_Type()
)
apBaseQoSBackgroundSvcAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBackgroundSvcAvgSpeed.setStatus("current")
_ApBaseQoSBackgroundSvcMaxBurst_Type = Integer32
_ApBaseQoSBackgroundSvcMaxBurst_Object = MibTableColumn
apBaseQoSBackgroundSvcMaxBurst = _ApBaseQoSBackgroundSvcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 11),
    _ApBaseQoSBackgroundSvcMaxBurst_Type()
)
apBaseQoSBackgroundSvcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBackgroundSvcMaxBurst.setStatus("current")
_ApBaseQoSBackgroundSvcPriority_Type = Integer32
_ApBaseQoSBackgroundSvcPriority_Object = MibTableColumn
apBaseQoSBackgroundSvcPriority = _ApBaseQoSBackgroundSvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 12),
    _ApBaseQoSBackgroundSvcPriority_Type()
)
apBaseQoSBackgroundSvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBackgroundSvcPriority.setStatus("current")
_ApBaseQoSBackgroundSvcResPriority_Type = Integer32
_ApBaseQoSBackgroundSvcResPriority_Object = MibTableColumn
apBaseQoSBackgroundSvcResPriority = _ApBaseQoSBackgroundSvcResPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 13),
    _ApBaseQoSBackgroundSvcResPriority_Type()
)
apBaseQoSBackgroundSvcResPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBackgroundSvcResPriority.setStatus("current")
_ApBaseQoSBestEffortSvcAvgSpeed_Type = Integer32
_ApBaseQoSBestEffortSvcAvgSpeed_Object = MibTableColumn
apBaseQoSBestEffortSvcAvgSpeed = _ApBaseQoSBestEffortSvcAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 14),
    _ApBaseQoSBestEffortSvcAvgSpeed_Type()
)
apBaseQoSBestEffortSvcAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBestEffortSvcAvgSpeed.setStatus("current")
_ApBaseQoSBestEffortSvcMaxBurst_Type = Integer32
_ApBaseQoSBestEffortSvcMaxBurst_Object = MibTableColumn
apBaseQoSBestEffortSvcMaxBurst = _ApBaseQoSBestEffortSvcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 15),
    _ApBaseQoSBestEffortSvcMaxBurst_Type()
)
apBaseQoSBestEffortSvcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBestEffortSvcMaxBurst.setStatus("current")
_ApBaseQoSBestEffortSvcPriority_Type = Integer32
_ApBaseQoSBestEffortSvcPriority_Object = MibTableColumn
apBaseQoSBestEffortSvcPriority = _ApBaseQoSBestEffortSvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 16),
    _ApBaseQoSBestEffortSvcPriority_Type()
)
apBaseQoSBestEffortSvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBestEffortSvcPriority.setStatus("current")
_ApBaseQoSBestEffortSvcResPriority_Type = Integer32
_ApBaseQoSBestEffortSvcResPriority_Object = MibTableColumn
apBaseQoSBestEffortSvcResPriority = _ApBaseQoSBestEffortSvcResPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 17),
    _ApBaseQoSBestEffortSvcResPriority_Type()
)
apBaseQoSBestEffortSvcResPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSBestEffortSvcResPriority.setStatus("current")
_ApBaseQoSVoiceSvcAvgSpeed_Type = Integer32
_ApBaseQoSVoiceSvcAvgSpeed_Object = MibTableColumn
apBaseQoSVoiceSvcAvgSpeed = _ApBaseQoSVoiceSvcAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 18),
    _ApBaseQoSVoiceSvcAvgSpeed_Type()
)
apBaseQoSVoiceSvcAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSVoiceSvcAvgSpeed.setStatus("current")
_ApBaseQoSVoiceSvcMaxBurst_Type = Integer32
_ApBaseQoSVoiceSvcMaxBurst_Object = MibTableColumn
apBaseQoSVoiceSvcMaxBurst = _ApBaseQoSVoiceSvcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 19),
    _ApBaseQoSVoiceSvcMaxBurst_Type()
)
apBaseQoSVoiceSvcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSVoiceSvcMaxBurst.setStatus("current")
_ApBaseQoSVoiceSvcPriority_Type = Integer32
_ApBaseQoSVoiceSvcPriority_Object = MibTableColumn
apBaseQoSVoiceSvcPriority = _ApBaseQoSVoiceSvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 20),
    _ApBaseQoSVoiceSvcPriority_Type()
)
apBaseQoSVoiceSvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSVoiceSvcPriority.setStatus("current")
_ApBaseQoSVoiceSvcResPriority_Type = Integer32
_ApBaseQoSVoiceSvcResPriority_Object = MibTableColumn
apBaseQoSVoiceSvcResPriority = _ApBaseQoSVoiceSvcResPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 21),
    _ApBaseQoSVoiceSvcResPriority_Type()
)
apBaseQoSVoiceSvcResPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSVoiceSvcResPriority.setStatus("current")
_ApBaseQoSVideoSvcAvgSpeed_Type = Integer32
_ApBaseQoSVideoSvcAvgSpeed_Object = MibTableColumn
apBaseQoSVideoSvcAvgSpeed = _ApBaseQoSVideoSvcAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 22),
    _ApBaseQoSVideoSvcAvgSpeed_Type()
)
apBaseQoSVideoSvcAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSVideoSvcAvgSpeed.setStatus("current")
_ApBaseQoSVideoSvcMaxBurst_Type = Integer32
_ApBaseQoSVideoSvcMaxBurst_Object = MibTableColumn
apBaseQoSVideoSvcMaxBurst = _ApBaseQoSVideoSvcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 23),
    _ApBaseQoSVideoSvcMaxBurst_Type()
)
apBaseQoSVideoSvcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSVideoSvcMaxBurst.setStatus("current")
_ApBaseQoSVideoSvcPriority_Type = Integer32
_ApBaseQoSVideoSvcPriority_Object = MibTableColumn
apBaseQoSVideoSvcPriority = _ApBaseQoSVideoSvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 24),
    _ApBaseQoSVideoSvcPriority_Type()
)
apBaseQoSVideoSvcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSVideoSvcPriority.setStatus("current")
_ApBaseQoSVideoSvcResPriority_Type = Integer32
_ApBaseQoSVideoSvcResPriority_Object = MibTableColumn
apBaseQoSVideoSvcResPriority = _ApBaseQoSVideoSvcResPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 2, 1, 1, 25),
    _ApBaseQoSVideoSvcResPriority_Type()
)
apBaseQoSVideoSvcResPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBaseQoSVideoSvcResPriority.setStatus("current")
_ApQOSBackgroundCfgObjects_ObjectIdentity = ObjectIdentity
apQOSBackgroundCfgObjects = _ApQOSBackgroundCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 3)
)
_ApQOSBackgroundCfgTable_Object = MibTable
apQOSBackgroundCfgTable = _ApQOSBackgroundCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 3, 1)
)
if mibBuilder.loadTexts:
    apQOSBackgroundCfgTable.setStatus("current")
_ApQOSBackgroundCfgTableEntry_Object = MibTableRow
apQOSBackgroundCfgTableEntry = _ApQOSBackgroundCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 3, 1, 1)
)
apQOSBackgroundCfgTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSBackgroundCfgTableEntry.setStatus("current")
_ApQOSBgMaxSvcCnt_Type = Integer32
_ApQOSBgMaxSvcCnt_Object = MibTableColumn
apQOSBgMaxSvcCnt = _ApQOSBgMaxSvcCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 3, 1, 1, 1),
    _ApQOSBgMaxSvcCnt_Type()
)
apQOSBgMaxSvcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBgMaxSvcCnt.setStatus("current")
_ApQOSBgSvcBW_Type = Integer32
_ApQOSBgSvcBW_Object = MibTableColumn
apQOSBgSvcBW = _ApQOSBgSvcBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 3, 1, 1, 2),
    _ApQOSBgSvcBW_Type()
)
apQOSBgSvcBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBgSvcBW.setStatus("current")
_ApQOSBgSvcBWPercent_Type = Integer32
_ApQOSBgSvcBWPercent_Object = MibTableColumn
apQOSBgSvcBWPercent = _ApQOSBgSvcBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 3, 1, 1, 3),
    _ApQOSBgSvcBWPercent_Type()
)
apQOSBgSvcBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBgSvcBWPercent.setStatus("current")
_ApQOSBgIsUseWREDAlg_Type = TruthValue
_ApQOSBgIsUseWREDAlg_Object = MibTableColumn
apQOSBgIsUseWREDAlg = _ApQOSBgIsUseWREDAlg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 3, 1, 1, 4),
    _ApQOSBgIsUseWREDAlg_Type()
)
apQOSBgIsUseWREDAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBgIsUseWREDAlg.setStatus("current")
_ApQOSBgIsUseTrafficShaping_Type = TruthValue
_ApQOSBgIsUseTrafficShaping_Object = MibTableColumn
apQOSBgIsUseTrafficShaping = _ApQOSBgIsUseTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 3, 1, 1, 5),
    _ApQOSBgIsUseTrafficShaping_Type()
)
apQOSBgIsUseTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBgIsUseTrafficShaping.setStatus("current")
_ApQOSBestEffortCfgObjects_ObjectIdentity = ObjectIdentity
apQOSBestEffortCfgObjects = _ApQOSBestEffortCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 4)
)
_ApQOSBestEffortCfgTable_Object = MibTable
apQOSBestEffortCfgTable = _ApQOSBestEffortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 4, 1)
)
if mibBuilder.loadTexts:
    apQOSBestEffortCfgTable.setStatus("current")
_ApQOSBestEffortCfgTableEntry_Object = MibTableRow
apQOSBestEffortCfgTableEntry = _ApQOSBestEffortCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 4, 1, 1)
)
apQOSBestEffortCfgTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSBestEffortCfgTableEntry.setStatus("current")
_ApQOSBeMaxSvcCnt_Type = Integer32
_ApQOSBeMaxSvcCnt_Object = MibTableColumn
apQOSBeMaxSvcCnt = _ApQOSBeMaxSvcCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 4, 1, 1, 1),
    _ApQOSBeMaxSvcCnt_Type()
)
apQOSBeMaxSvcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBeMaxSvcCnt.setStatus("current")
_ApQOSBeSvcBW_Type = Integer32
_ApQOSBeSvcBW_Object = MibTableColumn
apQOSBeSvcBW = _ApQOSBeSvcBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 4, 1, 1, 2),
    _ApQOSBeSvcBW_Type()
)
apQOSBeSvcBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBeSvcBW.setStatus("current")
_ApQOSBeSvcBWPercent_Type = Integer32
_ApQOSBeSvcBWPercent_Object = MibTableColumn
apQOSBeSvcBWPercent = _ApQOSBeSvcBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 4, 1, 1, 3),
    _ApQOSBeSvcBWPercent_Type()
)
apQOSBeSvcBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBeSvcBWPercent.setStatus("current")
_ApQOSBeIsUseWREDAlg_Type = TruthValue
_ApQOSBeIsUseWREDAlg_Object = MibTableColumn
apQOSBeIsUseWREDAlg = _ApQOSBeIsUseWREDAlg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 4, 1, 1, 4),
    _ApQOSBeIsUseWREDAlg_Type()
)
apQOSBeIsUseWREDAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBeIsUseWREDAlg.setStatus("current")
_ApQOSBeIsUseTrafficShaping_Type = TruthValue
_ApQOSBeIsUseTrafficShaping_Object = MibTableColumn
apQOSBeIsUseTrafficShaping = _ApQOSBeIsUseTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 4, 1, 1, 5),
    _ApQOSBeIsUseTrafficShaping_Type()
)
apQOSBeIsUseTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSBeIsUseTrafficShaping.setStatus("current")
_ApQOSVoiceInfoCfgObjects_ObjectIdentity = ObjectIdentity
apQOSVoiceInfoCfgObjects = _ApQOSVoiceInfoCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5)
)
_ApQOSVoiceInfoCfgTable_Object = MibTable
apQOSVoiceInfoCfgTable = _ApQOSVoiceInfoCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1)
)
if mibBuilder.loadTexts:
    apQOSVoiceInfoCfgTable.setStatus("current")
_ApQOSVoiceInfoCfgTableEntry_Object = MibTableRow
apQOSVoiceInfoCfgTableEntry = _ApQOSVoiceInfoCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1)
)
apQOSVoiceInfoCfgTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSVoiceInfoCfgTableEntry.setStatus("current")
_ApQOSVoiceMaxSvcCnt_Type = Integer32
_ApQOSVoiceMaxSvcCnt_Object = MibTableColumn
apQOSVoiceMaxSvcCnt = _ApQOSVoiceMaxSvcCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 1),
    _ApQOSVoiceMaxSvcCnt_Type()
)
apQOSVoiceMaxSvcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceMaxSvcCnt.setStatus("current")
_ApQOSVoiceSvcBW_Type = Integer32
_ApQOSVoiceSvcBW_Object = MibTableColumn
apQOSVoiceSvcBW = _ApQOSVoiceSvcBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 2),
    _ApQOSVoiceSvcBW_Type()
)
apQOSVoiceSvcBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceSvcBW.setStatus("current")
_ApQOSVoiceSvcBWPercent_Type = Integer32
_ApQOSVoiceSvcBWPercent_Object = MibTableColumn
apQOSVoiceSvcBWPercent = _ApQOSVoiceSvcBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 3),
    _ApQOSVoiceSvcBWPercent_Type()
)
apQOSVoiceSvcBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceSvcBWPercent.setStatus("current")
_ApQOSVoiceIsUseStreamBasedQueue_Type = TruthValue
_ApQOSVoiceIsUseStreamBasedQueue_Object = MibTableColumn
apQOSVoiceIsUseStreamBasedQueue = _ApQOSVoiceIsUseStreamBasedQueue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 4),
    _ApQOSVoiceIsUseStreamBasedQueue_Type()
)
apQOSVoiceIsUseStreamBasedQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceIsUseStreamBasedQueue.setStatus("current")
_ApQOSVoiceStreamMaxQueueLen_Type = Integer32
_ApQOSVoiceStreamMaxQueueLen_Object = MibTableColumn
apQOSVoiceStreamMaxQueueLen = _ApQOSVoiceStreamMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 5),
    _ApQOSVoiceStreamMaxQueueLen_Type()
)
apQOSVoiceStreamMaxQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceStreamMaxQueueLen.setStatus("current")
_ApQOSVoiceStreamAvgSpeed_Type = Integer32
_ApQOSVoiceStreamAvgSpeed_Object = MibTableColumn
apQOSVoiceStreamAvgSpeed = _ApQOSVoiceStreamAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 6),
    _ApQOSVoiceStreamAvgSpeed_Type()
)
apQOSVoiceStreamAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceStreamAvgSpeed.setStatus("current")
_ApQOSVoiceStreamMaxBurst_Type = Integer32
_ApQOSVoiceStreamMaxBurst_Object = MibTableColumn
apQOSVoiceStreamMaxBurst = _ApQOSVoiceStreamMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 7),
    _ApQOSVoiceStreamMaxBurst_Type()
)
apQOSVoiceStreamMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceStreamMaxBurst.setStatus("current")
_ApQOSVoiceIsUseWREDAlg_Type = TruthValue
_ApQOSVoiceIsUseWREDAlg_Object = MibTableColumn
apQOSVoiceIsUseWREDAlg = _ApQOSVoiceIsUseWREDAlg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 8),
    _ApQOSVoiceIsUseWREDAlg_Type()
)
apQOSVoiceIsUseWREDAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceIsUseWREDAlg.setStatus("current")
_ApQOSVoiceIsUseTrafficShaping_Type = TruthValue
_ApQOSVoiceIsUseTrafficShaping_Object = MibTableColumn
apQOSVoiceIsUseTrafficShaping = _ApQOSVoiceIsUseTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 5, 1, 1, 9),
    _ApQOSVoiceIsUseTrafficShaping_Type()
)
apQOSVoiceIsUseTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVoiceIsUseTrafficShaping.setStatus("current")
_ApQOSVideoInfoCfgObjects_ObjectIdentity = ObjectIdentity
apQOSVideoInfoCfgObjects = _ApQOSVideoInfoCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6)
)
_ApQOSVideoInfoCfgTable_Object = MibTable
apQOSVideoInfoCfgTable = _ApQOSVideoInfoCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1)
)
if mibBuilder.loadTexts:
    apQOSVideoInfoCfgTable.setStatus("current")
_ApQOSVideoInfoCfgTableEntry_Object = MibTableRow
apQOSVideoInfoCfgTableEntry = _ApQOSVideoInfoCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1)
)
apQOSVideoInfoCfgTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSVideoInfoCfgTableEntry.setStatus("current")
_ApQOSVideoMaxSvcCnt_Type = Integer32
_ApQOSVideoMaxSvcCnt_Object = MibTableColumn
apQOSVideoMaxSvcCnt = _ApQOSVideoMaxSvcCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 1),
    _ApQOSVideoMaxSvcCnt_Type()
)
apQOSVideoMaxSvcCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoMaxSvcCnt.setStatus("current")
_ApQOSVideoSvcBW_Type = Integer32
_ApQOSVideoSvcBW_Object = MibTableColumn
apQOSVideoSvcBW = _ApQOSVideoSvcBW_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 2),
    _ApQOSVideoSvcBW_Type()
)
apQOSVideoSvcBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoSvcBW.setStatus("current")
_ApQOSVideoSvcBWPercent_Type = Integer32
_ApQOSVideoSvcBWPercent_Object = MibTableColumn
apQOSVideoSvcBWPercent = _ApQOSVideoSvcBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 3),
    _ApQOSVideoSvcBWPercent_Type()
)
apQOSVideoSvcBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoSvcBWPercent.setStatus("current")
_ApQOSVideoIsUseStreamBasedQueue_Type = TruthValue
_ApQOSVideoIsUseStreamBasedQueue_Object = MibTableColumn
apQOSVideoIsUseStreamBasedQueue = _ApQOSVideoIsUseStreamBasedQueue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 4),
    _ApQOSVideoIsUseStreamBasedQueue_Type()
)
apQOSVideoIsUseStreamBasedQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoIsUseStreamBasedQueue.setStatus("current")
_ApQOSVideoStreamMaxQueueLen_Type = Integer32
_ApQOSVideoStreamMaxQueueLen_Object = MibTableColumn
apQOSVideoStreamMaxQueueLen = _ApQOSVideoStreamMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 5),
    _ApQOSVideoStreamMaxQueueLen_Type()
)
apQOSVideoStreamMaxQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoStreamMaxQueueLen.setStatus("current")
_ApQOSVideoStreamAvgSpeed_Type = Integer32
_ApQOSVideoStreamAvgSpeed_Object = MibTableColumn
apQOSVideoStreamAvgSpeed = _ApQOSVideoStreamAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 6),
    _ApQOSVideoStreamAvgSpeed_Type()
)
apQOSVideoStreamAvgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoStreamAvgSpeed.setStatus("current")
_ApQOSVideoStreamMaxBurst_Type = Integer32
_ApQOSVideoStreamMaxBurst_Object = MibTableColumn
apQOSVideoStreamMaxBurst = _ApQOSVideoStreamMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 7),
    _ApQOSVideoStreamMaxBurst_Type()
)
apQOSVideoStreamMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoStreamMaxBurst.setStatus("current")
_ApQOSVideoIsUseWREDAlg_Type = TruthValue
_ApQOSVideoIsUseWREDAlg_Object = MibTableColumn
apQOSVideoIsUseWREDAlg = _ApQOSVideoIsUseWREDAlg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 8),
    _ApQOSVideoIsUseWREDAlg_Type()
)
apQOSVideoIsUseWREDAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoIsUseWREDAlg.setStatus("current")
_ApQOSVideoIsUseTrafficShaping_Type = TruthValue
_ApQOSVideoIsUseTrafficShaping_Object = MibTableColumn
apQOSVideoIsUseTrafficShaping = _ApQOSVideoIsUseTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 6, 1, 1, 9),
    _ApQOSVideoIsUseTrafficShaping_Type()
)
apQOSVideoIsUseTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSVideoIsUseTrafficShaping.setStatus("current")
_ApQOSWMMConfigObjects_ObjectIdentity = ObjectIdentity
apQOSWMMConfigObjects = _ApQOSWMMConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7)
)
_ApQOSWMMConfigTable_Object = MibTable
apQOSWMMConfigTable = _ApQOSWMMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1)
)
if mibBuilder.loadTexts:
    apQOSWMMConfigTable.setStatus("current")
_ApQOSWMMConfigTableEntry_Object = MibTableRow
apQOSWMMConfigTableEntry = _ApQOSWMMConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1)
)
apQOSWMMConfigTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSWMMConfigTableEntry.setStatus("current")


class _ApQOSMode_Type(Integer32):
    """Custom type apQOSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wmm", 1),
          ("dot8011e", 2),
          ("wmm80211e", 3))
    )


_ApQOSMode_Type.__name__ = "Integer32"
_ApQOSMode_Object = MibTableColumn
apQOSMode = _ApQOSMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 1),
    _ApQOSMode_Type()
)
apQOSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSMode.setStatus("current")
_ApQOSUpdateSeq_Type = Integer32
_ApQOSUpdateSeq_Object = MibTableColumn
apQOSUpdateSeq = _ApQOSUpdateSeq_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 2),
    _ApQOSUpdateSeq_Type()
)
apQOSUpdateSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSUpdateSeq.setStatus("current")
_ApQOSSvpAcIndex_Type = Integer32
_ApQOSSvpAcIndex_Object = MibTableColumn
apQOSSvpAcIndex = _ApQOSSvpAcIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 3),
    _ApQOSSvpAcIndex_Type()
)
apQOSSvpAcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSSvpAcIndex.setStatus("current")
_ApQOSUapsd_Type = Integer32
_ApQOSUapsd_Object = MibTableColumn
apQOSUapsd = _ApQOSUapsd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 4),
    _ApQOSUapsd_Type()
)
apQOSUapsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSUapsd.setStatus("current")
_ApQOSAcIndx1_Type = Integer32
_ApQOSAcIndx1_Object = MibTableColumn
apQOSAcIndx1 = _ApQOSAcIndx1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 5),
    _ApQOSAcIndx1_Type()
)
apQOSAcIndx1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAcIndx1.setStatus("current")
_ApQOSAcIndx2_Type = Integer32
_ApQOSAcIndx2_Object = MibTableColumn
apQOSAcIndx2 = _ApQOSAcIndx2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 6),
    _ApQOSAcIndx2_Type()
)
apQOSAcIndx2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAcIndx2.setStatus("current")
_ApQOSAcIndx3_Type = Integer32
_ApQOSAcIndx3_Object = MibTableColumn
apQOSAcIndx3 = _ApQOSAcIndx3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 7),
    _ApQOSAcIndx3_Type()
)
apQOSAcIndx3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAcIndx3.setStatus("current")
_ApQOSAcIndx4_Type = Integer32
_ApQOSAcIndx4_Object = MibTableColumn
apQOSAcIndx4 = _ApQOSAcIndx4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 8),
    _ApQOSAcIndx4_Type()
)
apQOSAcIndx4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAcIndx4.setStatus("current")
_ApQOSAifsn1_Type = Integer32
_ApQOSAifsn1_Object = MibTableColumn
apQOSAifsn1 = _ApQOSAifsn1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 9),
    _ApQOSAifsn1_Type()
)
apQOSAifsn1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAifsn1.setStatus("current")
_ApQOSAifsn2_Type = Integer32
_ApQOSAifsn2_Object = MibTableColumn
apQOSAifsn2 = _ApQOSAifsn2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 10),
    _ApQOSAifsn2_Type()
)
apQOSAifsn2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAifsn2.setStatus("current")
_ApQOSAifsn3_Type = Integer32
_ApQOSAifsn3_Object = MibTableColumn
apQOSAifsn3 = _ApQOSAifsn3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 11),
    _ApQOSAifsn3_Type()
)
apQOSAifsn3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAifsn3.setStatus("current")
_ApQOSAifsn4_Type = Integer32
_ApQOSAifsn4_Object = MibTableColumn
apQOSAifsn4 = _ApQOSAifsn4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 12),
    _ApQOSAifsn4_Type()
)
apQOSAifsn4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAifsn4.setStatus("current")
_ApQOSEcwMin1_Type = Integer32
_ApQOSEcwMin1_Object = MibTableColumn
apQOSEcwMin1 = _ApQOSEcwMin1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 13),
    _ApQOSEcwMin1_Type()
)
apQOSEcwMin1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSEcwMin1.setStatus("current")
_ApQOSEcwMin2_Type = Integer32
_ApQOSEcwMin2_Object = MibTableColumn
apQOSEcwMin2 = _ApQOSEcwMin2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 14),
    _ApQOSEcwMin2_Type()
)
apQOSEcwMin2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSEcwMin2.setStatus("current")
_ApQOSEcwMin3_Type = Integer32
_ApQOSEcwMin3_Object = MibTableColumn
apQOSEcwMin3 = _ApQOSEcwMin3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 15),
    _ApQOSEcwMin3_Type()
)
apQOSEcwMin3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSEcwMin3.setStatus("current")
_ApQOSEcwMin4_Type = Integer32
_ApQOSEcwMin4_Object = MibTableColumn
apQOSEcwMin4 = _ApQOSEcwMin4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 16),
    _ApQOSEcwMin4_Type()
)
apQOSEcwMin4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSEcwMin4.setStatus("current")
_ApQOSEcwMax1_Type = Integer32
_ApQOSEcwMax1_Object = MibTableColumn
apQOSEcwMax1 = _ApQOSEcwMax1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 17),
    _ApQOSEcwMax1_Type()
)
apQOSEcwMax1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSEcwMax1.setStatus("current")
_ApQOSEcwMax2_Type = Integer32
_ApQOSEcwMax2_Object = MibTableColumn
apQOSEcwMax2 = _ApQOSEcwMax2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 18),
    _ApQOSEcwMax2_Type()
)
apQOSEcwMax2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSEcwMax2.setStatus("current")
_ApQOSEcwMax3_Type = Integer32
_ApQOSEcwMax3_Object = MibTableColumn
apQOSEcwMax3 = _ApQOSEcwMax3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 19),
    _ApQOSEcwMax3_Type()
)
apQOSEcwMax3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSEcwMax3.setStatus("current")
_ApQOSEcwMax4_Type = Integer32
_ApQOSEcwMax4_Object = MibTableColumn
apQOSEcwMax4 = _ApQOSEcwMax4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 20),
    _ApQOSEcwMax4_Type()
)
apQOSEcwMax4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSEcwMax4.setStatus("current")
_ApQOSTxopLmt1_Type = Integer32
_ApQOSTxopLmt1_Object = MibTableColumn
apQOSTxopLmt1 = _ApQOSTxopLmt1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 21),
    _ApQOSTxopLmt1_Type()
)
apQOSTxopLmt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSTxopLmt1.setStatus("current")
_ApQOSTxopLmt2_Type = Integer32
_ApQOSTxopLmt2_Object = MibTableColumn
apQOSTxopLmt2 = _ApQOSTxopLmt2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 22),
    _ApQOSTxopLmt2_Type()
)
apQOSTxopLmt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSTxopLmt2.setStatus("current")
_ApQOSTxopLmt3_Type = Integer32
_ApQOSTxopLmt3_Object = MibTableColumn
apQOSTxopLmt3 = _ApQOSTxopLmt3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 23),
    _ApQOSTxopLmt3_Type()
)
apQOSTxopLmt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSTxopLmt3.setStatus("current")
_ApQOSTxopLmt4_Type = Integer32
_ApQOSTxopLmt4_Object = MibTableColumn
apQOSTxopLmt4 = _ApQOSTxopLmt4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 24),
    _ApQOSTxopLmt4_Type()
)
apQOSTxopLmt4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSTxopLmt4.setStatus("current")
_ApQOSAcmAndAck1_Type = Integer32
_ApQOSAcmAndAck1_Object = MibTableColumn
apQOSAcmAndAck1 = _ApQOSAcmAndAck1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 25),
    _ApQOSAcmAndAck1_Type()
)
apQOSAcmAndAck1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAcmAndAck1.setStatus("current")
_ApQOSAcmAndAck2_Type = Integer32
_ApQOSAcmAndAck2_Object = MibTableColumn
apQOSAcmAndAck2 = _ApQOSAcmAndAck2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 26),
    _ApQOSAcmAndAck2_Type()
)
apQOSAcmAndAck2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAcmAndAck2.setStatus("current")
_ApQOSAcmAndAck3_Type = Integer32
_ApQOSAcmAndAck3_Object = MibTableColumn
apQOSAcmAndAck3 = _ApQOSAcmAndAck3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 27),
    _ApQOSAcmAndAck3_Type()
)
apQOSAcmAndAck3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAcmAndAck3.setStatus("current")
_ApQOSAcmAndAck4_Type = Integer32
_ApQOSAcmAndAck4_Object = MibTableColumn
apQOSAcmAndAck4 = _ApQOSAcmAndAck4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 7, 7, 1, 1, 28),
    _ApQOSAcmAndAck4_Type()
)
apQOSAcmAndAck4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apQOSAcmAndAck4.setStatus("current")
_ApAlarmParamConfigEntry_ObjectIdentity = ObjectIdentity
apAlarmParamConfigEntry = _ApAlarmParamConfigEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8)
)
_ApStaInterfNumThreshhd_Type = Integer32
_ApStaInterfNumThreshhd_Object = MibScalar
apStaInterfNumThreshhd = _ApStaInterfNumThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 1),
    _ApStaInterfNumThreshhd_Type()
)
apStaInterfNumThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apStaInterfNumThreshhd.setStatus("current")
_ApAPCoInterfThreshhd_Type = Integer32
_ApAPCoInterfThreshhd_Object = MibScalar
apAPCoInterfThreshhd = _ApAPCoInterfThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 2),
    _ApAPCoInterfThreshhd_Type()
)
apAPCoInterfThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAPCoInterfThreshhd.setStatus("current")
_ApAPNeiborInterfThreshhd_Type = Integer32
_ApAPNeiborInterfThreshhd_Object = MibScalar
apAPNeiborInterfThreshhd = _ApAPNeiborInterfThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 3),
    _ApAPNeiborInterfThreshhd_Type()
)
apAPNeiborInterfThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAPNeiborInterfThreshhd.setStatus("current")
_ApCPUusageThreshhd_Type = Integer32
_ApCPUusageThreshhd_Object = MibScalar
apCPUusageThreshhd = _ApCPUusageThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 4),
    _ApCPUusageThreshhd_Type()
)
apCPUusageThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCPUusageThreshhd.setStatus("current")
_ApMemUsageThreshhd_Type = Integer32
_ApMemUsageThreshhd_Object = MibScalar
apMemUsageThreshhd = _ApMemUsageThreshhd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 5),
    _ApMemUsageThreshhd_Type()
)
apMemUsageThreshhd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMemUsageThreshhd.setStatus("current")
_AcUserExcepOfflineTimes_Type = Counter32
_AcUserExcepOfflineTimes_Object = MibScalar
acUserExcepOfflineTimes = _AcUserExcepOfflineTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 6),
    _AcUserExcepOfflineTimes_Type()
)
acUserExcepOfflineTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acUserExcepOfflineTimes.setStatus("current")
_AcAuthReqTimes_Type = Counter32
_AcAuthReqTimes_Object = MibScalar
acAuthReqTimes = _AcAuthReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 7),
    _AcAuthReqTimes_Type()
)
acAuthReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuthReqTimes.setStatus("current")
_AcAuthSuccessTimes_Type = Counter32
_AcAuthSuccessTimes_Object = MibScalar
acAuthSuccessTimes = _AcAuthSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 8),
    _AcAuthSuccessTimes_Type()
)
acAuthSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuthSuccessTimes.setStatus("current")
_AcAuthReqFailTimes_Type = Counter32
_AcAuthReqFailTimes_Object = MibScalar
acAuthReqFailTimes = _AcAuthReqFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 9),
    _AcAuthReqFailTimes_Type()
)
acAuthReqFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuthReqFailTimes.setStatus("current")
_AcDisconnectOnlineUsersCount_Type = Counter32
_AcDisconnectOnlineUsersCount_Object = MibScalar
acDisconnectOnlineUsersCount = _AcDisconnectOnlineUsersCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 10),
    _AcDisconnectOnlineUsersCount_Type()
)
acDisconnectOnlineUsersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDisconnectOnlineUsersCount.setStatus("current")
_AcOnlineUserNum_Type = Counter32
_AcOnlineUserNum_Object = MibScalar
acOnlineUserNum = _AcOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 8, 11),
    _AcOnlineUserNum_Type()
)
acOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acOnlineUserNum.setStatus("current")
_ApVLANConfigObjects_ObjectIdentity = ObjectIdentity
apVLANConfigObjects = _ApVLANConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 9)
)
_ApVLANConfigTable_Object = MibTable
apVLANConfigTable = _ApVLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 9, 1)
)
if mibBuilder.loadTexts:
    apVLANConfigTable.setStatus("current")
_ApVLANConfigTableEntry_Object = MibTableRow
apVLANConfigTableEntry = _ApVLANConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 9, 1, 1)
)
apVLANConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apVLANConfigTableEntry.setStatus("current")
_ApVLANID_Type = Integer32
_ApVLANID_Object = MibTableColumn
apVLANID = _ApVLANID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 9, 1, 1, 1),
    _ApVLANID_Type()
)
apVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apVLANID.setStatus("current")
_ApVlanCfgStatus_Type = RowStatus
_ApVlanCfgStatus_Object = MibTableColumn
apVlanCfgStatus = _ApVlanCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 9, 1, 1, 2),
    _ApVlanCfgStatus_Type()
)
apVlanCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apVlanCfgStatus.setStatus("current")
_ApStatisticsInfoReadObjects_ObjectIdentity = ObjectIdentity
apStatisticsInfoReadObjects = _ApStatisticsInfoReadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10)
)
_ApSysCapabilityStatisticsObjects_ObjectIdentity = ObjectIdentity
apSysCapabilityStatisticsObjects = _ApSysCapabilityStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 1)
)
_ApSysCapabilityStatisticsTable_Object = MibTable
apSysCapabilityStatisticsTable = _ApSysCapabilityStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 1, 1)
)
if mibBuilder.loadTexts:
    apSysCapabilityStatisticsTable.setStatus("current")
_ApSysCapabilityStatisticsTableEntry_Object = MibTableRow
apSysCapabilityStatisticsTableEntry = _ApSysCapabilityStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 1, 1, 1)
)
apSysCapabilityStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    apSysCapabilityStatisticsTableEntry.setStatus("current")
_ApCPURTUsage_Type = Integer32
_ApCPURTUsage_Object = MibTableColumn
apCPURTUsage = _ApCPURTUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 1, 1, 1, 1),
    _ApCPURTUsage_Type()
)
apCPURTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCPURTUsage.setStatus("current")
_ApCPUAvgUsage_Type = Integer32
_ApCPUAvgUsage_Object = MibTableColumn
apCPUAvgUsage = _ApCPUAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 1, 1, 1, 2),
    _ApCPUAvgUsage_Type()
)
apCPUAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCPUAvgUsage.setStatus("current")
_ApMemRTUsage_Type = Integer32
_ApMemRTUsage_Object = MibTableColumn
apMemRTUsage = _ApMemRTUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 1, 1, 1, 3),
    _ApMemRTUsage_Type()
)
apMemRTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMemRTUsage.setStatus("current")
_ApMemAvgUsage_Type = Integer32
_ApMemAvgUsage_Object = MibTableColumn
apMemAvgUsage = _ApMemAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 1, 1, 1, 4),
    _ApMemAvgUsage_Type()
)
apMemAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMemAvgUsage.setStatus("current")
_ApLinkStatisticsObjects_ObjectIdentity = ObjectIdentity
apLinkStatisticsObjects = _ApLinkStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2)
)
_ApLinkStatisticsTable_Object = MibTable
apLinkStatisticsTable = _ApLinkStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1)
)
if mibBuilder.loadTexts:
    apLinkStatisticsTable.setStatus("current")
_ApLinkStatisticsTableEntry_Object = MibTableRow
apLinkStatisticsTableEntry = _ApLinkStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1)
)
apLinkStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    apLinkStatisticsTableEntry.setStatus("current")
_ApLinkStatStationAssocSum_Type = Integer32
_ApLinkStatStationAssocSum_Object = MibTableColumn
apLinkStatStationAssocSum = _ApLinkStatStationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 1),
    _ApLinkStatStationAssocSum_Type()
)
apLinkStatStationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatStationAssocSum.setStatus("current")
_ApLinkStatStationOnlineSum_Type = Integer32
_ApLinkStatStationOnlineSum_Object = MibTableColumn
apLinkStatStationOnlineSum = _ApLinkStatStationOnlineSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 2),
    _ApLinkStatStationOnlineSum_Type()
)
apLinkStatStationOnlineSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatStationOnlineSum.setStatus("current")
_ApLinkStatAssocTimes_Type = Counter32
_ApLinkStatAssocTimes_Object = MibTableColumn
apLinkStatAssocTimes = _ApLinkStatAssocTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 3),
    _ApLinkStatAssocTimes_Type()
)
apLinkStatAssocTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatAssocTimes.setStatus("current")
_ApLinkStatAssocFailTimes_Type = Counter32
_ApLinkStatAssocFailTimes_Object = MibTableColumn
apLinkStatAssocFailTimes = _ApLinkStatAssocFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 4),
    _ApLinkStatAssocFailTimes_Type()
)
apLinkStatAssocFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatAssocFailTimes.setStatus("current")
_ApLinkStatReassocTimes_Type = Counter32
_ApLinkStatReassocTimes_Object = MibTableColumn
apLinkStatReassocTimes = _ApLinkStatReassocTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 5),
    _ApLinkStatReassocTimes_Type()
)
apLinkStatReassocTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatReassocTimes.setStatus("current")
_ApLinkStatPreAssCannotShiftDeassocFailSum_Type = Counter32
_ApLinkStatPreAssCannotShiftDeassocFailSum_Object = MibTableColumn
apLinkStatPreAssCannotShiftDeassocFailSum = _ApLinkStatPreAssCannotShiftDeassocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 6),
    _ApLinkStatPreAssCannotShiftDeassocFailSum_Type()
)
apLinkStatPreAssCannotShiftDeassocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatPreAssCannotShiftDeassocFailSum.setStatus("current")
_ApLinkStatApStatsDisassociated_Type = Counter32
_ApLinkStatApStatsDisassociated_Object = MibTableColumn
apLinkStatApStatsDisassociated = _ApLinkStatApStatsDisassociated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 7),
    _ApLinkStatApStatsDisassociated_Type()
)
apLinkStatApStatsDisassociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatApStatsDisassociated.setStatus("current")
_ApLinkStatAssocRejectSum_Type = Counter32
_ApLinkStatAssocRejectSum_Object = MibTableColumn
apLinkStatAssocRejectSum = _ApLinkStatAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 8),
    _ApLinkStatAssocRejectSum_Type()
)
apLinkStatAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatAssocRejectSum.setStatus("current")
_ApLinkStatBSSNotSupportAssocFailSum_Type = Counter32
_ApLinkStatBSSNotSupportAssocFailSum_Object = MibTableColumn
apLinkStatBSSNotSupportAssocFailSum = _ApLinkStatBSSNotSupportAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 9),
    _ApLinkStatBSSNotSupportAssocFailSum_Type()
)
apLinkStatBSSNotSupportAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatBSSNotSupportAssocFailSum.setStatus("current")
_ApLinkStatApAuthReqTimes_Type = Counter32
_ApLinkStatApAuthReqTimes_Object = MibTableColumn
apLinkStatApAuthReqTimes = _ApLinkStatApAuthReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 10),
    _ApLinkStatApAuthReqTimes_Type()
)
apLinkStatApAuthReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatApAuthReqTimes.setStatus("current")
_ApLinkStatApAuthSuccessTimes_Type = Counter32
_ApLinkStatApAuthSuccessTimes_Object = MibTableColumn
apLinkStatApAuthSuccessTimes = _ApLinkStatApAuthSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 11),
    _ApLinkStatApAuthSuccessTimes_Type()
)
apLinkStatApAuthSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatApAuthSuccessTimes.setStatus("current")
_AcLinkStatApAuthReqFailTimes_Type = Counter32
_AcLinkStatApAuthReqFailTimes_Object = MibTableColumn
acLinkStatApAuthReqFailTimes = _AcLinkStatApAuthReqFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 12),
    _AcLinkStatApAuthReqFailTimes_Type()
)
acLinkStatApAuthReqFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLinkStatApAuthReqFailTimes.setStatus("current")
_ApLinkStatReassocFailTimes_Type = Counter32
_ApLinkStatReassocFailTimes_Object = MibTableColumn
apLinkStatReassocFailTimes = _ApLinkStatReassocFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 13),
    _ApLinkStatReassocFailTimes_Type()
)
apLinkStatReassocFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatReassocFailTimes.setStatus("current")
_ApLinkStatRSSILowAssocFailSum_Type = Counter32
_ApLinkStatRSSILowAssocFailSum_Object = MibTableColumn
apLinkStatRSSILowAssocFailSum = _ApLinkStatRSSILowAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 14),
    _ApLinkStatRSSILowAssocFailSum_Type()
)
apLinkStatRSSILowAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatRSSILowAssocFailSum.setStatus("current")
_ApLinkStatUnknowReasonAssoFailSum_Type = Counter32
_ApLinkStatUnknowReasonAssoFailSum_Object = MibTableColumn
apLinkStatUnknowReasonAssoFailSum = _ApLinkStatUnknowReasonAssoFailSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 15),
    _ApLinkStatUnknowReasonAssoFailSum_Type()
)
apLinkStatUnknowReasonAssoFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatUnknowReasonAssoFailSum.setStatus("current")
_ApLinkStatOut80211StandardAssocFailSum_Type = Counter32
_ApLinkStatOut80211StandardAssocFailSum_Object = MibTableColumn
apLinkStatOut80211StandardAssocFailSum = _ApLinkStatOut80211StandardAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 16),
    _ApLinkStatOut80211StandardAssocFailSum_Type()
)
apLinkStatOut80211StandardAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatOut80211StandardAssocFailSum.setStatus("current")
_ApLinkStatAllStationsTotalUpTime_Type = Integer32
_ApLinkStatAllStationsTotalUpTime_Object = MibTableColumn
apLinkStatAllStationsTotalUpTime = _ApLinkStatAllStationsTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 17),
    _ApLinkStatAllStationsTotalUpTime_Type()
)
apLinkStatAllStationsTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatAllStationsTotalUpTime.setStatus("current")
_ApLinkStatAssocRespTimes_Type = Counter32
_ApLinkStatAssocRespTimes_Object = MibTableColumn
apLinkStatAssocRespTimes = _ApLinkStatAssocRespTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 18),
    _ApLinkStatAssocRespTimes_Type()
)
apLinkStatAssocRespTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatAssocRespTimes.setStatus("current")
_ApLinkStatAssocSuccTimes_Type = Counter32
_ApLinkStatAssocSuccTimes_Object = MibTableColumn
apLinkStatAssocSuccTimes = _ApLinkStatAssocSuccTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 19),
    _ApLinkStatAssocSuccTimes_Type()
)
apLinkStatAssocSuccTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatAssocSuccTimes.setStatus("current")
_ApLinkStatUserRadiusOnlineSum_Type = Integer32
_ApLinkStatUserRadiusOnlineSum_Object = MibTableColumn
apLinkStatUserRadiusOnlineSum = _ApLinkStatUserRadiusOnlineSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 20),
    _ApLinkStatUserRadiusOnlineSum_Type()
)
apLinkStatUserRadiusOnlineSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatUserRadiusOnlineSum.setStatus("current")
_ApLinkStatAllUserOnlineTime_Type = TimeTicks
_ApLinkStatAllUserOnlineTime_Object = MibTableColumn
apLinkStatAllUserOnlineTime = _ApLinkStatAllUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 21),
    _ApLinkStatAllUserOnlineTime_Type()
)
apLinkStatAllUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatAllUserOnlineTime.setStatus("current")
_ApLinkStatRadiusAuthTimes_Type = Counter32
_ApLinkStatRadiusAuthTimes_Object = MibTableColumn
apLinkStatRadiusAuthTimes = _ApLinkStatRadiusAuthTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 22),
    _ApLinkStatRadiusAuthTimes_Type()
)
apLinkStatRadiusAuthTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatRadiusAuthTimes.setStatus("current")
_ApLinkStatRadiusAuthSuccTimes_Type = Counter32
_ApLinkStatRadiusAuthSuccTimes_Object = MibTableColumn
apLinkStatRadiusAuthSuccTimes = _ApLinkStatRadiusAuthSuccTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 23),
    _ApLinkStatRadiusAuthSuccTimes_Type()
)
apLinkStatRadiusAuthSuccTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatRadiusAuthSuccTimes.setStatus("current")
_ApLinkStatRadiusAuthFailTimes_Type = Counter32
_ApLinkStatRadiusAuthFailTimes_Object = MibTableColumn
apLinkStatRadiusAuthFailTimes = _ApLinkStatRadiusAuthFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 24),
    _ApLinkStatRadiusAuthFailTimes_Type()
)
apLinkStatRadiusAuthFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatRadiusAuthFailTimes.setStatus("current")
_ApLinkStatAssocSuccessTimes_Type = Counter32
_ApLinkStatAssocSuccessTimes_Object = MibTableColumn
apLinkStatAssocSuccessTimes = _ApLinkStatAssocSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 2, 1, 1, 25),
    _ApLinkStatAssocSuccessTimes_Type()
)
apLinkStatAssocSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLinkStatAssocSuccessTimes.setStatus("current")
_ApInterfaceRGMIIStatisticsObjects_ObjectIdentity = ObjectIdentity
apInterfaceRGMIIStatisticsObjects = _ApInterfaceRGMIIStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3)
)
_ApInterfaceRGMIIStatisticsTable_Object = MibTable
apInterfaceRGMIIStatisticsTable = _ApInterfaceRGMIIStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1)
)
if mibBuilder.loadTexts:
    apInterfaceRGMIIStatisticsTable.setStatus("current")
_ApInterfaceRGMIIStatisticsTableEntry_Object = MibTableRow
apInterfaceRGMIIStatisticsTableEntry = _ApInterfaceRGMIIStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1)
)
apInterfaceRGMIIStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apRGMIIIndex"),
)
if mibBuilder.loadTexts:
    apInterfaceRGMIIStatisticsTableEntry.setStatus("current")
_ApRGMIIIndex_Type = Integer32
_ApRGMIIIndex_Object = MibTableColumn
apRGMIIIndex = _ApRGMIIIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 1),
    _ApRGMIIIndex_Type()
)
apRGMIIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apRGMIIIndex.setStatus("current")
_ApifInUcastPkts_Type = Counter32
_ApifInUcastPkts_Object = MibTableColumn
apifInUcastPkts = _ApifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 2),
    _ApifInUcastPkts_Type()
)
apifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifInUcastPkts.setStatus("current")
_ApifInNUcastPkts_Type = Counter32
_ApifInNUcastPkts_Object = MibTableColumn
apifInNUcastPkts = _ApifInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 3),
    _ApifInNUcastPkts_Type()
)
apifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifInNUcastPkts.setStatus("current")
_ApifInOctets_Type = Counter32
_ApifInOctets_Object = MibTableColumn
apifInOctets = _ApifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 4),
    _ApifInOctets_Type()
)
apifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifInOctets.setStatus("current")
_ApifInDiscardPkts_Type = Counter32
_ApifInDiscardPkts_Object = MibTableColumn
apifInDiscardPkts = _ApifInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 5),
    _ApifInDiscardPkts_Type()
)
apifInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifInDiscardPkts.setStatus("current")
_ApifInErrors_Type = Counter32
_ApifInErrors_Object = MibTableColumn
apifInErrors = _ApifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 6),
    _ApifInErrors_Type()
)
apifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifInErrors.setStatus("current")
_ApifOutUcastPkts_Type = Counter32
_ApifOutUcastPkts_Object = MibTableColumn
apifOutUcastPkts = _ApifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 7),
    _ApifOutUcastPkts_Type()
)
apifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifOutUcastPkts.setStatus("current")
_ApifOutNUcastPkts_Type = Counter32
_ApifOutNUcastPkts_Object = MibTableColumn
apifOutNUcastPkts = _ApifOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 8),
    _ApifOutNUcastPkts_Type()
)
apifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifOutNUcastPkts.setStatus("current")
_ApifOutOctets_Type = Counter32
_ApifOutOctets_Object = MibTableColumn
apifOutOctets = _ApifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 9),
    _ApifOutOctets_Type()
)
apifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifOutOctets.setStatus("current")
_ApifOutDiscardPkts_Type = Counter32
_ApifOutDiscardPkts_Object = MibTableColumn
apifOutDiscardPkts = _ApifOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 10),
    _ApifOutDiscardPkts_Type()
)
apifOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifOutDiscardPkts.setStatus("current")
_ApifOutErrors_Type = Counter32
_ApifOutErrors_Object = MibTableColumn
apifOutErrors = _ApifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 11),
    _ApifOutErrors_Type()
)
apifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifOutErrors.setStatus("current")
_ApifUpDwnTimes_Type = Counter32
_ApifUpDwnTimes_Object = MibTableColumn
apifUpDwnTimes = _ApifUpDwnTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 3, 1, 1, 12),
    _ApifUpDwnTimes_Type()
)
apifUpDwnTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apifUpDwnTimes.setStatus("current")
_ApInterfaceWireStatisticsObjects_ObjectIdentity = ObjectIdentity
apInterfaceWireStatisticsObjects = _ApInterfaceWireStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4)
)
_ApInterfaceWireStatisticsTable_Object = MibTable
apInterfaceWireStatisticsTable = _ApInterfaceWireStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1)
)
if mibBuilder.loadTexts:
    apInterfaceWireStatisticsTable.setStatus("current")
_ApInterfaceWireStatisticsTableEntry_Object = MibTableRow
apInterfaceWireStatisticsTableEntry = _ApInterfaceWireStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1)
)
apInterfaceWireStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apInterfaceWireStatisticsTableEntry.setStatus("current")
_ApAvgRxSignalStrength_Type = DisplayString
_ApAvgRxSignalStrength_Object = MibTableColumn
apAvgRxSignalStrength = _ApAvgRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 1),
    _ApAvgRxSignalStrength_Type()
)
apAvgRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAvgRxSignalStrength.setStatus("current")
_ApHighestRxSignalStrength_Type = DisplayString
_ApHighestRxSignalStrength_Object = MibTableColumn
apHighestRxSignalStrength = _ApHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 2),
    _ApHighestRxSignalStrength_Type()
)
apHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHighestRxSignalStrength.setStatus("current")
_ApLowestRxSignalStrength_Type = DisplayString
_ApLowestRxSignalStrength_Object = MibTableColumn
apLowestRxSignalStrength = _ApLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 3),
    _ApLowestRxSignalStrength_Type()
)
apLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLowestRxSignalStrength.setStatus("current")
_ApWirelessUpdownTimes_Type = Counter32
_ApWirelessUpdownTimes_Object = MibTableColumn
apWirelessUpdownTimes = _ApWirelessUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 4),
    _ApWirelessUpdownTimes_Type()
)
apWirelessUpdownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWirelessUpdownTimes.setStatus("current")
_ApChStatsNumStations_Type = Counter32
_ApChStatsNumStations_Object = MibTableColumn
apChStatsNumStations = _ApChStatsNumStations_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 5),
    _ApChStatsNumStations_Type()
)
apChStatsNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsNumStations.setStatus("current")
_ApTxDataPkts_Type = Counter32
_ApTxDataPkts_Object = MibTableColumn
apTxDataPkts = _ApTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 6),
    _ApTxDataPkts_Type()
)
apTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxDataPkts.setStatus("current")
_ApRxDataPkts_Type = Counter32
_ApRxDataPkts_Object = MibTableColumn
apRxDataPkts = _ApRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 7),
    _ApRxDataPkts_Type()
)
apRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxDataPkts.setStatus("current")
_ApUplinkDataOctets_Type = Counter64
_ApUplinkDataOctets_Object = MibTableColumn
apUplinkDataOctets = _ApUplinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 8),
    _ApUplinkDataOctets_Type()
)
apUplinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUplinkDataOctets.setStatus("current")
_ApDwlinkDataOctets_Type = Counter64
_ApDwlinkDataOctets_Object = MibTableColumn
apDwlinkDataOctets = _ApDwlinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 9),
    _ApDwlinkDataOctets_Type()
)
apDwlinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDwlinkDataOctets.setStatus("current")
_ApChStatsDwlinkTotRetryPkts_Type = Counter32
_ApChStatsDwlinkTotRetryPkts_Object = MibTableColumn
apChStatsDwlinkTotRetryPkts = _ApChStatsDwlinkTotRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 10),
    _ApChStatsDwlinkTotRetryPkts_Type()
)
apChStatsDwlinkTotRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsDwlinkTotRetryPkts.setStatus("current")
_ApChStatsPhyErrPkts_Type = Counter32
_ApChStatsPhyErrPkts_Object = MibTableColumn
apChStatsPhyErrPkts = _ApChStatsPhyErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 11),
    _ApChStatsPhyErrPkts_Type()
)
apChStatsPhyErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsPhyErrPkts.setStatus("current")
_ApChStatsMacFcsErrPkts_Type = Counter32
_ApChStatsMacFcsErrPkts_Object = MibTableColumn
apChStatsMacFcsErrPkts = _ApChStatsMacFcsErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 12),
    _ApChStatsMacFcsErrPkts_Type()
)
apChStatsMacFcsErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsMacFcsErrPkts.setStatus("current")
_ApChStatsMacMicErrPkts_Type = Counter32
_ApChStatsMacMicErrPkts_Object = MibTableColumn
apChStatsMacMicErrPkts = _ApChStatsMacMicErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 13),
    _ApChStatsMacMicErrPkts_Type()
)
apChStatsMacMicErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsMacMicErrPkts.setStatus("current")
_ApChStatsMacDecryptErrPkts_Type = Counter32
_ApChStatsMacDecryptErrPkts_Object = MibTableColumn
apChStatsMacDecryptErrPkts = _ApChStatsMacDecryptErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 14),
    _ApChStatsMacDecryptErrPkts_Type()
)
apChStatsMacDecryptErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsMacDecryptErrPkts.setStatus("current")
_ApChStatsTotalErrPkts_Type = Counter32
_ApChStatsTotalErrPkts_Object = MibTableColumn
apChStatsTotalErrPkts = _ApChStatsTotalErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 15),
    _ApChStatsTotalErrPkts_Type()
)
apChStatsTotalErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsTotalErrPkts.setStatus("current")
_ApRxMgmtFrameCnt_Type = Counter32
_ApRxMgmtFrameCnt_Object = MibTableColumn
apRxMgmtFrameCnt = _ApRxMgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 16),
    _ApRxMgmtFrameCnt_Type()
)
apRxMgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxMgmtFrameCnt.setStatus("current")
_ApRxCtrlFrameCnt_Type = Counter32
_ApRxCtrlFrameCnt_Object = MibTableColumn
apRxCtrlFrameCnt = _ApRxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 17),
    _ApRxCtrlFrameCnt_Type()
)
apRxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxCtrlFrameCnt.setStatus("current")
_ApRxDataFrameCnt_Type = Counter32
_ApRxDataFrameCnt_Object = MibTableColumn
apRxDataFrameCnt = _ApRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 18),
    _ApRxDataFrameCnt_Type()
)
apRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxDataFrameCnt.setStatus("current")
_ApTxMgmtFrameCnt_Type = Counter32
_ApTxMgmtFrameCnt_Object = MibTableColumn
apTxMgmtFrameCnt = _ApTxMgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 19),
    _ApTxMgmtFrameCnt_Type()
)
apTxMgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxMgmtFrameCnt.setStatus("current")
_ApTxCtrlFrameCnt_Type = Counter32
_ApTxCtrlFrameCnt_Object = MibTableColumn
apTxCtrlFrameCnt = _ApTxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 20),
    _ApTxCtrlFrameCnt_Type()
)
apTxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxCtrlFrameCnt.setStatus("current")
_ApTxDataFrameCnt_Type = Counter32
_ApTxDataFrameCnt_Object = MibTableColumn
apTxDataFrameCnt = _ApTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 21),
    _ApTxDataFrameCnt_Type()
)
apTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxDataFrameCnt.setStatus("current")
_ApChStatsFrameErrorCnt_Type = Counter32
_ApChStatsFrameErrorCnt_Object = MibTableColumn
apChStatsFrameErrorCnt = _ApChStatsFrameErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 22),
    _ApChStatsFrameErrorCnt_Type()
)
apChStatsFrameErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChStatsFrameErrorCnt.setStatus("current")
_ApRetryCnt_Type = Counter32
_ApRetryCnt_Object = MibTableColumn
apRetryCnt = _ApRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 23),
    _ApRetryCnt_Type()
)
apRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRetryCnt.setStatus("current")
_ApCurTxPwr_Type = Integer32
_ApCurTxPwr_Object = MibTableColumn
apCurTxPwr = _ApCurTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 24),
    _ApCurTxPwr_Type()
)
apCurTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurTxPwr.setStatus("current")
_ApAPNeighborSSIDList_Type = DisplayString
_ApAPNeighborSSIDList_Object = MibTableColumn
apAPNeighborSSIDList = _ApAPNeighborSSIDList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 25),
    _ApAPNeighborSSIDList_Type()
)
apAPNeighborSSIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPNeighborSSIDList.setStatus("current")
_ApChDownUnicastFrame_Type = Counter32
_ApChDownUnicastFrame_Object = MibTableColumn
apChDownUnicastFrame = _ApChDownUnicastFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 26),
    _ApChDownUnicastFrame_Type()
)
apChDownUnicastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChDownUnicastFrame.setStatus("current")
_ApChDownNonUnicastFrame_Type = Counter32
_ApChDownNonUnicastFrame_Object = MibTableColumn
apChDownNonUnicastFrame = _ApChDownNonUnicastFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 27),
    _ApChDownNonUnicastFrame_Type()
)
apChDownNonUnicastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChDownNonUnicastFrame.setStatus("current")
_ApChTxThroughput_Type = Counter32
_ApChTxThroughput_Object = MibTableColumn
apChTxThroughput = _ApChTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 28),
    _ApChTxThroughput_Type()
)
apChTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChTxThroughput.setStatus("current")
_ApChRxThroughput_Type = Counter32
_ApChRxThroughput_Object = MibTableColumn
apChRxThroughput = _ApChRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 29),
    _ApChRxThroughput_Type()
)
apChRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChRxThroughput.setStatus("current")
_ApChTxDropPkts_Type = Counter32
_ApChTxDropPkts_Object = MibTableColumn
apChTxDropPkts = _ApChTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 30),
    _ApChTxDropPkts_Type()
)
apChTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChTxDropPkts.setStatus("current")
_ApChRxDropPkts_Type = Counter32
_ApChRxDropPkts_Object = MibTableColumn
apChRxDropPkts = _ApChRxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 31),
    _ApChRxDropPkts_Type()
)
apChRxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChRxDropPkts.setStatus("current")
_ApChTxErrorPkts_Type = Counter32
_ApChTxErrorPkts_Object = MibTableColumn
apChTxErrorPkts = _ApChTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 32),
    _ApChTxErrorPkts_Type()
)
apChTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChTxErrorPkts.setStatus("current")
_ApChRxErrorPkts_Type = Counter32
_ApChRxErrorPkts_Object = MibTableColumn
apChRxErrorPkts = _ApChRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 33),
    _ApChRxErrorPkts_Type()
)
apChRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChRxErrorPkts.setStatus("current")
_ApRxBytes_Type = Counter32
_ApRxBytes_Object = MibTableColumn
apRxBytes = _ApRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 34),
    _ApRxBytes_Type()
)
apRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxBytes.setStatus("current")
_ApRxPkts_Type = Counter32
_ApRxPkts_Object = MibTableColumn
apRxPkts = _ApRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 35),
    _ApRxPkts_Type()
)
apRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRxPkts.setStatus("current")
_ApTxBytes_Type = Counter32
_ApTxBytes_Object = MibTableColumn
apTxBytes = _ApTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 36),
    _ApTxBytes_Type()
)
apTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxBytes.setStatus("current")
_ApTxPkts_Type = Counter32
_ApTxPkts_Object = MibTableColumn
apTxPkts = _ApTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 37),
    _ApTxPkts_Type()
)
apTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxPkts.setStatus("current")
_ApDownNonUnicastPkts_Type = Counter32
_ApDownNonUnicastPkts_Object = MibTableColumn
apDownNonUnicastPkts = _ApDownNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 38),
    _ApDownNonUnicastPkts_Type()
)
apDownNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDownNonUnicastPkts.setStatus("current")
_ApDownUnicastPkts_Type = Counter32
_ApDownUnicastPkts_Object = MibTableColumn
apDownUnicastPkts = _ApDownUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 39),
    _ApDownUnicastPkts_Type()
)
apDownUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDownUnicastPkts.setStatus("current")
_ApUpNonUnicastPkts_Type = Counter32
_ApUpNonUnicastPkts_Object = MibTableColumn
apUpNonUnicastPkts = _ApUpNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 40),
    _ApUpNonUnicastPkts_Type()
)
apUpNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUpNonUnicastPkts.setStatus("current")
_ApUpUnicastPkts_Type = Counter32
_ApUpUnicastPkts_Object = MibTableColumn
apUpUnicastPkts = _ApUpUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 41),
    _ApUpUnicastPkts_Type()
)
apUpUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUpUnicastPkts.setStatus("current")
_ApAssoFailUnknowReason_Type = Counter32
_ApAssoFailUnknowReason_Object = MibTableColumn
apAssoFailUnknowReason = _ApAssoFailUnknowReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 42),
    _ApAssoFailUnknowReason_Type()
)
apAssoFailUnknowReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssoFailUnknowReason.setStatus("current")
_ApAssoFailOutofDot11_Type = Counter32
_ApAssoFailOutofDot11_Object = MibTableColumn
apAssoFailOutofDot11 = _ApAssoFailOutofDot11_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 43),
    _ApAssoFailOutofDot11_Type()
)
apAssoFailOutofDot11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssoFailOutofDot11.setStatus("current")
_ApAssoTotalTime_Type = Counter32
_ApAssoTotalTime_Object = MibTableColumn
apAssoTotalTime = _ApAssoTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 44),
    _ApAssoTotalTime_Type()
)
apAssoTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssoTotalTime.setStatus("current")
_ApAuthReqFailTimes_Type = Counter32
_ApAuthReqFailTimes_Object = MibTableColumn
apAuthReqFailTimes = _ApAuthReqFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 45),
    _ApAuthReqFailTimes_Type()
)
apAuthReqFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthReqFailTimes.setStatus("current")
_ApAuthReqTimes_Type = Counter32
_ApAuthReqTimes_Object = MibTableColumn
apAuthReqTimes = _ApAuthReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 46),
    _ApAuthReqTimes_Type()
)
apAuthReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthReqTimes.setStatus("current")
_ApAuthSuccessTimes_Type = Counter32
_ApAuthSuccessTimes_Object = MibTableColumn
apAuthSuccessTimes = _ApAuthSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 47),
    _ApAuthSuccessTimes_Type()
)
apAuthSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthSuccessTimes.setStatus("current")
_ApReAssoFailTimes_Type = Counter32
_ApReAssoFailTimes_Object = MibTableColumn
apReAssoFailTimes = _ApReAssoFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 48),
    _ApReAssoFailTimes_Type()
)
apReAssoFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apReAssoFailTimes.setStatus("current")
_ApMacTxCorrectFrameCnt_Type = Counter32
_ApMacTxCorrectFrameCnt_Object = MibTableColumn
apMacTxCorrectFrameCnt = _ApMacTxCorrectFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 49),
    _ApMacTxCorrectFrameCnt_Type()
)
apMacTxCorrectFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMacTxCorrectFrameCnt.setStatus("current")
_ApMacRxCorrectFrameCnt_Type = Counter32
_ApMacRxCorrectFrameCnt_Object = MibTableColumn
apMacRxCorrectFrameCnt = _ApMacRxCorrectFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 50),
    _ApMacRxCorrectFrameCnt_Type()
)
apMacRxCorrectFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMacRxCorrectFrameCnt.setStatus("current")
_ApPktErrRate_Type = Integer32
_ApPktErrRate_Object = MibTableColumn
apPktErrRate = _ApPktErrRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 51),
    _ApPktErrRate_Type()
)
apPktErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPktErrRate.setStatus("current")
_ApTotalRxBytes_Type = Counter64
_ApTotalRxBytes_Object = MibTableColumn
apTotalRxBytes = _ApTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 52),
    _ApTotalRxBytes_Type()
)
apTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalRxBytes.setStatus("current")
_ApTotalTxBytes_Type = Counter64
_ApTotalTxBytes_Object = MibTableColumn
apTotalTxBytes = _ApTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 53),
    _ApTotalTxBytes_Type()
)
apTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalTxBytes.setStatus("current")
_ApTxErrorPkts_Type = Counter32
_ApTxErrorPkts_Object = MibTableColumn
apTxErrorPkts = _ApTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 54),
    _ApTxErrorPkts_Type()
)
apTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxErrorPkts.setStatus("current")
_ApTxDropPkts_Type = Counter32
_ApTxDropPkts_Object = MibTableColumn
apTxDropPkts = _ApTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 55),
    _ApTxDropPkts_Type()
)
apTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxDropPkts.setStatus("current")
_ApIfRadiusOnlineUserNum_Type = Counter32
_ApIfRadiusOnlineUserNum_Object = MibTableColumn
apIfRadiusOnlineUserNum = _ApIfRadiusOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 4, 1, 1, 56),
    _ApIfRadiusOnlineUserNum_Type()
)
apIfRadiusOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfRadiusOnlineUserNum.setStatus("current")
_ApSSIDStatisticsObjects_ObjectIdentity = ObjectIdentity
apSSIDStatisticsObjects = _ApSSIDStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5)
)
_ApSSIDStatisticsTable_Object = MibTable
apSSIDStatisticsTable = _ApSSIDStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1)
)
if mibBuilder.loadTexts:
    apSSIDStatisticsTable.setStatus("current")
_ApSSIDStatisticsTableEntry_Object = MibTableRow
apSSIDStatisticsTableEntry = _ApSSIDStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1)
)
apSSIDStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsAPMac"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsRadioId"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsWlanId"),
)
if mibBuilder.loadTexts:
    apSSIDStatisticsTableEntry.setStatus("current")
_ApSSIDStatisticsAPMac_Type = MacAddress
_ApSSIDStatisticsAPMac_Object = MibTableColumn
apSSIDStatisticsAPMac = _ApSSIDStatisticsAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 1),
    _ApSSIDStatisticsAPMac_Type()
)
apSSIDStatisticsAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsAPMac.setStatus("current")
_ApSSIDStatisticsRadioId_Type = Integer32
_ApSSIDStatisticsRadioId_Object = MibTableColumn
apSSIDStatisticsRadioId = _ApSSIDStatisticsRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 2),
    _ApSSIDStatisticsRadioId_Type()
)
apSSIDStatisticsRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsRadioId.setStatus("current")
_ApSSIDStatisticsWlanId_Type = Integer32
_ApSSIDStatisticsWlanId_Object = MibTableColumn
apSSIDStatisticsWlanId = _ApSSIDStatisticsWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 3),
    _ApSSIDStatisticsWlanId_Type()
)
apSSIDStatisticsWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsWlanId.setStatus("current")
_ApSSIDTxDataPkts_Type = Counter32
_ApSSIDTxDataPkts_Object = MibTableColumn
apSSIDTxDataPkts = _ApSSIDTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 4),
    _ApSSIDTxDataPkts_Type()
)
apSSIDTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDTxDataPkts.setStatus("current")
_ApSSIDRxDataPkts_Type = Counter32
_ApSSIDRxDataPkts_Object = MibTableColumn
apSSIDRxDataPkts = _ApSSIDRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 5),
    _ApSSIDRxDataPkts_Type()
)
apSSIDRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDRxDataPkts.setStatus("current")
_ApSSIDUplinkDataOctets_Type = Counter64
_ApSSIDUplinkDataOctets_Object = MibTableColumn
apSSIDUplinkDataOctets = _ApSSIDUplinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 6),
    _ApSSIDUplinkDataOctets_Type()
)
apSSIDUplinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDUplinkDataOctets.setStatus("current")
_ApSSIDDwlinkDataOctets_Type = Counter64
_ApSSIDDwlinkDataOctets_Object = MibTableColumn
apSSIDDwlinkDataOctets = _ApSSIDDwlinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 7),
    _ApSSIDDwlinkDataOctets_Type()
)
apSSIDDwlinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDDwlinkDataOctets.setStatus("current")
_ApSSIDChStatsDwlinkTotRetryPkts_Type = Counter32
_ApSSIDChStatsDwlinkTotRetryPkts_Object = MibTableColumn
apSSIDChStatsDwlinkTotRetryPkts = _ApSSIDChStatsDwlinkTotRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 8),
    _ApSSIDChStatsDwlinkTotRetryPkts_Type()
)
apSSIDChStatsDwlinkTotRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDChStatsDwlinkTotRetryPkts.setStatus("current")
_ApSSIDApChStatsNumStations_Type = Integer32
_ApSSIDApChStatsNumStations_Object = MibTableColumn
apSSIDApChStatsNumStations = _ApSSIDApChStatsNumStations_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 9),
    _ApSSIDApChStatsNumStations_Type()
)
apSSIDApChStatsNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDApChStatsNumStations.setStatus("current")
_ApApChStatsOnlineSum_Type = Integer32
_ApApChStatsOnlineSum_Object = MibTableColumn
apApChStatsOnlineSum = _ApApChStatsOnlineSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 10),
    _ApApChStatsOnlineSum_Type()
)
apApChStatsOnlineSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApChStatsOnlineSum.setStatus("current")
_ApSSIDStatisticsName_Type = DisplayString
_ApSSIDStatisticsName_Object = MibTableColumn
apSSIDStatisticsName = _ApSSIDStatisticsName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 11),
    _ApSSIDStatisticsName_Type()
)
apSSIDStatisticsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsName.setStatus("current")
_ApSSIDMacTxPkts_Type = Counter32
_ApSSIDMacTxPkts_Object = MibTableColumn
apSSIDMacTxPkts = _ApSSIDMacTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 12),
    _ApSSIDMacTxPkts_Type()
)
apSSIDMacTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDMacTxPkts.setStatus("current")
_ApSSIDMacRxPkts_Type = Counter32
_ApSSIDMacRxPkts_Object = MibTableColumn
apSSIDMacRxPkts = _ApSSIDMacRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 1, 1, 13),
    _ApSSIDMacRxPkts_Type()
)
apSSIDMacRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDMacRxPkts.setStatus("current")
_ApSSIDStatisticsNewTable_Object = MibTable
apSSIDStatisticsNewTable = _ApSSIDStatisticsNewTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2)
)
if mibBuilder.loadTexts:
    apSSIDStatisticsNewTable.setStatus("current")
_ApSSIDStatisticsNewTableEntry_Object = MibTableRow
apSSIDStatisticsNewTableEntry = _ApSSIDStatisticsNewTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1)
)
apSSIDStatisticsNewTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsNewAPMac"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsNewRadioId"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsNewSSID"),
)
if mibBuilder.loadTexts:
    apSSIDStatisticsNewTableEntry.setStatus("current")
_ApSSIDStatisticsNewAPMac_Type = MacAddress
_ApSSIDStatisticsNewAPMac_Object = MibTableColumn
apSSIDStatisticsNewAPMac = _ApSSIDStatisticsNewAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 1),
    _ApSSIDStatisticsNewAPMac_Type()
)
apSSIDStatisticsNewAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsNewAPMac.setStatus("current")
_ApSSIDStatisticsNewRadioId_Type = Integer32
_ApSSIDStatisticsNewRadioId_Object = MibTableColumn
apSSIDStatisticsNewRadioId = _ApSSIDStatisticsNewRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 2),
    _ApSSIDStatisticsNewRadioId_Type()
)
apSSIDStatisticsNewRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsNewRadioId.setStatus("current")
_ApSSIDStatisticsNewSSID_Type = DisplayString
_ApSSIDStatisticsNewSSID_Object = MibTableColumn
apSSIDStatisticsNewSSID = _ApSSIDStatisticsNewSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 3),
    _ApSSIDStatisticsNewSSID_Type()
)
apSSIDStatisticsNewSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsNewSSID.setStatus("current")
_ApSSIDNewTxDataPkts_Type = Counter32
_ApSSIDNewTxDataPkts_Object = MibTableColumn
apSSIDNewTxDataPkts = _ApSSIDNewTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 4),
    _ApSSIDNewTxDataPkts_Type()
)
apSSIDNewTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDNewTxDataPkts.setStatus("current")
_ApSSIDNewRxDataPkts_Type = Counter32
_ApSSIDNewRxDataPkts_Object = MibTableColumn
apSSIDNewRxDataPkts = _ApSSIDNewRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 5),
    _ApSSIDNewRxDataPkts_Type()
)
apSSIDNewRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDNewRxDataPkts.setStatus("current")
_ApSSIDNewUplinkDataOctets_Type = Counter64
_ApSSIDNewUplinkDataOctets_Object = MibTableColumn
apSSIDNewUplinkDataOctets = _ApSSIDNewUplinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 6),
    _ApSSIDNewUplinkDataOctets_Type()
)
apSSIDNewUplinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDNewUplinkDataOctets.setStatus("current")
_ApSSIDNewDwlinkDataOctets_Type = Counter64
_ApSSIDNewDwlinkDataOctets_Object = MibTableColumn
apSSIDNewDwlinkDataOctets = _ApSSIDNewDwlinkDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 7),
    _ApSSIDNewDwlinkDataOctets_Type()
)
apSSIDNewDwlinkDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDNewDwlinkDataOctets.setStatus("current")
_ApSSIDNewChStatsDwlinkTotRetryPkts_Type = Counter32
_ApSSIDNewChStatsDwlinkTotRetryPkts_Object = MibTableColumn
apSSIDNewChStatsDwlinkTotRetryPkts = _ApSSIDNewChStatsDwlinkTotRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 8),
    _ApSSIDNewChStatsDwlinkTotRetryPkts_Type()
)
apSSIDNewChStatsDwlinkTotRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDNewChStatsDwlinkTotRetryPkts.setStatus("current")
_ApSSIDNewApChStatsNumStations_Type = Integer32
_ApSSIDNewApChStatsNumStations_Object = MibTableColumn
apSSIDNewApChStatsNumStations = _ApSSIDNewApChStatsNumStations_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 9),
    _ApSSIDNewApChStatsNumStations_Type()
)
apSSIDNewApChStatsNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDNewApChStatsNumStations.setStatus("current")
_ApApNewChStatsOnlineSum_Type = Integer32
_ApApNewChStatsOnlineSum_Object = MibTableColumn
apApNewChStatsOnlineSum = _ApApNewChStatsOnlineSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 10),
    _ApApNewChStatsOnlineSum_Type()
)
apApNewChStatsOnlineSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApNewChStatsOnlineSum.setStatus("current")
_ApSSIDNewMacTxPkts_Type = Counter32
_ApSSIDNewMacTxPkts_Object = MibTableColumn
apSSIDNewMacTxPkts = _ApSSIDNewMacTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 11),
    _ApSSIDNewMacTxPkts_Type()
)
apSSIDNewMacTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDNewMacTxPkts.setStatus("current")
_ApSSIDNewMacRxPkts_Type = Counter32
_ApSSIDNewMacRxPkts_Object = MibTableColumn
apSSIDNewMacRxPkts = _ApSSIDNewMacRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 2, 1, 12),
    _ApSSIDNewMacRxPkts_Type()
)
apSSIDNewMacRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDNewMacRxPkts.setStatus("current")
_ApSSIDStatisticsOptimizationTable_Object = MibTable
apSSIDStatisticsOptimizationTable = _ApSSIDStatisticsOptimizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 3)
)
if mibBuilder.loadTexts:
    apSSIDStatisticsOptimizationTable.setStatus("current")
_ApSSIDStatisticsOptimizationTableEntry_Object = MibTableRow
apSSIDStatisticsOptimizationTableEntry = _ApSSIDStatisticsOptimizationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 3, 1)
)
apSSIDStatisticsOptimizationTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsOptimizationAPMac"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsOptimizationRadioId"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDStatisticsOptimizationSSID"),
)
if mibBuilder.loadTexts:
    apSSIDStatisticsOptimizationTableEntry.setStatus("current")
_ApSSIDStatisticsOptimizationAPMac_Type = MacAddress
_ApSSIDStatisticsOptimizationAPMac_Object = MibTableColumn
apSSIDStatisticsOptimizationAPMac = _ApSSIDStatisticsOptimizationAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 3, 1, 1),
    _ApSSIDStatisticsOptimizationAPMac_Type()
)
apSSIDStatisticsOptimizationAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsOptimizationAPMac.setStatus("current")
_ApSSIDStatisticsOptimizationRadioId_Type = Integer32
_ApSSIDStatisticsOptimizationRadioId_Object = MibTableColumn
apSSIDStatisticsOptimizationRadioId = _ApSSIDStatisticsOptimizationRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 3, 1, 2),
    _ApSSIDStatisticsOptimizationRadioId_Type()
)
apSSIDStatisticsOptimizationRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsOptimizationRadioId.setStatus("current")
_ApSSIDStatisticsOptimizationSSID_Type = DisplayString
_ApSSIDStatisticsOptimizationSSID_Object = MibTableColumn
apSSIDStatisticsOptimizationSSID = _ApSSIDStatisticsOptimizationSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 3, 1, 3),
    _ApSSIDStatisticsOptimizationSSID_Type()
)
apSSIDStatisticsOptimizationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsOptimizationSSID.setStatus("current")


class _ApSSIDStatisticsOptimizationinfo_Type(OctetString):
    """Custom type apSSIDStatisticsOptimizationinfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_ApSSIDStatisticsOptimizationinfo_Type.__name__ = "OctetString"
_ApSSIDStatisticsOptimizationinfo_Object = MibTableColumn
apSSIDStatisticsOptimizationinfo = _ApSSIDStatisticsOptimizationinfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 5, 3, 1, 4),
    _ApSSIDStatisticsOptimizationinfo_Type()
)
apSSIDStatisticsOptimizationinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDStatisticsOptimizationinfo.setStatus("current")
_ApWAPIStatisticsObjects_ObjectIdentity = ObjectIdentity
apWAPIStatisticsObjects = _ApWAPIStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6)
)
_ApWAPIStatisticsTable_Object = MibTable
apWAPIStatisticsTable = _ApWAPIStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1)
)
if mibBuilder.loadTexts:
    apWAPIStatisticsTable.setStatus("current")
_ApWAPIStatisticsTableEntry_Object = MibTableRow
apWAPIStatisticsTableEntry = _ApWAPIStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1)
)
apWAPIStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apWAPIStatisticsTableEntry.setStatus("current")
_ApWAPIControlledPortStatus_Type = TruthValue
_ApWAPIControlledPortStatus_Object = MibTableColumn
apWAPIControlledPortStatus = _ApWAPIControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 1),
    _ApWAPIControlledPortStatus_Type()
)
apWAPIControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIControlledPortStatus.setStatus("current")
_ApWAPISelectedUnicastCipher_Type = OctetString
_ApWAPISelectedUnicastCipher_Object = MibTableColumn
apWAPISelectedUnicastCipher = _ApWAPISelectedUnicastCipher_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 2),
    _ApWAPISelectedUnicastCipher_Type()
)
apWAPISelectedUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPISelectedUnicastCipher.setStatus("current")
_ApWPIReplayCounters_Type = Counter32
_ApWPIReplayCounters_Object = MibTableColumn
apWPIReplayCounters = _ApWPIReplayCounters_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 3),
    _ApWPIReplayCounters_Type()
)
apWPIReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWPIReplayCounters.setStatus("current")
_ApWPIDecryptableErrors_Type = Counter32
_ApWPIDecryptableErrors_Object = MibTableColumn
apWPIDecryptableErrors = _ApWPIDecryptableErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 4),
    _ApWPIDecryptableErrors_Type()
)
apWPIDecryptableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWPIDecryptableErrors.setStatus("current")
_ApWPIMICErrors_Type = Counter32
_ApWPIMICErrors_Object = MibTableColumn
apWPIMICErrors = _ApWPIMICErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 5),
    _ApWPIMICErrors_Type()
)
apWPIMICErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWPIMICErrors.setStatus("current")
_ApWAISignatureErrors_Type = Counter32
_ApWAISignatureErrors_Object = MibTableColumn
apWAISignatureErrors = _ApWAISignatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 6),
    _ApWAISignatureErrors_Type()
)
apWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAISignatureErrors.setStatus("current")
_ApWAIHMACErrors_Type = Counter32
_ApWAIHMACErrors_Object = MibTableColumn
apWAIHMACErrors = _ApWAIHMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 7),
    _ApWAIHMACErrors_Type()
)
apWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIHMACErrors.setStatus("current")
_ApWAIAuthResultFailures_Type = Counter32
_ApWAIAuthResultFailures_Object = MibTableColumn
apWAIAuthResultFailures = _ApWAIAuthResultFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 8),
    _ApWAIAuthResultFailures_Type()
)
apWAIAuthResultFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIAuthResultFailures.setStatus("current")
_ApWAIDiscardCounters_Type = Counter32
_ApWAIDiscardCounters_Object = MibTableColumn
apWAIDiscardCounters = _ApWAIDiscardCounters_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 9),
    _ApWAIDiscardCounters_Type()
)
apWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIDiscardCounters.setStatus("current")
_ApWAITimeoutCounters_Type = Counter32
_ApWAITimeoutCounters_Object = MibTableColumn
apWAITimeoutCounters = _ApWAITimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 10),
    _ApWAITimeoutCounters_Type()
)
apWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAITimeoutCounters.setStatus("current")
_ApWAIFormatErrors_Type = Counter32
_ApWAIFormatErrors_Object = MibTableColumn
apWAIFormatErrors = _ApWAIFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 11),
    _ApWAIFormatErrors_Type()
)
apWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIFormatErrors.setStatus("current")
_ApWAICertificateHandshakeFailures_Type = Counter32
_ApWAICertificateHandshakeFailures_Object = MibTableColumn
apWAICertificateHandshakeFailures = _ApWAICertificateHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 12),
    _ApWAICertificateHandshakeFailures_Type()
)
apWAICertificateHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAICertificateHandshakeFailures.setStatus("current")
_ApWAIUnicastHandshakeFailures_Type = Counter32
_ApWAIUnicastHandshakeFailures_Object = MibTableColumn
apWAIUnicastHandshakeFailures = _ApWAIUnicastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 13),
    _ApWAIUnicastHandshakeFailures_Type()
)
apWAIUnicastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIUnicastHandshakeFailures.setStatus("current")
_ApWAIMulticastHandshakeFailures_Type = Counter32
_ApWAIMulticastHandshakeFailures_Object = MibTableColumn
apWAIMulticastHandshakeFailures = _ApWAIMulticastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 6, 1, 1, 14),
    _ApWAIMulticastHandshakeFailures_Type()
)
apWAIMulticastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAIMulticastHandshakeFailures.setStatus("current")
_ApStationStatisticsObjects_ObjectIdentity = ObjectIdentity
apStationStatisticsObjects = _ApStationStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7)
)
_ApStationStatisticsTable_Object = MibTable
apStationStatisticsTable = _ApStationStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1)
)
if mibBuilder.loadTexts:
    apStationStatisticsTable.setStatus("current")
_ApStationStatisticsTableEntry_Object = MibTableRow
apStationStatisticsTableEntry = _ApStationStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1)
)
apStationStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieStaMacAddr"),
)
if mibBuilder.loadTexts:
    apStationStatisticsTableEntry.setStatus("current")
_ApStaAddress_Type = MacAddress
_ApStaAddress_Object = MibTableColumn
apStaAddress = _ApStaAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 1),
    _ApStaAddress_Type()
)
apStaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaAddress.setStatus("current")
_ApStaUpTime_Type = TimeTicks
_ApStaUpTime_Object = MibTableColumn
apStaUpTime = _ApStaUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 2),
    _ApStaUpTime_Type()
)
apStaUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUpTime.setStatus("current")
_ApReceivedStaSignalStrength_Type = DisplayString
_ApReceivedStaSignalStrength_Object = MibTableColumn
apReceivedStaSignalStrength = _ApReceivedStaSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 3),
    _ApReceivedStaSignalStrength_Type()
)
apReceivedStaSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apReceivedStaSignalStrength.setStatus("current")
_ApAPReceiveStaSNR_Type = DisplayString
_ApAPReceiveStaSNR_Object = MibTableColumn
apAPReceiveStaSNR = _ApAPReceiveStaSNR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 4),
    _ApAPReceiveStaSNR_Type()
)
apAPReceiveStaSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPReceiveStaSNR.setStatus("current")
_ApStaTxPkts_Type = Counter32
_ApStaTxPkts_Object = MibTableColumn
apStaTxPkts = _ApStaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 5),
    _ApStaTxPkts_Type()
)
apStaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaTxPkts.setStatus("current")
_ApStaTxBytes_Type = Counter64
_ApStaTxBytes_Object = MibTableColumn
apStaTxBytes = _ApStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 6),
    _ApStaTxBytes_Type()
)
apStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaTxBytes.setStatus("current")
_ApStaRxPkts_Type = Counter32
_ApStaRxPkts_Object = MibTableColumn
apStaRxPkts = _ApStaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 7),
    _ApStaRxPkts_Type()
)
apStaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRxPkts.setStatus("current")
_ApStaRxBytes_Type = Counter64
_ApStaRxBytes_Object = MibTableColumn
apStaRxBytes = _ApStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 8),
    _ApStaRxBytes_Type()
)
apStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRxBytes.setStatus("current")
_ApWAPISTAAddress_Type = MacAddress
_ApWAPISTAAddress_Object = MibTableColumn
apWAPISTAAddress = _ApWAPISTAAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 9),
    _ApWAPISTAAddress_Type()
)
apWAPISTAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPISTAAddress.setStatus("current")
_ApWAPIVersion_Type = Integer32
_ApWAPIVersion_Object = MibTableColumn
apWAPIVersion = _ApWAPIVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 10),
    _ApWAPIVersion_Type()
)
apWAPIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWAPIVersion.setStatus("current")
_ApStaLinkSpeed_Type = Integer32
_ApStaLinkSpeed_Object = MibTableColumn
apStaLinkSpeed = _ApStaLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 11),
    _ApStaLinkSpeed_Type()
)
apStaLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaLinkSpeed.setStatus("current")
_ApStaUpRate_Type = Integer32
_ApStaUpRate_Object = MibTableColumn
apStaUpRate = _ApStaUpRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 12),
    _ApStaUpRate_Type()
)
apStaUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUpRate.setStatus("current")
_ApStaDownRate_Type = Integer32
_ApStaDownRate_Object = MibTableColumn
apStaDownRate = _ApStaDownRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 13),
    _ApStaDownRate_Type()
)
apStaDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownRate.setStatus("current")
_ApStaTxThroughput_Type = Counter32
_ApStaTxThroughput_Object = MibTableColumn
apStaTxThroughput = _ApStaTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 14),
    _ApStaTxThroughput_Type()
)
apStaTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaTxThroughput.setStatus("current")
_ApStaRxThroughput_Type = Counter32
_ApStaRxThroughput_Object = MibTableColumn
apStaRxThroughput = _ApStaRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 15),
    _ApStaRxThroughput_Type()
)
apStaRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRxThroughput.setStatus("current")
_ApStaRxRetryBytes_Type = Counter64
_ApStaRxRetryBytes_Object = MibTableColumn
apStaRxRetryBytes = _ApStaRxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 7, 1, 1, 16),
    _ApStaRxRetryBytes_Type()
)
apStaRxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRxRetryBytes.setStatus("current")
_ApQOSStatisticsObjects_ObjectIdentity = ObjectIdentity
apQOSStatisticsObjects = _ApQOSStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8)
)
_ApQOSBaseStatisticsObjects_ObjectIdentity = ObjectIdentity
apQOSBaseStatisticsObjects = _ApQOSBaseStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 1)
)
_ApQOSBaseStatisticsTable_Object = MibTable
apQOSBaseStatisticsTable = _ApQOSBaseStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 1, 1)
)
if mibBuilder.loadTexts:
    apQOSBaseStatisticsTable.setStatus("current")
_ApQOSBaseStatisticsTableEntry_Object = MibTableRow
apQOSBaseStatisticsTableEntry = _ApQOSBaseStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 1, 1, 1)
)
apQOSBaseStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSBaseStatisticsTableEntry.setStatus("current")
_ApBaseQoSSvcQueAvgLen_Type = Integer32
_ApBaseQoSSvcQueAvgLen_Object = MibTableColumn
apBaseQoSSvcQueAvgLen = _ApBaseQoSSvcQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 1, 1, 1, 1),
    _ApBaseQoSSvcQueAvgLen_Type()
)
apBaseQoSSvcQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBaseQoSSvcQueAvgLen.setStatus("current")
_ApBaseQoSSvcPktLossRatio_Type = Integer32
_ApBaseQoSSvcPktLossRatio_Object = MibTableColumn
apBaseQoSSvcPktLossRatio = _ApBaseQoSSvcPktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 1, 1, 1, 2),
    _ApBaseQoSSvcPktLossRatio_Type()
)
apBaseQoSSvcPktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBaseQoSSvcPktLossRatio.setStatus("current")
_ApBaseAvgTransSpeed_Type = Integer32
_ApBaseAvgTransSpeed_Object = MibTableColumn
apBaseAvgTransSpeed = _ApBaseAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 1, 1, 1, 3),
    _ApBaseAvgTransSpeed_Type()
)
apBaseAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBaseAvgTransSpeed.setStatus("current")
_ApQOSBackgroundStatisticsObjects_ObjectIdentity = ObjectIdentity
apQOSBackgroundStatisticsObjects = _ApQOSBackgroundStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 2)
)
_ApQOSBackgroundStatisticsTable_Object = MibTable
apQOSBackgroundStatisticsTable = _ApQOSBackgroundStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 2, 1)
)
if mibBuilder.loadTexts:
    apQOSBackgroundStatisticsTable.setStatus("current")
_ApQOSBackgroundStatisticsTableEntry_Object = MibTableRow
apQOSBackgroundStatisticsTableEntry = _ApQOSBackgroundStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 2, 1, 1)
)
apQOSBackgroundStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSBackgroundStatisticsTableEntry.setStatus("current")
_ApQOSBgQueAvgLen_Type = Integer32
_ApQOSBgQueAvgLen_Object = MibTableColumn
apQOSBgQueAvgLen = _ApQOSBgQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 2, 1, 1, 1),
    _ApQOSBgQueAvgLen_Type()
)
apQOSBgQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBgQueAvgLen.setStatus("current")
_ApQOSBgAvgBurst_Type = Integer32
_ApQOSBgAvgBurst_Object = MibTableColumn
apQOSBgAvgBurst = _ApQOSBgAvgBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 2, 1, 1, 2),
    _ApQOSBgAvgBurst_Type()
)
apQOSBgAvgBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBgAvgBurst.setStatus("current")
_ApQOSBgPktLossRatio_Type = Integer32
_ApQOSBgPktLossRatio_Object = MibTableColumn
apQOSBgPktLossRatio = _ApQOSBgPktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 2, 1, 1, 3),
    _ApQOSBgPktLossRatio_Type()
)
apQOSBgPktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBgPktLossRatio.setStatus("current")
_ApQOSBgAvgTransSpeed_Type = Integer32
_ApQOSBgAvgTransSpeed_Object = MibTableColumn
apQOSBgAvgTransSpeed = _ApQOSBgAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 2, 1, 1, 4),
    _ApQOSBgAvgTransSpeed_Type()
)
apQOSBgAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBgAvgTransSpeed.setStatus("current")
_ApQOSBgSvcLoss_Type = Integer32
_ApQOSBgSvcLoss_Object = MibTableColumn
apQOSBgSvcLoss = _ApQOSBgSvcLoss_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 2, 1, 1, 5),
    _ApQOSBgSvcLoss_Type()
)
apQOSBgSvcLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBgSvcLoss.setStatus("current")
_ApQOSBestEffortStatisticsObjects_ObjectIdentity = ObjectIdentity
apQOSBestEffortStatisticsObjects = _ApQOSBestEffortStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 3)
)
_ApQOSBestEffortStatisticsTable_Object = MibTable
apQOSBestEffortStatisticsTable = _ApQOSBestEffortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 3, 1)
)
if mibBuilder.loadTexts:
    apQOSBestEffortStatisticsTable.setStatus("current")
_ApQOSBestEffortStatisticsTableEntry_Object = MibTableRow
apQOSBestEffortStatisticsTableEntry = _ApQOSBestEffortStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 3, 1, 1)
)
apQOSBestEffortStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSBestEffortStatisticsTableEntry.setStatus("current")
_ApQOSBeQueAvgLen_Type = Integer32
_ApQOSBeQueAvgLen_Object = MibTableColumn
apQOSBeQueAvgLen = _ApQOSBeQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 3, 1, 1, 1),
    _ApQOSBeQueAvgLen_Type()
)
apQOSBeQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBeQueAvgLen.setStatus("current")
_ApQOSBeAvgBurst_Type = Integer32
_ApQOSBeAvgBurst_Object = MibTableColumn
apQOSBeAvgBurst = _ApQOSBeAvgBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 3, 1, 1, 2),
    _ApQOSBeAvgBurst_Type()
)
apQOSBeAvgBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBeAvgBurst.setStatus("current")
_ApQOSBePktLossRatio_Type = Integer32
_ApQOSBePktLossRatio_Object = MibTableColumn
apQOSBePktLossRatio = _ApQOSBePktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 3, 1, 1, 3),
    _ApQOSBePktLossRatio_Type()
)
apQOSBePktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBePktLossRatio.setStatus("current")
_ApQOSBeAvgTransSpeed_Type = Integer32
_ApQOSBeAvgTransSpeed_Object = MibTableColumn
apQOSBeAvgTransSpeed = _ApQOSBeAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 3, 1, 1, 4),
    _ApQOSBeAvgTransSpeed_Type()
)
apQOSBeAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBeAvgTransSpeed.setStatus("current")
_ApQOSBeSvcLoss_Type = Integer32
_ApQOSBeSvcLoss_Object = MibTableColumn
apQOSBeSvcLoss = _ApQOSBeSvcLoss_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 3, 1, 1, 5),
    _ApQOSBeSvcLoss_Type()
)
apQOSBeSvcLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSBeSvcLoss.setStatus("current")
_ApQOSVoiceStatisticsObjects_ObjectIdentity = ObjectIdentity
apQOSVoiceStatisticsObjects = _ApQOSVoiceStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4)
)
_ApQOSVoiceStatisticsTable_Object = MibTable
apQOSVoiceStatisticsTable = _ApQOSVoiceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1)
)
if mibBuilder.loadTexts:
    apQOSVoiceStatisticsTable.setStatus("current")
_ApQOSVoiceStatisticsTableEntry_Object = MibTableRow
apQOSVoiceStatisticsTableEntry = _ApQOSVoiceStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1)
)
apQOSVoiceStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSVoiceStatisticsTableEntry.setStatus("current")
_ApQOSVoiceQueAvgLen_Type = Integer32
_ApQOSVoiceQueAvgLen_Object = MibTableColumn
apQOSVoiceQueAvgLen = _ApQOSVoiceQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1, 1),
    _ApQOSVoiceQueAvgLen_Type()
)
apQOSVoiceQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVoiceQueAvgLen.setStatus("current")
_ApQOSVoiceAvgBurst_Type = Integer32
_ApQOSVoiceAvgBurst_Object = MibTableColumn
apQOSVoiceAvgBurst = _ApQOSVoiceAvgBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1, 2),
    _ApQOSVoiceAvgBurst_Type()
)
apQOSVoiceAvgBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVoiceAvgBurst.setStatus("current")
_ApQOSVoicePktLossRatio_Type = Integer32
_ApQOSVoicePktLossRatio_Object = MibTableColumn
apQOSVoicePktLossRatio = _ApQOSVoicePktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1, 3),
    _ApQOSVoicePktLossRatio_Type()
)
apQOSVoicePktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVoicePktLossRatio.setStatus("current")
_ApQOSVoiceAvgTransSpeed_Type = Integer32
_ApQOSVoiceAvgTransSpeed_Object = MibTableColumn
apQOSVoiceAvgTransSpeed = _ApQOSVoiceAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1, 4),
    _ApQOSVoiceAvgTransSpeed_Type()
)
apQOSVoiceAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVoiceAvgTransSpeed.setStatus("current")
_ApQOSVoicePutThroughRatio_Type = Integer32
_ApQOSVoicePutThroughRatio_Object = MibTableColumn
apQOSVoicePutThroughRatio = _ApQOSVoicePutThroughRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1, 5),
    _ApQOSVoicePutThroughRatio_Type()
)
apQOSVoicePutThroughRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVoicePutThroughRatio.setStatus("current")
_ApQOSVoiceDropRatio_Type = Integer32
_ApQOSVoiceDropRatio_Object = MibTableColumn
apQOSVoiceDropRatio = _ApQOSVoiceDropRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1, 6),
    _ApQOSVoiceDropRatio_Type()
)
apQOSVoiceDropRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVoiceDropRatio.setStatus("current")
_ApQOSVoiceSvcLoss_Type = Integer32
_ApQOSVoiceSvcLoss_Object = MibTableColumn
apQOSVoiceSvcLoss = _ApQOSVoiceSvcLoss_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1, 7),
    _ApQOSVoiceSvcLoss_Type()
)
apQOSVoiceSvcLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVoiceSvcLoss.setStatus("current")
_ApQOSVoiceExceedMaxUsersRequest_Type = Counter32
_ApQOSVoiceExceedMaxUsersRequest_Object = MibTableColumn
apQOSVoiceExceedMaxUsersRequest = _ApQOSVoiceExceedMaxUsersRequest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 4, 1, 1, 8),
    _ApQOSVoiceExceedMaxUsersRequest_Type()
)
apQOSVoiceExceedMaxUsersRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVoiceExceedMaxUsersRequest.setStatus("current")
_ApQOSVideoStatisticsObjects_ObjectIdentity = ObjectIdentity
apQOSVideoStatisticsObjects = _ApQOSVideoStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5)
)
_ApQOSVideoStatisticsTable_Object = MibTable
apQOSVideoStatisticsTable = _ApQOSVideoStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1)
)
if mibBuilder.loadTexts:
    apQOSVideoStatisticsTable.setStatus("current")
_ApQOSVideoStatisticsTableEntry_Object = MibTableRow
apQOSVideoStatisticsTableEntry = _ApQOSVideoStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1)
)
apQOSVideoStatisticsTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    apQOSVideoStatisticsTableEntry.setStatus("current")
_ApQOSVideoQueAvgLen_Type = Integer32
_ApQOSVideoQueAvgLen_Object = MibTableColumn
apQOSVideoQueAvgLen = _ApQOSVideoQueAvgLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1, 1),
    _ApQOSVideoQueAvgLen_Type()
)
apQOSVideoQueAvgLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVideoQueAvgLen.setStatus("current")
_ApQOSVideoAvgBurst_Type = Integer32
_ApQOSVideoAvgBurst_Object = MibTableColumn
apQOSVideoAvgBurst = _ApQOSVideoAvgBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1, 2),
    _ApQOSVideoAvgBurst_Type()
)
apQOSVideoAvgBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVideoAvgBurst.setStatus("current")
_ApQOSVideoPktLossRatio_Type = Integer32
_ApQOSVideoPktLossRatio_Object = MibTableColumn
apQOSVideoPktLossRatio = _ApQOSVideoPktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1, 3),
    _ApQOSVideoPktLossRatio_Type()
)
apQOSVideoPktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVideoPktLossRatio.setStatus("current")
_ApQOSVideoAvgTransSpeed_Type = Integer32
_ApQOSVideoAvgTransSpeed_Object = MibTableColumn
apQOSVideoAvgTransSpeed = _ApQOSVideoAvgTransSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1, 4),
    _ApQOSVideoAvgTransSpeed_Type()
)
apQOSVideoAvgTransSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVideoAvgTransSpeed.setStatus("current")
_ApQOSVideoPutThroughRatio_Type = Integer32
_ApQOSVideoPutThroughRatio_Object = MibTableColumn
apQOSVideoPutThroughRatio = _ApQOSVideoPutThroughRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1, 5),
    _ApQOSVideoPutThroughRatio_Type()
)
apQOSVideoPutThroughRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVideoPutThroughRatio.setStatus("current")
_ApQOSVideoDropRatio_Type = Integer32
_ApQOSVideoDropRatio_Object = MibTableColumn
apQOSVideoDropRatio = _ApQOSVideoDropRatio_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1, 6),
    _ApQOSVideoDropRatio_Type()
)
apQOSVideoDropRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVideoDropRatio.setStatus("current")
_ApQOSVideoSvcLoss_Type = Integer32
_ApQOSVideoSvcLoss_Object = MibTableColumn
apQOSVideoSvcLoss = _ApQOSVideoSvcLoss_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1, 7),
    _ApQOSVideoSvcLoss_Type()
)
apQOSVideoSvcLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVideoSvcLoss.setStatus("current")
_ApQOSVideoExceedMaxUsersRequest_Type = Counter32
_ApQOSVideoExceedMaxUsersRequest_Object = MibTableColumn
apQOSVideoExceedMaxUsersRequest = _ApQOSVideoExceedMaxUsersRequest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 8, 5, 1, 1, 8),
    _ApQOSVideoExceedMaxUsersRequest_Type()
)
apQOSVideoExceedMaxUsersRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apQOSVideoExceedMaxUsersRequest.setStatus("current")
_ApWIDSRogueApInfoObjects_ObjectIdentity = ObjectIdentity
apWIDSRogueApInfoObjects = _ApWIDSRogueApInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 9)
)
_ApWIDSRogueApInfoTable_Object = MibTable
apWIDSRogueApInfoTable = _ApWIDSRogueApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 9, 1)
)
if mibBuilder.loadTexts:
    apWIDSRogueApInfoTable.setStatus("current")
_ApWIDSRogueApInfoTableEntry_Object = MibTableRow
apWIDSRogueApInfoTableEntry = _ApWIDSRogueApInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 9, 1, 1)
)
apWIDSRogueApInfoTableEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "ruijieRogueApMacAddr"),
)
if mibBuilder.loadTexts:
    apWIDSRogueApInfoTableEntry.setStatus("current")
_RuijieRogueApMacAddr_Type = MacAddress
_RuijieRogueApMacAddr_Object = MibTableColumn
ruijieRogueApMacAddr = _RuijieRogueApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 9, 1, 1, 1),
    _RuijieRogueApMacAddr_Type()
)
ruijieRogueApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRogueApMacAddr.setStatus("current")
_RuijieRogueApRSSI_Type = Integer32
_RuijieRogueApRSSI_Object = MibTableColumn
ruijieRogueApRSSI = _RuijieRogueApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 9, 1, 1, 2),
    _RuijieRogueApRSSI_Type()
)
ruijieRogueApRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRogueApRSSI.setStatus("current")
_ApStaTransSpeedObjects_ObjectIdentity = ObjectIdentity
apStaTransSpeedObjects = _ApStaTransSpeedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10)
)
_ApStaTransSpeedTable_Object = MibTable
apStaTransSpeedTable = _ApStaTransSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1)
)
if mibBuilder.loadTexts:
    apStaTransSpeedTable.setStatus("current")
_ApStaTransSpeedTableEntry_Object = MibTableRow
apStaTransSpeedTableEntry = _ApStaTransSpeedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1)
)
apStaTransSpeedTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    apStaTransSpeedTableEntry.setStatus("current")
_ApStaUplinkTransSpeed1M_Type = Unsigned32
_ApStaUplinkTransSpeed1M_Object = MibTableColumn
apStaUplinkTransSpeed1M = _ApStaUplinkTransSpeed1M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 1),
    _ApStaUplinkTransSpeed1M_Type()
)
apStaUplinkTransSpeed1M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed1M.setStatus("current")
_ApStaUplinkTransSpeed2M_Type = Unsigned32
_ApStaUplinkTransSpeed2M_Object = MibTableColumn
apStaUplinkTransSpeed2M = _ApStaUplinkTransSpeed2M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 2),
    _ApStaUplinkTransSpeed2M_Type()
)
apStaUplinkTransSpeed2M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed2M.setStatus("current")
_ApStaUplinkTransSpeed5M_Type = Unsigned32
_ApStaUplinkTransSpeed5M_Object = MibTableColumn
apStaUplinkTransSpeed5M = _ApStaUplinkTransSpeed5M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 3),
    _ApStaUplinkTransSpeed5M_Type()
)
apStaUplinkTransSpeed5M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed5M.setStatus("current")
_ApStaUplinkTransSpeed11M_Type = Unsigned32
_ApStaUplinkTransSpeed11M_Object = MibTableColumn
apStaUplinkTransSpeed11M = _ApStaUplinkTransSpeed11M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 4),
    _ApStaUplinkTransSpeed11M_Type()
)
apStaUplinkTransSpeed11M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed11M.setStatus("current")
_ApStaUplinkTransSpeed6M_Type = Unsigned32
_ApStaUplinkTransSpeed6M_Object = MibTableColumn
apStaUplinkTransSpeed6M = _ApStaUplinkTransSpeed6M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 5),
    _ApStaUplinkTransSpeed6M_Type()
)
apStaUplinkTransSpeed6M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed6M.setStatus("current")
_ApStaUplinkTransSpeed9M_Type = Unsigned32
_ApStaUplinkTransSpeed9M_Object = MibTableColumn
apStaUplinkTransSpeed9M = _ApStaUplinkTransSpeed9M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 6),
    _ApStaUplinkTransSpeed9M_Type()
)
apStaUplinkTransSpeed9M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed9M.setStatus("current")
_ApStaUplinkTransSpeed12M_Type = Unsigned32
_ApStaUplinkTransSpeed12M_Object = MibTableColumn
apStaUplinkTransSpeed12M = _ApStaUplinkTransSpeed12M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 7),
    _ApStaUplinkTransSpeed12M_Type()
)
apStaUplinkTransSpeed12M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed12M.setStatus("current")
_ApStaUplinkTransSpeed18M_Type = Unsigned32
_ApStaUplinkTransSpeed18M_Object = MibTableColumn
apStaUplinkTransSpeed18M = _ApStaUplinkTransSpeed18M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 8),
    _ApStaUplinkTransSpeed18M_Type()
)
apStaUplinkTransSpeed18M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed18M.setStatus("current")
_ApStaUplinkTransSpeed24M_Type = Unsigned32
_ApStaUplinkTransSpeed24M_Object = MibTableColumn
apStaUplinkTransSpeed24M = _ApStaUplinkTransSpeed24M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 9),
    _ApStaUplinkTransSpeed24M_Type()
)
apStaUplinkTransSpeed24M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed24M.setStatus("current")
_ApStaUplinkTransSpeed36M_Type = Unsigned32
_ApStaUplinkTransSpeed36M_Object = MibTableColumn
apStaUplinkTransSpeed36M = _ApStaUplinkTransSpeed36M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 10),
    _ApStaUplinkTransSpeed36M_Type()
)
apStaUplinkTransSpeed36M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed36M.setStatus("current")
_ApStaUplinkTransSpeed48M_Type = Unsigned32
_ApStaUplinkTransSpeed48M_Object = MibTableColumn
apStaUplinkTransSpeed48M = _ApStaUplinkTransSpeed48M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 11),
    _ApStaUplinkTransSpeed48M_Type()
)
apStaUplinkTransSpeed48M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed48M.setStatus("current")
_ApStaUplinkTransSpeed54M_Type = Unsigned32
_ApStaUplinkTransSpeed54M_Object = MibTableColumn
apStaUplinkTransSpeed54M = _ApStaUplinkTransSpeed54M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 12),
    _ApStaUplinkTransSpeed54M_Type()
)
apStaUplinkTransSpeed54M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeed54M.setStatus("current")
_ApStaDownlinkTransSpeed1M_Type = Unsigned32
_ApStaDownlinkTransSpeed1M_Object = MibTableColumn
apStaDownlinkTransSpeed1M = _ApStaDownlinkTransSpeed1M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 13),
    _ApStaDownlinkTransSpeed1M_Type()
)
apStaDownlinkTransSpeed1M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed1M.setStatus("current")
_ApStaDownlinkTransSpeed2M_Type = Unsigned32
_ApStaDownlinkTransSpeed2M_Object = MibTableColumn
apStaDownlinkTransSpeed2M = _ApStaDownlinkTransSpeed2M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 14),
    _ApStaDownlinkTransSpeed2M_Type()
)
apStaDownlinkTransSpeed2M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed2M.setStatus("current")
_ApStaDownlinkTransSpeed5M_Type = Unsigned32
_ApStaDownlinkTransSpeed5M_Object = MibTableColumn
apStaDownlinkTransSpeed5M = _ApStaDownlinkTransSpeed5M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 15),
    _ApStaDownlinkTransSpeed5M_Type()
)
apStaDownlinkTransSpeed5M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed5M.setStatus("current")
_ApStaDownlinkTransSpeed11M_Type = Unsigned32
_ApStaDownlinkTransSpeed11M_Object = MibTableColumn
apStaDownlinkTransSpeed11M = _ApStaDownlinkTransSpeed11M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 16),
    _ApStaDownlinkTransSpeed11M_Type()
)
apStaDownlinkTransSpeed11M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed11M.setStatus("current")
_ApStaDownlinkTransSpeed6M_Type = Unsigned32
_ApStaDownlinkTransSpeed6M_Object = MibTableColumn
apStaDownlinkTransSpeed6M = _ApStaDownlinkTransSpeed6M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 17),
    _ApStaDownlinkTransSpeed6M_Type()
)
apStaDownlinkTransSpeed6M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed6M.setStatus("current")
_ApStaDownlinkTransSpeed9M_Type = Unsigned32
_ApStaDownlinkTransSpeed9M_Object = MibTableColumn
apStaDownlinkTransSpeed9M = _ApStaDownlinkTransSpeed9M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 18),
    _ApStaDownlinkTransSpeed9M_Type()
)
apStaDownlinkTransSpeed9M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed9M.setStatus("current")
_ApStaDownlinkTransSpeed12M_Type = Unsigned32
_ApStaDownlinkTransSpeed12M_Object = MibTableColumn
apStaDownlinkTransSpeed12M = _ApStaDownlinkTransSpeed12M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 19),
    _ApStaDownlinkTransSpeed12M_Type()
)
apStaDownlinkTransSpeed12M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed12M.setStatus("current")
_ApStaDownlinkTransSpeed18M_Type = Unsigned32
_ApStaDownlinkTransSpeed18M_Object = MibTableColumn
apStaDownlinkTransSpeed18M = _ApStaDownlinkTransSpeed18M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 20),
    _ApStaDownlinkTransSpeed18M_Type()
)
apStaDownlinkTransSpeed18M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed18M.setStatus("current")
_ApStaDownlinkTransSpeed24M_Type = Unsigned32
_ApStaDownlinkTransSpeed24M_Object = MibTableColumn
apStaDownlinkTransSpeed24M = _ApStaDownlinkTransSpeed24M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 21),
    _ApStaDownlinkTransSpeed24M_Type()
)
apStaDownlinkTransSpeed24M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed24M.setStatus("current")
_ApStaDownlinkTransSpeed36M_Type = Unsigned32
_ApStaDownlinkTransSpeed36M_Object = MibTableColumn
apStaDownlinkTransSpeed36M = _ApStaDownlinkTransSpeed36M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 22),
    _ApStaDownlinkTransSpeed36M_Type()
)
apStaDownlinkTransSpeed36M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed36M.setStatus("current")
_ApStaDownlinkTransSpeed48M_Type = Unsigned32
_ApStaDownlinkTransSpeed48M_Object = MibTableColumn
apStaDownlinkTransSpeed48M = _ApStaDownlinkTransSpeed48M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 23),
    _ApStaDownlinkTransSpeed48M_Type()
)
apStaDownlinkTransSpeed48M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed48M.setStatus("current")
_ApStaDownlinkTransSpeed54M_Type = Unsigned32
_ApStaDownlinkTransSpeed54M_Object = MibTableColumn
apStaDownlinkTransSpeed54M = _ApStaDownlinkTransSpeed54M_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 24),
    _ApStaDownlinkTransSpeed54M_Type()
)
apStaDownlinkTransSpeed54M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeed54M.setStatus("current")
_ApStaUplinkTransSpeedMCS0_Type = Unsigned32
_ApStaUplinkTransSpeedMCS0_Object = MibTableColumn
apStaUplinkTransSpeedMCS0 = _ApStaUplinkTransSpeedMCS0_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 25),
    _ApStaUplinkTransSpeedMCS0_Type()
)
apStaUplinkTransSpeedMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS0.setStatus("current")
_ApStaUplinkTransSpeedMCS1_Type = Unsigned32
_ApStaUplinkTransSpeedMCS1_Object = MibTableColumn
apStaUplinkTransSpeedMCS1 = _ApStaUplinkTransSpeedMCS1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 26),
    _ApStaUplinkTransSpeedMCS1_Type()
)
apStaUplinkTransSpeedMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS1.setStatus("current")
_ApStaUplinkTransSpeedMCS2_Type = Unsigned32
_ApStaUplinkTransSpeedMCS2_Object = MibTableColumn
apStaUplinkTransSpeedMCS2 = _ApStaUplinkTransSpeedMCS2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 27),
    _ApStaUplinkTransSpeedMCS2_Type()
)
apStaUplinkTransSpeedMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS2.setStatus("current")
_ApStaUplinkTransSpeedMCS3_Type = Unsigned32
_ApStaUplinkTransSpeedMCS3_Object = MibTableColumn
apStaUplinkTransSpeedMCS3 = _ApStaUplinkTransSpeedMCS3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 28),
    _ApStaUplinkTransSpeedMCS3_Type()
)
apStaUplinkTransSpeedMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS3.setStatus("current")
_ApStaUplinkTransSpeedMCS4_Type = Unsigned32
_ApStaUplinkTransSpeedMCS4_Object = MibTableColumn
apStaUplinkTransSpeedMCS4 = _ApStaUplinkTransSpeedMCS4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 29),
    _ApStaUplinkTransSpeedMCS4_Type()
)
apStaUplinkTransSpeedMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS4.setStatus("current")
_ApStaUplinkTransSpeedMCS5_Type = Unsigned32
_ApStaUplinkTransSpeedMCS5_Object = MibTableColumn
apStaUplinkTransSpeedMCS5 = _ApStaUplinkTransSpeedMCS5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 30),
    _ApStaUplinkTransSpeedMCS5_Type()
)
apStaUplinkTransSpeedMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS5.setStatus("current")
_ApStaUplinkTransSpeedMCS6_Type = Unsigned32
_ApStaUplinkTransSpeedMCS6_Object = MibTableColumn
apStaUplinkTransSpeedMCS6 = _ApStaUplinkTransSpeedMCS6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 31),
    _ApStaUplinkTransSpeedMCS6_Type()
)
apStaUplinkTransSpeedMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS6.setStatus("current")
_ApStaUplinkTransSpeedMCS7_Type = Unsigned32
_ApStaUplinkTransSpeedMCS7_Object = MibTableColumn
apStaUplinkTransSpeedMCS7 = _ApStaUplinkTransSpeedMCS7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 32),
    _ApStaUplinkTransSpeedMCS7_Type()
)
apStaUplinkTransSpeedMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS7.setStatus("current")
_ApStaUplinkTransSpeedMCS8_Type = Unsigned32
_ApStaUplinkTransSpeedMCS8_Object = MibTableColumn
apStaUplinkTransSpeedMCS8 = _ApStaUplinkTransSpeedMCS8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 33),
    _ApStaUplinkTransSpeedMCS8_Type()
)
apStaUplinkTransSpeedMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS8.setStatus("current")
_ApStaUplinkTransSpeedMCS9_Type = Unsigned32
_ApStaUplinkTransSpeedMCS9_Object = MibTableColumn
apStaUplinkTransSpeedMCS9 = _ApStaUplinkTransSpeedMCS9_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 34),
    _ApStaUplinkTransSpeedMCS9_Type()
)
apStaUplinkTransSpeedMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS9.setStatus("current")
_ApStaUplinkTransSpeedMCS10_Type = Unsigned32
_ApStaUplinkTransSpeedMCS10_Object = MibTableColumn
apStaUplinkTransSpeedMCS10 = _ApStaUplinkTransSpeedMCS10_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 35),
    _ApStaUplinkTransSpeedMCS10_Type()
)
apStaUplinkTransSpeedMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS10.setStatus("current")
_ApStaUplinkTransSpeedMCS11_Type = Unsigned32
_ApStaUplinkTransSpeedMCS11_Object = MibTableColumn
apStaUplinkTransSpeedMCS11 = _ApStaUplinkTransSpeedMCS11_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 36),
    _ApStaUplinkTransSpeedMCS11_Type()
)
apStaUplinkTransSpeedMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS11.setStatus("current")
_ApStaUplinkTransSpeedMCS12_Type = Unsigned32
_ApStaUplinkTransSpeedMCS12_Object = MibTableColumn
apStaUplinkTransSpeedMCS12 = _ApStaUplinkTransSpeedMCS12_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 37),
    _ApStaUplinkTransSpeedMCS12_Type()
)
apStaUplinkTransSpeedMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS12.setStatus("current")
_ApStaUplinkTransSpeedMCS13_Type = Unsigned32
_ApStaUplinkTransSpeedMCS13_Object = MibTableColumn
apStaUplinkTransSpeedMCS13 = _ApStaUplinkTransSpeedMCS13_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 38),
    _ApStaUplinkTransSpeedMCS13_Type()
)
apStaUplinkTransSpeedMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS13.setStatus("current")
_ApStaUplinkTransSpeedMCS14_Type = Unsigned32
_ApStaUplinkTransSpeedMCS14_Object = MibTableColumn
apStaUplinkTransSpeedMCS14 = _ApStaUplinkTransSpeedMCS14_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 39),
    _ApStaUplinkTransSpeedMCS14_Type()
)
apStaUplinkTransSpeedMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS14.setStatus("current")
_ApStaUplinkTransSpeedMCS15_Type = Unsigned32
_ApStaUplinkTransSpeedMCS15_Object = MibTableColumn
apStaUplinkTransSpeedMCS15 = _ApStaUplinkTransSpeedMCS15_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 40),
    _ApStaUplinkTransSpeedMCS15_Type()
)
apStaUplinkTransSpeedMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS15.setStatus("current")
_ApStaUplinkTransSpeedMCS16_Type = Unsigned32
_ApStaUplinkTransSpeedMCS16_Object = MibTableColumn
apStaUplinkTransSpeedMCS16 = _ApStaUplinkTransSpeedMCS16_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 41),
    _ApStaUplinkTransSpeedMCS16_Type()
)
apStaUplinkTransSpeedMCS16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS16.setStatus("current")
_ApStaUplinkTransSpeedMCS17_Type = Unsigned32
_ApStaUplinkTransSpeedMCS17_Object = MibTableColumn
apStaUplinkTransSpeedMCS17 = _ApStaUplinkTransSpeedMCS17_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 42),
    _ApStaUplinkTransSpeedMCS17_Type()
)
apStaUplinkTransSpeedMCS17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS17.setStatus("current")
_ApStaUplinkTransSpeedMCS18_Type = Unsigned32
_ApStaUplinkTransSpeedMCS18_Object = MibTableColumn
apStaUplinkTransSpeedMCS18 = _ApStaUplinkTransSpeedMCS18_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 43),
    _ApStaUplinkTransSpeedMCS18_Type()
)
apStaUplinkTransSpeedMCS18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS18.setStatus("current")
_ApStaUplinkTransSpeedMCS19_Type = Unsigned32
_ApStaUplinkTransSpeedMCS19_Object = MibTableColumn
apStaUplinkTransSpeedMCS19 = _ApStaUplinkTransSpeedMCS19_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 44),
    _ApStaUplinkTransSpeedMCS19_Type()
)
apStaUplinkTransSpeedMCS19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS19.setStatus("current")
_ApStaUplinkTransSpeedMCS20_Type = Unsigned32
_ApStaUplinkTransSpeedMCS20_Object = MibTableColumn
apStaUplinkTransSpeedMCS20 = _ApStaUplinkTransSpeedMCS20_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 45),
    _ApStaUplinkTransSpeedMCS20_Type()
)
apStaUplinkTransSpeedMCS20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS20.setStatus("current")
_ApStaUplinkTransSpeedMCS21_Type = Unsigned32
_ApStaUplinkTransSpeedMCS21_Object = MibTableColumn
apStaUplinkTransSpeedMCS21 = _ApStaUplinkTransSpeedMCS21_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 46),
    _ApStaUplinkTransSpeedMCS21_Type()
)
apStaUplinkTransSpeedMCS21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS21.setStatus("current")
_ApStaUplinkTransSpeedMCS22_Type = Unsigned32
_ApStaUplinkTransSpeedMCS22_Object = MibTableColumn
apStaUplinkTransSpeedMCS22 = _ApStaUplinkTransSpeedMCS22_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 47),
    _ApStaUplinkTransSpeedMCS22_Type()
)
apStaUplinkTransSpeedMCS22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS22.setStatus("current")
_ApStaUplinkTransSpeedMCS23_Type = Unsigned32
_ApStaUplinkTransSpeedMCS23_Object = MibTableColumn
apStaUplinkTransSpeedMCS23 = _ApStaUplinkTransSpeedMCS23_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 48),
    _ApStaUplinkTransSpeedMCS23_Type()
)
apStaUplinkTransSpeedMCS23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS23.setStatus("current")
_ApStaUplinkTransSpeedMCS24_Type = Unsigned32
_ApStaUplinkTransSpeedMCS24_Object = MibTableColumn
apStaUplinkTransSpeedMCS24 = _ApStaUplinkTransSpeedMCS24_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 49),
    _ApStaUplinkTransSpeedMCS24_Type()
)
apStaUplinkTransSpeedMCS24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS24.setStatus("current")
_ApStaUplinkTransSpeedMCS25_Type = Unsigned32
_ApStaUplinkTransSpeedMCS25_Object = MibTableColumn
apStaUplinkTransSpeedMCS25 = _ApStaUplinkTransSpeedMCS25_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 50),
    _ApStaUplinkTransSpeedMCS25_Type()
)
apStaUplinkTransSpeedMCS25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS25.setStatus("current")
_ApStaUplinkTransSpeedMCS26_Type = Unsigned32
_ApStaUplinkTransSpeedMCS26_Object = MibTableColumn
apStaUplinkTransSpeedMCS26 = _ApStaUplinkTransSpeedMCS26_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 51),
    _ApStaUplinkTransSpeedMCS26_Type()
)
apStaUplinkTransSpeedMCS26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS26.setStatus("current")
_ApStaUplinkTransSpeedMCS27_Type = Unsigned32
_ApStaUplinkTransSpeedMCS27_Object = MibTableColumn
apStaUplinkTransSpeedMCS27 = _ApStaUplinkTransSpeedMCS27_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 52),
    _ApStaUplinkTransSpeedMCS27_Type()
)
apStaUplinkTransSpeedMCS27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS27.setStatus("current")
_ApStaUplinkTransSpeedMCS28_Type = Unsigned32
_ApStaUplinkTransSpeedMCS28_Object = MibTableColumn
apStaUplinkTransSpeedMCS28 = _ApStaUplinkTransSpeedMCS28_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 53),
    _ApStaUplinkTransSpeedMCS28_Type()
)
apStaUplinkTransSpeedMCS28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS28.setStatus("current")
_ApStaUplinkTransSpeedMCS29_Type = Unsigned32
_ApStaUplinkTransSpeedMCS29_Object = MibTableColumn
apStaUplinkTransSpeedMCS29 = _ApStaUplinkTransSpeedMCS29_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 54),
    _ApStaUplinkTransSpeedMCS29_Type()
)
apStaUplinkTransSpeedMCS29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS29.setStatus("current")
_ApStaUplinkTransSpeedMCS30_Type = Unsigned32
_ApStaUplinkTransSpeedMCS30_Object = MibTableColumn
apStaUplinkTransSpeedMCS30 = _ApStaUplinkTransSpeedMCS30_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 55),
    _ApStaUplinkTransSpeedMCS30_Type()
)
apStaUplinkTransSpeedMCS30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS30.setStatus("current")
_ApStaUplinkTransSpeedMCS31_Type = Unsigned32
_ApStaUplinkTransSpeedMCS31_Object = MibTableColumn
apStaUplinkTransSpeedMCS31 = _ApStaUplinkTransSpeedMCS31_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 56),
    _ApStaUplinkTransSpeedMCS31_Type()
)
apStaUplinkTransSpeedMCS31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaUplinkTransSpeedMCS31.setStatus("current")
_ApStaDownlinkTransSpeedMCS0_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS0_Object = MibTableColumn
apStaDownlinkTransSpeedMCS0 = _ApStaDownlinkTransSpeedMCS0_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 57),
    _ApStaDownlinkTransSpeedMCS0_Type()
)
apStaDownlinkTransSpeedMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS0.setStatus("current")
_ApStaDownlinkTransSpeedMCS1_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS1_Object = MibTableColumn
apStaDownlinkTransSpeedMCS1 = _ApStaDownlinkTransSpeedMCS1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 58),
    _ApStaDownlinkTransSpeedMCS1_Type()
)
apStaDownlinkTransSpeedMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS1.setStatus("current")
_ApStaDownlinkTransSpeedMCS2_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS2_Object = MibTableColumn
apStaDownlinkTransSpeedMCS2 = _ApStaDownlinkTransSpeedMCS2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 59),
    _ApStaDownlinkTransSpeedMCS2_Type()
)
apStaDownlinkTransSpeedMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS2.setStatus("current")
_ApStaDownlinkTransSpeedMCS3_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS3_Object = MibTableColumn
apStaDownlinkTransSpeedMCS3 = _ApStaDownlinkTransSpeedMCS3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 60),
    _ApStaDownlinkTransSpeedMCS3_Type()
)
apStaDownlinkTransSpeedMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS3.setStatus("current")
_ApStaDownlinkTransSpeedMCS4_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS4_Object = MibTableColumn
apStaDownlinkTransSpeedMCS4 = _ApStaDownlinkTransSpeedMCS4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 61),
    _ApStaDownlinkTransSpeedMCS4_Type()
)
apStaDownlinkTransSpeedMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS4.setStatus("current")
_ApStaDownlinkTransSpeedMCS5_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS5_Object = MibTableColumn
apStaDownlinkTransSpeedMCS5 = _ApStaDownlinkTransSpeedMCS5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 62),
    _ApStaDownlinkTransSpeedMCS5_Type()
)
apStaDownlinkTransSpeedMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS5.setStatus("current")
_ApStaDownlinkTransSpeedMCS6_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS6_Object = MibTableColumn
apStaDownlinkTransSpeedMCS6 = _ApStaDownlinkTransSpeedMCS6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 63),
    _ApStaDownlinkTransSpeedMCS6_Type()
)
apStaDownlinkTransSpeedMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS6.setStatus("current")
_ApStaDownlinkTransSpeedMCS7_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS7_Object = MibTableColumn
apStaDownlinkTransSpeedMCS7 = _ApStaDownlinkTransSpeedMCS7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 64),
    _ApStaDownlinkTransSpeedMCS7_Type()
)
apStaDownlinkTransSpeedMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS7.setStatus("current")
_ApStaDownlinkTransSpeedMCS8_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS8_Object = MibTableColumn
apStaDownlinkTransSpeedMCS8 = _ApStaDownlinkTransSpeedMCS8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 65),
    _ApStaDownlinkTransSpeedMCS8_Type()
)
apStaDownlinkTransSpeedMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS8.setStatus("current")
_ApStaDownlinkTransSpeedMCS9_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS9_Object = MibTableColumn
apStaDownlinkTransSpeedMCS9 = _ApStaDownlinkTransSpeedMCS9_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 66),
    _ApStaDownlinkTransSpeedMCS9_Type()
)
apStaDownlinkTransSpeedMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS9.setStatus("current")
_ApStaDownlinkTransSpeedMCS10_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS10_Object = MibTableColumn
apStaDownlinkTransSpeedMCS10 = _ApStaDownlinkTransSpeedMCS10_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 67),
    _ApStaDownlinkTransSpeedMCS10_Type()
)
apStaDownlinkTransSpeedMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS10.setStatus("current")
_ApStaDownlinkTransSpeedMCS11_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS11_Object = MibTableColumn
apStaDownlinkTransSpeedMCS11 = _ApStaDownlinkTransSpeedMCS11_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 68),
    _ApStaDownlinkTransSpeedMCS11_Type()
)
apStaDownlinkTransSpeedMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS11.setStatus("current")
_ApStaDownlinkTransSpeedMCS12_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS12_Object = MibTableColumn
apStaDownlinkTransSpeedMCS12 = _ApStaDownlinkTransSpeedMCS12_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 69),
    _ApStaDownlinkTransSpeedMCS12_Type()
)
apStaDownlinkTransSpeedMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS12.setStatus("current")
_ApStaDownlinkTransSpeedMCS13_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS13_Object = MibTableColumn
apStaDownlinkTransSpeedMCS13 = _ApStaDownlinkTransSpeedMCS13_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 70),
    _ApStaDownlinkTransSpeedMCS13_Type()
)
apStaDownlinkTransSpeedMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS13.setStatus("current")
_ApStaDownlinkTransSpeedMCS14_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS14_Object = MibTableColumn
apStaDownlinkTransSpeedMCS14 = _ApStaDownlinkTransSpeedMCS14_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 71),
    _ApStaDownlinkTransSpeedMCS14_Type()
)
apStaDownlinkTransSpeedMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS14.setStatus("current")
_ApStaDownlinkTransSpeedMCS15_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS15_Object = MibTableColumn
apStaDownlinkTransSpeedMCS15 = _ApStaDownlinkTransSpeedMCS15_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 72),
    _ApStaDownlinkTransSpeedMCS15_Type()
)
apStaDownlinkTransSpeedMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS15.setStatus("current")
_ApStaDownlinkTransSpeedMCS16_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS16_Object = MibTableColumn
apStaDownlinkTransSpeedMCS16 = _ApStaDownlinkTransSpeedMCS16_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 73),
    _ApStaDownlinkTransSpeedMCS16_Type()
)
apStaDownlinkTransSpeedMCS16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS16.setStatus("current")
_ApStaDownlinkTransSpeedMCS17_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS17_Object = MibTableColumn
apStaDownlinkTransSpeedMCS17 = _ApStaDownlinkTransSpeedMCS17_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 74),
    _ApStaDownlinkTransSpeedMCS17_Type()
)
apStaDownlinkTransSpeedMCS17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS17.setStatus("current")
_ApStaDownlinkTransSpeedMCS18_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS18_Object = MibTableColumn
apStaDownlinkTransSpeedMCS18 = _ApStaDownlinkTransSpeedMCS18_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 75),
    _ApStaDownlinkTransSpeedMCS18_Type()
)
apStaDownlinkTransSpeedMCS18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS18.setStatus("current")
_ApStaDownlinkTransSpeedMCS19_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS19_Object = MibTableColumn
apStaDownlinkTransSpeedMCS19 = _ApStaDownlinkTransSpeedMCS19_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 76),
    _ApStaDownlinkTransSpeedMCS19_Type()
)
apStaDownlinkTransSpeedMCS19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS19.setStatus("current")
_ApStaDownlinkTransSpeedMCS20_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS20_Object = MibTableColumn
apStaDownlinkTransSpeedMCS20 = _ApStaDownlinkTransSpeedMCS20_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 77),
    _ApStaDownlinkTransSpeedMCS20_Type()
)
apStaDownlinkTransSpeedMCS20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS20.setStatus("current")
_ApStaDownlinkTransSpeedMCS21_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS21_Object = MibTableColumn
apStaDownlinkTransSpeedMCS21 = _ApStaDownlinkTransSpeedMCS21_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 78),
    _ApStaDownlinkTransSpeedMCS21_Type()
)
apStaDownlinkTransSpeedMCS21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS21.setStatus("current")
_ApStaDownlinkTransSpeedMCS22_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS22_Object = MibTableColumn
apStaDownlinkTransSpeedMCS22 = _ApStaDownlinkTransSpeedMCS22_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 79),
    _ApStaDownlinkTransSpeedMCS22_Type()
)
apStaDownlinkTransSpeedMCS22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS22.setStatus("current")
_ApStaDownlinkTransSpeedMCS23_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS23_Object = MibTableColumn
apStaDownlinkTransSpeedMCS23 = _ApStaDownlinkTransSpeedMCS23_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 80),
    _ApStaDownlinkTransSpeedMCS23_Type()
)
apStaDownlinkTransSpeedMCS23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS23.setStatus("current")
_ApStaDownlinkTransSpeedMCS24_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS24_Object = MibTableColumn
apStaDownlinkTransSpeedMCS24 = _ApStaDownlinkTransSpeedMCS24_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 81),
    _ApStaDownlinkTransSpeedMCS24_Type()
)
apStaDownlinkTransSpeedMCS24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS24.setStatus("current")
_ApStaDownlinkTransSpeedMCS25_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS25_Object = MibTableColumn
apStaDownlinkTransSpeedMCS25 = _ApStaDownlinkTransSpeedMCS25_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 82),
    _ApStaDownlinkTransSpeedMCS25_Type()
)
apStaDownlinkTransSpeedMCS25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS25.setStatus("current")
_ApStaDownlinkTransSpeedMCS26_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS26_Object = MibTableColumn
apStaDownlinkTransSpeedMCS26 = _ApStaDownlinkTransSpeedMCS26_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 83),
    _ApStaDownlinkTransSpeedMCS26_Type()
)
apStaDownlinkTransSpeedMCS26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS26.setStatus("current")
_ApStaDownlinkTransSpeedMCS27_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS27_Object = MibTableColumn
apStaDownlinkTransSpeedMCS27 = _ApStaDownlinkTransSpeedMCS27_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 84),
    _ApStaDownlinkTransSpeedMCS27_Type()
)
apStaDownlinkTransSpeedMCS27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS27.setStatus("current")
_ApStaDownlinkTransSpeedMCS28_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS28_Object = MibTableColumn
apStaDownlinkTransSpeedMCS28 = _ApStaDownlinkTransSpeedMCS28_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 85),
    _ApStaDownlinkTransSpeedMCS28_Type()
)
apStaDownlinkTransSpeedMCS28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS28.setStatus("current")
_ApStaDownlinkTransSpeedMCS29_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS29_Object = MibTableColumn
apStaDownlinkTransSpeedMCS29 = _ApStaDownlinkTransSpeedMCS29_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 86),
    _ApStaDownlinkTransSpeedMCS29_Type()
)
apStaDownlinkTransSpeedMCS29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS29.setStatus("current")
_ApStaDownlinkTransSpeedMCS30_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS30_Object = MibTableColumn
apStaDownlinkTransSpeedMCS30 = _ApStaDownlinkTransSpeedMCS30_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 87),
    _ApStaDownlinkTransSpeedMCS30_Type()
)
apStaDownlinkTransSpeedMCS30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS30.setStatus("current")
_ApStaDownlinkTransSpeedMCS31_Type = Unsigned32
_ApStaDownlinkTransSpeedMCS31_Object = MibTableColumn
apStaDownlinkTransSpeedMCS31 = _ApStaDownlinkTransSpeedMCS31_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 10, 1, 1, 88),
    _ApStaDownlinkTransSpeedMCS31_Type()
)
apStaDownlinkTransSpeedMCS31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaDownlinkTransSpeedMCS31.setStatus("current")
_ApStationAssoRssiObjects_ObjectIdentity = ObjectIdentity
apStationAssoRssiObjects = _ApStationAssoRssiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11)
)
_ApStationAssoRssiTable_Object = MibTable
apStationAssoRssiTable = _ApStationAssoRssiTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1)
)
if mibBuilder.loadTexts:
    apStationAssoRssiTable.setStatus("current")
_ApStationAssoRssiTableEntry_Object = MibTableRow
apStationAssoRssiTableEntry = _ApStationAssoRssiTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1)
)
apStationAssoRssiTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    apStationAssoRssiTableEntry.setStatus("current")
_ApStationAssoRxSignalStrength1_Type = Counter32
_ApStationAssoRxSignalStrength1_Object = MibTableColumn
apStationAssoRxSignalStrength1 = _ApStationAssoRxSignalStrength1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 1),
    _ApStationAssoRxSignalStrength1_Type()
)
apStationAssoRxSignalStrength1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength1.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength1.setUnits("packets")
_ApStationAssoRxSignalStrength2_Type = Counter32
_ApStationAssoRxSignalStrength2_Object = MibTableColumn
apStationAssoRxSignalStrength2 = _ApStationAssoRxSignalStrength2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 2),
    _ApStationAssoRxSignalStrength2_Type()
)
apStationAssoRxSignalStrength2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength2.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength2.setUnits("packets")
_ApStationAssoRxSignalStrength3_Type = Counter32
_ApStationAssoRxSignalStrength3_Object = MibTableColumn
apStationAssoRxSignalStrength3 = _ApStationAssoRxSignalStrength3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 3),
    _ApStationAssoRxSignalStrength3_Type()
)
apStationAssoRxSignalStrength3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength3.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength3.setUnits("packets")
_ApStationAssoRxSignalStrength4_Type = Counter32
_ApStationAssoRxSignalStrength4_Object = MibTableColumn
apStationAssoRxSignalStrength4 = _ApStationAssoRxSignalStrength4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 4),
    _ApStationAssoRxSignalStrength4_Type()
)
apStationAssoRxSignalStrength4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength4.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength4.setUnits("packets")
_ApStationAssoRxSignalStrength5_Type = Counter32
_ApStationAssoRxSignalStrength5_Object = MibTableColumn
apStationAssoRxSignalStrength5 = _ApStationAssoRxSignalStrength5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 5),
    _ApStationAssoRxSignalStrength5_Type()
)
apStationAssoRxSignalStrength5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength5.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength5.setUnits("packets")
_ApStationAssoRxSignalStrength6_Type = Counter32
_ApStationAssoRxSignalStrength6_Object = MibTableColumn
apStationAssoRxSignalStrength6 = _ApStationAssoRxSignalStrength6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 6),
    _ApStationAssoRxSignalStrength6_Type()
)
apStationAssoRxSignalStrength6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength6.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength6.setUnits("packets")
_ApStationAssoRxSignalStrength7_Type = Counter32
_ApStationAssoRxSignalStrength7_Object = MibTableColumn
apStationAssoRxSignalStrength7 = _ApStationAssoRxSignalStrength7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 7),
    _ApStationAssoRxSignalStrength7_Type()
)
apStationAssoRxSignalStrength7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength7.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength7.setUnits("packets")
_ApStationAssoRxSignalStrength8_Type = Counter32
_ApStationAssoRxSignalStrength8_Object = MibTableColumn
apStationAssoRxSignalStrength8 = _ApStationAssoRxSignalStrength8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 8),
    _ApStationAssoRxSignalStrength8_Type()
)
apStationAssoRxSignalStrength8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength8.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength8.setUnits("packets")
_ApStationAssoRxSignalStrength9_Type = Counter32
_ApStationAssoRxSignalStrength9_Object = MibTableColumn
apStationAssoRxSignalStrength9 = _ApStationAssoRxSignalStrength9_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 9),
    _ApStationAssoRxSignalStrength9_Type()
)
apStationAssoRxSignalStrength9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength9.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength9.setUnits("packets")
_ApStationAssoRxSignalStrength10_Type = Counter32
_ApStationAssoRxSignalStrength10_Object = MibTableColumn
apStationAssoRxSignalStrength10 = _ApStationAssoRxSignalStrength10_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 10),
    _ApStationAssoRxSignalStrength10_Type()
)
apStationAssoRxSignalStrength10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength10.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength10.setUnits("packets")
_ApStationAssoRxSignalStrength11_Type = Counter32
_ApStationAssoRxSignalStrength11_Object = MibTableColumn
apStationAssoRxSignalStrength11 = _ApStationAssoRxSignalStrength11_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 11),
    _ApStationAssoRxSignalStrength11_Type()
)
apStationAssoRxSignalStrength11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength11.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength11.setUnits("packets")
_ApStationAssoRxSignalStrength12_Type = Counter32
_ApStationAssoRxSignalStrength12_Object = MibTableColumn
apStationAssoRxSignalStrength12 = _ApStationAssoRxSignalStrength12_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 12),
    _ApStationAssoRxSignalStrength12_Type()
)
apStationAssoRxSignalStrength12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength12.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength12.setUnits("packets")
_ApStationAssoRxSignalStrength13_Type = Counter32
_ApStationAssoRxSignalStrength13_Object = MibTableColumn
apStationAssoRxSignalStrength13 = _ApStationAssoRxSignalStrength13_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 13),
    _ApStationAssoRxSignalStrength13_Type()
)
apStationAssoRxSignalStrength13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength13.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength13.setUnits("packets")
_ApStationAssoRxSignalStrength14_Type = Counter32
_ApStationAssoRxSignalStrength14_Object = MibTableColumn
apStationAssoRxSignalStrength14 = _ApStationAssoRxSignalStrength14_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 14),
    _ApStationAssoRxSignalStrength14_Type()
)
apStationAssoRxSignalStrength14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength14.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength14.setUnits("packets")
_ApStationAssoRxSignalStrength15_Type = Counter32
_ApStationAssoRxSignalStrength15_Object = MibTableColumn
apStationAssoRxSignalStrength15 = _ApStationAssoRxSignalStrength15_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 10, 11, 1, 1, 15),
    _ApStationAssoRxSignalStrength15_Type()
)
apStationAssoRxSignalStrength15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength15.setStatus("current")
if mibBuilder.loadTexts:
    apStationAssoRxSignalStrength15.setUnits("packets")
_ApRuijieAlarmTrapObjects_ObjectIdentity = ObjectIdentity
apRuijieAlarmTrapObjects = _ApRuijieAlarmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11)
)
_ApAPMac_Type = MacAddress
_ApAPMac_Object = MibScalar
apAPMac = _ApAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 1),
    _ApAPMac_Type()
)
apAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPMac.setStatus("current")
_ApWorkModeBeforeChange_Type = Integer32
_ApWorkModeBeforeChange_Object = MibScalar
apWorkModeBeforeChange = _ApWorkModeBeforeChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 2),
    _ApWorkModeBeforeChange_Type()
)
apWorkModeBeforeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkModeBeforeChange.setStatus("current")
_ApWorkModeAfterChange_Type = Integer32
_ApWorkModeAfterChange_Object = MibScalar
apWorkModeAfterChange = _ApWorkModeAfterChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 3),
    _ApWorkModeAfterChange_Type()
)
apWorkModeAfterChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkModeAfterChange.setStatus("current")
_ApSSIDKey_Type = DisplayString
_ApSSIDKey_Object = MibScalar
apSSIDKey = _ApSSIDKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 4),
    _ApSSIDKey_Type()
)
apSSIDKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDKey.setStatus("current")
_ApSSIDKeyConflict_Type = DisplayString
_ApSSIDKeyConflict_Object = MibScalar
apSSIDKeyConflict = _ApSSIDKeyConflict_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 5),
    _ApSSIDKeyConflict_Type()
)
apSSIDKeyConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSSIDKeyConflict.setStatus("current")
_ApCyperIndex_Type = Integer32
_ApCyperIndex_Object = MibScalar
apCyperIndex = _ApCyperIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 6),
    _ApCyperIndex_Type()
)
apCyperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCyperIndex.setStatus("current")
_ApInterruptReason_Type = DisplayString
_ApInterruptReason_Object = MibScalar
apInterruptReason = _ApInterruptReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 7),
    _ApInterruptReason_Type()
)
apInterruptReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterruptReason.setStatus("current")
_ApWorkingAPRadioIfInfo_Type = MacAddress
_ApWorkingAPRadioIfInfo_Object = MibScalar
apWorkingAPRadioIfInfo = _ApWorkingAPRadioIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 8),
    _ApWorkingAPRadioIfInfo_Type()
)
apWorkingAPRadioIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingAPRadioIfInfo.setStatus("current")
_ApWorkingAPChannel_Type = Integer32
_ApWorkingAPChannel_Object = MibScalar
apWorkingAPChannel = _ApWorkingAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 9),
    _ApWorkingAPChannel_Type()
)
apWorkingAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingAPChannel.setStatus("current")
_ApInterfAPChannel_Type = Integer32
_ApInterfAPChannel_Object = MibScalar
apInterfAPChannel = _ApInterfAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 10),
    _ApInterfAPChannel_Type()
)
apInterfAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfAPChannel.setStatus("current")
_ApInterfAPBSSID_Type = MacAddress
_ApInterfAPBSSID_Object = MibScalar
apInterfAPBSSID = _ApInterfAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 11),
    _ApInterfAPBSSID_Type()
)
apInterfAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfAPBSSID.setStatus("current")
_ApInterfStaMac_Type = MacAddress
_ApInterfStaMac_Object = MibScalar
apInterfStaMac = _ApInterfStaMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 12),
    _ApInterfStaMac_Type()
)
apInterfStaMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfStaMac.setStatus("current")
_ApPermitAssoUser_Type = Integer32
_ApPermitAssoUser_Object = MibScalar
apPermitAssoUser = _ApPermitAssoUser_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 13),
    _ApPermitAssoUser_Type()
)
apPermitAssoUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPermitAssoUser.setStatus("current")
_ApAssoFailReason_Type = DisplayString
_ApAssoFailReason_Object = MibScalar
apAssoFailReason = _ApAssoFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 14),
    _ApAssoFailReason_Type()
)
apAssoFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssoFailReason.setStatus("current")
_ApChannelBeforeChange_Type = Integer32
_ApChannelBeforeChange_Object = MibScalar
apChannelBeforeChange = _ApChannelBeforeChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 15),
    _ApChannelBeforeChange_Type()
)
apChannelBeforeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelBeforeChange.setStatus("current")
_ApChannelAfterChange_Type = Integer32
_ApChannelAfterChange_Object = MibScalar
apChannelAfterChange = _ApChannelAfterChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 16),
    _ApChannelAfterChange_Type()
)
apChannelAfterChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChannelAfterChange.setStatus("current")
_ApChanChangeMode_Type = Integer32
_ApChanChangeMode_Object = MibScalar
apChanChangeMode = _ApChanChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 17),
    _ApChanChangeMode_Type()
)
apChanChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChanChangeMode.setStatus("current")
_ApWorkingAPBSSID_Type = MacAddress
_ApWorkingAPBSSID_Object = MibScalar
apWorkingAPBSSID = _ApWorkingAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 18),
    _ApWorkingAPBSSID_Type()
)
apWorkingAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingAPBSSID.setStatus("current")
_ApWorkingAPSSID_Type = DisplayString
_ApWorkingAPSSID_Object = MibScalar
apWorkingAPSSID = _ApWorkingAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 19),
    _ApWorkingAPSSID_Type()
)
apWorkingAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingAPSSID.setStatus("current")
_ApStaMacAddr_Type = MacAddress
_ApStaMacAddr_Object = MibScalar
apStaMacAddr = _ApStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 20),
    _ApStaMacAddr_Type()
)
apStaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaMacAddr.setStatus("current")
_ApAuthMode_Type = Integer32
_ApAuthMode_Object = MibScalar
apAuthMode = _ApAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 21),
    _ApAuthMode_Type()
)
apAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthMode.setStatus("current")
_ApAuthFailReason_Type = DisplayString
_ApAuthFailReason_Object = MibScalar
apAuthFailReason = _ApAuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 22),
    _ApAuthFailReason_Type()
)
apAuthFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAuthFailReason.setStatus("current")
_UpdateFailReason_Type = DisplayString
_UpdateFailReason_Object = MibScalar
updateFailReason = _UpdateFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 23),
    _UpdateFailReason_Type()
)
updateFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateFailReason.setStatus("current")
_ApSWVersionBeforeUpdate_Type = DisplayString
_ApSWVersionBeforeUpdate_Object = MibScalar
apSWVersionBeforeUpdate = _ApSWVersionBeforeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 24),
    _ApSWVersionBeforeUpdate_Type()
)
apSWVersionBeforeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSWVersionBeforeUpdate.setStatus("current")
_ApAPRadioId_Type = Integer32
_ApAPRadioId_Object = MibScalar
apAPRadioId = _ApAPRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 25),
    _ApAPRadioId_Type()
)
apAPRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPRadioId.setStatus("current")
_ApRevPackages_Type = Integer32
_ApRevPackages_Object = MibScalar
apRevPackages = _ApRevPackages_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 26),
    _ApRevPackages_Type()
)
apRevPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRevPackages.setStatus("current")
_ApCPUUsage_Type = Integer32
_ApCPUUsage_Object = MibScalar
apCPUUsage = _ApCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 27),
    _ApCPUUsage_Type()
)
apCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCPUUsage.setStatus("current")
_ApSpeciousDeviceMac_Type = MacAddress
_ApSpeciousDeviceMac_Object = MibScalar
apSpeciousDeviceMac = _ApSpeciousDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 28),
    _ApSpeciousDeviceMac_Type()
)
apSpeciousDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSpeciousDeviceMac.setStatus("current")
_ApRSSI_Type = Integer32
_ApRSSI_Object = MibScalar
apRSSI = _ApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 29),
    _ApRSSI_Type()
)
apRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRSSI.setStatus("current")
_ApAttackReason_Type = DisplayString
_ApAttackReason_Object = MibScalar
apAttackReason = _ApAttackReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 30),
    _ApAttackReason_Type()
)
apAttackReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAttackReason.setStatus("current")
_ApWlanId_Type = Integer32
_ApWlanId_Object = MibScalar
apWlanId = _ApWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 31),
    _ApWlanId_Type()
)
apWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanId.setStatus("current")
_ApWlanSSID_Type = DisplayString
_ApWlanSSID_Object = MibScalar
apWlanSSID = _ApWlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 32),
    _ApWlanSSID_Type()
)
apWlanSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanSSID.setStatus("current")
_ApWlanSecurityModeBeforeChg_Type = DisplayString
_ApWlanSecurityModeBeforeChg_Object = MibScalar
apWlanSecurityModeBeforeChg = _ApWlanSecurityModeBeforeChg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 33),
    _ApWlanSecurityModeBeforeChg_Type()
)
apWlanSecurityModeBeforeChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanSecurityModeBeforeChg.setStatus("current")
_ApWlanSecurityModeAfterChg_Type = DisplayString
_ApWlanSecurityModeAfterChg_Object = MibScalar
apWlanSecurityModeAfterChg = _ApWlanSecurityModeAfterChg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 34),
    _ApWlanSecurityModeAfterChg_Type()
)
apWlanSecurityModeAfterChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanSecurityModeAfterChg.setStatus("current")
_ApTrapIllegalApMac_Type = MacAddress
_ApTrapIllegalApMac_Object = MibScalar
apTrapIllegalApMac = _ApTrapIllegalApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 35),
    _ApTrapIllegalApMac_Type()
)
apTrapIllegalApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapIllegalApMac.setStatus("current")
_ApTrapIllegalApChannel_Type = Integer32
_ApTrapIllegalApChannel_Object = MibScalar
apTrapIllegalApChannel = _ApTrapIllegalApChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 36),
    _ApTrapIllegalApChannel_Type()
)
apTrapIllegalApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapIllegalApChannel.setStatus("current")
_ApTrapIllegalApRSSI_Type = Integer32
_ApTrapIllegalApRSSI_Object = MibScalar
apTrapIllegalApRSSI = _ApTrapIllegalApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 37),
    _ApTrapIllegalApRSSI_Type()
)
apTrapIllegalApRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapIllegalApRSSI.setStatus("current")
_ApTrapWorkingApMac_Type = MacAddress
_ApTrapWorkingApMac_Object = MibScalar
apTrapWorkingApMac = _ApTrapWorkingApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 38),
    _ApTrapWorkingApMac_Type()
)
apTrapWorkingApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapWorkingApMac.setStatus("current")
_ApTrapWorkingApBSSID_Type = MacAddress
_ApTrapWorkingApBSSID_Object = MibScalar
apTrapWorkingApBSSID = _ApTrapWorkingApBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 39),
    _ApTrapWorkingApBSSID_Type()
)
apTrapWorkingApBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapWorkingApBSSID.setStatus("current")
_ApTrapIllegalApType_Type = Integer32
_ApTrapIllegalApType_Object = MibScalar
apTrapIllegalApType = _ApTrapIllegalApType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 40),
    _ApTrapIllegalApType_Type()
)
apTrapIllegalApType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapIllegalApType.setStatus("current")
_ApTrapIllegalApSSID_Type = DisplayString
_ApTrapIllegalApSSID_Object = MibScalar
apTrapIllegalApSSID = _ApTrapIllegalApSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 41),
    _ApTrapIllegalApSSID_Type()
)
apTrapIllegalApSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapIllegalApSSID.setStatus("current")


class _ApAPRadioType_Type(Integer32):
    """Custom type apAPRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 0),
          ("dot11b", 1))
    )


_ApAPRadioType_Type.__name__ = "Integer32"
_ApAPRadioType_Object = MibScalar
apAPRadioType = _ApAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 42),
    _ApAPRadioType_Type()
)
apAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPRadioType.setStatus("current")
_ApAssocAuthMode_Type = Integer32
_ApAssocAuthMode_Object = MibScalar
apAssocAuthMode = _ApAssocAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 43),
    _ApAssocAuthMode_Type()
)
apAssocAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssocAuthMode.setStatus("current")
_ApStaRSSI_Type = DisplayString
_ApStaRSSI_Object = MibScalar
apStaRSSI = _ApStaRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 44),
    _ApStaRSSI_Type()
)
apStaRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaRSSI.setStatus("current")
_ApAssocFailReason_Type = Integer32
_ApAssocFailReason_Object = MibScalar
apAssocFailReason = _ApAssocFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 45),
    _ApAssocFailReason_Type()
)
apAssocFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAssocFailReason.setStatus("current")
_ApSpectralInfoApMac_Type = MacAddress
_ApSpectralInfoApMac_Object = MibScalar
apSpectralInfoApMac = _ApSpectralInfoApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 46),
    _ApSpectralInfoApMac_Type()
)
apSpectralInfoApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSpectralInfoApMac.setStatus("current")
_ApSpectralInfoType_Type = Integer32
_ApSpectralInfoType_Object = MibScalar
apSpectralInfoType = _ApSpectralInfoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 47),
    _ApSpectralInfoType_Type()
)
apSpectralInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSpectralInfoType.setStatus("current")
_ApSpectralInfoFreq_Type = Integer32
_ApSpectralInfoFreq_Object = MibScalar
apSpectralInfoFreq = _ApSpectralInfoFreq_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 48),
    _ApSpectralInfoFreq_Type()
)
apSpectralInfoFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSpectralInfoFreq.setStatus("current")
_ApSpectralInfoRssi_Type = Integer32
_ApSpectralInfoRssi_Object = MibScalar
apSpectralInfoRssi = _ApSpectralInfoRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 49),
    _ApSpectralInfoRssi_Type()
)
apSpectralInfoRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSpectralInfoRssi.setStatus("current")
_ApCounterMeasureApMac_Type = MacAddress
_ApCounterMeasureApMac_Object = MibScalar
apCounterMeasureApMac = _ApCounterMeasureApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 50),
    _ApCounterMeasureApMac_Type()
)
apCounterMeasureApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCounterMeasureApMac.setStatus("current")
_ApCounterMeasureBssid_Type = MacAddress
_ApCounterMeasureBssid_Object = MibScalar
apCounterMeasureBssid = _ApCounterMeasureBssid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 51),
    _ApCounterMeasureBssid_Type()
)
apCounterMeasureBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCounterMeasureBssid.setStatus("current")
_ApApName_Type = DisplayString
_ApApName_Object = MibScalar
apApName = _ApApName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 52),
    _ApApName_Type()
)
apApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApName.setStatus("current")
_ApApLocation_Type = DisplayString
_ApApLocation_Object = MibScalar
apApLocation = _ApApLocation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 53),
    _ApApLocation_Type()
)
apApLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApLocation.setStatus("current")
_ApApUptime_Type = Integer32
_ApApUptime_Object = MibScalar
apApUptime = _ApApUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 54),
    _ApApUptime_Type()
)
apApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApUptime.setStatus("current")
_ApApUserNum_Type = Integer32
_ApApUserNum_Object = MibScalar
apApUserNum = _ApApUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 55),
    _ApApUserNum_Type()
)
apApUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApUserNum.setStatus("current")
_ApApChannel2_Type = DisplayString
_ApApChannel2_Object = MibScalar
apApChannel2 = _ApApChannel2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 56),
    _ApApChannel2_Type()
)
apApChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApChannel2.setStatus("current")
_ApApChannel5_Type = DisplayString
_ApApChannel5_Object = MibScalar
apApChannel5 = _ApApChannel5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 57),
    _ApApChannel5_Type()
)
apApChannel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apApChannel5.setStatus("current")
_ApSsidName_Type = DisplayString
_ApSsidName_Object = MibScalar
apSsidName = _ApSsidName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 58),
    _ApSsidName_Type()
)
apSsidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidName.setStatus("current")
_ApSsidIndex_Type = DisplayString
_ApSsidIndex_Object = MibScalar
apSsidIndex = _ApSsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 59),
    _ApSsidIndex_Type()
)
apSsidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidIndex.setStatus("current")
_ApSsidDot11Auth_Type = Integer32
_ApSsidDot11Auth_Object = MibScalar
apSsidDot11Auth = _ApSsidDot11Auth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 60),
    _ApSsidDot11Auth_Type()
)
apSsidDot11Auth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidDot11Auth.setStatus("current")
_ApSsidSecurityMode_Type = Integer32
_ApSsidSecurityMode_Object = MibScalar
apSsidSecurityMode = _ApSsidSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 61),
    _ApSsidSecurityMode_Type()
)
apSsidSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidSecurityMode.setStatus("current")
_ApSsidAuthenMode_Type = Integer32
_ApSsidAuthenMode_Object = MibScalar
apSsidAuthenMode = _ApSsidAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 62),
    _ApSsidAuthenMode_Type()
)
apSsidAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidAuthenMode.setStatus("current")
_WebAuthTlvCount_Type = Integer32
_WebAuthTlvCount_Object = MibScalar
webAuthTlvCount = _WebAuthTlvCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 63),
    _WebAuthTlvCount_Type()
)
webAuthTlvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAuthTlvCount.setStatus("current")
_WebAuthTlvString_Type = DisplayString
_WebAuthTlvString_Object = MibScalar
webAuthTlvString = _WebAuthTlvString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 11, 64),
    _WebAuthTlvString_Type()
)
webAuthTlvString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAuthTlvString.setStatus("current")
_ApAccessControl_ObjectIdentity = ObjectIdentity
apAccessControl = _ApAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12)
)
_ApTerminalPermitTable_Object = MibTable
apTerminalPermitTable = _ApTerminalPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 1)
)
if mibBuilder.loadTexts:
    apTerminalPermitTable.setStatus("current")
_ApTerminalPermitEntry_Object = MibTableRow
apTerminalPermitEntry = _ApTerminalPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 1, 1)
)
apTerminalPermitEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apWhiteListIndex"),
)
if mibBuilder.loadTexts:
    apTerminalPermitEntry.setStatus("current")
_ApWhiteListIndex_Type = Integer32
_ApWhiteListIndex_Object = MibTableColumn
apWhiteListIndex = _ApWhiteListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 1, 1, 1),
    _ApWhiteListIndex_Type()
)
apWhiteListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWhiteListIndex.setStatus("current")
_ApPermitMAC_Type = MacAddress
_ApPermitMAC_Object = MibTableColumn
apPermitMAC = _ApPermitMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 1, 1, 2),
    _ApPermitMAC_Type()
)
apPermitMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apPermitMAC.setStatus("current")
_ApWhiteListStatus_Type = RowStatus
_ApWhiteListStatus_Object = MibTableColumn
apWhiteListStatus = _ApWhiteListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 1, 1, 3),
    _ApWhiteListStatus_Type()
)
apWhiteListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apWhiteListStatus.setStatus("current")
_ApTerminalDeniedTable_Object = MibTable
apTerminalDeniedTable = _ApTerminalDeniedTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 2)
)
if mibBuilder.loadTexts:
    apTerminalDeniedTable.setStatus("current")
_ApTerminalDeniedEntry_Object = MibTableRow
apTerminalDeniedEntry = _ApTerminalDeniedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 2, 1)
)
apTerminalDeniedEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apBlackListIndex"),
)
if mibBuilder.loadTexts:
    apTerminalDeniedEntry.setStatus("current")
_ApBlackListIndex_Type = Integer32
_ApBlackListIndex_Object = MibTableColumn
apBlackListIndex = _ApBlackListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 2, 1, 1),
    _ApBlackListIndex_Type()
)
apBlackListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlackListIndex.setStatus("current")
_ApAttackDeviceMAC_Type = MacAddress
_ApAttackDeviceMAC_Object = MibTableColumn
apAttackDeviceMAC = _ApAttackDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 2, 1, 2),
    _ApAttackDeviceMAC_Type()
)
apAttackDeviceMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAttackDeviceMAC.setStatus("current")
_ApBlackListStatus_Type = RowStatus
_ApBlackListStatus_Object = MibTableColumn
apBlackListStatus = _ApBlackListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 2, 1, 3),
    _ApBlackListStatus_Type()
)
apBlackListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBlackListStatus.setStatus("current")
_ApTerminalBlackListTable_Object = MibTable
apTerminalBlackListTable = _ApTerminalBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 3)
)
if mibBuilder.loadTexts:
    apTerminalBlackListTable.setStatus("current")
_ApTerminalBlackListEntry_Object = MibTableRow
apTerminalBlackListEntry = _ApTerminalBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 3, 1)
)
apTerminalBlackListEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apBlackListDeviceMAC"),
)
if mibBuilder.loadTexts:
    apTerminalBlackListEntry.setStatus("current")
_ApBlackListDeviceMAC_Type = MacAddress
_ApBlackListDeviceMAC_Object = MibTableColumn
apBlackListDeviceMAC = _ApBlackListDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 3, 1, 1),
    _ApBlackListDeviceMAC_Type()
)
apBlackListDeviceMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBlackListDeviceMAC.setStatus("current")
_ApBlackListAddReason_Type = OctetString
_ApBlackListAddReason_Object = MibTableColumn
apBlackListAddReason = _ApBlackListAddReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 3, 1, 2),
    _ApBlackListAddReason_Type()
)
apBlackListAddReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlackListAddReason.setStatus("current")
_ApBlackListDuration_Type = TimeTicks
_ApBlackListDuration_Object = MibTableColumn
apBlackListDuration = _ApBlackListDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 12, 3, 1, 3),
    _ApBlackListDuration_Type()
)
apBlackListDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlackListDuration.setStatus("current")
_AcCapabilityStatistics_ObjectIdentity = ObjectIdentity
acCapabilityStatistics = _AcCapabilityStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13)
)
_AcWirelessDownDropFrame_Type = Counter64
_AcWirelessDownDropFrame_Object = MibScalar
acWirelessDownDropFrame = _AcWirelessDownDropFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 1),
    _AcWirelessDownDropFrame_Type()
)
acWirelessDownDropFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessDownDropFrame.setStatus("current")
_AcWirelessDownRetryFrame_Type = Counter64
_AcWirelessDownRetryFrame_Object = MibScalar
acWirelessDownRetryFrame = _AcWirelessDownRetryFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 2),
    _AcWirelessDownRetryFrame_Type()
)
acWirelessDownRetryFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessDownRetryFrame.setStatus("current")
_AcWirelessDownFrame_Type = Counter64
_AcWirelessDownFrame_Object = MibScalar
acWirelessDownFrame = _AcWirelessDownFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 3),
    _AcWirelessDownFrame_Type()
)
acWirelessDownFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessDownFrame.setStatus("current")
_AcWirelessDownErrorFrame_Type = Counter64
_AcWirelessDownErrorFrame_Object = MibScalar
acWirelessDownErrorFrame = _AcWirelessDownErrorFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 4),
    _AcWirelessDownErrorFrame_Type()
)
acWirelessDownErrorFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessDownErrorFrame.setStatus("current")
_AcWirelessUpFrame_Type = Counter64
_AcWirelessUpFrame_Object = MibScalar
acWirelessUpFrame = _AcWirelessUpFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 5),
    _AcWirelessUpFrame_Type()
)
acWirelessUpFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessUpFrame.setStatus("current")
_AcWirelessUpDropFrame_Type = Counter64
_AcWirelessUpDropFrame_Object = MibScalar
acWirelessUpDropFrame = _AcWirelessUpDropFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 6),
    _AcWirelessUpDropFrame_Type()
)
acWirelessUpDropFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessUpDropFrame.setStatus("current")
_AcWirelessUpRetryFrame_Type = Counter64
_AcWirelessUpRetryFrame_Object = MibScalar
acWirelessUpRetryFrame = _AcWirelessUpRetryFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 7),
    _AcWirelessUpRetryFrame_Type()
)
acWirelessUpRetryFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessUpRetryFrame.setStatus("current")
_AcWirelessUpRate_Type = Counter64
_AcWirelessUpRate_Object = MibScalar
acWirelessUpRate = _AcWirelessUpRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 8),
    _AcWirelessUpRate_Type()
)
acWirelessUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessUpRate.setStatus("current")
_AcWirelessDownRate_Type = Counter64
_AcWirelessDownRate_Object = MibScalar
acWirelessDownRate = _AcWirelessDownRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 13, 9),
    _AcWirelessDownRate_Type()
)
acWirelessDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWirelessDownRate.setStatus("current")
_ApWidsInfoObjects_ObjectIdentity = ObjectIdentity
apWidsInfoObjects = _ApWidsInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14)
)
_ApWidsIllegalApTable_Object = MibTable
apWidsIllegalApTable = _ApWidsIllegalApTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1)
)
if mibBuilder.loadTexts:
    apWidsIllegalApTable.setStatus("current")
_ApWidsIllegalApEntry_Object = MibTableRow
apWidsIllegalApEntry = _ApWidsIllegalApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1, 1)
)
apWidsIllegalApEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apIllegalApMac"),
)
if mibBuilder.loadTexts:
    apWidsIllegalApEntry.setStatus("current")
_ApIllegalApMac_Type = MacAddress
_ApIllegalApMac_Object = MibTableColumn
apIllegalApMac = _ApIllegalApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1, 1, 1),
    _ApIllegalApMac_Type()
)
apIllegalApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIllegalApMac.setStatus("current")
_ApIllegalApChannel_Type = Integer32
_ApIllegalApChannel_Object = MibTableColumn
apIllegalApChannel = _ApIllegalApChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1, 1, 2),
    _ApIllegalApChannel_Type()
)
apIllegalApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIllegalApChannel.setStatus("current")
_ApIllegalApRSSI_Type = Integer32
_ApIllegalApRSSI_Object = MibTableColumn
apIllegalApRSSI = _ApIllegalApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1, 1, 3),
    _ApIllegalApRSSI_Type()
)
apIllegalApRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIllegalApRSSI.setStatus("current")
_ApWorkingApMac_Type = MacAddress
_ApWorkingApMac_Object = MibTableColumn
apWorkingApMac = _ApWorkingApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1, 1, 4),
    _ApWorkingApMac_Type()
)
apWorkingApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWorkingApMac.setStatus("current")
_ApDetectAPBSSID_Type = MacAddress
_ApDetectAPBSSID_Object = MibTableColumn
apDetectAPBSSID = _ApDetectAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1, 1, 5),
    _ApDetectAPBSSID_Type()
)
apDetectAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDetectAPBSSID.setStatus("current")
_ApIllegalApType_Type = Integer32
_ApIllegalApType_Object = MibTableColumn
apIllegalApType = _ApIllegalApType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1, 1, 6),
    _ApIllegalApType_Type()
)
apIllegalApType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIllegalApType.setStatus("current")
_ApIllegalApSSID_Type = DisplayString
_ApIllegalApSSID_Object = MibTableColumn
apIllegalApSSID = _ApIllegalApSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 1, 1, 7),
    _ApIllegalApSSID_Type()
)
apIllegalApSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIllegalApSSID.setStatus("current")
_ApWidsApCounterTable_Object = MibTable
apWidsApCounterTable = _ApWidsApCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 2)
)
if mibBuilder.loadTexts:
    apWidsApCounterTable.setStatus("current")
_ApWidsApCounterEntry_Object = MibTableRow
apWidsApCounterEntry = _ApWidsApCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 2, 1)
)
apWidsApCounterEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apCounterMac"),
)
if mibBuilder.loadTexts:
    apWidsApCounterEntry.setStatus("current")
_ApCounterMac_Type = MacAddress
_ApCounterMac_Object = MibTableColumn
apCounterMac = _ApCounterMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 2, 1, 1),
    _ApCounterMac_Type()
)
apCounterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCounterMac.setStatus("current")
_ApCounter_Type = Integer32
_ApCounter_Object = MibTableColumn
apCounter = _ApCounter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 2, 1, 2),
    _ApCounter_Type()
)
apCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCounter.setStatus("current")
_ApCounterMode_Type = Integer32
_ApCounterMode_Object = MibTableColumn
apCounterMode = _ApCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 2, 1, 3),
    _ApCounterMode_Type()
)
apCounterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCounterMode.setStatus("current")
_ApCounterRssiThreshold_Type = Integer32
_ApCounterRssiThreshold_Object = MibTableColumn
apCounterRssiThreshold = _ApCounterRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 2, 1, 4),
    _ApCounterRssiThreshold_Type()
)
apCounterRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCounterRssiThreshold.setStatus("current")
_ApWidsDeviceMode_Type = Integer32
_ApWidsDeviceMode_Object = MibScalar
apWidsDeviceMode = _ApWidsDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 3),
    _ApWidsDeviceMode_Type()
)
apWidsDeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsDeviceMode.setStatus("current")
_ApWidsCounterIllegalAp_Type = Integer32
_ApWidsCounterIllegalAp_Object = MibScalar
apWidsCounterIllegalAp = _ApWidsCounterIllegalAp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 4),
    _ApWidsCounterIllegalAp_Type()
)
apWidsCounterIllegalAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsCounterIllegalAp.setStatus("current")
_ApWidsCounterModeIllegalAp_Type = Integer32
_ApWidsCounterModeIllegalAp_Object = MibScalar
apWidsCounterModeIllegalAp = _ApWidsCounterModeIllegalAp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 5),
    _ApWidsCounterModeIllegalAp_Type()
)
apWidsCounterModeIllegalAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsCounterModeIllegalAp.setStatus("current")
_ApWidsDeviceModeFlag_Type = Integer32
_ApWidsDeviceModeFlag_Object = MibScalar
apWidsDeviceModeFlag = _ApWidsDeviceModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 6),
    _ApWidsDeviceModeFlag_Type()
)
apWidsDeviceModeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWidsDeviceModeFlag.setStatus("current")
_ApWidsCounterIllegalApFlag_Type = Integer32
_ApWidsCounterIllegalApFlag_Object = MibScalar
apWidsCounterIllegalApFlag = _ApWidsCounterIllegalApFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 7),
    _ApWidsCounterIllegalApFlag_Type()
)
apWidsCounterIllegalApFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWidsCounterIllegalApFlag.setStatus("current")
_ApWidsCounterModeIllegalApFlag_Type = Integer32
_ApWidsCounterModeIllegalApFlag_Object = MibScalar
apWidsCounterModeIllegalApFlag = _ApWidsCounterModeIllegalApFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 8),
    _ApWidsCounterModeIllegalApFlag_Type()
)
apWidsCounterModeIllegalApFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWidsCounterModeIllegalApFlag.setStatus("current")
_ApWidsPermitMacTable_Object = MibTable
apWidsPermitMacTable = _ApWidsPermitMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 9)
)
if mibBuilder.loadTexts:
    apWidsPermitMacTable.setStatus("current")
_ApWidsPermitMacEntry_Object = MibTableRow
apWidsPermitMacEntry = _ApWidsPermitMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 9, 1)
)
apWidsPermitMacEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apWidsPermitMac"),
)
if mibBuilder.loadTexts:
    apWidsPermitMacEntry.setStatus("current")
_ApWidsPermitMac_Type = MacAddress
_ApWidsPermitMac_Object = MibTableColumn
apWidsPermitMac = _ApWidsPermitMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 9, 1, 1),
    _ApWidsPermitMac_Type()
)
apWidsPermitMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWidsPermitMac.setStatus("current")
_ApPermitMacrowstatus_Type = RowStatus
_ApPermitMacrowstatus_Object = MibTableColumn
apPermitMacrowstatus = _ApPermitMacrowstatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 9, 1, 2),
    _ApPermitMacrowstatus_Type()
)
apPermitMacrowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apPermitMacrowstatus.setStatus("current")
_ApWidsPermitSSIDTable_Object = MibTable
apWidsPermitSSIDTable = _ApWidsPermitSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 10)
)
if mibBuilder.loadTexts:
    apWidsPermitSSIDTable.setStatus("current")
_ApWidsPermitSSIDEntry_Object = MibTableRow
apWidsPermitSSIDEntry = _ApWidsPermitSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 10, 1)
)
apWidsPermitSSIDEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apCounterSSID"),
)
if mibBuilder.loadTexts:
    apWidsPermitSSIDEntry.setStatus("current")
_ApCounterSSID_Type = DisplayString
_ApCounterSSID_Object = MibTableColumn
apCounterSSID = _ApCounterSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 10, 1, 1),
    _ApCounterSSID_Type()
)
apCounterSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCounterSSID.setStatus("current")
_ApPermitSSIDrowstatus_Type = RowStatus
_ApPermitSSIDrowstatus_Object = MibTableColumn
apPermitSSIDrowstatus = _ApPermitSSIDrowstatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 10, 1, 2),
    _ApPermitSSIDrowstatus_Type()
)
apPermitSSIDrowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apPermitSSIDrowstatus.setStatus("current")
_ApWidsPermitVendorTable_Object = MibTable
apWidsPermitVendorTable = _ApWidsPermitVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 11)
)
if mibBuilder.loadTexts:
    apWidsPermitVendorTable.setStatus("current")
_ApWidsPermitVendorEntry_Object = MibTableRow
apWidsPermitVendorEntry = _ApWidsPermitVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 11, 1)
)
apWidsPermitVendorEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apCounterVendor"),
)
if mibBuilder.loadTexts:
    apWidsPermitVendorEntry.setStatus("current")
_ApCounterVendor_Type = MacAddress
_ApCounterVendor_Object = MibTableColumn
apCounterVendor = _ApCounterVendor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 11, 1, 1),
    _ApCounterVendor_Type()
)
apCounterVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCounterVendor.setStatus("current")
_ApPermitVendorrowstatus_Type = RowStatus
_ApPermitVendorrowstatus_Object = MibTableColumn
apPermitVendorrowstatus = _ApPermitVendorrowstatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 11, 1, 2),
    _ApPermitVendorrowstatus_Type()
)
apPermitVendorrowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apPermitVendorrowstatus.setStatus("current")
_ApWidsStaticAttackTable_Object = MibTable
apWidsStaticAttackTable = _ApWidsStaticAttackTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 12)
)
if mibBuilder.loadTexts:
    apWidsStaticAttackTable.setStatus("current")
_ApWidsStaticAttackEntry_Object = MibTableRow
apWidsStaticAttackEntry = _ApWidsStaticAttackEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 12, 1)
)
apWidsStaticAttackEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaticAttackMac"),
)
if mibBuilder.loadTexts:
    apWidsStaticAttackEntry.setStatus("current")
_ApStaticAttackMac_Type = MacAddress
_ApStaticAttackMac_Object = MibTableColumn
apStaticAttackMac = _ApStaticAttackMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 12, 1, 1),
    _ApStaticAttackMac_Type()
)
apStaticAttackMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStaticAttackMac.setStatus("current")
_ApStaticAttackrowstatus_Type = RowStatus
_ApStaticAttackrowstatus_Object = MibTableColumn
apStaticAttackrowstatus = _ApStaticAttackrowstatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 12, 1, 2),
    _ApStaticAttackrowstatus_Type()
)
apStaticAttackrowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStaticAttackrowstatus.setStatus("current")
_ApWidsNeighborApInfoTable_Object = MibTable
apWidsNeighborApInfoTable = _ApWidsNeighborApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 13)
)
if mibBuilder.loadTexts:
    apWidsNeighborApInfoTable.setStatus("current")
_ApWidsNeighborApInfoEntry_Object = MibTableRow
apWidsNeighborApInfoEntry = _ApWidsNeighborApInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 13, 1)
)
apWidsNeighborApInfoEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "neighborApMac"),
)
if mibBuilder.loadTexts:
    apWidsNeighborApInfoEntry.setStatus("current")
_NeighborApMac_Type = MacAddress
_NeighborApMac_Object = MibTableColumn
neighborApMac = _NeighborApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 13, 1, 1),
    _NeighborApMac_Type()
)
neighborApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborApMac.setStatus("current")
_NeighborApSSID_Type = DisplayString
_NeighborApSSID_Object = MibTableColumn
neighborApSSID = _NeighborApSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 13, 1, 2),
    _NeighborApSSID_Type()
)
neighborApSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborApSSID.setStatus("current")
_NeighborApRSSI_Type = Integer32
_NeighborApRSSI_Object = MibTableColumn
neighborApRSSI = _NeighborApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 13, 1, 3),
    _NeighborApRSSI_Type()
)
neighborApRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborApRSSI.setStatus("current")
_NeighborApChannel_Type = Integer32
_NeighborApChannel_Object = MibTableColumn
neighborApChannel = _NeighborApChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 13, 1, 4),
    _NeighborApChannel_Type()
)
neighborApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborApChannel.setStatus("current")
_NeighborApInControl_Type = Integer32
_NeighborApInControl_Object = MibTableColumn
neighborApInControl = _NeighborApInControl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 13, 1, 5),
    _NeighborApInControl_Type()
)
neighborApInControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborApInControl.setStatus("current")
_ApWidsClearIlleglApListFlag_Type = TruthValue
_ApWidsClearIlleglApListFlag_Object = MibScalar
apWidsClearIlleglApListFlag = _ApWidsClearIlleglApListFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 14),
    _ApWidsClearIlleglApListFlag_Type()
)
apWidsClearIlleglApListFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsClearIlleglApListFlag.setStatus("current")
_ApWidsFloodInterval_Type = Unsigned32
_ApWidsFloodInterval_Object = MibScalar
apWidsFloodInterval = _ApWidsFloodInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 15),
    _ApWidsFloodInterval_Type()
)
apWidsFloodInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsFloodInterval.setStatus("current")
_ApWidsBlackListThreshold_Type = Unsigned32
_ApWidsBlackListThreshold_Object = MibScalar
apWidsBlackListThreshold = _ApWidsBlackListThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 16),
    _ApWidsBlackListThreshold_Type()
)
apWidsBlackListThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsBlackListThreshold.setStatus("current")
_ApWidsBlackListDuration_Type = Unsigned32
_ApWidsBlackListDuration_Object = MibScalar
apWidsBlackListDuration = _ApWidsBlackListDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 17),
    _ApWidsBlackListDuration_Type()
)
apWidsBlackListDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsBlackListDuration.setStatus("current")
_ApWidsFloodDetectOnOff_Type = Integer32
_ApWidsFloodDetectOnOff_Object = MibScalar
apWidsFloodDetectOnOff = _ApWidsFloodDetectOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 18),
    _ApWidsFloodDetectOnOff_Type()
)
apWidsFloodDetectOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsFloodDetectOnOff.setStatus("current")
_ApWidsCounterRssiThreshold_Type = Integer32
_ApWidsCounterRssiThreshold_Object = MibScalar
apWidsCounterRssiThreshold = _ApWidsCounterRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 19),
    _ApWidsCounterRssiThreshold_Type()
)
apWidsCounterRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWidsCounterRssiThreshold.setStatus("current")
_ApWidsBlackSSIDTable_Object = MibTable
apWidsBlackSSIDTable = _ApWidsBlackSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 20)
)
if mibBuilder.loadTexts:
    apWidsBlackSSIDTable.setStatus("current")
_ApWidsBlackSSIDEntry_Object = MibTableRow
apWidsBlackSSIDEntry = _ApWidsBlackSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 20, 1)
)
apWidsBlackSSIDEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apBlackSSID"),
)
if mibBuilder.loadTexts:
    apWidsBlackSSIDEntry.setStatus("current")
_ApBlackSSID_Type = DisplayString
_ApBlackSSID_Object = MibTableColumn
apBlackSSID = _ApBlackSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 20, 1, 1),
    _ApBlackSSID_Type()
)
apBlackSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBlackSSID.setStatus("current")
_ApBlackSSIDrowstatus_Type = RowStatus
_ApBlackSSIDrowstatus_Object = MibTableColumn
apBlackSSIDrowstatus = _ApBlackSSIDrowstatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 14, 20, 1, 2),
    _ApBlackSSIDrowstatus_Type()
)
apBlackSSIDrowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBlackSSIDrowstatus.setStatus("current")
_ApConfigInfoObjects_ObjectIdentity = ObjectIdentity
apConfigInfoObjects = _ApConfigInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15)
)
_ApConfigInfoTable_Object = MibTable
apConfigInfoTable = _ApConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1)
)
if mibBuilder.loadTexts:
    apConfigInfoTable.setStatus("current")
_ApConfigInfoEntry_Object = MibTableRow
apConfigInfoEntry = _ApConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1)
)
apConfigInfoEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apConfigInfoMac"),
)
if mibBuilder.loadTexts:
    apConfigInfoEntry.setStatus("current")
_ApConfigInfoMac_Type = MacAddress
_ApConfigInfoMac_Object = MibTableColumn
apConfigInfoMac = _ApConfigInfoMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 1),
    _ApConfigInfoMac_Type()
)
apConfigInfoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apConfigInfoMac.setStatus("current")
_ApSpectralSwitch_Type = Integer32
_ApSpectralSwitch_Object = MibTableColumn
apSpectralSwitch = _ApSpectralSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 2),
    _ApSpectralSwitch_Type()
)
apSpectralSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSpectralSwitch.setStatus("current")
_ApSpectralSupport_Type = Integer32
_ApSpectralSupport_Object = MibTableColumn
apSpectralSupport = _ApSpectralSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 3),
    _ApSpectralSupport_Type()
)
apSpectralSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSpectralSupport.setStatus("current")
_ApSmartAntSupport_Type = Integer32
_ApSmartAntSupport_Object = MibTableColumn
apSmartAntSupport = _ApSmartAntSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 4),
    _ApSmartAntSupport_Type()
)
apSmartAntSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSmartAntSupport.setStatus("current")
_ApSmartDisSupport_Type = Integer32
_ApSmartDisSupport_Object = MibTableColumn
apSmartDisSupport = _ApSmartDisSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 5),
    _ApSmartDisSupport_Type()
)
apSmartDisSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSmartDisSupport.setStatus("current")
_ApAntdetectSupport_Type = Integer32
_ApAntdetectSupport_Object = MibTableColumn
apAntdetectSupport = _ApAntdetectSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 6),
    _ApAntdetectSupport_Type()
)
apAntdetectSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntdetectSupport.setStatus("current")
_ApAntdetectEnable_Type = Integer32
_ApAntdetectEnable_Object = MibTableColumn
apAntdetectEnable = _ApAntdetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 7),
    _ApAntdetectEnable_Type()
)
apAntdetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAntdetectEnable.setStatus("current")
_ApAntdetectInterval_Type = Integer32
_ApAntdetectInterval_Object = MibTableColumn
apAntdetectInterval = _ApAntdetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 8),
    _ApAntdetectInterval_Type()
)
apAntdetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAntdetectInterval.setStatus("current")
_ApAntdetectState_Type = Integer32
_ApAntdetectState_Object = MibTableColumn
apAntdetectState = _ApAntdetectState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 15, 1, 1, 9),
    _ApAntdetectState_Type()
)
apAntdetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntdetectState.setStatus("current")
_ApAntDetectObjects_ObjectIdentity = ObjectIdentity
apAntDetectObjects = _ApAntDetectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16)
)
_ApAntDetectTable_Object = MibTable
apAntDetectTable = _ApAntDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 1)
)
if mibBuilder.loadTexts:
    apAntDetectTable.setStatus("current")
_ApAntDetectEntry_Object = MibTableRow
apAntDetectEntry = _ApAntDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 1, 1)
)
apAntDetectEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apAntDetectAPMac"),
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apAntDetectAntIndex"),
)
if mibBuilder.loadTexts:
    apAntDetectEntry.setStatus("current")
_ApAntDetectAPMac_Type = MacAddress
_ApAntDetectAPMac_Object = MibTableColumn
apAntDetectAPMac = _ApAntDetectAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 1, 1, 1),
    _ApAntDetectAPMac_Type()
)
apAntDetectAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntDetectAPMac.setStatus("current")
_ApAntDetectAntIndex_Type = Integer32
_ApAntDetectAntIndex_Object = MibTableColumn
apAntDetectAntIndex = _ApAntDetectAntIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 1, 1, 2),
    _ApAntDetectAntIndex_Type()
)
apAntDetectAntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntDetectAntIndex.setStatus("current")
_ApAntDetectDesc_Type = DisplayString
_ApAntDetectDesc_Object = MibTableColumn
apAntDetectDesc = _ApAntDetectDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 1, 1, 3),
    _ApAntDetectDesc_Type()
)
apAntDetectDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntDetectDesc.setStatus("current")
_ApAntDetectRadioId_Type = DisplayString
_ApAntDetectRadioId_Object = MibTableColumn
apAntDetectRadioId = _ApAntDetectRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 1, 1, 4),
    _ApAntDetectRadioId_Type()
)
apAntDetectRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntDetectRadioId.setStatus("current")
_ApAntDetectStatus_Type = Integer32
_ApAntDetectStatus_Object = MibTableColumn
apAntDetectStatus = _ApAntDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 1, 1, 5),
    _ApAntDetectStatus_Type()
)
apAntDetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntDetectStatus.setStatus("current")
_ApAntDetectCfgTable_Object = MibTable
apAntDetectCfgTable = _ApAntDetectCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 2)
)
if mibBuilder.loadTexts:
    apAntDetectCfgTable.setStatus("current")
_ApAntDetectCfgEntry_Object = MibTableRow
apAntDetectCfgEntry = _ApAntDetectCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 2, 1)
)
apAntDetectCfgEntry.setIndexNames(
    (0, "RUIJIE-WLAN-FIT-AP-CF-MIB", "apAntDetectCfgAPMac"),
)
if mibBuilder.loadTexts:
    apAntDetectCfgEntry.setStatus("current")
_ApAntDetectCfgAPMac_Type = MacAddress
_ApAntDetectCfgAPMac_Object = MibTableColumn
apAntDetectCfgAPMac = _ApAntDetectCfgAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 2, 1, 1),
    _ApAntDetectCfgAPMac_Type()
)
apAntDetectCfgAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntDetectCfgAPMac.setStatus("current")
_ApAntDetectCfgSupport_Type = Integer32
_ApAntDetectCfgSupport_Object = MibTableColumn
apAntDetectCfgSupport = _ApAntDetectCfgSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 2, 1, 2),
    _ApAntDetectCfgSupport_Type()
)
apAntDetectCfgSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntDetectCfgSupport.setStatus("current")
_ApAntDetectCfgSwitch_Type = Integer32
_ApAntDetectCfgSwitch_Object = MibTableColumn
apAntDetectCfgSwitch = _ApAntDetectCfgSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 16, 2, 1, 3),
    _ApAntDetectCfgSwitch_Type()
)
apAntDetectCfgSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAntDetectCfgSwitch.setStatus("current")

# Managed Objects groups


# Notification objects

apCPUusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 1)
)
if mibBuilder.loadTexts:
    apCPUusageTooHighTrap.setStatus(
        "current"
    )

apCPUusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 2)
)
if mibBuilder.loadTexts:
    apCPUusageTooHighRecovTrap.setStatus(
        "current"
    )

apMemUsageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 3)
)
if mibBuilder.loadTexts:
    apMemUsageTooHighTrap.setStatus(
        "current"
    )

apMemUsageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 4)
)
if mibBuilder.loadTexts:
    apMemUsageTooHighRecovTrap.setStatus(
        "current"
    )

aPOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 5)
)
if mibBuilder.loadTexts:
    aPOfflineTrap.setStatus(
        "current"
    )

aPOnlineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 6)
)
if mibBuilder.loadTexts:
    aPOnlineTrap.setStatus(
        "current"
    )

aPMtWorkModeChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 7)
)
aPMtWorkModeChgTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkModeBeforeChange"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkModeAfterChange"))
)
if mibBuilder.loadTexts:
    aPMtWorkModeChgTrap.setStatus(
        "current"
    )

apSoftwareUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 8)
)
apSoftwareUpdateFailTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "updateFailReason"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSWVersionBeforeUpdate"))
)
if mibBuilder.loadTexts:
    apSoftwareUpdateFailTrap.setStatus(
        "current"
    )

apSSIDCyperConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 1, 9)
)
apSSIDCyperConflictTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDKey"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSSIDKeyConflict"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apCyperIndex"))
)
if mibBuilder.loadTexts:
    apSSIDCyperConflictTrap.setStatus(
        "current"
    )

aPCoInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 1)
)
aPCoInterfDetectedTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterfAPBSSID"))
)
if mibBuilder.loadTexts:
    aPCoInterfDetectedTrap.setStatus(
        "current"
    )

aPCoInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 2)
)
aPCoInterfClearTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterfAPBSSID"))
)
if mibBuilder.loadTexts:
    aPCoInterfClearTrap.setStatus(
        "current"
    )

aPNerborInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 3)
)
aPNerborInterfDetectedTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterfAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterfAPChannel"))
)
if mibBuilder.loadTexts:
    aPNerborInterfDetectedTrap.setStatus(
        "current"
    )

aPNeiborInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 4)
)
aPNeiborInterfClearTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterfAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterfAPChannel"))
)
if mibBuilder.loadTexts:
    aPNeiborInterfClearTrap.setStatus(
        "current"
    )

staInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 5)
)
staInterfDetectedTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterfStaMac"))
)
if mibBuilder.loadTexts:
    staInterfDetectedTrap.setStatus(
        "current"
    )

staInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 6)
)
staInterfClearTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterfStaMac"))
)
if mibBuilder.loadTexts:
    staInterfClearTrap.setStatus(
        "current"
    )

otherDeviceInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 7)
)
otherDeviceInterfDetectedTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"))
)
if mibBuilder.loadTexts:
    otherDeviceInterfDetectedTrap.setStatus(
        "current"
    )

otherDevInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 8)
)
otherDevInterfClearTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"))
)
if mibBuilder.loadTexts:
    otherDevInterfClearTrap.setStatus(
        "current"
    )

apRadioDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 9)
)
apRadioDownTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterruptReason"))
)
if mibBuilder.loadTexts:
    apRadioDownTrap.setStatus(
        "current"
    )

apRadioDownRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 10)
)
apRadioDownRecovTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterruptReason"))
)
if mibBuilder.loadTexts:
    apRadioDownRecovTrap.setStatus(
        "current"
    )

aPStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 11)
)
aPStaFullTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apPermitAssoUser"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAssoFailReason"))
)
if mibBuilder.loadTexts:
    aPStaFullTrap.setStatus(
        "current"
    )

aPStaFullRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 12)
)
aPStaFullRecoverTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apPermitAssoUser"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAssoFailReason"))
)
if mibBuilder.loadTexts:
    aPStaFullRecoverTrap.setStatus(
        "current"
    )

aPMtRdoChanlChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 13)
)
aPMtRdoChanlChgTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apChannelBeforeChange"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apChannelAfterChange"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apChanChangeMode"))
)
if mibBuilder.loadTexts:
    aPMtRdoChanlChgTrap.setStatus(
        "current"
    )

apSpeciusDeviceDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 14)
)
apSpeciusDeviceDetectTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSpeciousDeviceMac"))
)
if mibBuilder.loadTexts:
    apSpeciusDeviceDetectTrap.setStatus(
        "current"
    )

apRadioRxPackagesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 15)
)
apRadioRxPackagesTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAPRadioId"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apRevPackages"))
)
if mibBuilder.loadTexts:
    apRadioRxPackagesTrap.setStatus(
        "current"
    )

apCPUUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 16)
)
apCPUUsageTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apCPUUsage"))
)
if mibBuilder.loadTexts:
    apCPUUsageTrap.setStatus(
        "current"
    )

apSTARefusedRSSITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 17)
)
apSTARefusedRSSITrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apRSSI"))
)
if mibBuilder.loadTexts:
    apSTARefusedRSSITrap.setStatus(
        "current"
    )

apSTARefusedRatesetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 18)
)
apSTARefusedRatesetTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    apSTARefusedRatesetTrap.setStatus(
        "current"
    )

apFindAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 19)
)
apFindAttackTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAttackReason"))
)
if mibBuilder.loadTexts:
    apFindAttackTrap.setStatus(
        "current"
    )

wlanSecurityChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 20)
)
wlanSecurityChgTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanId"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanSecurityModeBeforeChg"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanSecurityModeAfterChg"))
)
if mibBuilder.loadTexts:
    wlanSecurityChgTrap.setStatus(
        "current"
    )

apRadioFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 21)
)
apRadioFailureTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apInterruptReason"))
)
if mibBuilder.loadTexts:
    apRadioFailureTrap.setStatus(
        "current"
    )

apIllegalApTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 22)
)
apIllegalApTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApChannel"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApRSSI"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapWorkingApMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapWorkingApBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApType"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApSSID"))
)
if mibBuilder.loadTexts:
    apIllegalApTrap.setStatus(
        "current"
    )

apIllegalApRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 23)
)
apIllegalApRecoverTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApChannel"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApRSSI"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapWorkingApMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapWorkingApBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApType"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apTrapIllegalApSSID"))
)
if mibBuilder.loadTexts:
    apIllegalApRecoverTrap.setStatus(
        "current"
    )

apStaAssocFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 24)
)
apStaAssocFailTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAPRadioId"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAPRadioType"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAssocAuthMode"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaRSSI"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAssocFailReason"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPChannel"))
)
if mibBuilder.loadTexts:
    apStaAssocFailTrap.setStatus(
        "current"
    )

apSpectralInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 25)
)
apSpectralInfoTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSpectralInfoApMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSpectralInfoType"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSpectralInfoFreq"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSpectralInfoRssi"))
)
if mibBuilder.loadTexts:
    apSpectralInfoTrap.setStatus(
        "current"
    )

apCounterMeasureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 2, 26)
)
apCounterMeasureTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apCounterMeasureApMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apCounterMeasureBssid"))
)
if mibBuilder.loadTexts:
    apCounterMeasureTrap.setStatus(
        "current"
    )

apStaAuthErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 3, 1)
)
apStaAuthErrorTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAuthMode"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAuthFailReason"))
)
if mibBuilder.loadTexts:
    apStaAuthErrorTrap.setStatus(
        "current"
    )

apStAssociationFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 3, 2)
)
apStAssociationFailTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAssoFailReason"))
)
if mibBuilder.loadTexts:
    apStAssociationFailTrap.setStatus(
        "current"
    )

ruijieNotifyWebAuthMacTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 3, 3)
)
ruijieNotifyWebAuthMacTrap.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "webAuthTlvCount"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "webAuthTlvString"))
)
if mibBuilder.loadTexts:
    ruijieNotifyWebAuthMacTrap.setStatus(
        "current"
    )

userwithInvalidCerficationInbreakNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 4, 1)
)
userwithInvalidCerficationInbreakNetwork.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    userwithInvalidCerficationInbreakNetwork.setStatus(
        "current"
    )

stationRepititiveAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 4, 2)
)
stationRepititiveAttack.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    stationRepititiveAttack.setStatus(
        "current"
    )

tamperAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 4, 3)
)
tamperAttack.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    tamperAttack.setStatus(
        "current"
    )

lowSafeLevelAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 4, 4)
)
lowSafeLevelAttack.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    lowSafeLevelAttack.setStatus(
        "current"
    )

addressRedirectionAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 4, 5)
)
addressRedirectionAttack.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPRadioIfInfo"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPBSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWorkingAPSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"))
)
if mibBuilder.loadTexts:
    addressRedirectionAttack.setStatus(
        "current"
    )

apEgAnnounceApReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 5, 1)
)
apEgAnnounceApReport.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAPMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apApName"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apApLocation"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apApUptime"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apApChannel2"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apApChannel5"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apApUserNum"))
)
if mibBuilder.loadTexts:
    apEgAnnounceApReport.setStatus(
        "current"
    )

apEgAnnounceSsidReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 5, 2)
)
apEgAnnounceSsidReport.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAPMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSsidName"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSsidIndex"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSsidDot11Auth"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSsidSecurityMode"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apSsidAuthenMode"))
)
if mibBuilder.loadTexts:
    apEgAnnounceSsidReport.setStatus(
        "current"
    )

apEgAnnounceApDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 5, 3)
)
apEgAnnounceApDown.setObjects(
    ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAPMac")
)
if mibBuilder.loadTexts:
    apEgAnnounceApDown.setStatus(
        "current"
    )

apEgAnnounceStaUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 5, 4)
)
apEgAnnounceStaUp.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAPMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaRSSI"))
)
if mibBuilder.loadTexts:
    apEgAnnounceStaUp.setStatus(
        "current"
    )

apEgAnnounceStaDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 81, 0, 5, 5)
)
apEgAnnounceStaDown.setObjects(
      *(("RUIJIE-WLAN-FIT-AP-CF-MIB", "apAPMac"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaMacAddr"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apWlanSSID"),
        ("RUIJIE-WLAN-FIT-AP-CF-MIB", "apStaRSSI"))
)
if mibBuilder.loadTexts:
    apEgAnnounceStaDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WLAN-FIT-AP-CF-MIB",
    **{"ruijieFitApMibModule": ruijieFitApMibModule,
       "apRuijieAlarmTraps": apRuijieAlarmTraps,
       "apSystemAlarmTraps": apSystemAlarmTraps,
       "apCPUusageTooHighTrap": apCPUusageTooHighTrap,
       "apCPUusageTooHighRecovTrap": apCPUusageTooHighRecovTrap,
       "apMemUsageTooHighTrap": apMemUsageTooHighTrap,
       "apMemUsageTooHighRecovTrap": apMemUsageTooHighRecovTrap,
       "aPOfflineTrap": aPOfflineTrap,
       "aPOnlineTrap": aPOnlineTrap,
       "aPMtWorkModeChgTrap": aPMtWorkModeChgTrap,
       "apSoftwareUpdateFailTrap": apSoftwareUpdateFailTrap,
       "apSSIDCyperConflictTrap": apSSIDCyperConflictTrap,
       "apWirelessAlarmTraps": apWirelessAlarmTraps,
       "aPCoInterfDetectedTrap": aPCoInterfDetectedTrap,
       "aPCoInterfClearTrap": aPCoInterfClearTrap,
       "aPNerborInterfDetectedTrap": aPNerborInterfDetectedTrap,
       "aPNeiborInterfClearTrap": aPNeiborInterfClearTrap,
       "staInterfDetectedTrap": staInterfDetectedTrap,
       "staInterfClearTrap": staInterfClearTrap,
       "otherDeviceInterfDetectedTrap": otherDeviceInterfDetectedTrap,
       "otherDevInterfClearTrap": otherDevInterfClearTrap,
       "apRadioDownTrap": apRadioDownTrap,
       "apRadioDownRecovTrap": apRadioDownRecovTrap,
       "aPStaFullTrap": aPStaFullTrap,
       "aPStaFullRecoverTrap": aPStaFullRecoverTrap,
       "aPMtRdoChanlChgTrap": aPMtRdoChanlChgTrap,
       "apSpeciusDeviceDetectTrap": apSpeciusDeviceDetectTrap,
       "apRadioRxPackagesTrap": apRadioRxPackagesTrap,
       "apCPUUsageTrap": apCPUUsageTrap,
       "apSTARefusedRSSITrap": apSTARefusedRSSITrap,
       "apSTARefusedRatesetTrap": apSTARefusedRatesetTrap,
       "apFindAttackTrap": apFindAttackTrap,
       "wlanSecurityChgTrap": wlanSecurityChgTrap,
       "apRadioFailureTrap": apRadioFailureTrap,
       "apIllegalApTrap": apIllegalApTrap,
       "apIllegalApRecoverTrap": apIllegalApRecoverTrap,
       "apStaAssocFailTrap": apStaAssocFailTrap,
       "apSpectralInfoTrap": apSpectralInfoTrap,
       "apCounterMeasureTrap": apCounterMeasureTrap,
       "apStaAnnounceTraps": apStaAnnounceTraps,
       "apStaAuthErrorTrap": apStaAuthErrorTrap,
       "apStAssociationFailTrap": apStAssociationFailTrap,
       "ruijieNotifyWebAuthMacTrap": ruijieNotifyWebAuthMacTrap,
       "apWAPISecurityAlarmTraps": apWAPISecurityAlarmTraps,
       "userwithInvalidCerficationInbreakNetwork": userwithInvalidCerficationInbreakNetwork,
       "stationRepititiveAttack": stationRepititiveAttack,
       "tamperAttack": tamperAttack,
       "lowSafeLevelAttack": lowSafeLevelAttack,
       "addressRedirectionAttack": addressRedirectionAttack,
       "apEgAnnounceTraps": apEgAnnounceTraps,
       "apEgAnnounceApReport": apEgAnnounceApReport,
       "apEgAnnounceSsidReport": apEgAnnounceSsidReport,
       "apEgAnnounceApDown": apEgAnnounceApDown,
       "apEgAnnounceStaUp": apEgAnnounceStaUp,
       "apEgAnnounceStaDown": apEgAnnounceStaDown,
       "apSystemInfoConfigObjects": apSystemInfoConfigObjects,
       "apGeneralInfoConfigObjects": apGeneralInfoConfigObjects,
       "apGeneralInfoConfigTable": apGeneralInfoConfigTable,
       "apGeneralInfoConfigTableEntry": apGeneralInfoConfigTableEntry,
       "apSysNEId": apSysNEId,
       "apSysName": apSysName,
       "apStatWindowTime": apStatWindowTime,
       "apSampleTime": apSampleTime,
       "apRtCollectOnoff": apRtCollectOnoff,
       "apSysRestart": apSysRestart,
       "apSysReset": apSysReset,
       "apGeneralInfoReadObjects": apGeneralInfoReadObjects,
       "apGeneralCfgInfoReadTable": apGeneralCfgInfoReadTable,
       "apGeneralCfgInfoReadTableEntry": apGeneralCfgInfoReadTableEntry,
       "apSysDescr": apSysDescr,
       "apSysManufacture": apSysManufacture,
       "apSerialNumber": apSerialNumber,
       "apSysModel": apSysModel,
       "apSysUpTime": apSysUpTime,
       "apSysOnlineTime": apSysOnlineTime,
       "apSysIPAddress": apSysIPAddress,
       "apSysIPNetMask": apSysIPNetMask,
       "apSysGateWayAddr": apSysGateWayAddr,
       "apSysMacAddrConnectToAC": apSysMacAddrConnectToAC,
       "apSoftwareName": apSoftwareName,
       "apSoftwareVersion": apSoftwareVersion,
       "apSoftwareVendor": apSoftwareVendor,
       "apCPUType": apCPUType,
       "apMemoryType": apMemoryType,
       "apMemorySize": apMemorySize,
       "apFlashSize": apFlashSize,
       "apGeneralStatusCFGObjects": apGeneralStatusCFGObjects,
       "apGeneralStatusCFGTable": apGeneralStatusCFGTable,
       "apGeneralStatusCFGTableEntry": apGeneralStatusCFGTableEntry,
       "apGeneralStatusCFGAPName": apGeneralStatusCFGAPName,
       "apGeneralStatusCFGACAssociateStatus": apGeneralStatusCFGACAssociateStatus,
       "apGeneralStatusCFGMonitorMode": apGeneralStatusCFGMonitorMode,
       "apGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac": apGeneralStatusCFGGeneralStatusCFGAssoStatusAPMac,
       "apGeneralStatusCFGACHbAssocStatus": apGeneralStatusCFGACHbAssocStatus,
       "apGeneralStatusCFGScanType": apGeneralStatusCFGScanType,
       "apGeneralStatusCFGAssocTimes": apGeneralStatusCFGAssocTimes,
       "apGeneralStatusCFGAssocSuccessTimes": apGeneralStatusCFGAssocSuccessTimes,
       "apGeneralStatusCFGAssocFailTimes": apGeneralStatusCFGAssocFailTimes,
       "apGeneralStatusCFG24GSignalStrength": apGeneralStatusCFG24GSignalStrength,
       "apGeneralStatusCFG5GSignalStrength": apGeneralStatusCFG5GSignalStrength,
       "apGeneralStatusCFGTotalRxBytes": apGeneralStatusCFGTotalRxBytes,
       "apGeneralStatusCFGTotalTxBytes": apGeneralStatusCFGTotalTxBytes,
       "apInterfaceConfigObjects": apInterfaceConfigObjects,
       "apInterfaceNumberObjects": apInterfaceNumberObjects,
       "apInterfaceNumberTable": apInterfaceNumberTable,
       "apInterfaceNumberTableEntry": apInterfaceNumberTableEntry,
       "apIfNumber": apIfNumber,
       "apBSSIDNum": apBSSIDNum,
       "apInterfaceRGMIIcfgObjects": apInterfaceRGMIIcfgObjects,
       "apInterfaceRGMIIconfigTable": apInterfaceRGMIIconfigTable,
       "apInterfaceRGMIIconfigTableEntry": apInterfaceRGMIIconfigTableEntry,
       "apIfLocalRGMIINum": apIfLocalRGMIINum,
       "apIfRGMIIDescr": apIfRGMIIDescr,
       "apIfRGMIIType": apIfRGMIIType,
       "apIfRGMIIMtu": apIfRGMIIMtu,
       "apIfRGMIISpeed": apIfRGMIISpeed,
       "apIfRGMIIPhysAddress": apIfRGMIIPhysAddress,
       "apIfRGMIIAdminStatusEnable": apIfRGMIIAdminStatusEnable,
       "apIfRGMIIOperStatus": apIfRGMIIOperStatus,
       "apIfRGMIILastChange": apIfRGMIILastChange,
       "apInterfaceWirelesscfgObjects": apInterfaceWirelesscfgObjects,
       "apInterfaceWirelessconfigTable": apInterfaceWirelessconfigTable,
       "apInterfaceWirelessconfigTableEntry": apInterfaceWirelessconfigTableEntry,
       "apIfWireDescr": apIfWireDescr,
       "apIfWireType": apIfWireType,
       "apIfWireMtu": apIfWireMtu,
       "apIfWireSpeed": apIfWireSpeed,
       "apIfWirePhysAddress": apIfWirePhysAddress,
       "apIfWireAdminStatusEnable": apIfWireAdminStatusEnable,
       "apIfWireOperStatus": apIfWireOperStatus,
       "apIfWireLastChange": apIfWireLastChange,
       "apIfWireChannelAutoSelectEnable": apIfWireChannelAutoSelectEnable,
       "apIfWireRadioChannelConfig": apIfWireRadioChannelConfig,
       "apIfWireRadioChannelUsing": apIfWireRadioChannelUsing,
       "apIfWireCurrRadioModeSupport": apIfWireCurrRadioModeSupport,
       "apIfWireRadioModeConfig": apIfWireRadioModeConfig,
       "apIfWireTransmitSpeedConfig": apIfWireTransmitSpeedConfig,
       "apIfWireMaxTxPwrLvl": apIfWireMaxTxPwrLvl,
       "apIfWirePwrAttRange": apIfWirePwrAttRange,
       "apIfWirePwrAttValue": apIfWirePwrAttValue,
       "apIfWireAntennaGain": apIfWireAntennaGain,
       "apIfWirePowerMgmtEnable": apIfWirePowerMgmtEnable,
       "apTxPwr": apTxPwr,
       "apIfWireMaxStationNumPermitted": apIfWireMaxStationNumPermitted,
       "apIfWireAMPDUEnabled": apIfWireAMPDUEnabled,
       "apIfWireBWMode": apIfWireBWMode,
       "apIfWireShortGIEnabled": apIfWireShortGIEnabled,
       "apIfWireIs11nOnly": apIfWireIs11nOnly,
       "apIfWireBeaconIntvl": apIfWireBeaconIntvl,
       "apIfWireDtimIntvl": apIfWireDtimIntvl,
       "apIfWireRtsThreshold": apIfWireRtsThreshold,
       "apIfWireFragThreshlod": apIfWireFragThreshlod,
       "apIfWirePreambleLen": apIfWirePreambleLen,
       "apAntennaReceiveMask": apAntennaReceiveMask,
       "apAntennaTransmitMask": apAntennaTransmitMask,
       "apIfWireAMSDUEnabled": apIfWireAMSDUEnabled,
       "apIfwireMcsSuppIndex": apIfwireMcsSuppIndex,
       "apIfwireMcsMandIndex": apIfwireMcsMandIndex,
       "apIfwire11nSuppEnable": apIfwire11nSuppEnable,
       "apShtRetryThld": apShtRetryThld,
       "apLongRetryThld": apLongRetryThld,
       "apIfWireResponseRssi": apIfWireResponseRssi,
       "apIfWireMaxStationLimit": apIfWireMaxStationLimit,
       "apIfWireLinkscan": apIfWireLinkscan,
       "apIfWireRadioChannelutilization": apIfWireRadioChannelutilization,
       "apSSIDConfigObjects": apSSIDConfigObjects,
       "apSSIDListCreateTable": apSSIDListCreateTable,
       "apSSIDListCreateTableEntry": apSSIDListCreateTableEntry,
       "apSSIDAPMac": apSSIDAPMac,
       "apSSIDRadioId": apSSIDRadioId,
       "apSSIDListName": apSSIDListName,
       "apListBSSIDAddr": apListBSSIDAddr,
       "apSSIDListStatus": apSSIDListStatus,
       "apSSIDConfigTable": apSSIDConfigTable,
       "apSSIDConfigTableEntry": apSSIDConfigTableEntry,
       "apSSIDName": apSSIDName,
       "apSSIDEnabled": apSSIDEnabled,
       "apSSIDHidden": apSSIDHidden,
       "apStaIsolate": apStaIsolate,
       "apDot11Auth": apDot11Auth,
       "apsecurityMode": apsecurityMode,
       "apAuthenMode": apAuthenMode,
       "apSecurityCiphers": apSecurityCiphers,
       "apVlanId": apVlanId,
       "apVlanIpAddr": apVlanIpAddr,
       "apMaxSimultUsers": apMaxSimultUsers,
       "apStaUplinkMaxRate": apStaUplinkMaxRate,
       "apStaDwlinkMaxRate": apStaDwlinkMaxRate,
       "apSSIDCfgStatus": apSSIDCfgStatus,
       "apSecurityConfigObjects": apSecurityConfigObjects,
       "apSecurityConfigTable": apSecurityConfigTable,
       "apSecurityConfigTableEntry": apSecurityConfigTableEntry,
       "apWEPCipherKeyIndex": apWEPCipherKeyIndex,
       "apWEPCipherKeyValue": apWEPCipherKeyValue,
       "apWEPCipherKeyCharType": apWEPCipherKeyCharType,
       "apPSKCipherKeyValue": apPSKCipherKeyValue,
       "apPSKCipherKeyCharType": apPSKCipherKeyCharType,
       "apWAPIAuthModeEnable": apWAPIAuthModeEnable,
       "apWAPIASIPAddress": apWAPIASIPAddress,
       "apWAPIIsInstalledCer": apWAPIIsInstalledCer,
       "apWlanSecurityTable": apWlanSecurityTable,
       "apWlanSecurityTableEntry": apWlanSecurityTableEntry,
       "apWlanSecurityAPMac": apWlanSecurityAPMac,
       "apWlanSecurityRadioId": apWlanSecurityRadioId,
       "apWlanSecurityWlanId": apWlanSecurityWlanId,
       "apWlanSecurityAuthenMode": apWlanSecurityAuthenMode,
       "apWAPIExternInfoConfigObjects": apWAPIExternInfoConfigObjects,
       "apWAPIExternInfoConfigTable": apWAPIExternInfoConfigTable,
       "apWAPIExternInfoConfigTableEntry": apWAPIExternInfoConfigTableEntry,
       "apWAPIConfigVersion": apWAPIConfigVersion,
       "apWAPIControlledAuthControl": apWAPIControlledAuthControl,
       "apWAPIControlledPortControl": apWAPIControlledPortControl,
       "apWAPIOptionImplemented": apWAPIOptionImplemented,
       "apWAPIPreauthenticationImplemented": apWAPIPreauthenticationImplemented,
       "apWAPIEnabled": apWAPIEnabled,
       "apWAPIPreauthEnabled": apWAPIPreauthEnabled,
       "apWAPIUnicastKeysSupported": apWAPIUnicastKeysSupported,
       "apWAPIUnicastRekeyMethod": apWAPIUnicastRekeyMethod,
       "apWAPIUnicastRekeyTime": apWAPIUnicastRekeyTime,
       "apWAPIUnicastRekeyPackets": apWAPIUnicastRekeyPackets,
       "apWAPIMulticastCipher": apWAPIMulticastCipher,
       "apWAPIMulticastRekeyMethod": apWAPIMulticastRekeyMethod,
       "apWAPIMulticastRekeyTime": apWAPIMulticastRekeyTime,
       "apWAPIMulticastRekeyPackets": apWAPIMulticastRekeyPackets,
       "apWAPIMulticastRekeyStrict": apWAPIMulticastRekeyStrict,
       "apWAPIPSKValue": apWAPIPSKValue,
       "apWAPIPSKPassPhrase": apWAPIPSKPassPhrase,
       "apWAPICertificateUpdateCount": apWAPICertificateUpdateCount,
       "apWAPIMulticastUpdateCount": apWAPIMulticastUpdateCount,
       "apWAPIUnicastUpdateCount": apWAPIUnicastUpdateCount,
       "apWAPIMulticastCipherSize": apWAPIMulticastCipherSize,
       "apWAPIBKLifetime": apWAPIBKLifetime,
       "apWAPIBKReauthThreshold": apWAPIBKReauthThreshold,
       "apWAPISATimeout": apWAPISATimeout,
       "apWAPIAuthSuiteSelected": apWAPIAuthSuiteSelected,
       "apWAPIUnicastCipherSelected": apWAPIUnicastCipherSelected,
       "apWAPIMulticastCipherSelected": apWAPIMulticastCipherSelected,
       "apWAPIBKIDUsed": apWAPIBKIDUsed,
       "apWAPIAuthSuiteRequested": apWAPIAuthSuiteRequested,
       "apWAPIUnicastCipherRequested": apWAPIUnicastCipherRequested,
       "apWAPIMulticastCipherRequested": apWAPIMulticastCipherRequested,
       "apWAPIUnicastCipher": apWAPIUnicastCipher,
       "apWAPIUnicastCipherEnabled": apWAPIUnicastCipherEnabled,
       "apWAPIUnicastCipherSize": apWAPIUnicastCipherSize,
       "apWAPIAuthenticationSuite": apWAPIAuthenticationSuite,
       "apWAPIAuthenticationSuiteEnabled": apWAPIAuthenticationSuiteEnabled,
       "apWAPIAECertFile": apWAPIAECertFile,
       "apWAPICACertFile": apWAPICACertFile,
       "apWAPIASUCertFile": apWAPIASUCertFile,
       "apStationInfoGetObjects": apStationInfoGetObjects,
       "apStationInfoGetTable": apStationInfoGetTable,
       "apStationInfoGetTableEntry": apStationInfoGetTableEntry,
       "apStaMAC": apStaMAC,
       "apStaWMMAttr": apStaWMMAttr,
       "apStaIPAddress": apStaIPAddress,
       "apStaRadioMode": apStaRadioMode,
       "apStaRadioChannel": apStaRadioChannel,
       "apAPTxRates": apAPTxRates,
       "apStaPowerSaveMode": apStaPowerSaveMode,
       "apStaVlanId": apStaVlanId,
       "apStaSSIDName": apStaSSIDName,
       "apAPId": apAPId,
       "apStaDot11Auth": apStaDot11Auth,
       "apsecurity": apsecurity,
       "apStaAuthenMode": apStaAuthenMode,
       "apStaSecurityCiphers": apStaSecurityCiphers,
       "apAPIdMac": apAPIdMac,
       "apStaMode": apStaMode,
       "apStaBand": apStaBand,
       "apStationRefusedAccessTable": apStationRefusedAccessTable,
       "apStationRefusedAccessTableEntry": apStationRefusedAccessTableEntry,
       "apRefusedStaMAC": apRefusedStaMAC,
       "apFailReason": apFailReason,
       "apRefusedTime": apRefusedTime,
       "apRefusedAPMac": apRefusedAPMac,
       "apStationRadiusInfoTable": apStationRadiusInfoTable,
       "apStationRadiusInfoTableEntry": apStationRadiusInfoTableEntry,
       "apUserMacAddress": apUserMacAddress,
       "apUserIpAddress": apUserIpAddress,
       "apUserLoginName": apUserLoginName,
       "apUserLoginTime": apUserLoginTime,
       "apUserOnlineTime": apUserOnlineTime,
       "apStationInfoJsonTable": apStationInfoJsonTable,
       "apStationInfoJsonEntry": apStationInfoJsonEntry,
       "apStationInfoJsonMacAddr": apStationInfoJsonMacAddr,
       "apStationInfoJsonContent": apStationInfoJsonContent,
       "apQOSInfoConfigObjects": apQOSInfoConfigObjects,
       "apQOSWirelessConfigObjects": apQOSWirelessConfigObjects,
       "apQOSWirelessConfigTable": apQOSWirelessConfigTable,
       "apQOSWirelessConfigTableEntry": apQOSWirelessConfigTableEntry,
       "apWireQoSTrafficClassId": apWireQoSTrafficClassId,
       "apWireQosAIFS": apWireQosAIFS,
       "apWireQoSCWmin": apWireQoSCWmin,
       "apWireQoSCWmax": apWireQoSCWmax,
       "apWireQoSTXOPLim": apWireQoSTXOPLim,
       "apQOSBaseInfoConfigObjects": apQOSBaseInfoConfigObjects,
       "apQOSBaseInfoConfigTable": apQOSBaseInfoConfigTable,
       "apQOSBaseInfoConfigTableEntry": apQOSBaseInfoConfigTableEntry,
       "apBaseQoSTrafficClass": apBaseQoSTrafficClass,
       "apBaseQoSEnabled": apBaseQoSEnabled,
       "apBaseQoSBW": apBaseQoSBW,
       "apBaseQoSResPercent": apBaseQoSResPercent,
       "apBaseQoSsharedBW": apBaseQoSsharedBW,
       "apBaseQoSsharedBWPercent": apBaseQoSsharedBWPercent,
       "apBaseQoSSchedAlgName": apBaseQoSSchedAlgName,
       "apBaseQoSResPolicyEnabled": apBaseQoSResPolicyEnabled,
       "apBaseQoSResPolicyName": apBaseQoSResPolicyName,
       "apBaseQoSBackgroundSvcAvgSpeed": apBaseQoSBackgroundSvcAvgSpeed,
       "apBaseQoSBackgroundSvcMaxBurst": apBaseQoSBackgroundSvcMaxBurst,
       "apBaseQoSBackgroundSvcPriority": apBaseQoSBackgroundSvcPriority,
       "apBaseQoSBackgroundSvcResPriority": apBaseQoSBackgroundSvcResPriority,
       "apBaseQoSBestEffortSvcAvgSpeed": apBaseQoSBestEffortSvcAvgSpeed,
       "apBaseQoSBestEffortSvcMaxBurst": apBaseQoSBestEffortSvcMaxBurst,
       "apBaseQoSBestEffortSvcPriority": apBaseQoSBestEffortSvcPriority,
       "apBaseQoSBestEffortSvcResPriority": apBaseQoSBestEffortSvcResPriority,
       "apBaseQoSVoiceSvcAvgSpeed": apBaseQoSVoiceSvcAvgSpeed,
       "apBaseQoSVoiceSvcMaxBurst": apBaseQoSVoiceSvcMaxBurst,
       "apBaseQoSVoiceSvcPriority": apBaseQoSVoiceSvcPriority,
       "apBaseQoSVoiceSvcResPriority": apBaseQoSVoiceSvcResPriority,
       "apBaseQoSVideoSvcAvgSpeed": apBaseQoSVideoSvcAvgSpeed,
       "apBaseQoSVideoSvcMaxBurst": apBaseQoSVideoSvcMaxBurst,
       "apBaseQoSVideoSvcPriority": apBaseQoSVideoSvcPriority,
       "apBaseQoSVideoSvcResPriority": apBaseQoSVideoSvcResPriority,
       "apQOSBackgroundCfgObjects": apQOSBackgroundCfgObjects,
       "apQOSBackgroundCfgTable": apQOSBackgroundCfgTable,
       "apQOSBackgroundCfgTableEntry": apQOSBackgroundCfgTableEntry,
       "apQOSBgMaxSvcCnt": apQOSBgMaxSvcCnt,
       "apQOSBgSvcBW": apQOSBgSvcBW,
       "apQOSBgSvcBWPercent": apQOSBgSvcBWPercent,
       "apQOSBgIsUseWREDAlg": apQOSBgIsUseWREDAlg,
       "apQOSBgIsUseTrafficShaping": apQOSBgIsUseTrafficShaping,
       "apQOSBestEffortCfgObjects": apQOSBestEffortCfgObjects,
       "apQOSBestEffortCfgTable": apQOSBestEffortCfgTable,
       "apQOSBestEffortCfgTableEntry": apQOSBestEffortCfgTableEntry,
       "apQOSBeMaxSvcCnt": apQOSBeMaxSvcCnt,
       "apQOSBeSvcBW": apQOSBeSvcBW,
       "apQOSBeSvcBWPercent": apQOSBeSvcBWPercent,
       "apQOSBeIsUseWREDAlg": apQOSBeIsUseWREDAlg,
       "apQOSBeIsUseTrafficShaping": apQOSBeIsUseTrafficShaping,
       "apQOSVoiceInfoCfgObjects": apQOSVoiceInfoCfgObjects,
       "apQOSVoiceInfoCfgTable": apQOSVoiceInfoCfgTable,
       "apQOSVoiceInfoCfgTableEntry": apQOSVoiceInfoCfgTableEntry,
       "apQOSVoiceMaxSvcCnt": apQOSVoiceMaxSvcCnt,
       "apQOSVoiceSvcBW": apQOSVoiceSvcBW,
       "apQOSVoiceSvcBWPercent": apQOSVoiceSvcBWPercent,
       "apQOSVoiceIsUseStreamBasedQueue": apQOSVoiceIsUseStreamBasedQueue,
       "apQOSVoiceStreamMaxQueueLen": apQOSVoiceStreamMaxQueueLen,
       "apQOSVoiceStreamAvgSpeed": apQOSVoiceStreamAvgSpeed,
       "apQOSVoiceStreamMaxBurst": apQOSVoiceStreamMaxBurst,
       "apQOSVoiceIsUseWREDAlg": apQOSVoiceIsUseWREDAlg,
       "apQOSVoiceIsUseTrafficShaping": apQOSVoiceIsUseTrafficShaping,
       "apQOSVideoInfoCfgObjects": apQOSVideoInfoCfgObjects,
       "apQOSVideoInfoCfgTable": apQOSVideoInfoCfgTable,
       "apQOSVideoInfoCfgTableEntry": apQOSVideoInfoCfgTableEntry,
       "apQOSVideoMaxSvcCnt": apQOSVideoMaxSvcCnt,
       "apQOSVideoSvcBW": apQOSVideoSvcBW,
       "apQOSVideoSvcBWPercent": apQOSVideoSvcBWPercent,
       "apQOSVideoIsUseStreamBasedQueue": apQOSVideoIsUseStreamBasedQueue,
       "apQOSVideoStreamMaxQueueLen": apQOSVideoStreamMaxQueueLen,
       "apQOSVideoStreamAvgSpeed": apQOSVideoStreamAvgSpeed,
       "apQOSVideoStreamMaxBurst": apQOSVideoStreamMaxBurst,
       "apQOSVideoIsUseWREDAlg": apQOSVideoIsUseWREDAlg,
       "apQOSVideoIsUseTrafficShaping": apQOSVideoIsUseTrafficShaping,
       "apQOSWMMConfigObjects": apQOSWMMConfigObjects,
       "apQOSWMMConfigTable": apQOSWMMConfigTable,
       "apQOSWMMConfigTableEntry": apQOSWMMConfigTableEntry,
       "apQOSMode": apQOSMode,
       "apQOSUpdateSeq": apQOSUpdateSeq,
       "apQOSSvpAcIndex": apQOSSvpAcIndex,
       "apQOSUapsd": apQOSUapsd,
       "apQOSAcIndx1": apQOSAcIndx1,
       "apQOSAcIndx2": apQOSAcIndx2,
       "apQOSAcIndx3": apQOSAcIndx3,
       "apQOSAcIndx4": apQOSAcIndx4,
       "apQOSAifsn1": apQOSAifsn1,
       "apQOSAifsn2": apQOSAifsn2,
       "apQOSAifsn3": apQOSAifsn3,
       "apQOSAifsn4": apQOSAifsn4,
       "apQOSEcwMin1": apQOSEcwMin1,
       "apQOSEcwMin2": apQOSEcwMin2,
       "apQOSEcwMin3": apQOSEcwMin3,
       "apQOSEcwMin4": apQOSEcwMin4,
       "apQOSEcwMax1": apQOSEcwMax1,
       "apQOSEcwMax2": apQOSEcwMax2,
       "apQOSEcwMax3": apQOSEcwMax3,
       "apQOSEcwMax4": apQOSEcwMax4,
       "apQOSTxopLmt1": apQOSTxopLmt1,
       "apQOSTxopLmt2": apQOSTxopLmt2,
       "apQOSTxopLmt3": apQOSTxopLmt3,
       "apQOSTxopLmt4": apQOSTxopLmt4,
       "apQOSAcmAndAck1": apQOSAcmAndAck1,
       "apQOSAcmAndAck2": apQOSAcmAndAck2,
       "apQOSAcmAndAck3": apQOSAcmAndAck3,
       "apQOSAcmAndAck4": apQOSAcmAndAck4,
       "apAlarmParamConfigEntry": apAlarmParamConfigEntry,
       "apStaInterfNumThreshhd": apStaInterfNumThreshhd,
       "apAPCoInterfThreshhd": apAPCoInterfThreshhd,
       "apAPNeiborInterfThreshhd": apAPNeiborInterfThreshhd,
       "apCPUusageThreshhd": apCPUusageThreshhd,
       "apMemUsageThreshhd": apMemUsageThreshhd,
       "acUserExcepOfflineTimes": acUserExcepOfflineTimes,
       "acAuthReqTimes": acAuthReqTimes,
       "acAuthSuccessTimes": acAuthSuccessTimes,
       "acAuthReqFailTimes": acAuthReqFailTimes,
       "acDisconnectOnlineUsersCount": acDisconnectOnlineUsersCount,
       "acOnlineUserNum": acOnlineUserNum,
       "apVLANConfigObjects": apVLANConfigObjects,
       "apVLANConfigTable": apVLANConfigTable,
       "apVLANConfigTableEntry": apVLANConfigTableEntry,
       "apVLANID": apVLANID,
       "apVlanCfgStatus": apVlanCfgStatus,
       "apStatisticsInfoReadObjects": apStatisticsInfoReadObjects,
       "apSysCapabilityStatisticsObjects": apSysCapabilityStatisticsObjects,
       "apSysCapabilityStatisticsTable": apSysCapabilityStatisticsTable,
       "apSysCapabilityStatisticsTableEntry": apSysCapabilityStatisticsTableEntry,
       "apCPURTUsage": apCPURTUsage,
       "apCPUAvgUsage": apCPUAvgUsage,
       "apMemRTUsage": apMemRTUsage,
       "apMemAvgUsage": apMemAvgUsage,
       "apLinkStatisticsObjects": apLinkStatisticsObjects,
       "apLinkStatisticsTable": apLinkStatisticsTable,
       "apLinkStatisticsTableEntry": apLinkStatisticsTableEntry,
       "apLinkStatStationAssocSum": apLinkStatStationAssocSum,
       "apLinkStatStationOnlineSum": apLinkStatStationOnlineSum,
       "apLinkStatAssocTimes": apLinkStatAssocTimes,
       "apLinkStatAssocFailTimes": apLinkStatAssocFailTimes,
       "apLinkStatReassocTimes": apLinkStatReassocTimes,
       "apLinkStatPreAssCannotShiftDeassocFailSum": apLinkStatPreAssCannotShiftDeassocFailSum,
       "apLinkStatApStatsDisassociated": apLinkStatApStatsDisassociated,
       "apLinkStatAssocRejectSum": apLinkStatAssocRejectSum,
       "apLinkStatBSSNotSupportAssocFailSum": apLinkStatBSSNotSupportAssocFailSum,
       "apLinkStatApAuthReqTimes": apLinkStatApAuthReqTimes,
       "apLinkStatApAuthSuccessTimes": apLinkStatApAuthSuccessTimes,
       "acLinkStatApAuthReqFailTimes": acLinkStatApAuthReqFailTimes,
       "apLinkStatReassocFailTimes": apLinkStatReassocFailTimes,
       "apLinkStatRSSILowAssocFailSum": apLinkStatRSSILowAssocFailSum,
       "apLinkStatUnknowReasonAssoFailSum": apLinkStatUnknowReasonAssoFailSum,
       "apLinkStatOut80211StandardAssocFailSum": apLinkStatOut80211StandardAssocFailSum,
       "apLinkStatAllStationsTotalUpTime": apLinkStatAllStationsTotalUpTime,
       "apLinkStatAssocRespTimes": apLinkStatAssocRespTimes,
       "apLinkStatAssocSuccTimes": apLinkStatAssocSuccTimes,
       "apLinkStatUserRadiusOnlineSum": apLinkStatUserRadiusOnlineSum,
       "apLinkStatAllUserOnlineTime": apLinkStatAllUserOnlineTime,
       "apLinkStatRadiusAuthTimes": apLinkStatRadiusAuthTimes,
       "apLinkStatRadiusAuthSuccTimes": apLinkStatRadiusAuthSuccTimes,
       "apLinkStatRadiusAuthFailTimes": apLinkStatRadiusAuthFailTimes,
       "apLinkStatAssocSuccessTimes": apLinkStatAssocSuccessTimes,
       "apInterfaceRGMIIStatisticsObjects": apInterfaceRGMIIStatisticsObjects,
       "apInterfaceRGMIIStatisticsTable": apInterfaceRGMIIStatisticsTable,
       "apInterfaceRGMIIStatisticsTableEntry": apInterfaceRGMIIStatisticsTableEntry,
       "apRGMIIIndex": apRGMIIIndex,
       "apifInUcastPkts": apifInUcastPkts,
       "apifInNUcastPkts": apifInNUcastPkts,
       "apifInOctets": apifInOctets,
       "apifInDiscardPkts": apifInDiscardPkts,
       "apifInErrors": apifInErrors,
       "apifOutUcastPkts": apifOutUcastPkts,
       "apifOutNUcastPkts": apifOutNUcastPkts,
       "apifOutOctets": apifOutOctets,
       "apifOutDiscardPkts": apifOutDiscardPkts,
       "apifOutErrors": apifOutErrors,
       "apifUpDwnTimes": apifUpDwnTimes,
       "apInterfaceWireStatisticsObjects": apInterfaceWireStatisticsObjects,
       "apInterfaceWireStatisticsTable": apInterfaceWireStatisticsTable,
       "apInterfaceWireStatisticsTableEntry": apInterfaceWireStatisticsTableEntry,
       "apAvgRxSignalStrength": apAvgRxSignalStrength,
       "apHighestRxSignalStrength": apHighestRxSignalStrength,
       "apLowestRxSignalStrength": apLowestRxSignalStrength,
       "apWirelessUpdownTimes": apWirelessUpdownTimes,
       "apChStatsNumStations": apChStatsNumStations,
       "apTxDataPkts": apTxDataPkts,
       "apRxDataPkts": apRxDataPkts,
       "apUplinkDataOctets": apUplinkDataOctets,
       "apDwlinkDataOctets": apDwlinkDataOctets,
       "apChStatsDwlinkTotRetryPkts": apChStatsDwlinkTotRetryPkts,
       "apChStatsPhyErrPkts": apChStatsPhyErrPkts,
       "apChStatsMacFcsErrPkts": apChStatsMacFcsErrPkts,
       "apChStatsMacMicErrPkts": apChStatsMacMicErrPkts,
       "apChStatsMacDecryptErrPkts": apChStatsMacDecryptErrPkts,
       "apChStatsTotalErrPkts": apChStatsTotalErrPkts,
       "apRxMgmtFrameCnt": apRxMgmtFrameCnt,
       "apRxCtrlFrameCnt": apRxCtrlFrameCnt,
       "apRxDataFrameCnt": apRxDataFrameCnt,
       "apTxMgmtFrameCnt": apTxMgmtFrameCnt,
       "apTxCtrlFrameCnt": apTxCtrlFrameCnt,
       "apTxDataFrameCnt": apTxDataFrameCnt,
       "apChStatsFrameErrorCnt": apChStatsFrameErrorCnt,
       "apRetryCnt": apRetryCnt,
       "apCurTxPwr": apCurTxPwr,
       "apAPNeighborSSIDList": apAPNeighborSSIDList,
       "apChDownUnicastFrame": apChDownUnicastFrame,
       "apChDownNonUnicastFrame": apChDownNonUnicastFrame,
       "apChTxThroughput": apChTxThroughput,
       "apChRxThroughput": apChRxThroughput,
       "apChTxDropPkts": apChTxDropPkts,
       "apChRxDropPkts": apChRxDropPkts,
       "apChTxErrorPkts": apChTxErrorPkts,
       "apChRxErrorPkts": apChRxErrorPkts,
       "apRxBytes": apRxBytes,
       "apRxPkts": apRxPkts,
       "apTxBytes": apTxBytes,
       "apTxPkts": apTxPkts,
       "apDownNonUnicastPkts": apDownNonUnicastPkts,
       "apDownUnicastPkts": apDownUnicastPkts,
       "apUpNonUnicastPkts": apUpNonUnicastPkts,
       "apUpUnicastPkts": apUpUnicastPkts,
       "apAssoFailUnknowReason": apAssoFailUnknowReason,
       "apAssoFailOutofDot11": apAssoFailOutofDot11,
       "apAssoTotalTime": apAssoTotalTime,
       "apAuthReqFailTimes": apAuthReqFailTimes,
       "apAuthReqTimes": apAuthReqTimes,
       "apAuthSuccessTimes": apAuthSuccessTimes,
       "apReAssoFailTimes": apReAssoFailTimes,
       "apMacTxCorrectFrameCnt": apMacTxCorrectFrameCnt,
       "apMacRxCorrectFrameCnt": apMacRxCorrectFrameCnt,
       "apPktErrRate": apPktErrRate,
       "apTotalRxBytes": apTotalRxBytes,
       "apTotalTxBytes": apTotalTxBytes,
       "apTxErrorPkts": apTxErrorPkts,
       "apTxDropPkts": apTxDropPkts,
       "apIfRadiusOnlineUserNum": apIfRadiusOnlineUserNum,
       "apSSIDStatisticsObjects": apSSIDStatisticsObjects,
       "apSSIDStatisticsTable": apSSIDStatisticsTable,
       "apSSIDStatisticsTableEntry": apSSIDStatisticsTableEntry,
       "apSSIDStatisticsAPMac": apSSIDStatisticsAPMac,
       "apSSIDStatisticsRadioId": apSSIDStatisticsRadioId,
       "apSSIDStatisticsWlanId": apSSIDStatisticsWlanId,
       "apSSIDTxDataPkts": apSSIDTxDataPkts,
       "apSSIDRxDataPkts": apSSIDRxDataPkts,
       "apSSIDUplinkDataOctets": apSSIDUplinkDataOctets,
       "apSSIDDwlinkDataOctets": apSSIDDwlinkDataOctets,
       "apSSIDChStatsDwlinkTotRetryPkts": apSSIDChStatsDwlinkTotRetryPkts,
       "apSSIDApChStatsNumStations": apSSIDApChStatsNumStations,
       "apApChStatsOnlineSum": apApChStatsOnlineSum,
       "apSSIDStatisticsName": apSSIDStatisticsName,
       "apSSIDMacTxPkts": apSSIDMacTxPkts,
       "apSSIDMacRxPkts": apSSIDMacRxPkts,
       "apSSIDStatisticsNewTable": apSSIDStatisticsNewTable,
       "apSSIDStatisticsNewTableEntry": apSSIDStatisticsNewTableEntry,
       "apSSIDStatisticsNewAPMac": apSSIDStatisticsNewAPMac,
       "apSSIDStatisticsNewRadioId": apSSIDStatisticsNewRadioId,
       "apSSIDStatisticsNewSSID": apSSIDStatisticsNewSSID,
       "apSSIDNewTxDataPkts": apSSIDNewTxDataPkts,
       "apSSIDNewRxDataPkts": apSSIDNewRxDataPkts,
       "apSSIDNewUplinkDataOctets": apSSIDNewUplinkDataOctets,
       "apSSIDNewDwlinkDataOctets": apSSIDNewDwlinkDataOctets,
       "apSSIDNewChStatsDwlinkTotRetryPkts": apSSIDNewChStatsDwlinkTotRetryPkts,
       "apSSIDNewApChStatsNumStations": apSSIDNewApChStatsNumStations,
       "apApNewChStatsOnlineSum": apApNewChStatsOnlineSum,
       "apSSIDNewMacTxPkts": apSSIDNewMacTxPkts,
       "apSSIDNewMacRxPkts": apSSIDNewMacRxPkts,
       "apSSIDStatisticsOptimizationTable": apSSIDStatisticsOptimizationTable,
       "apSSIDStatisticsOptimizationTableEntry": apSSIDStatisticsOptimizationTableEntry,
       "apSSIDStatisticsOptimizationAPMac": apSSIDStatisticsOptimizationAPMac,
       "apSSIDStatisticsOptimizationRadioId": apSSIDStatisticsOptimizationRadioId,
       "apSSIDStatisticsOptimizationSSID": apSSIDStatisticsOptimizationSSID,
       "apSSIDStatisticsOptimizationinfo": apSSIDStatisticsOptimizationinfo,
       "apWAPIStatisticsObjects": apWAPIStatisticsObjects,
       "apWAPIStatisticsTable": apWAPIStatisticsTable,
       "apWAPIStatisticsTableEntry": apWAPIStatisticsTableEntry,
       "apWAPIControlledPortStatus": apWAPIControlledPortStatus,
       "apWAPISelectedUnicastCipher": apWAPISelectedUnicastCipher,
       "apWPIReplayCounters": apWPIReplayCounters,
       "apWPIDecryptableErrors": apWPIDecryptableErrors,
       "apWPIMICErrors": apWPIMICErrors,
       "apWAISignatureErrors": apWAISignatureErrors,
       "apWAIHMACErrors": apWAIHMACErrors,
       "apWAIAuthResultFailures": apWAIAuthResultFailures,
       "apWAIDiscardCounters": apWAIDiscardCounters,
       "apWAITimeoutCounters": apWAITimeoutCounters,
       "apWAIFormatErrors": apWAIFormatErrors,
       "apWAICertificateHandshakeFailures": apWAICertificateHandshakeFailures,
       "apWAIUnicastHandshakeFailures": apWAIUnicastHandshakeFailures,
       "apWAIMulticastHandshakeFailures": apWAIMulticastHandshakeFailures,
       "apStationStatisticsObjects": apStationStatisticsObjects,
       "apStationStatisticsTable": apStationStatisticsTable,
       "apStationStatisticsTableEntry": apStationStatisticsTableEntry,
       "apStaAddress": apStaAddress,
       "apStaUpTime": apStaUpTime,
       "apReceivedStaSignalStrength": apReceivedStaSignalStrength,
       "apAPReceiveStaSNR": apAPReceiveStaSNR,
       "apStaTxPkts": apStaTxPkts,
       "apStaTxBytes": apStaTxBytes,
       "apStaRxPkts": apStaRxPkts,
       "apStaRxBytes": apStaRxBytes,
       "apWAPISTAAddress": apWAPISTAAddress,
       "apWAPIVersion": apWAPIVersion,
       "apStaLinkSpeed": apStaLinkSpeed,
       "apStaUpRate": apStaUpRate,
       "apStaDownRate": apStaDownRate,
       "apStaTxThroughput": apStaTxThroughput,
       "apStaRxThroughput": apStaRxThroughput,
       "apStaRxRetryBytes": apStaRxRetryBytes,
       "apQOSStatisticsObjects": apQOSStatisticsObjects,
       "apQOSBaseStatisticsObjects": apQOSBaseStatisticsObjects,
       "apQOSBaseStatisticsTable": apQOSBaseStatisticsTable,
       "apQOSBaseStatisticsTableEntry": apQOSBaseStatisticsTableEntry,
       "apBaseQoSSvcQueAvgLen": apBaseQoSSvcQueAvgLen,
       "apBaseQoSSvcPktLossRatio": apBaseQoSSvcPktLossRatio,
       "apBaseAvgTransSpeed": apBaseAvgTransSpeed,
       "apQOSBackgroundStatisticsObjects": apQOSBackgroundStatisticsObjects,
       "apQOSBackgroundStatisticsTable": apQOSBackgroundStatisticsTable,
       "apQOSBackgroundStatisticsTableEntry": apQOSBackgroundStatisticsTableEntry,
       "apQOSBgQueAvgLen": apQOSBgQueAvgLen,
       "apQOSBgAvgBurst": apQOSBgAvgBurst,
       "apQOSBgPktLossRatio": apQOSBgPktLossRatio,
       "apQOSBgAvgTransSpeed": apQOSBgAvgTransSpeed,
       "apQOSBgSvcLoss": apQOSBgSvcLoss,
       "apQOSBestEffortStatisticsObjects": apQOSBestEffortStatisticsObjects,
       "apQOSBestEffortStatisticsTable": apQOSBestEffortStatisticsTable,
       "apQOSBestEffortStatisticsTableEntry": apQOSBestEffortStatisticsTableEntry,
       "apQOSBeQueAvgLen": apQOSBeQueAvgLen,
       "apQOSBeAvgBurst": apQOSBeAvgBurst,
       "apQOSBePktLossRatio": apQOSBePktLossRatio,
       "apQOSBeAvgTransSpeed": apQOSBeAvgTransSpeed,
       "apQOSBeSvcLoss": apQOSBeSvcLoss,
       "apQOSVoiceStatisticsObjects": apQOSVoiceStatisticsObjects,
       "apQOSVoiceStatisticsTable": apQOSVoiceStatisticsTable,
       "apQOSVoiceStatisticsTableEntry": apQOSVoiceStatisticsTableEntry,
       "apQOSVoiceQueAvgLen": apQOSVoiceQueAvgLen,
       "apQOSVoiceAvgBurst": apQOSVoiceAvgBurst,
       "apQOSVoicePktLossRatio": apQOSVoicePktLossRatio,
       "apQOSVoiceAvgTransSpeed": apQOSVoiceAvgTransSpeed,
       "apQOSVoicePutThroughRatio": apQOSVoicePutThroughRatio,
       "apQOSVoiceDropRatio": apQOSVoiceDropRatio,
       "apQOSVoiceSvcLoss": apQOSVoiceSvcLoss,
       "apQOSVoiceExceedMaxUsersRequest": apQOSVoiceExceedMaxUsersRequest,
       "apQOSVideoStatisticsObjects": apQOSVideoStatisticsObjects,
       "apQOSVideoStatisticsTable": apQOSVideoStatisticsTable,
       "apQOSVideoStatisticsTableEntry": apQOSVideoStatisticsTableEntry,
       "apQOSVideoQueAvgLen": apQOSVideoQueAvgLen,
       "apQOSVideoAvgBurst": apQOSVideoAvgBurst,
       "apQOSVideoPktLossRatio": apQOSVideoPktLossRatio,
       "apQOSVideoAvgTransSpeed": apQOSVideoAvgTransSpeed,
       "apQOSVideoPutThroughRatio": apQOSVideoPutThroughRatio,
       "apQOSVideoDropRatio": apQOSVideoDropRatio,
       "apQOSVideoSvcLoss": apQOSVideoSvcLoss,
       "apQOSVideoExceedMaxUsersRequest": apQOSVideoExceedMaxUsersRequest,
       "apWIDSRogueApInfoObjects": apWIDSRogueApInfoObjects,
       "apWIDSRogueApInfoTable": apWIDSRogueApInfoTable,
       "apWIDSRogueApInfoTableEntry": apWIDSRogueApInfoTableEntry,
       "ruijieRogueApMacAddr": ruijieRogueApMacAddr,
       "ruijieRogueApRSSI": ruijieRogueApRSSI,
       "apStaTransSpeedObjects": apStaTransSpeedObjects,
       "apStaTransSpeedTable": apStaTransSpeedTable,
       "apStaTransSpeedTableEntry": apStaTransSpeedTableEntry,
       "apStaUplinkTransSpeed1M": apStaUplinkTransSpeed1M,
       "apStaUplinkTransSpeed2M": apStaUplinkTransSpeed2M,
       "apStaUplinkTransSpeed5M": apStaUplinkTransSpeed5M,
       "apStaUplinkTransSpeed11M": apStaUplinkTransSpeed11M,
       "apStaUplinkTransSpeed6M": apStaUplinkTransSpeed6M,
       "apStaUplinkTransSpeed9M": apStaUplinkTransSpeed9M,
       "apStaUplinkTransSpeed12M": apStaUplinkTransSpeed12M,
       "apStaUplinkTransSpeed18M": apStaUplinkTransSpeed18M,
       "apStaUplinkTransSpeed24M": apStaUplinkTransSpeed24M,
       "apStaUplinkTransSpeed36M": apStaUplinkTransSpeed36M,
       "apStaUplinkTransSpeed48M": apStaUplinkTransSpeed48M,
       "apStaUplinkTransSpeed54M": apStaUplinkTransSpeed54M,
       "apStaDownlinkTransSpeed1M": apStaDownlinkTransSpeed1M,
       "apStaDownlinkTransSpeed2M": apStaDownlinkTransSpeed2M,
       "apStaDownlinkTransSpeed5M": apStaDownlinkTransSpeed5M,
       "apStaDownlinkTransSpeed11M": apStaDownlinkTransSpeed11M,
       "apStaDownlinkTransSpeed6M": apStaDownlinkTransSpeed6M,
       "apStaDownlinkTransSpeed9M": apStaDownlinkTransSpeed9M,
       "apStaDownlinkTransSpeed12M": apStaDownlinkTransSpeed12M,
       "apStaDownlinkTransSpeed18M": apStaDownlinkTransSpeed18M,
       "apStaDownlinkTransSpeed24M": apStaDownlinkTransSpeed24M,
       "apStaDownlinkTransSpeed36M": apStaDownlinkTransSpeed36M,
       "apStaDownlinkTransSpeed48M": apStaDownlinkTransSpeed48M,
       "apStaDownlinkTransSpeed54M": apStaDownlinkTransSpeed54M,
       "apStaUplinkTransSpeedMCS0": apStaUplinkTransSpeedMCS0,
       "apStaUplinkTransSpeedMCS1": apStaUplinkTransSpeedMCS1,
       "apStaUplinkTransSpeedMCS2": apStaUplinkTransSpeedMCS2,
       "apStaUplinkTransSpeedMCS3": apStaUplinkTransSpeedMCS3,
       "apStaUplinkTransSpeedMCS4": apStaUplinkTransSpeedMCS4,
       "apStaUplinkTransSpeedMCS5": apStaUplinkTransSpeedMCS5,
       "apStaUplinkTransSpeedMCS6": apStaUplinkTransSpeedMCS6,
       "apStaUplinkTransSpeedMCS7": apStaUplinkTransSpeedMCS7,
       "apStaUplinkTransSpeedMCS8": apStaUplinkTransSpeedMCS8,
       "apStaUplinkTransSpeedMCS9": apStaUplinkTransSpeedMCS9,
       "apStaUplinkTransSpeedMCS10": apStaUplinkTransSpeedMCS10,
       "apStaUplinkTransSpeedMCS11": apStaUplinkTransSpeedMCS11,
       "apStaUplinkTransSpeedMCS12": apStaUplinkTransSpeedMCS12,
       "apStaUplinkTransSpeedMCS13": apStaUplinkTransSpeedMCS13,
       "apStaUplinkTransSpeedMCS14": apStaUplinkTransSpeedMCS14,
       "apStaUplinkTransSpeedMCS15": apStaUplinkTransSpeedMCS15,
       "apStaUplinkTransSpeedMCS16": apStaUplinkTransSpeedMCS16,
       "apStaUplinkTransSpeedMCS17": apStaUplinkTransSpeedMCS17,
       "apStaUplinkTransSpeedMCS18": apStaUplinkTransSpeedMCS18,
       "apStaUplinkTransSpeedMCS19": apStaUplinkTransSpeedMCS19,
       "apStaUplinkTransSpeedMCS20": apStaUplinkTransSpeedMCS20,
       "apStaUplinkTransSpeedMCS21": apStaUplinkTransSpeedMCS21,
       "apStaUplinkTransSpeedMCS22": apStaUplinkTransSpeedMCS22,
       "apStaUplinkTransSpeedMCS23": apStaUplinkTransSpeedMCS23,
       "apStaUplinkTransSpeedMCS24": apStaUplinkTransSpeedMCS24,
       "apStaUplinkTransSpeedMCS25": apStaUplinkTransSpeedMCS25,
       "apStaUplinkTransSpeedMCS26": apStaUplinkTransSpeedMCS26,
       "apStaUplinkTransSpeedMCS27": apStaUplinkTransSpeedMCS27,
       "apStaUplinkTransSpeedMCS28": apStaUplinkTransSpeedMCS28,
       "apStaUplinkTransSpeedMCS29": apStaUplinkTransSpeedMCS29,
       "apStaUplinkTransSpeedMCS30": apStaUplinkTransSpeedMCS30,
       "apStaUplinkTransSpeedMCS31": apStaUplinkTransSpeedMCS31,
       "apStaDownlinkTransSpeedMCS0": apStaDownlinkTransSpeedMCS0,
       "apStaDownlinkTransSpeedMCS1": apStaDownlinkTransSpeedMCS1,
       "apStaDownlinkTransSpeedMCS2": apStaDownlinkTransSpeedMCS2,
       "apStaDownlinkTransSpeedMCS3": apStaDownlinkTransSpeedMCS3,
       "apStaDownlinkTransSpeedMCS4": apStaDownlinkTransSpeedMCS4,
       "apStaDownlinkTransSpeedMCS5": apStaDownlinkTransSpeedMCS5,
       "apStaDownlinkTransSpeedMCS6": apStaDownlinkTransSpeedMCS6,
       "apStaDownlinkTransSpeedMCS7": apStaDownlinkTransSpeedMCS7,
       "apStaDownlinkTransSpeedMCS8": apStaDownlinkTransSpeedMCS8,
       "apStaDownlinkTransSpeedMCS9": apStaDownlinkTransSpeedMCS9,
       "apStaDownlinkTransSpeedMCS10": apStaDownlinkTransSpeedMCS10,
       "apStaDownlinkTransSpeedMCS11": apStaDownlinkTransSpeedMCS11,
       "apStaDownlinkTransSpeedMCS12": apStaDownlinkTransSpeedMCS12,
       "apStaDownlinkTransSpeedMCS13": apStaDownlinkTransSpeedMCS13,
       "apStaDownlinkTransSpeedMCS14": apStaDownlinkTransSpeedMCS14,
       "apStaDownlinkTransSpeedMCS15": apStaDownlinkTransSpeedMCS15,
       "apStaDownlinkTransSpeedMCS16": apStaDownlinkTransSpeedMCS16,
       "apStaDownlinkTransSpeedMCS17": apStaDownlinkTransSpeedMCS17,
       "apStaDownlinkTransSpeedMCS18": apStaDownlinkTransSpeedMCS18,
       "apStaDownlinkTransSpeedMCS19": apStaDownlinkTransSpeedMCS19,
       "apStaDownlinkTransSpeedMCS20": apStaDownlinkTransSpeedMCS20,
       "apStaDownlinkTransSpeedMCS21": apStaDownlinkTransSpeedMCS21,
       "apStaDownlinkTransSpeedMCS22": apStaDownlinkTransSpeedMCS22,
       "apStaDownlinkTransSpeedMCS23": apStaDownlinkTransSpeedMCS23,
       "apStaDownlinkTransSpeedMCS24": apStaDownlinkTransSpeedMCS24,
       "apStaDownlinkTransSpeedMCS25": apStaDownlinkTransSpeedMCS25,
       "apStaDownlinkTransSpeedMCS26": apStaDownlinkTransSpeedMCS26,
       "apStaDownlinkTransSpeedMCS27": apStaDownlinkTransSpeedMCS27,
       "apStaDownlinkTransSpeedMCS28": apStaDownlinkTransSpeedMCS28,
       "apStaDownlinkTransSpeedMCS29": apStaDownlinkTransSpeedMCS29,
       "apStaDownlinkTransSpeedMCS30": apStaDownlinkTransSpeedMCS30,
       "apStaDownlinkTransSpeedMCS31": apStaDownlinkTransSpeedMCS31,
       "apStationAssoRssiObjects": apStationAssoRssiObjects,
       "apStationAssoRssiTable": apStationAssoRssiTable,
       "apStationAssoRssiTableEntry": apStationAssoRssiTableEntry,
       "apStationAssoRxSignalStrength1": apStationAssoRxSignalStrength1,
       "apStationAssoRxSignalStrength2": apStationAssoRxSignalStrength2,
       "apStationAssoRxSignalStrength3": apStationAssoRxSignalStrength3,
       "apStationAssoRxSignalStrength4": apStationAssoRxSignalStrength4,
       "apStationAssoRxSignalStrength5": apStationAssoRxSignalStrength5,
       "apStationAssoRxSignalStrength6": apStationAssoRxSignalStrength6,
       "apStationAssoRxSignalStrength7": apStationAssoRxSignalStrength7,
       "apStationAssoRxSignalStrength8": apStationAssoRxSignalStrength8,
       "apStationAssoRxSignalStrength9": apStationAssoRxSignalStrength9,
       "apStationAssoRxSignalStrength10": apStationAssoRxSignalStrength10,
       "apStationAssoRxSignalStrength11": apStationAssoRxSignalStrength11,
       "apStationAssoRxSignalStrength12": apStationAssoRxSignalStrength12,
       "apStationAssoRxSignalStrength13": apStationAssoRxSignalStrength13,
       "apStationAssoRxSignalStrength14": apStationAssoRxSignalStrength14,
       "apStationAssoRxSignalStrength15": apStationAssoRxSignalStrength15,
       "apRuijieAlarmTrapObjects": apRuijieAlarmTrapObjects,
       "apAPMac": apAPMac,
       "apWorkModeBeforeChange": apWorkModeBeforeChange,
       "apWorkModeAfterChange": apWorkModeAfterChange,
       "apSSIDKey": apSSIDKey,
       "apSSIDKeyConflict": apSSIDKeyConflict,
       "apCyperIndex": apCyperIndex,
       "apInterruptReason": apInterruptReason,
       "apWorkingAPRadioIfInfo": apWorkingAPRadioIfInfo,
       "apWorkingAPChannel": apWorkingAPChannel,
       "apInterfAPChannel": apInterfAPChannel,
       "apInterfAPBSSID": apInterfAPBSSID,
       "apInterfStaMac": apInterfStaMac,
       "apPermitAssoUser": apPermitAssoUser,
       "apAssoFailReason": apAssoFailReason,
       "apChannelBeforeChange": apChannelBeforeChange,
       "apChannelAfterChange": apChannelAfterChange,
       "apChanChangeMode": apChanChangeMode,
       "apWorkingAPBSSID": apWorkingAPBSSID,
       "apWorkingAPSSID": apWorkingAPSSID,
       "apStaMacAddr": apStaMacAddr,
       "apAuthMode": apAuthMode,
       "apAuthFailReason": apAuthFailReason,
       "updateFailReason": updateFailReason,
       "apSWVersionBeforeUpdate": apSWVersionBeforeUpdate,
       "apAPRadioId": apAPRadioId,
       "apRevPackages": apRevPackages,
       "apCPUUsage": apCPUUsage,
       "apSpeciousDeviceMac": apSpeciousDeviceMac,
       "apRSSI": apRSSI,
       "apAttackReason": apAttackReason,
       "apWlanId": apWlanId,
       "apWlanSSID": apWlanSSID,
       "apWlanSecurityModeBeforeChg": apWlanSecurityModeBeforeChg,
       "apWlanSecurityModeAfterChg": apWlanSecurityModeAfterChg,
       "apTrapIllegalApMac": apTrapIllegalApMac,
       "apTrapIllegalApChannel": apTrapIllegalApChannel,
       "apTrapIllegalApRSSI": apTrapIllegalApRSSI,
       "apTrapWorkingApMac": apTrapWorkingApMac,
       "apTrapWorkingApBSSID": apTrapWorkingApBSSID,
       "apTrapIllegalApType": apTrapIllegalApType,
       "apTrapIllegalApSSID": apTrapIllegalApSSID,
       "apAPRadioType": apAPRadioType,
       "apAssocAuthMode": apAssocAuthMode,
       "apStaRSSI": apStaRSSI,
       "apAssocFailReason": apAssocFailReason,
       "apSpectralInfoApMac": apSpectralInfoApMac,
       "apSpectralInfoType": apSpectralInfoType,
       "apSpectralInfoFreq": apSpectralInfoFreq,
       "apSpectralInfoRssi": apSpectralInfoRssi,
       "apCounterMeasureApMac": apCounterMeasureApMac,
       "apCounterMeasureBssid": apCounterMeasureBssid,
       "apApName": apApName,
       "apApLocation": apApLocation,
       "apApUptime": apApUptime,
       "apApUserNum": apApUserNum,
       "apApChannel2": apApChannel2,
       "apApChannel5": apApChannel5,
       "apSsidName": apSsidName,
       "apSsidIndex": apSsidIndex,
       "apSsidDot11Auth": apSsidDot11Auth,
       "apSsidSecurityMode": apSsidSecurityMode,
       "apSsidAuthenMode": apSsidAuthenMode,
       "webAuthTlvCount": webAuthTlvCount,
       "webAuthTlvString": webAuthTlvString,
       "apAccessControl": apAccessControl,
       "apTerminalPermitTable": apTerminalPermitTable,
       "apTerminalPermitEntry": apTerminalPermitEntry,
       "apWhiteListIndex": apWhiteListIndex,
       "apPermitMAC": apPermitMAC,
       "apWhiteListStatus": apWhiteListStatus,
       "apTerminalDeniedTable": apTerminalDeniedTable,
       "apTerminalDeniedEntry": apTerminalDeniedEntry,
       "apBlackListIndex": apBlackListIndex,
       "apAttackDeviceMAC": apAttackDeviceMAC,
       "apBlackListStatus": apBlackListStatus,
       "apTerminalBlackListTable": apTerminalBlackListTable,
       "apTerminalBlackListEntry": apTerminalBlackListEntry,
       "apBlackListDeviceMAC": apBlackListDeviceMAC,
       "apBlackListAddReason": apBlackListAddReason,
       "apBlackListDuration": apBlackListDuration,
       "acCapabilityStatistics": acCapabilityStatistics,
       "acWirelessDownDropFrame": acWirelessDownDropFrame,
       "acWirelessDownRetryFrame": acWirelessDownRetryFrame,
       "acWirelessDownFrame": acWirelessDownFrame,
       "acWirelessDownErrorFrame": acWirelessDownErrorFrame,
       "acWirelessUpFrame": acWirelessUpFrame,
       "acWirelessUpDropFrame": acWirelessUpDropFrame,
       "acWirelessUpRetryFrame": acWirelessUpRetryFrame,
       "acWirelessUpRate": acWirelessUpRate,
       "acWirelessDownRate": acWirelessDownRate,
       "apWidsInfoObjects": apWidsInfoObjects,
       "apWidsIllegalApTable": apWidsIllegalApTable,
       "apWidsIllegalApEntry": apWidsIllegalApEntry,
       "apIllegalApMac": apIllegalApMac,
       "apIllegalApChannel": apIllegalApChannel,
       "apIllegalApRSSI": apIllegalApRSSI,
       "apWorkingApMac": apWorkingApMac,
       "apDetectAPBSSID": apDetectAPBSSID,
       "apIllegalApType": apIllegalApType,
       "apIllegalApSSID": apIllegalApSSID,
       "apWidsApCounterTable": apWidsApCounterTable,
       "apWidsApCounterEntry": apWidsApCounterEntry,
       "apCounterMac": apCounterMac,
       "apCounter": apCounter,
       "apCounterMode": apCounterMode,
       "apCounterRssiThreshold": apCounterRssiThreshold,
       "apWidsDeviceMode": apWidsDeviceMode,
       "apWidsCounterIllegalAp": apWidsCounterIllegalAp,
       "apWidsCounterModeIllegalAp": apWidsCounterModeIllegalAp,
       "apWidsDeviceModeFlag": apWidsDeviceModeFlag,
       "apWidsCounterIllegalApFlag": apWidsCounterIllegalApFlag,
       "apWidsCounterModeIllegalApFlag": apWidsCounterModeIllegalApFlag,
       "apWidsPermitMacTable": apWidsPermitMacTable,
       "apWidsPermitMacEntry": apWidsPermitMacEntry,
       "apWidsPermitMac": apWidsPermitMac,
       "apPermitMacrowstatus": apPermitMacrowstatus,
       "apWidsPermitSSIDTable": apWidsPermitSSIDTable,
       "apWidsPermitSSIDEntry": apWidsPermitSSIDEntry,
       "apCounterSSID": apCounterSSID,
       "apPermitSSIDrowstatus": apPermitSSIDrowstatus,
       "apWidsPermitVendorTable": apWidsPermitVendorTable,
       "apWidsPermitVendorEntry": apWidsPermitVendorEntry,
       "apCounterVendor": apCounterVendor,
       "apPermitVendorrowstatus": apPermitVendorrowstatus,
       "apWidsStaticAttackTable": apWidsStaticAttackTable,
       "apWidsStaticAttackEntry": apWidsStaticAttackEntry,
       "apStaticAttackMac": apStaticAttackMac,
       "apStaticAttackrowstatus": apStaticAttackrowstatus,
       "apWidsNeighborApInfoTable": apWidsNeighborApInfoTable,
       "apWidsNeighborApInfoEntry": apWidsNeighborApInfoEntry,
       "neighborApMac": neighborApMac,
       "neighborApSSID": neighborApSSID,
       "neighborApRSSI": neighborApRSSI,
       "neighborApChannel": neighborApChannel,
       "neighborApInControl": neighborApInControl,
       "apWidsClearIlleglApListFlag": apWidsClearIlleglApListFlag,
       "apWidsFloodInterval": apWidsFloodInterval,
       "apWidsBlackListThreshold": apWidsBlackListThreshold,
       "apWidsBlackListDuration": apWidsBlackListDuration,
       "apWidsFloodDetectOnOff": apWidsFloodDetectOnOff,
       "apWidsCounterRssiThreshold": apWidsCounterRssiThreshold,
       "apWidsBlackSSIDTable": apWidsBlackSSIDTable,
       "apWidsBlackSSIDEntry": apWidsBlackSSIDEntry,
       "apBlackSSID": apBlackSSID,
       "apBlackSSIDrowstatus": apBlackSSIDrowstatus,
       "apConfigInfoObjects": apConfigInfoObjects,
       "apConfigInfoTable": apConfigInfoTable,
       "apConfigInfoEntry": apConfigInfoEntry,
       "apConfigInfoMac": apConfigInfoMac,
       "apSpectralSwitch": apSpectralSwitch,
       "apSpectralSupport": apSpectralSupport,
       "apSmartAntSupport": apSmartAntSupport,
       "apSmartDisSupport": apSmartDisSupport,
       "apAntdetectSupport": apAntdetectSupport,
       "apAntdetectEnable": apAntdetectEnable,
       "apAntdetectInterval": apAntdetectInterval,
       "apAntdetectState": apAntdetectState,
       "apAntDetectObjects": apAntDetectObjects,
       "apAntDetectTable": apAntDetectTable,
       "apAntDetectEntry": apAntDetectEntry,
       "apAntDetectAPMac": apAntDetectAPMac,
       "apAntDetectAntIndex": apAntDetectAntIndex,
       "apAntDetectDesc": apAntDetectDesc,
       "apAntDetectRadioId": apAntDetectRadioId,
       "apAntDetectStatus": apAntDetectStatus,
       "apAntDetectCfgTable": apAntDetectCfgTable,
       "apAntDetectCfgEntry": apAntDetectCfgEntry,
       "apAntDetectCfgAPMac": apAntDetectCfgAPMac,
       "apAntDetectCfgSupport": apAntDetectCfgSupport,
       "apAntDetectCfgSwitch": apAntDetectCfgSwitch}
)
