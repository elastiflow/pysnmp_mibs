# SNMP MIB module (RUIJIE-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SECURITY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:10 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

ruijieSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6)
)
if mibBuilder.loadTexts:
    ruijieSecurityMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSecurityMIBObjects_ObjectIdentity = ObjectIdentity
ruijieSecurityMIBObjects = _RuijieSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1)
)
_RuijieUserManagementObjects_ObjectIdentity = ObjectIdentity
ruijieUserManagementObjects = _RuijieUserManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1)
)
_RuijieEnableSnmpAgent_Type = EnabledStatus
_RuijieEnableSnmpAgent_Object = MibScalar
ruijieEnableSnmpAgent = _RuijieEnableSnmpAgent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 1),
    _RuijieEnableSnmpAgent_Type()
)
ruijieEnableSnmpAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieEnableSnmpAgent.setStatus("current")
_RuijieEnableWeb_Type = EnabledStatus
_RuijieEnableWeb_Object = MibScalar
ruijieEnableWeb = _RuijieEnableWeb_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 2),
    _RuijieEnableWeb_Type()
)
ruijieEnableWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieEnableWeb.setStatus("current")
_RuijieEnableTelnet_Type = EnabledStatus
_RuijieEnableTelnet_Object = MibScalar
ruijieEnableTelnet = _RuijieEnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 3),
    _RuijieEnableTelnet_Type()
)
ruijieEnableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieEnableTelnet.setStatus("current")
_RuijieTelnetHostIpTable_Object = MibTable
ruijieTelnetHostIpTable = _RuijieTelnetHostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieTelnetHostIpTable.setStatus("current")
_RuijieTelnetHostIpEntry_Object = MibTableRow
ruijieTelnetHostIpEntry = _RuijieTelnetHostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 4, 1)
)
ruijieTelnetHostIpEntry.setIndexNames(
    (0, "RUIJIE-SECURITY-MIB", "ruijieTelnetHostIpAddress"),
)
if mibBuilder.loadTexts:
    ruijieTelnetHostIpEntry.setStatus("current")
_RuijieTelnetHostIpAddress_Type = IpAddress
_RuijieTelnetHostIpAddress_Object = MibTableColumn
ruijieTelnetHostIpAddress = _RuijieTelnetHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 4, 1, 1),
    _RuijieTelnetHostIpAddress_Type()
)
ruijieTelnetHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTelnetHostIpAddress.setStatus("current")


class _RuijieTelnetHostIpEnable_Type(Integer32):
    """Custom type ruijieTelnetHostIpEnable based on Integer32"""
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


_RuijieTelnetHostIpEnable_Type.__name__ = "Integer32"
_RuijieTelnetHostIpEnable_Object = MibTableColumn
ruijieTelnetHostIpEnable = _RuijieTelnetHostIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 4, 1, 2),
    _RuijieTelnetHostIpEnable_Type()
)
ruijieTelnetHostIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieTelnetHostIpEnable.setStatus("current")
_RuijieWebHostIpTable_Object = MibTable
ruijieWebHostIpTable = _RuijieWebHostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieWebHostIpTable.setStatus("current")
_RuijieWebHostIpEntry_Object = MibTableRow
ruijieWebHostIpEntry = _RuijieWebHostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 5, 1)
)
ruijieWebHostIpEntry.setIndexNames(
    (0, "RUIJIE-SECURITY-MIB", "ruijieWebHostIpAddress"),
)
if mibBuilder.loadTexts:
    ruijieWebHostIpEntry.setStatus("current")
_RuijieWebHostIpAddress_Type = IpAddress
_RuijieWebHostIpAddress_Object = MibTableColumn
ruijieWebHostIpAddress = _RuijieWebHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 5, 1, 1),
    _RuijieWebHostIpAddress_Type()
)
ruijieWebHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebHostIpAddress.setStatus("current")


class _RuijieWebHostIpEnable_Type(Integer32):
    """Custom type ruijieWebHostIpEnable based on Integer32"""
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


_RuijieWebHostIpEnable_Type.__name__ = "Integer32"
_RuijieWebHostIpEnable_Object = MibTableColumn
ruijieWebHostIpEnable = _RuijieWebHostIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 1, 5, 1, 2),
    _RuijieWebHostIpEnable_Type()
)
ruijieWebHostIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWebHostIpEnable.setStatus("current")
_RuijieSecurityAddressObjects_ObjectIdentity = ObjectIdentity
ruijieSecurityAddressObjects = _RuijieSecurityAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2)
)
_RuijieSecurityAddressTable_Object = MibTable
ruijieSecurityAddressTable = _RuijieSecurityAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieSecurityAddressTable.setStatus("current")
_RuijieSecurityAddressEntry_Object = MibTableRow
ruijieSecurityAddressEntry = _RuijieSecurityAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1)
)
ruijieSecurityAddressEntry.setIndexNames(
    (0, "RUIJIE-SECURITY-MIB", "ruijieSecurityAddressFdbId"),
    (0, "RUIJIE-SECURITY-MIB", "ruijieSecurityAddressAddress"),
    (0, "RUIJIE-SECURITY-MIB", "ruijieSecurityAddressPort"),
    (0, "RUIJIE-SECURITY-MIB", "ruijieSecurityAddressIpAddr"),
)
if mibBuilder.loadTexts:
    ruijieSecurityAddressEntry.setStatus("current")
_RuijieSecurityAddressFdbId_Type = Unsigned32
_RuijieSecurityAddressFdbId_Object = MibTableColumn
ruijieSecurityAddressFdbId = _RuijieSecurityAddressFdbId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1, 1),
    _RuijieSecurityAddressFdbId_Type()
)
ruijieSecurityAddressFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecurityAddressFdbId.setStatus("current")
_RuijieSecurityAddressAddress_Type = MacAddress
_RuijieSecurityAddressAddress_Object = MibTableColumn
ruijieSecurityAddressAddress = _RuijieSecurityAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1, 2),
    _RuijieSecurityAddressAddress_Type()
)
ruijieSecurityAddressAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecurityAddressAddress.setStatus("current")
_RuijieSecurityAddressPort_Type = IfIndex
_RuijieSecurityAddressPort_Object = MibTableColumn
ruijieSecurityAddressPort = _RuijieSecurityAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1, 3),
    _RuijieSecurityAddressPort_Type()
)
ruijieSecurityAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecurityAddressPort.setStatus("current")
_RuijieSecurityAddressIpAddr_Type = IpAddress
_RuijieSecurityAddressIpAddr_Object = MibTableColumn
ruijieSecurityAddressIpAddr = _RuijieSecurityAddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1, 4),
    _RuijieSecurityAddressIpAddr_Type()
)
ruijieSecurityAddressIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecurityAddressIpAddr.setStatus("current")
_RuijieSecurityAddressIfBindIp_Type = TruthValue
_RuijieSecurityAddressIfBindIp_Object = MibTableColumn
ruijieSecurityAddressIfBindIp = _RuijieSecurityAddressIfBindIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1, 5),
    _RuijieSecurityAddressIfBindIp_Type()
)
ruijieSecurityAddressIfBindIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecurityAddressIfBindIp.setStatus("current")
_RuijieSecurityAddressRemainAge_Type = Integer32
_RuijieSecurityAddressRemainAge_Object = MibTableColumn
ruijieSecurityAddressRemainAge = _RuijieSecurityAddressRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1, 6),
    _RuijieSecurityAddressRemainAge_Type()
)
ruijieSecurityAddressRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecurityAddressRemainAge.setStatus("current")


class _RuijieSecurityAddressType_Type(Integer32):
    """Custom type ruijieSecurityAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secureConfigured", 1),
          ("dynamicLearn", 2))
    )


_RuijieSecurityAddressType_Type.__name__ = "Integer32"
_RuijieSecurityAddressType_Object = MibTableColumn
ruijieSecurityAddressType = _RuijieSecurityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1, 7),
    _RuijieSecurityAddressType_Type()
)
ruijieSecurityAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecurityAddressType.setStatus("current")
_RuijieSecurityAddressStatus_Type = RowStatus
_RuijieSecurityAddressStatus_Object = MibTableColumn
ruijieSecurityAddressStatus = _RuijieSecurityAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 1, 1, 8),
    _RuijieSecurityAddressStatus_Type()
)
ruijieSecurityAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecurityAddressStatus.setStatus("current")
_RuijieBindAddressTable_Object = MibTable
ruijieBindAddressTable = _RuijieBindAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieBindAddressTable.setStatus("current")
_RuijieBindAddressEntry_Object = MibTableRow
ruijieBindAddressEntry = _RuijieBindAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 2, 1)
)
ruijieBindAddressEntry.setIndexNames(
    (0, "RUIJIE-SECURITY-MIB", "ruijieBindAddressIpAddr"),
)
if mibBuilder.loadTexts:
    ruijieBindAddressEntry.setStatus("current")
_RuijieBindAddressIpAddr_Type = IpAddress
_RuijieBindAddressIpAddr_Object = MibTableColumn
ruijieBindAddressIpAddr = _RuijieBindAddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 2, 1, 1),
    _RuijieBindAddressIpAddr_Type()
)
ruijieBindAddressIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBindAddressIpAddr.setStatus("current")
_RuijieBindMacAddress_Type = MacAddress
_RuijieBindMacAddress_Object = MibTableColumn
ruijieBindMacAddress = _RuijieBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 2, 1, 2),
    _RuijieBindMacAddress_Type()
)
ruijieBindMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBindMacAddress.setStatus("current")
_RuijieBindAddressStatus_Type = ConfigStatus
_RuijieBindAddressStatus_Object = MibTableColumn
ruijieBindAddressStatus = _RuijieBindAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 2, 2, 1, 3),
    _RuijieBindAddressStatus_Type()
)
ruijieBindAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieBindAddressStatus.setStatus("current")
_RuijiePortSecrrityObjects_ObjectIdentity = ObjectIdentity
ruijiePortSecrrityObjects = _RuijiePortSecrrityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3)
)
_RuijiePortSecurityTable_Object = MibTable
ruijiePortSecurityTable = _RuijiePortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijiePortSecurityTable.setStatus("current")
_RuijiePortSecurityEntry_Object = MibTableRow
ruijiePortSecurityEntry = _RuijiePortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1)
)
ruijiePortSecurityEntry.setIndexNames(
    (0, "RUIJIE-SECURITY-MIB", "ruijiePortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    ruijiePortSecurityEntry.setStatus("current")
_RuijiePortSecurityPortIndex_Type = IfIndex
_RuijiePortSecurityPortIndex_Object = MibTableColumn
ruijiePortSecurityPortIndex = _RuijiePortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 1),
    _RuijiePortSecurityPortIndex_Type()
)
ruijiePortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePortSecurityPortIndex.setStatus("current")


class _RuijiePortSecurityStatus_Type(EnabledStatus):
    """Custom type ruijiePortSecurityStatus based on EnabledStatus"""
    defaultValue = 2


_RuijiePortSecurityStatus_Type.__name__ = "EnabledStatus"
_RuijiePortSecurityStatus_Object = MibTableColumn
ruijiePortSecurityStatus = _RuijiePortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 2),
    _RuijiePortSecurityStatus_Type()
)
ruijiePortSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePortSecurityStatus.setStatus("current")


class _RuijiePortSecurViolationType_Type(Integer32):
    """Custom type ruijiePortSecurViolationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("violation-protect", 1),
          ("violation-restrict", 2),
          ("violation-shutdown", 3))
    )


_RuijiePortSecurViolationType_Type.__name__ = "Integer32"
_RuijiePortSecurViolationType_Object = MibTableColumn
ruijiePortSecurViolationType = _RuijiePortSecurViolationType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 3),
    _RuijiePortSecurViolationType_Type()
)
ruijiePortSecurViolationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePortSecurViolationType.setStatus("current")
_RuijiePortSecurityAddrNum_Type = Integer32
_RuijiePortSecurityAddrNum_Object = MibTableColumn
ruijiePortSecurityAddrNum = _RuijiePortSecurityAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 4),
    _RuijiePortSecurityAddrNum_Type()
)
ruijiePortSecurityAddrNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePortSecurityAddrNum.setStatus("current")
_RuijiePortSecurityAddrAge_Type = Integer32
_RuijiePortSecurityAddrAge_Object = MibTableColumn
ruijiePortSecurityAddrAge = _RuijiePortSecurityAddrAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 5),
    _RuijiePortSecurityAddrAge_Type()
)
ruijiePortSecurityAddrAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePortSecurityAddrAge.setStatus("current")
_RuijiePortStaticSecurAddrIfAge_Type = EnabledStatus
_RuijiePortStaticSecurAddrIfAge_Object = MibTableColumn
ruijiePortStaticSecurAddrIfAge = _RuijiePortStaticSecurAddrIfAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 6),
    _RuijiePortStaticSecurAddrIfAge_Type()
)
ruijiePortStaticSecurAddrIfAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePortStaticSecurAddrIfAge.setStatus("current")
_RuijiePortSecurityAddressCurrentNum_Type = Integer32
_RuijiePortSecurityAddressCurrentNum_Object = MibTableColumn
ruijiePortSecurityAddressCurrentNum = _RuijiePortSecurityAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 7),
    _RuijiePortSecurityAddressCurrentNum_Type()
)
ruijiePortSecurityAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePortSecurityAddressCurrentNum.setStatus("current")
_RuijiePortStaticSecurAddrCurrentNum_Type = Integer32
_RuijiePortStaticSecurAddrCurrentNum_Object = MibTableColumn
ruijiePortStaticSecurAddrCurrentNum = _RuijiePortStaticSecurAddrCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 8),
    _RuijiePortStaticSecurAddrCurrentNum_Type()
)
ruijiePortStaticSecurAddrCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePortStaticSecurAddrCurrentNum.setStatus("current")


class _RuijiePortSecurityIpDistrMode_Type(Integer32):
    """Custom type ruijiePortSecurityIpDistrMode based on Integer32"""
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
        *(("static", 1),
          ("dynamic", 2),
          ("staticAndDynamic", 3),
          ("unSpecified", 4))
    )


_RuijiePortSecurityIpDistrMode_Type.__name__ = "Integer32"
_RuijiePortSecurityIpDistrMode_Object = MibTableColumn
ruijiePortSecurityIpDistrMode = _RuijiePortSecurityIpDistrMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 1, 3, 1, 1, 9),
    _RuijiePortSecurityIpDistrMode_Type()
)
ruijiePortSecurityIpDistrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePortSecurityIpDistrMode.setStatus("current")
_RuijieSecurityTraps_ObjectIdentity = ObjectIdentity
ruijieSecurityTraps = _RuijieSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 2)
)
_RuijieSecurityMIBConformance_ObjectIdentity = ObjectIdentity
ruijieSecurityMIBConformance = _RuijieSecurityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 3)
)
_RuijieSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieSecurityMIBCompliances = _RuijieSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 3, 1)
)
_RuijieSecurityMIBGroups_ObjectIdentity = ObjectIdentity
ruijieSecurityMIBGroups = _RuijieSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 3, 2)
)

# Managed Objects groups

ruijieUserManageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 3, 2, 1)
)
ruijieUserManageMIBGroup.setObjects(
      *(("RUIJIE-SECURITY-MIB", "ruijieEnableSnmpAgent"),
        ("RUIJIE-SECURITY-MIB", "ruijieEnableWeb"),
        ("RUIJIE-SECURITY-MIB", "ruijieEnableTelnet"))
)
if mibBuilder.loadTexts:
    ruijieUserManageMIBGroup.setStatus("current")

ruijieSecurityAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 3, 2, 2)
)
ruijieSecurityAddressMIBGroup.setObjects(
      *(("RUIJIE-SECURITY-MIB", "ruijieSecurityAddressIfBindIp"),
        ("RUIJIE-SECURITY-MIB", "ruijieSecurityAddressRemainAge"),
        ("RUIJIE-SECURITY-MIB", "ruijieSecurityAddressType"),
        ("RUIJIE-SECURITY-MIB", "ruijieSecurityAddressStatus"),
        ("RUIJIE-SECURITY-MIB", "ruijieBindMacAddress"),
        ("RUIJIE-SECURITY-MIB", "ruijieBindAddressStatus"))
)
if mibBuilder.loadTexts:
    ruijieSecurityAddressMIBGroup.setStatus("current")

ruijiePortSecurityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 3, 2, 3)
)
ruijiePortSecurityMIBGroup.setObjects(
      *(("RUIJIE-SECURITY-MIB", "ruijiePortSecurityPortIndex"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortSecurityStatus"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortSecurViolationType"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortSecurityAddrNum"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortSecurityAddrAge"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortStaticSecurAddrIfAge"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortSecurityAddressCurrentNum"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortStaticSecurAddrCurrentNum"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortSecurityIpDistrMode"))
)
if mibBuilder.loadTexts:
    ruijiePortSecurityMIBGroup.setStatus("current")


# Notification objects

portSecurityViolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 2, 1)
)
portSecurityViolate.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portSecurityViolate.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieSecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 6, 3, 1, 1)
)
ruijieSecurityMIBCompliance.setObjects(
      *(("RUIJIE-SECURITY-MIB", "ruijieUserManageMIBGroup"),
        ("RUIJIE-SECURITY-MIB", "ruijieSecurityAddressMIBGroup"),
        ("RUIJIE-SECURITY-MIB", "ruijiePortSecurityMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieSecurityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SECURITY-MIB",
    **{"ruijieSecurityMIB": ruijieSecurityMIB,
       "ruijieSecurityMIBObjects": ruijieSecurityMIBObjects,
       "ruijieUserManagementObjects": ruijieUserManagementObjects,
       "ruijieEnableSnmpAgent": ruijieEnableSnmpAgent,
       "ruijieEnableWeb": ruijieEnableWeb,
       "ruijieEnableTelnet": ruijieEnableTelnet,
       "ruijieTelnetHostIpTable": ruijieTelnetHostIpTable,
       "ruijieTelnetHostIpEntry": ruijieTelnetHostIpEntry,
       "ruijieTelnetHostIpAddress": ruijieTelnetHostIpAddress,
       "ruijieTelnetHostIpEnable": ruijieTelnetHostIpEnable,
       "ruijieWebHostIpTable": ruijieWebHostIpTable,
       "ruijieWebHostIpEntry": ruijieWebHostIpEntry,
       "ruijieWebHostIpAddress": ruijieWebHostIpAddress,
       "ruijieWebHostIpEnable": ruijieWebHostIpEnable,
       "ruijieSecurityAddressObjects": ruijieSecurityAddressObjects,
       "ruijieSecurityAddressTable": ruijieSecurityAddressTable,
       "ruijieSecurityAddressEntry": ruijieSecurityAddressEntry,
       "ruijieSecurityAddressFdbId": ruijieSecurityAddressFdbId,
       "ruijieSecurityAddressAddress": ruijieSecurityAddressAddress,
       "ruijieSecurityAddressPort": ruijieSecurityAddressPort,
       "ruijieSecurityAddressIpAddr": ruijieSecurityAddressIpAddr,
       "ruijieSecurityAddressIfBindIp": ruijieSecurityAddressIfBindIp,
       "ruijieSecurityAddressRemainAge": ruijieSecurityAddressRemainAge,
       "ruijieSecurityAddressType": ruijieSecurityAddressType,
       "ruijieSecurityAddressStatus": ruijieSecurityAddressStatus,
       "ruijieBindAddressTable": ruijieBindAddressTable,
       "ruijieBindAddressEntry": ruijieBindAddressEntry,
       "ruijieBindAddressIpAddr": ruijieBindAddressIpAddr,
       "ruijieBindMacAddress": ruijieBindMacAddress,
       "ruijieBindAddressStatus": ruijieBindAddressStatus,
       "ruijiePortSecrrityObjects": ruijiePortSecrrityObjects,
       "ruijiePortSecurityTable": ruijiePortSecurityTable,
       "ruijiePortSecurityEntry": ruijiePortSecurityEntry,
       "ruijiePortSecurityPortIndex": ruijiePortSecurityPortIndex,
       "ruijiePortSecurityStatus": ruijiePortSecurityStatus,
       "ruijiePortSecurViolationType": ruijiePortSecurViolationType,
       "ruijiePortSecurityAddrNum": ruijiePortSecurityAddrNum,
       "ruijiePortSecurityAddrAge": ruijiePortSecurityAddrAge,
       "ruijiePortStaticSecurAddrIfAge": ruijiePortStaticSecurAddrIfAge,
       "ruijiePortSecurityAddressCurrentNum": ruijiePortSecurityAddressCurrentNum,
       "ruijiePortStaticSecurAddrCurrentNum": ruijiePortStaticSecurAddrCurrentNum,
       "ruijiePortSecurityIpDistrMode": ruijiePortSecurityIpDistrMode,
       "ruijieSecurityTraps": ruijieSecurityTraps,
       "portSecurityViolate": portSecurityViolate,
       "ruijieSecurityMIBConformance": ruijieSecurityMIBConformance,
       "ruijieSecurityMIBCompliances": ruijieSecurityMIBCompliances,
       "ruijieSecurityMIBCompliance": ruijieSecurityMIBCompliance,
       "ruijieSecurityMIBGroups": ruijieSecurityMIBGroups,
       "ruijieUserManageMIBGroup": ruijieUserManageMIBGroup,
       "ruijieSecurityAddressMIBGroup": ruijieSecurityAddressMIBGroup,
       "ruijiePortSecurityMIBGroup": ruijiePortSecurityMIBGroup}
)
