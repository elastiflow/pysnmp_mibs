# SNMP MIB module (RUIJIE-VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VMSUP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieVMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96)
)
if mibBuilder.loadTexts:
    ruijieVMMIB.setRevisions(
        ("2012-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieVMMIBObjects_ObjectIdentity = ObjectIdentity
ruijieVMMIBObjects = _RuijieVMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1)
)
_RuijieVMFuncVMSupport_Type = ConfigStatus
_RuijieVMFuncVMSupport_Object = MibScalar
ruijieVMFuncVMSupport = _RuijieVMFuncVMSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 1),
    _RuijieVMFuncVMSupport_Type()
)
ruijieVMFuncVMSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMFuncVMSupport.setStatus("current")
_RuijieVMTrapCfgNotifyStatus_Type = ConfigStatus
_RuijieVMTrapCfgNotifyStatus_Object = MibScalar
ruijieVMTrapCfgNotifyStatus = _RuijieVMTrapCfgNotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 2),
    _RuijieVMTrapCfgNotifyStatus_Type()
)
ruijieVMTrapCfgNotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMTrapCfgNotifyStatus.setStatus("current")
_RuijieVMTrapCfgHistorySize_Type = Unsigned32
_RuijieVMTrapCfgHistorySize_Object = MibScalar
ruijieVMTrapCfgHistorySize = _RuijieVMTrapCfgHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 3),
    _RuijieVMTrapCfgHistorySize_Type()
)
ruijieVMTrapCfgHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMTrapCfgHistorySize.setStatus("current")
_RuijieVMInfoTable_Object = MibTable
ruijieVMInfoTable = _RuijieVMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieVMInfoTable.setStatus("current")
_RuijieVMInfoEntry_Object = MibTableRow
ruijieVMInfoEntry = _RuijieVMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 4, 1)
)
ruijieVMInfoEntry.setIndexNames(
    (0, "RUIJIE-VM-MIB", "ruijieVMInfoVMMac"),
    (0, "RUIJIE-VM-MIB", "ruijieVMInfoVMGroup"),
)
if mibBuilder.loadTexts:
    ruijieVMInfoEntry.setStatus("current")
_RuijieVMInfoVMMac_Type = MacAddress
_RuijieVMInfoVMMac_Object = MibTableColumn
ruijieVMInfoVMMac = _RuijieVMInfoVMMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 4, 1, 1),
    _RuijieVMInfoVMMac_Type()
)
ruijieVMInfoVMMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMInfoVMMac.setStatus("current")
_RuijieVMInfoVMGroup_Type = Integer32
_RuijieVMInfoVMGroup_Object = MibTableColumn
ruijieVMInfoVMGroup = _RuijieVMInfoVMGroup_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 4, 1, 2),
    _RuijieVMInfoVMGroup_Type()
)
ruijieVMInfoVMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMInfoVMGroup.setStatus("current")
_RuijieVMInfoRowStatus_Type = RowStatus
_RuijieVMInfoRowStatus_Object = MibTableColumn
ruijieVMInfoRowStatus = _RuijieVMInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 4, 1, 3),
    _RuijieVMInfoRowStatus_Type()
)
ruijieVMInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVMInfoRowStatus.setStatus("current")
_RuijieVMGroupInfoTable_Object = MibTable
ruijieVMGroupInfoTable = _RuijieVMGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieVMGroupInfoTable.setStatus("current")
_RuijieVMGroupInfoEntry_Object = MibTableRow
ruijieVMGroupInfoEntry = _RuijieVMGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 5, 1)
)
ruijieVMGroupInfoEntry.setIndexNames(
    (0, "RUIJIE-VM-MIB", "ruijieVMGroupInfoGroupName"),
)
if mibBuilder.loadTexts:
    ruijieVMGroupInfoEntry.setStatus("current")
_RuijieVMGroupInfoGroupName_Type = Integer32
_RuijieVMGroupInfoGroupName_Object = MibTableColumn
ruijieVMGroupInfoGroupName = _RuijieVMGroupInfoGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 5, 1, 1),
    _RuijieVMGroupInfoGroupName_Type()
)
ruijieVMGroupInfoGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMGroupInfoGroupName.setStatus("current")
_RuijieVMGroupInfoProfileCfg_Type = ConfigStatus
_RuijieVMGroupInfoProfileCfg_Object = MibTableColumn
ruijieVMGroupInfoProfileCfg = _RuijieVMGroupInfoProfileCfg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 5, 1, 2),
    _RuijieVMGroupInfoProfileCfg_Type()
)
ruijieVMGroupInfoProfileCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMGroupInfoProfileCfg.setStatus("current")


class _RuijieVMGroupInfoProfileName_Type(DisplayString):
    """Custom type ruijieVMGroupInfoProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieVMGroupInfoProfileName_Type.__name__ = "DisplayString"
_RuijieVMGroupInfoProfileName_Object = MibTableColumn
ruijieVMGroupInfoProfileName = _RuijieVMGroupInfoProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 5, 1, 3),
    _RuijieVMGroupInfoProfileName_Type()
)
ruijieVMGroupInfoProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMGroupInfoProfileName.setStatus("current")
_RuijieVMGroupInfoRowStatus_Type = RowStatus
_RuijieVMGroupInfoRowStatus_Object = MibTableColumn
ruijieVMGroupInfoRowStatus = _RuijieVMGroupInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 5, 1, 4),
    _RuijieVMGroupInfoRowStatus_Type()
)
ruijieVMGroupInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVMGroupInfoRowStatus.setStatus("current")
_RuijieVMProfileTable_Object = MibTable
ruijieVMProfileTable = _RuijieVMProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieVMProfileTable.setStatus("current")
_RuijieVMProfileEntry_Object = MibTableRow
ruijieVMProfileEntry = _RuijieVMProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1)
)
ruijieVMProfileEntry.setIndexNames(
    (0, "RUIJIE-VM-MIB", "ruijieVMProfileName"),
)
if mibBuilder.loadTexts:
    ruijieVMProfileEntry.setStatus("current")


class _RuijieVMProfileName_Type(DisplayString):
    """Custom type ruijieVMProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieVMProfileName_Type.__name__ = "DisplayString"
_RuijieVMProfileName_Object = MibTableColumn
ruijieVMProfileName = _RuijieVMProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 1),
    _RuijieVMProfileName_Type()
)
ruijieVMProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMProfileName.setStatus("current")


class _RuijieVMProfileAclIn_Type(DisplayString):
    """Custom type ruijieVMProfileAclIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_RuijieVMProfileAclIn_Type.__name__ = "DisplayString"
_RuijieVMProfileAclIn_Object = MibTableColumn
ruijieVMProfileAclIn = _RuijieVMProfileAclIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 2),
    _RuijieVMProfileAclIn_Type()
)
ruijieVMProfileAclIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileAclIn.setStatus("current")


class _RuijieVMProfileAclOut_Type(DisplayString):
    """Custom type ruijieVMProfileAclOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_RuijieVMProfileAclOut_Type.__name__ = "DisplayString"
_RuijieVMProfileAclOut_Object = MibTableColumn
ruijieVMProfileAclOut = _RuijieVMProfileAclOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 3),
    _RuijieVMProfileAclOut_Type()
)
ruijieVMProfileAclOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileAclOut.setStatus("current")
_RuijieVMProfileTxRate_Type = Unsigned32
_RuijieVMProfileTxRate_Object = MibTableColumn
ruijieVMProfileTxRate = _RuijieVMProfileTxRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 4),
    _RuijieVMProfileTxRate_Type()
)
ruijieVMProfileTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileTxRate.setStatus("current")
_RuijieVMProfileTxBurst_Type = Integer32
_RuijieVMProfileTxBurst_Object = MibTableColumn
ruijieVMProfileTxBurst = _RuijieVMProfileTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 5),
    _RuijieVMProfileTxBurst_Type()
)
ruijieVMProfileTxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileTxBurst.setStatus("current")
_RuijieVMProfileRxRate_Type = Unsigned32
_RuijieVMProfileRxRate_Object = MibTableColumn
ruijieVMProfileRxRate = _RuijieVMProfileRxRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 6),
    _RuijieVMProfileRxRate_Type()
)
ruijieVMProfileRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileRxRate.setStatus("current")
_RuijieVMProfileRxBurst_Type = Integer32
_RuijieVMProfileRxBurst_Object = MibTableColumn
ruijieVMProfileRxBurst = _RuijieVMProfileRxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 7),
    _RuijieVMProfileRxBurst_Type()
)
ruijieVMProfileRxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileRxBurst.setStatus("current")
_RuijieVMProfileRowStatus_Type = RowStatus
_RuijieVMProfileRowStatus_Object = MibTableColumn
ruijieVMProfileRowStatus = _RuijieVMProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 8),
    _RuijieVMProfileRowStatus_Type()
)
ruijieVMProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVMProfileRowStatus.setStatus("current")


class _RuijieVMProfileQosTrustMode_Type(Integer32):
    """Custom type ruijieVMProfileQosTrustMode based on Integer32"""
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
        *(("not-trust", 0),
          ("trust-cos", 1),
          ("trust-dscp", 2),
          ("trust-ip-precedence", 3))
    )


_RuijieVMProfileQosTrustMode_Type.__name__ = "Integer32"
_RuijieVMProfileQosTrustMode_Object = MibTableColumn
ruijieVMProfileQosTrustMode = _RuijieVMProfileQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 9),
    _RuijieVMProfileQosTrustMode_Type()
)
ruijieVMProfileQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileQosTrustMode.setStatus("current")


class _RuijieVMProfileQosDefCos_Type(Integer32):
    """Custom type ruijieVMProfileQosDefCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("invalid", 8)
    )


_RuijieVMProfileQosDefCos_Type.__name__ = "Integer32"
_RuijieVMProfileQosDefCos_Object = MibTableColumn
ruijieVMProfileQosDefCos = _RuijieVMProfileQosDefCos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 10),
    _RuijieVMProfileQosDefCos_Type()
)
ruijieVMProfileQosDefCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileQosDefCos.setStatus("current")


class _RuijieVMProfileQosRxPolicyMap_Type(DisplayString):
    """Custom type ruijieVMProfileQosRxPolicyMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieVMProfileQosRxPolicyMap_Type.__name__ = "DisplayString"
_RuijieVMProfileQosRxPolicyMap_Object = MibTableColumn
ruijieVMProfileQosRxPolicyMap = _RuijieVMProfileQosRxPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 6, 1, 11),
    _RuijieVMProfileQosRxPolicyMap_Type()
)
ruijieVMProfileQosRxPolicyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMProfileQosRxPolicyMap.setStatus("current")
_RuijieVMLocInfoTable_Object = MibTable
ruijieVMLocInfoTable = _RuijieVMLocInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieVMLocInfoTable.setStatus("current")
_RuijieVMLocInfoEntry_Object = MibTableRow
ruijieVMLocInfoEntry = _RuijieVMLocInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 7, 1)
)
ruijieVMLocInfoEntry.setIndexNames(
    (0, "RUIJIE-VM-MIB", "ruijieVMLocInfoVMMac"),
    (0, "RUIJIE-VM-MIB", "ruijieVMLocInfoPort"),
)
if mibBuilder.loadTexts:
    ruijieVMLocInfoEntry.setStatus("current")
_RuijieVMLocInfoVMMac_Type = MacAddress
_RuijieVMLocInfoVMMac_Object = MibTableColumn
ruijieVMLocInfoVMMac = _RuijieVMLocInfoVMMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 7, 1, 1),
    _RuijieVMLocInfoVMMac_Type()
)
ruijieVMLocInfoVMMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMLocInfoVMMac.setStatus("current")
_RuijieVMLocInfoPort_Type = IfIndex
_RuijieVMLocInfoPort_Object = MibTableColumn
ruijieVMLocInfoPort = _RuijieVMLocInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 7, 1, 2),
    _RuijieVMLocInfoPort_Type()
)
ruijieVMLocInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMLocInfoPort.setStatus("current")
_RuijieVMLocInfoType_Type = Unsigned32
_RuijieVMLocInfoType_Object = MibTableColumn
ruijieVMLocInfoType = _RuijieVMLocInfoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 7, 1, 3),
    _RuijieVMLocInfoType_Type()
)
ruijieVMLocInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMLocInfoType.setStatus("current")
_RuijieVMLocInfoRowStatus_Type = RowStatus
_RuijieVMLocInfoRowStatus_Object = MibTableColumn
ruijieVMLocInfoRowStatus = _RuijieVMLocInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 7, 1, 4),
    _RuijieVMLocInfoRowStatus_Type()
)
ruijieVMLocInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVMLocInfoRowStatus.setStatus("current")
_RuijieVMPortInfoTable_Object = MibTable
ruijieVMPortInfoTable = _RuijieVMPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieVMPortInfoTable.setStatus("current")
_RuijieVMPortInfoEntry_Object = MibTableRow
ruijieVMPortInfoEntry = _RuijieVMPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 8, 1)
)
ruijieVMPortInfoEntry.setIndexNames(
    (0, "RUIJIE-VM-MIB", "ruijieVMPortInfoPort"),
)
if mibBuilder.loadTexts:
    ruijieVMPortInfoEntry.setStatus("current")
_RuijieVMPortInfoPort_Type = IfIndex
_RuijieVMPortInfoPort_Object = MibTableColumn
ruijieVMPortInfoPort = _RuijieVMPortInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 8, 1, 1),
    _RuijieVMPortInfoPort_Type()
)
ruijieVMPortInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMPortInfoPort.setStatus("current")
_RuijieVMPortInfoStatus_Type = ConfigStatus
_RuijieVMPortInfoStatus_Object = MibTableColumn
ruijieVMPortInfoStatus = _RuijieVMPortInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 8, 1, 2),
    _RuijieVMPortInfoStatus_Type()
)
ruijieVMPortInfoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMPortInfoStatus.setStatus("current")
_RuijieVMPortInfoReflectStatus_Type = ConfigStatus
_RuijieVMPortInfoReflectStatus_Object = MibTableColumn
ruijieVMPortInfoReflectStatus = _RuijieVMPortInfoReflectStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 8, 1, 3),
    _RuijieVMPortInfoReflectStatus_Type()
)
ruijieVMPortInfoReflectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMPortInfoReflectStatus.setStatus("current")
_RuijieVMPortTrapCfgTable_Object = MibTable
ruijieVMPortTrapCfgTable = _RuijieVMPortTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieVMPortTrapCfgTable.setStatus("current")
_RuijieVMPortTrapCfgEntry_Object = MibTableRow
ruijieVMPortTrapCfgEntry = _RuijieVMPortTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 9, 1)
)
ruijieVMPortTrapCfgEntry.setIndexNames(
    (0, "RUIJIE-VM-MIB", "ruijieVMPortTrapCfgPort"),
)
if mibBuilder.loadTexts:
    ruijieVMPortTrapCfgEntry.setStatus("current")
_RuijieVMPortTrapCfgPort_Type = IfIndex
_RuijieVMPortTrapCfgPort_Object = MibTableColumn
ruijieVMPortTrapCfgPort = _RuijieVMPortTrapCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 9, 1, 1),
    _RuijieVMPortTrapCfgPort_Type()
)
ruijieVMPortTrapCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMPortTrapCfgPort.setStatus("current")
_RuijieVMPortTrapCfgNotifyStatus_Type = ConfigStatus
_RuijieVMPortTrapCfgNotifyStatus_Object = MibTableColumn
ruijieVMPortTrapCfgNotifyStatus = _RuijieVMPortTrapCfgNotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 9, 1, 2),
    _RuijieVMPortTrapCfgNotifyStatus_Type()
)
ruijieVMPortTrapCfgNotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVMPortTrapCfgNotifyStatus.setStatus("current")
_RuijieVMInfoChgTable_Object = MibTable
ruijieVMInfoChgTable = _RuijieVMInfoChgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieVMInfoChgTable.setStatus("current")
_RuijieVMInfoChgEntry_Object = MibTableRow
ruijieVMInfoChgEntry = _RuijieVMInfoChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 10, 1)
)
ruijieVMInfoChgEntry.setIndexNames(
    (0, "RUIJIE-VM-MIB", "ruijieVMInfoChgVMMac"),
    (0, "RUIJIE-VM-MIB", "ruijieVMInfoChgVlan"),
)
if mibBuilder.loadTexts:
    ruijieVMInfoChgEntry.setStatus("current")
_RuijieVMInfoChgVMMac_Type = MacAddress
_RuijieVMInfoChgVMMac_Object = MibTableColumn
ruijieVMInfoChgVMMac = _RuijieVMInfoChgVMMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 10, 1, 1),
    _RuijieVMInfoChgVMMac_Type()
)
ruijieVMInfoChgVMMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVMInfoChgVMMac.setStatus("current")
_RuijieVMInfoChgVlan_Type = VlanId
_RuijieVMInfoChgVlan_Object = MibTableColumn
ruijieVMInfoChgVlan = _RuijieVMInfoChgVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 10, 1, 2),
    _RuijieVMInfoChgVlan_Type()
)
ruijieVMInfoChgVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVMInfoChgVlan.setStatus("current")
_RuijieVMInfoChgPort_Type = IfIndex
_RuijieVMInfoChgPort_Object = MibTableColumn
ruijieVMInfoChgPort = _RuijieVMInfoChgPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 10, 1, 3),
    _RuijieVMInfoChgPort_Type()
)
ruijieVMInfoChgPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVMInfoChgPort.setStatus("current")


class _RuijieVMInfoChgAction_Type(DisplayString):
    """Custom type ruijieVMInfoChgAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieVMInfoChgAction_Type.__name__ = "DisplayString"
_RuijieVMInfoChgAction_Object = MibTableColumn
ruijieVMInfoChgAction = _RuijieVMInfoChgAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 10, 1, 4),
    _RuijieVMInfoChgAction_Type()
)
ruijieVMInfoChgAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVMInfoChgAction.setStatus("current")
_RuijieVMInfoChgDate_Type = DateAndTime
_RuijieVMInfoChgDate_Object = MibTableColumn
ruijieVMInfoChgDate = _RuijieVMInfoChgDate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 10, 1, 5),
    _RuijieVMInfoChgDate_Type()
)
ruijieVMInfoChgDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVMInfoChgDate.setStatus("current")
_RuijieVMOuiInfoTable_Object = MibTable
ruijieVMOuiInfoTable = _RuijieVMOuiInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieVMOuiInfoTable.setStatus("current")
_RuijieVMOuiInfoEntry_Object = MibTableRow
ruijieVMOuiInfoEntry = _RuijieVMOuiInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 11, 1)
)
ruijieVMOuiInfoEntry.setIndexNames(
    (0, "RUIJIE-VM-MIB", "ruijieVMOuiInfoOui"),
)
if mibBuilder.loadTexts:
    ruijieVMOuiInfoEntry.setStatus("current")
_RuijieVMOuiInfoOui_Type = MacAddress
_RuijieVMOuiInfoOui_Object = MibTableColumn
ruijieVMOuiInfoOui = _RuijieVMOuiInfoOui_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 11, 1, 1),
    _RuijieVMOuiInfoOui_Type()
)
ruijieVMOuiInfoOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMOuiInfoOui.setStatus("current")
_RuijieVMOuiInfoRowStatus_Type = RowStatus
_RuijieVMOuiInfoRowStatus_Object = MibTableColumn
ruijieVMOuiInfoRowStatus = _RuijieVMOuiInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 11, 1, 2),
    _RuijieVMOuiInfoRowStatus_Type()
)
ruijieVMOuiInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVMOuiInfoRowStatus.setStatus("current")
_RuijieVMRateMin_Type = Unsigned32
_RuijieVMRateMin_Object = MibScalar
ruijieVMRateMin = _RuijieVMRateMin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 12),
    _RuijieVMRateMin_Type()
)
ruijieVMRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMRateMin.setStatus("current")
_RuijieVMRateMax_Type = Unsigned32
_RuijieVMRateMax_Object = MibScalar
ruijieVMRateMax = _RuijieVMRateMax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 13),
    _RuijieVMRateMax_Type()
)
ruijieVMRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMRateMax.setStatus("current")
_RuijieVMBurstMin_Type = Unsigned32
_RuijieVMBurstMin_Object = MibScalar
ruijieVMBurstMin = _RuijieVMBurstMin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 14),
    _RuijieVMBurstMin_Type()
)
ruijieVMBurstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMBurstMin.setStatus("current")
_RuijieVMBurstMax_Type = Unsigned32
_RuijieVMBurstMax_Object = MibScalar
ruijieVMBurstMax = _RuijieVMBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 1, 15),
    _RuijieVMBurstMax_Type()
)
ruijieVMBurstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVMBurstMax.setStatus("current")
_RuijieVMMIBTraps_ObjectIdentity = ObjectIdentity
ruijieVMMIBTraps = _RuijieVMMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 2)
)
_RuijieVMMIBConformance_ObjectIdentity = ObjectIdentity
ruijieVMMIBConformance = _RuijieVMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 3)
)
_RuijieVMMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieVMMIBCompliances = _RuijieVMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 3, 1)
)
_RuijieVMMIBGroups_ObjectIdentity = ObjectIdentity
ruijieVMMIBGroups = _RuijieVMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 3, 2)
)

# Managed Objects groups

ruijieVMMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 3, 2, 1)
)
ruijieVMMIBGroup.setObjects(
      *(("RUIJIE-VM-MIB", "ruijieVMFuncVMSupport"),
        ("RUIJIE-VM-MIB", "ruijieVMTrapCfgNotifyStatus"),
        ("RUIJIE-VM-MIB", "ruijieVMTrapCfgHistorySize"),
        ("RUIJIE-VM-MIB", "ruijieVMRateMin"),
        ("RUIJIE-VM-MIB", "ruijieVMRateMax"),
        ("RUIJIE-VM-MIB", "ruijieVMBurstMin"),
        ("RUIJIE-VM-MIB", "ruijieVMBurstMax"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoVMMac"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoVMGroup"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoRowStatus"),
        ("RUIJIE-VM-MIB", "ruijieVMGroupInfoGroupName"),
        ("RUIJIE-VM-MIB", "ruijieVMGroupInfoProfileCfg"),
        ("RUIJIE-VM-MIB", "ruijieVMGroupInfoProfileName"),
        ("RUIJIE-VM-MIB", "ruijieVMGroupInfoRowStatus"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileName"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileAclIn"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileAclOut"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileTxRate"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileTxBurst"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileRxRate"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileRxBurst"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileRowStatus"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileQosTrustMode"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileQosDefCos"),
        ("RUIJIE-VM-MIB", "ruijieVMProfileQosRxPolicyMap"),
        ("RUIJIE-VM-MIB", "ruijieVMLocInfoVMMac"),
        ("RUIJIE-VM-MIB", "ruijieVMLocInfoPort"),
        ("RUIJIE-VM-MIB", "ruijieVMLocInfoType"),
        ("RUIJIE-VM-MIB", "ruijieVMLocInfoRowStatus"),
        ("RUIJIE-VM-MIB", "ruijieVMPortInfoPort"),
        ("RUIJIE-VM-MIB", "ruijieVMPortInfoStatus"),
        ("RUIJIE-VM-MIB", "ruijieVMPortInfoReflectStatus"),
        ("RUIJIE-VM-MIB", "ruijieVMPortTrapCfgPort"),
        ("RUIJIE-VM-MIB", "ruijieVMPortTrapCfgNotifyStatus"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgVMMac"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgVlan"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgPort"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgAction"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgDate"),
        ("RUIJIE-VM-MIB", "ruijieVMOuiInfoOui"),
        ("RUIJIE-VM-MIB", "ruijieVMOuiInfoRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieVMMIBGroup.setStatus("current")


# Notification objects

ruijieVMsupMIBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 2, 1)
)
ruijieVMsupMIBTrap.setObjects(
      *(("RUIJIE-VM-MIB", "ruijieVMInfoChgVMMac"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgVlan"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgPort"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgAction"),
        ("RUIJIE-VM-MIB", "ruijieVMInfoChgDate"))
)
if mibBuilder.loadTexts:
    ruijieVMsupMIBTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieVMMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 96, 3, 1, 1)
)
ruijieVMMIBCompliance.setObjects(
    ("RUIJIE-VM-MIB", "ruijieVMMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieVMMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VM-MIB",
    **{"ruijieVMMIB": ruijieVMMIB,
       "ruijieVMMIBObjects": ruijieVMMIBObjects,
       "ruijieVMFuncVMSupport": ruijieVMFuncVMSupport,
       "ruijieVMTrapCfgNotifyStatus": ruijieVMTrapCfgNotifyStatus,
       "ruijieVMTrapCfgHistorySize": ruijieVMTrapCfgHistorySize,
       "ruijieVMInfoTable": ruijieVMInfoTable,
       "ruijieVMInfoEntry": ruijieVMInfoEntry,
       "ruijieVMInfoVMMac": ruijieVMInfoVMMac,
       "ruijieVMInfoVMGroup": ruijieVMInfoVMGroup,
       "ruijieVMInfoRowStatus": ruijieVMInfoRowStatus,
       "ruijieVMGroupInfoTable": ruijieVMGroupInfoTable,
       "ruijieVMGroupInfoEntry": ruijieVMGroupInfoEntry,
       "ruijieVMGroupInfoGroupName": ruijieVMGroupInfoGroupName,
       "ruijieVMGroupInfoProfileCfg": ruijieVMGroupInfoProfileCfg,
       "ruijieVMGroupInfoProfileName": ruijieVMGroupInfoProfileName,
       "ruijieVMGroupInfoRowStatus": ruijieVMGroupInfoRowStatus,
       "ruijieVMProfileTable": ruijieVMProfileTable,
       "ruijieVMProfileEntry": ruijieVMProfileEntry,
       "ruijieVMProfileName": ruijieVMProfileName,
       "ruijieVMProfileAclIn": ruijieVMProfileAclIn,
       "ruijieVMProfileAclOut": ruijieVMProfileAclOut,
       "ruijieVMProfileTxRate": ruijieVMProfileTxRate,
       "ruijieVMProfileTxBurst": ruijieVMProfileTxBurst,
       "ruijieVMProfileRxRate": ruijieVMProfileRxRate,
       "ruijieVMProfileRxBurst": ruijieVMProfileRxBurst,
       "ruijieVMProfileRowStatus": ruijieVMProfileRowStatus,
       "ruijieVMProfileQosTrustMode": ruijieVMProfileQosTrustMode,
       "ruijieVMProfileQosDefCos": ruijieVMProfileQosDefCos,
       "ruijieVMProfileQosRxPolicyMap": ruijieVMProfileQosRxPolicyMap,
       "ruijieVMLocInfoTable": ruijieVMLocInfoTable,
       "ruijieVMLocInfoEntry": ruijieVMLocInfoEntry,
       "ruijieVMLocInfoVMMac": ruijieVMLocInfoVMMac,
       "ruijieVMLocInfoPort": ruijieVMLocInfoPort,
       "ruijieVMLocInfoType": ruijieVMLocInfoType,
       "ruijieVMLocInfoRowStatus": ruijieVMLocInfoRowStatus,
       "ruijieVMPortInfoTable": ruijieVMPortInfoTable,
       "ruijieVMPortInfoEntry": ruijieVMPortInfoEntry,
       "ruijieVMPortInfoPort": ruijieVMPortInfoPort,
       "ruijieVMPortInfoStatus": ruijieVMPortInfoStatus,
       "ruijieVMPortInfoReflectStatus": ruijieVMPortInfoReflectStatus,
       "ruijieVMPortTrapCfgTable": ruijieVMPortTrapCfgTable,
       "ruijieVMPortTrapCfgEntry": ruijieVMPortTrapCfgEntry,
       "ruijieVMPortTrapCfgPort": ruijieVMPortTrapCfgPort,
       "ruijieVMPortTrapCfgNotifyStatus": ruijieVMPortTrapCfgNotifyStatus,
       "ruijieVMInfoChgTable": ruijieVMInfoChgTable,
       "ruijieVMInfoChgEntry": ruijieVMInfoChgEntry,
       "ruijieVMInfoChgVMMac": ruijieVMInfoChgVMMac,
       "ruijieVMInfoChgVlan": ruijieVMInfoChgVlan,
       "ruijieVMInfoChgPort": ruijieVMInfoChgPort,
       "ruijieVMInfoChgAction": ruijieVMInfoChgAction,
       "ruijieVMInfoChgDate": ruijieVMInfoChgDate,
       "ruijieVMOuiInfoTable": ruijieVMOuiInfoTable,
       "ruijieVMOuiInfoEntry": ruijieVMOuiInfoEntry,
       "ruijieVMOuiInfoOui": ruijieVMOuiInfoOui,
       "ruijieVMOuiInfoRowStatus": ruijieVMOuiInfoRowStatus,
       "ruijieVMRateMin": ruijieVMRateMin,
       "ruijieVMRateMax": ruijieVMRateMax,
       "ruijieVMBurstMin": ruijieVMBurstMin,
       "ruijieVMBurstMax": ruijieVMBurstMax,
       "ruijieVMMIBTraps": ruijieVMMIBTraps,
       "ruijieVMsupMIBTrap": ruijieVMsupMIBTrap,
       "ruijieVMMIBConformance": ruijieVMMIBConformance,
       "ruijieVMMIBCompliances": ruijieVMMIBCompliances,
       "ruijieVMMIBCompliance": ruijieVMMIBCompliance,
       "ruijieVMMIBGroups": ruijieVMMIBGroups,
       "ruijieVMMIBGroup": ruijieVMMIBGroup}
)
