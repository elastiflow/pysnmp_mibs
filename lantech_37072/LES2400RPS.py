# SNMP MIB module (LES2400RPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/lantech_37072/LES2400RPS.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:14:09 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 internet,
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
    "internet",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

contact = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 0)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



class DisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Lantech_ObjectIdentity = ObjectIdentity
lantech = _Lantech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303)
)
_L2switch_ObjectIdentity = ObjectIdentity
l2switch = _L2switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1)
)
_Les2400rps_ObjectIdentity = ObjectIdentity
les2400rps = _Les2400rps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66)
)
_SystemMgt_ObjectIdentity = ObjectIdentity
systemMgt = _SystemMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1)
)
_SwitchInfo_ObjectIdentity = ObjectIdentity
switchInfo = _SwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1)
)
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1)
)
switchInfoEntry.setIndexNames(
    (0, "LES2400RPS", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")
_SwUnitIndex_Type = Integer32
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 1),
    _SwUnitIndex_Type()
)
swUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUnitIndex.setStatus("current")


class _SwsysName_Type(DisplayString):
    """Custom type swsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwsysName_Type.__name__ = "DisplayString"
_SwsysName_Object = MibTableColumn
swsysName = _SwsysName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 2),
    _SwsysName_Type()
)
swsysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swsysName.setStatus("current")


class _SwsysDescr_Type(DisplayString):
    """Custom type swsysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwsysDescr_Type.__name__ = "DisplayString"
_SwsysDescr_Object = MibTableColumn
swsysDescr = _SwsysDescr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 3),
    _SwsysDescr_Type()
)
swsysDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swsysDescr.setStatus("current")


class _SwsysLocation_Type(DisplayString):
    """Custom type swsysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwsysLocation_Type.__name__ = "DisplayString"
_SwsysLocation_Object = MibTableColumn
swsysLocation = _SwsysLocation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 4),
    _SwsysLocation_Type()
)
swsysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swsysLocation.setStatus("current")


class _SwsysContact_Type(DisplayString):
    """Custom type swsysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwsysContact_Type.__name__ = "DisplayString"
_SwsysContact_Object = MibTableColumn
swsysContact = _SwsysContact_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 5),
    _SwsysContact_Type()
)
swsysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swsysContact.setStatus("current")


class _SwFwVer_Type(DisplayString):
    """Custom type swFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwFwVer_Type.__name__ = "DisplayString"
_SwFwVer_Object = MibTableColumn
swFwVer = _SwFwVer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 6),
    _SwFwVer_Type()
)
swFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwVer.setStatus("current")


class _SwKerVer_Type(DisplayString):
    """Custom type swKerVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwKerVer_Type.__name__ = "DisplayString"
_SwKerVer_Object = MibTableColumn
swKerVer = _SwKerVer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 7),
    _SwKerVer_Type()
)
swKerVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swKerVer.setStatus("current")
_SwMacAddress_Type = MacAddress
_SwMacAddress_Object = MibTableColumn
swMacAddress = _SwMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 8),
    _SwMacAddress_Type()
)
swMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacAddress.setStatus("current")


class _SwSerialNum_Type(DisplayString):
    """Custom type swSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_SwSerialNum_Type.__name__ = "DisplayString"
_SwSerialNum_Object = MibTableColumn
swSerialNum = _SwSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 1, 1, 9),
    _SwSerialNum_Type()
)
swSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNum.setStatus("current")
_SwitchCurrentPortNameListTable_Object = MibTable
switchCurrentPortNameListTable = _SwitchCurrentPortNameListTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 2)
)
if mibBuilder.loadTexts:
    switchCurrentPortNameListTable.setStatus("current")
_SwitchCurrentPortNameListEntry_Object = MibTableRow
switchCurrentPortNameListEntry = _SwitchCurrentPortNameListEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 2, 1)
)
switchCurrentPortNameListEntry.setIndexNames(
    (0, "LES2400RPS", "swCurrentPortNameListIndex"),
)
if mibBuilder.loadTexts:
    switchCurrentPortNameListEntry.setStatus("current")
_SwCurrentPortNameListIndex_Type = Integer32
_SwCurrentPortNameListIndex_Object = MibTableColumn
swCurrentPortNameListIndex = _SwCurrentPortNameListIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 2, 1, 1),
    _SwCurrentPortNameListIndex_Type()
)
swCurrentPortNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swCurrentPortNameListIndex.setStatus("current")


class _SwCurrentPortNameListPortName_Type(DisplayString):
    """Custom type swCurrentPortNameListPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SwCurrentPortNameListPortName_Type.__name__ = "DisplayString"
_SwCurrentPortNameListPortName_Object = MibTableColumn
swCurrentPortNameListPortName = _SwCurrentPortNameListPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 2, 1, 2),
    _SwCurrentPortNameListPortName_Type()
)
swCurrentPortNameListPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentPortNameListPortName.setStatus("current")


class _SwCurrentPortNameListPortNumber_Type(DisplayString):
    """Custom type swCurrentPortNameListPortNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SwCurrentPortNameListPortNumber_Type.__name__ = "DisplayString"
_SwCurrentPortNameListPortNumber_Object = MibTableColumn
swCurrentPortNameListPortNumber = _SwCurrentPortNameListPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 1, 2, 1, 3),
    _SwCurrentPortNameListPortNumber_Type()
)
swCurrentPortNameListPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentPortNameListPortNumber.setStatus("current")
_SwitchIpCfg_ObjectIdentity = ObjectIdentity
switchIpCfg = _SwitchIpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2)
)
_SwitchIpCfgTable_Object = MibTable
switchIpCfgTable = _SwitchIpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1)
)
if mibBuilder.loadTexts:
    switchIpCfgTable.setStatus("current")
_SwitchIpCfgEntry_Object = MibTableRow
switchIpCfgEntry = _SwitchIpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1, 1)
)
switchIpCfgEntry.setIndexNames(
    (0, "LES2400RPS", "swIpCfgIndex"),
)
if mibBuilder.loadTexts:
    switchIpCfgEntry.setStatus("current")
_SwIpCfgIndex_Type = Integer32
_SwIpCfgIndex_Object = MibTableColumn
swIpCfgIndex = _SwIpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1, 1, 1),
    _SwIpCfgIndex_Type()
)
swIpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIpCfgIndex.setStatus("current")


class _SwIpCfgDHCPStatus_Type(Integer32):
    """Custom type swIpCfgDHCPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwIpCfgDHCPStatus_Type.__name__ = "Integer32"
_SwIpCfgDHCPStatus_Object = MibTableColumn
swIpCfgDHCPStatus = _SwIpCfgDHCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1, 1, 2),
    _SwIpCfgDHCPStatus_Type()
)
swIpCfgDHCPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpCfgDHCPStatus.setStatus("current")
_SwIpCfgAddress_Type = IpAddress
_SwIpCfgAddress_Object = MibTableColumn
swIpCfgAddress = _SwIpCfgAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1, 1, 3),
    _SwIpCfgAddress_Type()
)
swIpCfgAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpCfgAddress.setStatus("current")
_SwIpCfgSubMask_Type = IpAddress
_SwIpCfgSubMask_Object = MibTableColumn
swIpCfgSubMask = _SwIpCfgSubMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1, 1, 4),
    _SwIpCfgSubMask_Type()
)
swIpCfgSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpCfgSubMask.setStatus("current")
_SwIpCfgGateway_Type = IpAddress
_SwIpCfgGateway_Object = MibTableColumn
swIpCfgGateway = _SwIpCfgGateway_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1, 1, 5),
    _SwIpCfgGateway_Type()
)
swIpCfgGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpCfgGateway.setStatus("current")
_SwIpCfgDNS1_Type = IpAddress
_SwIpCfgDNS1_Object = MibTableColumn
swIpCfgDNS1 = _SwIpCfgDNS1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1, 1, 6),
    _SwIpCfgDNS1_Type()
)
swIpCfgDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpCfgDNS1.setStatus("current")
_SwIpCfgDNS2_Type = IpAddress
_SwIpCfgDNS2_Object = MibTableColumn
swIpCfgDNS2 = _SwIpCfgDNS2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 2, 1, 1, 7),
    _SwIpCfgDNS2_Type()
)
swIpCfgDNS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpCfgDNS2.setStatus("current")
_SwitchDHCPServerMgt_ObjectIdentity = ObjectIdentity
switchDHCPServerMgt = _SwitchDHCPServerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3)
)
_SwitchDHCPServerCfgTable_Object = MibTable
switchDHCPServerCfgTable = _SwitchDHCPServerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1)
)
if mibBuilder.loadTexts:
    switchDHCPServerCfgTable.setStatus("current")
_SwitchDHCPServerCfgEntry_Object = MibTableRow
switchDHCPServerCfgEntry = _SwitchDHCPServerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1)
)
switchDHCPServerCfgEntry.setIndexNames(
    (0, "LES2400RPS", "swDHCPServerCfgIndex"),
)
if mibBuilder.loadTexts:
    switchDHCPServerCfgEntry.setStatus("current")
_SwDHCPServerCfgIndex_Type = Integer32
_SwDHCPServerCfgIndex_Object = MibTableColumn
swDHCPServerCfgIndex = _SwDHCPServerCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1, 1),
    _SwDHCPServerCfgIndex_Type()
)
swDHCPServerCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPServerCfgIndex.setStatus("current")


class _SwDHCPServerCfgStatus_Type(Integer32):
    """Custom type swDHCPServerCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPServerCfgStatus_Type.__name__ = "Integer32"
_SwDHCPServerCfgStatus_Object = MibTableColumn
swDHCPServerCfgStatus = _SwDHCPServerCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1, 2),
    _SwDHCPServerCfgStatus_Type()
)
swDHCPServerCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPServerCfgStatus.setStatus("current")
_SwDHCPServerCfgLowIPAddr_Type = IpAddress
_SwDHCPServerCfgLowIPAddr_Object = MibTableColumn
swDHCPServerCfgLowIPAddr = _SwDHCPServerCfgLowIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1, 3),
    _SwDHCPServerCfgLowIPAddr_Type()
)
swDHCPServerCfgLowIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPServerCfgLowIPAddr.setStatus("current")
_SwDHCPServerCfgHighIPAddr_Type = IpAddress
_SwDHCPServerCfgHighIPAddr_Object = MibTableColumn
swDHCPServerCfgHighIPAddr = _SwDHCPServerCfgHighIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1, 4),
    _SwDHCPServerCfgHighIPAddr_Type()
)
swDHCPServerCfgHighIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPServerCfgHighIPAddr.setStatus("current")
_SwDHCPServerCfgSubMask_Type = IpAddress
_SwDHCPServerCfgSubMask_Object = MibTableColumn
swDHCPServerCfgSubMask = _SwDHCPServerCfgSubMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1, 5),
    _SwDHCPServerCfgSubMask_Type()
)
swDHCPServerCfgSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPServerCfgSubMask.setStatus("current")
_SwDHCPServerCfgGateway_Type = IpAddress
_SwDHCPServerCfgGateway_Object = MibTableColumn
swDHCPServerCfgGateway = _SwDHCPServerCfgGateway_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1, 6),
    _SwDHCPServerCfgGateway_Type()
)
swDHCPServerCfgGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPServerCfgGateway.setStatus("current")
_SwDHCPServerCfgDNS_Type = IpAddress
_SwDHCPServerCfgDNS_Object = MibTableColumn
swDHCPServerCfgDNS = _SwDHCPServerCfgDNS_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1, 7),
    _SwDHCPServerCfgDNS_Type()
)
swDHCPServerCfgDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPServerCfgDNS.setStatus("current")
_SwDHCPServerCfgLeaseTime_Type = Integer32
_SwDHCPServerCfgLeaseTime_Object = MibTableColumn
swDHCPServerCfgLeaseTime = _SwDHCPServerCfgLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 1, 1, 8),
    _SwDHCPServerCfgLeaseTime_Type()
)
swDHCPServerCfgLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPServerCfgLeaseTime.setStatus("current")
_SwitchDHCPServerClientInfoTable_Object = MibTable
switchDHCPServerClientInfoTable = _SwitchDHCPServerClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 2)
)
if mibBuilder.loadTexts:
    switchDHCPServerClientInfoTable.setStatus("current")
_SwitchDHCPServerClientInfoEntry_Object = MibTableRow
switchDHCPServerClientInfoEntry = _SwitchDHCPServerClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 2, 1)
)
switchDHCPServerClientInfoEntry.setIndexNames(
    (0, "LES2400RPS", "swDHCPServerClientInfoIndex"),
)
if mibBuilder.loadTexts:
    switchDHCPServerClientInfoEntry.setStatus("current")
_SwDHCPServerClientInfoIndex_Type = Integer32
_SwDHCPServerClientInfoIndex_Object = MibTableColumn
swDHCPServerClientInfoIndex = _SwDHCPServerClientInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 2, 1, 1),
    _SwDHCPServerClientInfoIndex_Type()
)
swDHCPServerClientInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPServerClientInfoIndex.setStatus("current")


class _SwDHCPServerClientInfoIPAddr_Type(DisplayString):
    """Custom type swDHCPServerClientInfoIPAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwDHCPServerClientInfoIPAddr_Type.__name__ = "DisplayString"
_SwDHCPServerClientInfoIPAddr_Object = MibTableColumn
swDHCPServerClientInfoIPAddr = _SwDHCPServerClientInfoIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 2, 1, 2),
    _SwDHCPServerClientInfoIPAddr_Type()
)
swDHCPServerClientInfoIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPServerClientInfoIPAddr.setStatus("current")


class _SwDHCPServerClientInfoID_Type(DisplayString):
    """Custom type swDHCPServerClientInfoID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SwDHCPServerClientInfoID_Type.__name__ = "DisplayString"
_SwDHCPServerClientInfoID_Object = MibTableColumn
swDHCPServerClientInfoID = _SwDHCPServerClientInfoID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 2, 1, 3),
    _SwDHCPServerClientInfoID_Type()
)
swDHCPServerClientInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPServerClientInfoID.setStatus("current")


class _SwDHCPServerClientInfoType_Type(DisplayString):
    """Custom type swDHCPServerClientInfoType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SwDHCPServerClientInfoType_Type.__name__ = "DisplayString"
_SwDHCPServerClientInfoType_Object = MibTableColumn
swDHCPServerClientInfoType = _SwDHCPServerClientInfoType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 2, 1, 4),
    _SwDHCPServerClientInfoType_Type()
)
swDHCPServerClientInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPServerClientInfoType.setStatus("current")


class _SwDHCPServerClientInfoStatus_Type(DisplayString):
    """Custom type swDHCPServerClientInfoStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SwDHCPServerClientInfoStatus_Type.__name__ = "DisplayString"
_SwDHCPServerClientInfoStatus_Object = MibTableColumn
swDHCPServerClientInfoStatus = _SwDHCPServerClientInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 2, 1, 5),
    _SwDHCPServerClientInfoStatus_Type()
)
swDHCPServerClientInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPServerClientInfoStatus.setStatus("current")
_SwDHCPServerClientInfoLease_Type = Integer32
_SwDHCPServerClientInfoLease_Object = MibTableColumn
swDHCPServerClientInfoLease = _SwDHCPServerClientInfoLease_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 2, 1, 6),
    _SwDHCPServerClientInfoLease_Type()
)
swDHCPServerClientInfoLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPServerClientInfoLease.setStatus("current")
_SwitchDHCPServerIPBindingTable_Object = MibTable
switchDHCPServerIPBindingTable = _SwitchDHCPServerIPBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 3)
)
if mibBuilder.loadTexts:
    switchDHCPServerIPBindingTable.setStatus("current")
_SwitchDHCPServerIPBindingEntry_Object = MibTableRow
switchDHCPServerIPBindingEntry = _SwitchDHCPServerIPBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 3, 1)
)
switchDHCPServerIPBindingEntry.setIndexNames(
    (0, "LES2400RPS", "swDHCPServerIPBindingPortNum"),
)
if mibBuilder.loadTexts:
    switchDHCPServerIPBindingEntry.setStatus("current")
_SwDHCPServerIPBindingPortNum_Type = Integer32
_SwDHCPServerIPBindingPortNum_Object = MibTableColumn
swDHCPServerIPBindingPortNum = _SwDHCPServerIPBindingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 3, 1, 1),
    _SwDHCPServerIPBindingPortNum_Type()
)
swDHCPServerIPBindingPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPServerIPBindingPortNum.setStatus("current")
_SwDHCPServerIPBindingAddr_Type = IpAddress
_SwDHCPServerIPBindingAddr_Object = MibTableColumn
swDHCPServerIPBindingAddr = _SwDHCPServerIPBindingAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 3, 1, 2),
    _SwDHCPServerIPBindingAddr_Type()
)
swDHCPServerIPBindingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPServerIPBindingAddr.setStatus("current")


class _SwDHCPServerIPBindingPortName_Type(DisplayString):
    """Custom type swDHCPServerIPBindingPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwDHCPServerIPBindingPortName_Type.__name__ = "DisplayString"
_SwDHCPServerIPBindingPortName_Object = MibTableColumn
swDHCPServerIPBindingPortName = _SwDHCPServerIPBindingPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 3, 3, 1, 3),
    _SwDHCPServerIPBindingPortName_Type()
)
swDHCPServerIPBindingPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPServerIPBindingPortName.setStatus("current")
_SwitchSyslogMgt_ObjectIdentity = ObjectIdentity
switchSyslogMgt = _SwitchSyslogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4)
)
_SwitchSyslogCfg_ObjectIdentity = ObjectIdentity
switchSyslogCfg = _SwitchSyslogCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 1)
)


class _SwSyslogStatus_Type(Integer32):
    """Custom type swSyslogStatus based on Integer32"""
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
        *(("clientOnly", 1),
          ("serverOnly", 2),
          ("bothClientAndServer", 3),
          ("disabled", 4))
    )


_SwSyslogStatus_Type.__name__ = "Integer32"
_SwSyslogStatus_Object = MibScalar
swSyslogStatus = _SwSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 1, 1),
    _SwSyslogStatus_Type()
)
swSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogStatus.setStatus("current")
_SwSyslogServerAddr_Type = IpAddress
_SwSyslogServerAddr_Object = MibScalar
swSyslogServerAddr = _SwSyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 1, 2),
    _SwSyslogServerAddr_Type()
)
swSyslogServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogServerAddr.setStatus("current")
_SwitchSyslogLogTable_Object = MibTable
switchSyslogLogTable = _SwitchSyslogLogTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    switchSyslogLogTable.setStatus("current")
_SwitchSyslogLogEntry_Object = MibTableRow
switchSyslogLogEntry = _SwitchSyslogLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 1, 3, 1)
)
switchSyslogLogEntry.setIndexNames(
    (0, "LES2400RPS", "swSyslogLogIndex"),
)
if mibBuilder.loadTexts:
    switchSyslogLogEntry.setStatus("current")
_SwSyslogLogIndex_Type = Integer32
_SwSyslogLogIndex_Object = MibTableColumn
swSyslogLogIndex = _SwSyslogLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 1, 3, 1, 1),
    _SwSyslogLogIndex_Type()
)
swSyslogLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSyslogLogIndex.setStatus("current")


class _SwSyslogLogDescription_Type(DisplayString):
    """Custom type swSyslogLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SwSyslogLogDescription_Type.__name__ = "DisplayString"
_SwSyslogLogDescription_Object = MibTableColumn
swSyslogLogDescription = _SwSyslogLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 1, 3, 1, 2),
    _SwSyslogLogDescription_Type()
)
swSyslogLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSyslogLogDescription.setStatus("current")


class _SwSyslogClearLogTable_Type(Integer32):
    """Custom type swSyslogClearLogTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SwSyslogClearLogTable_Type.__name__ = "Integer32"
_SwSyslogClearLogTable_Object = MibScalar
swSyslogClearLogTable = _SwSyslogClearLogTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 1, 4),
    _SwSyslogClearLogTable_Type()
)
swSyslogClearLogTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogClearLogTable.setStatus("current")
_SwitchSyslogSmtpCfg_ObjectIdentity = ObjectIdentity
switchSyslogSmtpCfg = _SwitchSyslogSmtpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2)
)


class _SwSyslogEmailAlertStatus_Type(Integer32):
    """Custom type swSyslogEmailAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwSyslogEmailAlertStatus_Type.__name__ = "Integer32"
_SwSyslogEmailAlertStatus_Object = MibScalar
swSyslogEmailAlertStatus = _SwSyslogEmailAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 1),
    _SwSyslogEmailAlertStatus_Type()
)
swSyslogEmailAlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogEmailAlertStatus.setStatus("current")
_SwSyslogEmailAlertAddr_Type = IpAddress
_SwSyslogEmailAlertAddr_Object = MibScalar
swSyslogEmailAlertAddr = _SwSyslogEmailAlertAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 2),
    _SwSyslogEmailAlertAddr_Type()
)
swSyslogEmailAlertAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogEmailAlertAddr.setStatus("current")


class _SwSyslogEmailAlertSubject_Type(DisplayString):
    """Custom type swSyslogEmailAlertSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSyslogEmailAlertSubject_Type.__name__ = "DisplayString"
_SwSyslogEmailAlertSubject_Object = MibScalar
swSyslogEmailAlertSubject = _SwSyslogEmailAlertSubject_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 3),
    _SwSyslogEmailAlertSubject_Type()
)
swSyslogEmailAlertSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogEmailAlertSubject.setStatus("current")


class _SwSyslogEmailAlertSender_Type(DisplayString):
    """Custom type swSyslogEmailAlertSender based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SwSyslogEmailAlertSender_Type.__name__ = "DisplayString"
_SwSyslogEmailAlertSender_Object = MibScalar
swSyslogEmailAlertSender = _SwSyslogEmailAlertSender_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 4),
    _SwSyslogEmailAlertSender_Type()
)
swSyslogEmailAlertSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogEmailAlertSender.setStatus("current")


class _SwSyslogEmailAlertAuthentication_Type(Integer32):
    """Custom type swSyslogEmailAlertAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwSyslogEmailAlertAuthentication_Type.__name__ = "Integer32"
_SwSyslogEmailAlertAuthentication_Object = MibScalar
swSyslogEmailAlertAuthentication = _SwSyslogEmailAlertAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 5),
    _SwSyslogEmailAlertAuthentication_Type()
)
swSyslogEmailAlertAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogEmailAlertAuthentication.setStatus("current")


class _SwSyslogEmailAlertAccount_Type(DisplayString):
    """Custom type swSyslogEmailAlertAccount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SwSyslogEmailAlertAccount_Type.__name__ = "DisplayString"
_SwSyslogEmailAlertAccount_Object = MibScalar
swSyslogEmailAlertAccount = _SwSyslogEmailAlertAccount_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 6),
    _SwSyslogEmailAlertAccount_Type()
)
swSyslogEmailAlertAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogEmailAlertAccount.setStatus("current")


class _SwSyslogEmailAlertPassword_Type(DisplayString):
    """Custom type swSyslogEmailAlertPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_SwSyslogEmailAlertPassword_Type.__name__ = "DisplayString"
_SwSyslogEmailAlertPassword_Object = MibScalar
swSyslogEmailAlertPassword = _SwSyslogEmailAlertPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 7),
    _SwSyslogEmailAlertPassword_Type()
)
swSyslogEmailAlertPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swSyslogEmailAlertPassword.setStatus("current")
_SwitchSyslogEmailAlertRcptTable_Object = MibTable
switchSyslogEmailAlertRcptTable = _SwitchSyslogEmailAlertRcptTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 8)
)
if mibBuilder.loadTexts:
    switchSyslogEmailAlertRcptTable.setStatus("current")
_SwitchSyslogEmailAlertRcptEntry_Object = MibTableRow
switchSyslogEmailAlertRcptEntry = _SwitchSyslogEmailAlertRcptEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 8, 1)
)
switchSyslogEmailAlertRcptEntry.setIndexNames(
    (0, "LES2400RPS", "swSyslogEmailAlertRcptIndex"),
)
if mibBuilder.loadTexts:
    switchSyslogEmailAlertRcptEntry.setStatus("current")
_SwSyslogEmailAlertRcptIndex_Type = Integer32
_SwSyslogEmailAlertRcptIndex_Object = MibTableColumn
swSyslogEmailAlertRcptIndex = _SwSyslogEmailAlertRcptIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 8, 1, 1),
    _SwSyslogEmailAlertRcptIndex_Type()
)
swSyslogEmailAlertRcptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSyslogEmailAlertRcptIndex.setStatus("current")


class _SwSyslogEmailAlertRcptEmailAddr_Type(DisplayString):
    """Custom type swSyslogEmailAlertRcptEmailAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SwSyslogEmailAlertRcptEmailAddr_Type.__name__ = "DisplayString"
_SwSyslogEmailAlertRcptEmailAddr_Object = MibTableColumn
swSyslogEmailAlertRcptEmailAddr = _SwSyslogEmailAlertRcptEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 2, 8, 1, 2),
    _SwSyslogEmailAlertRcptEmailAddr_Type()
)
swSyslogEmailAlertRcptEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogEmailAlertRcptEmailAddr.setStatus("current")
_SwitchSyslogEventCfg_ObjectIdentity = ObjectIdentity
switchSyslogEventCfg = _SwitchSyslogEventCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3)
)
_SwitchSyslogSystemEventsTable_Object = MibTable
switchSyslogSystemEventsTable = _SwitchSyslogSystemEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    switchSyslogSystemEventsTable.setStatus("current")
_SwitchSyslogSystemEventsEntry_Object = MibTableRow
switchSyslogSystemEventsEntry = _SwitchSyslogSystemEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 1, 1)
)
switchSyslogSystemEventsEntry.setIndexNames(
    (0, "LES2400RPS", "swSyslogSystemEventsIndex"),
)
if mibBuilder.loadTexts:
    switchSyslogSystemEventsEntry.setStatus("current")
_SwSyslogSystemEventsIndex_Type = Integer32
_SwSyslogSystemEventsIndex_Object = MibTableColumn
swSyslogSystemEventsIndex = _SwSyslogSystemEventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 1, 1, 1),
    _SwSyslogSystemEventsIndex_Type()
)
swSyslogSystemEventsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSyslogSystemEventsIndex.setStatus("current")


class _SwSyslogDeviceColdStartEvent_Type(Integer32):
    """Custom type swSyslogDeviceColdStartEvent based on Integer32"""
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
        *(("log", 1),
          ("smtp", 2),
          ("logandsmtp", 3),
          ("disabled", 4))
    )


_SwSyslogDeviceColdStartEvent_Type.__name__ = "Integer32"
_SwSyslogDeviceColdStartEvent_Object = MibTableColumn
swSyslogDeviceColdStartEvent = _SwSyslogDeviceColdStartEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 1, 1, 2),
    _SwSyslogDeviceColdStartEvent_Type()
)
swSyslogDeviceColdStartEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogDeviceColdStartEvent.setStatus("current")


class _SwSyslogDeviceWarmStartEvent_Type(Integer32):
    """Custom type swSyslogDeviceWarmStartEvent based on Integer32"""
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
        *(("log", 1),
          ("smtp", 2),
          ("logandsmtp", 3),
          ("disabled", 4))
    )


_SwSyslogDeviceWarmStartEvent_Type.__name__ = "Integer32"
_SwSyslogDeviceWarmStartEvent_Object = MibTableColumn
swSyslogDeviceWarmStartEvent = _SwSyslogDeviceWarmStartEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 1, 1, 3),
    _SwSyslogDeviceWarmStartEvent_Type()
)
swSyslogDeviceWarmStartEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogDeviceWarmStartEvent.setStatus("current")


class _SwSyslogAuthenticationFailureEvent_Type(Integer32):
    """Custom type swSyslogAuthenticationFailureEvent based on Integer32"""
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
        *(("log", 1),
          ("smtp", 2),
          ("logandsmtp", 3),
          ("disabled", 4))
    )


_SwSyslogAuthenticationFailureEvent_Type.__name__ = "Integer32"
_SwSyslogAuthenticationFailureEvent_Object = MibTableColumn
swSyslogAuthenticationFailureEvent = _SwSyslogAuthenticationFailureEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 1, 1, 4),
    _SwSyslogAuthenticationFailureEvent_Type()
)
swSyslogAuthenticationFailureEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogAuthenticationFailureEvent.setStatus("current")


class _SwSyslogFanFailureEvent_Type(Integer32):
    """Custom type swSyslogFanFailureEvent based on Integer32"""
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
        *(("log", 1),
          ("smtp", 2),
          ("logandsmtp", 3),
          ("disabled", 4))
    )


_SwSyslogFanFailureEvent_Type.__name__ = "Integer32"
_SwSyslogFanFailureEvent_Object = MibTableColumn
swSyslogFanFailureEvent = _SwSyslogFanFailureEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 1, 1, 6),
    _SwSyslogFanFailureEvent_Type()
)
swSyslogFanFailureEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogFanFailureEvent.setStatus("current")
_SwitchSyslogPortEventsTable_Object = MibTable
switchSyslogPortEventsTable = _SwitchSyslogPortEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    switchSyslogPortEventsTable.setStatus("current")
_SwitchSyslogPortEventsEntry_Object = MibTableRow
switchSyslogPortEventsEntry = _SwitchSyslogPortEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 2, 1)
)
switchSyslogPortEventsEntry.setIndexNames(
    (0, "LES2400RPS", "swSyslogPortNumber"),
)
if mibBuilder.loadTexts:
    switchSyslogPortEventsEntry.setStatus("current")
_SwSyslogPortNumber_Type = Integer32
_SwSyslogPortNumber_Object = MibTableColumn
swSyslogPortNumber = _SwSyslogPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 2, 1, 1),
    _SwSyslogPortNumber_Type()
)
swSyslogPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSyslogPortNumber.setStatus("current")


class _SwSyslogPortEventLog_Type(Integer32):
    """Custom type swSyslogPortEventLog based on Integer32"""
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
        *(("linkup", 1),
          ("linkdown", 2),
          ("linkupandlinkdown", 3),
          ("disabled", 4))
    )


_SwSyslogPortEventLog_Type.__name__ = "Integer32"
_SwSyslogPortEventLog_Object = MibTableColumn
swSyslogPortEventLog = _SwSyslogPortEventLog_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 2, 1, 2),
    _SwSyslogPortEventLog_Type()
)
swSyslogPortEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogPortEventLog.setStatus("current")


class _SwSyslogPortEventSMTP_Type(Integer32):
    """Custom type swSyslogPortEventSMTP based on Integer32"""
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
        *(("linkup", 1),
          ("linkdown", 2),
          ("linkupandlinkdown", 3),
          ("disabled", 4))
    )


_SwSyslogPortEventSMTP_Type.__name__ = "Integer32"
_SwSyslogPortEventSMTP_Object = MibTableColumn
swSyslogPortEventSMTP = _SwSyslogPortEventSMTP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 2, 1, 3),
    _SwSyslogPortEventSMTP_Type()
)
swSyslogPortEventSMTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSyslogPortEventSMTP.setStatus("current")


class _SwSyslogPortName_Type(DisplayString):
    """Custom type swSyslogPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwSyslogPortName_Type.__name__ = "DisplayString"
_SwSyslogPortName_Object = MibTableColumn
swSyslogPortName = _SwSyslogPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 4, 3, 2, 1, 4),
    _SwSyslogPortName_Type()
)
swSyslogPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSyslogPortName.setStatus("current")
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5)
)


class _SntpClientStatus_Type(Integer32):
    """Custom type sntpClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SntpClientStatus_Type.__name__ = "Integer32"
_SntpClientStatus_Object = MibScalar
sntpClientStatus = _SntpClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5, 1),
    _SntpClientStatus_Type()
)
sntpClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientStatus.setStatus("current")


class _SntpDaylightSavingTime_Type(Integer32):
    """Custom type sntpDaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SntpDaylightSavingTime_Type.__name__ = "Integer32"
_SntpDaylightSavingTime_Object = MibScalar
sntpDaylightSavingTime = _SntpDaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5, 2),
    _SntpDaylightSavingTime_Type()
)
sntpDaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingTime.setStatus("current")


class _SntpUTCTimezone_Type(Integer32):
    """Custom type sntpUTCTimezone based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("gmt-negative-12-00-Eniwetok-Kwajalein", 1),
          ("gmt-negative-11-00-Midway-Island-Samoa", 2),
          ("gmt-negative-10-00-Hawaii", 3),
          ("gmt-negative-09-00-Alaska", 4),
          ("gmt-negative-08-00-Pacific-Time-US-and-Canada-Tijuana", 5),
          ("gmt-negative-07-00-Arizona", 6),
          ("gmt-negative-07-00-Mountain-Time-US-and-Canada", 7),
          ("gmt-negative-06-00-Central-Time-US-and-Canada", 8),
          ("gmt-negative-06-00-Mexico-City-Tegucigalpa", 9),
          ("gmt-negative-06-00-Saskatchewan", 10),
          ("gmt-negative-05-00-Bogota-Lima-Quito", 11),
          ("gmt-negative-05-00-Eastern-Time-US-and-Canada", 12),
          ("gmt-negative-05-00-Indiana-East", 13),
          ("gmt-negative-04-00-Atlantic-Time-Canada", 14),
          ("gmt-negative-04-00-Caracas-La-Paz", 15),
          ("gmt-negative-04-00-Santiago", 16),
          ("gmt-negative-03-30-Newfoundland", 17),
          ("gmt-negative-03-00-Brasilia", 18),
          ("gmt-negative-03-00-Buenos-Aires-Georgetown", 19),
          ("gmt-negative-02-00-Mid-Atlantic", 20),
          ("gmt-negative-01-00-Azores-Cape-Verde-Is", 21),
          ("gmt-Casablanca-Monrovia", 22),
          ("gmt-Greenwich-Mean-Time-Dublin-Edinburgh-Lisbon-London", 23),
          ("gmt-positive-01-00-Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna", 24),
          ("gmt-positive-01-00-Belgrade-Bratislava-Budapest-Ljubljana-Prague", 25),
          ("gmt-positive-01-00-Brussels-Copenhagen-Madrid-Paris-Vilnius", 26),
          ("gmt-positive-01-00-Sarajevo-Skopje-Sofija-Warsaw-Zagreb", 27),
          ("gmt-positive-02-00-Athens-Istanbul-Minsk", 28),
          ("gmt-positive-02-00-Bucharest", 29),
          ("gmt-positive-02-00-Cairo", 30),
          ("gmt-positive-02-00-Harare-Pretoria", 31),
          ("gmt-positive-02-00-Helsinki-Riga-Tallinn", 32),
          ("gmt-positive-02-00-Jerusalem", 33),
          ("gmt-positive-03-00-Baghdad-Kuwait-Riyadh", 34),
          ("gmt-positive-03-00-Moscow-St-Petersburg-Volgograd", 35),
          ("gmt-positive-03-00-Mairobi", 36),
          ("gmt-positive-03-30-Tehran", 37),
          ("gmt-positive-04-00-Abu-Dhabi-Muscat", 38),
          ("gmt-positive-04-00-Baku-Tbilisi", 39),
          ("gmt-positive-04-30-Kabul", 40),
          ("gmt-positive-05-00-Ekaterinburg", 41),
          ("gmt-positive-05-00-Islamabad-Karachi-Tashkent", 42),
          ("gmt-positive-05-30-Bombay-Calcutta-Madras-New-Delhi", 43),
          ("gmt-positive-06-00-Astana-Almaty-Dhaka", 44),
          ("gmt-positive-06-00-Colombo", 45),
          ("gmt-positive-07-00-Bangkok-Hanoi-Jakarta", 46),
          ("gmt-positive-08-00-Beijing-Chongqing-Hong-Kong-Urumqi", 47),
          ("gmt-positive-08-00-Perth", 48),
          ("gmt-positive-08-00-Singapore", 49),
          ("gmt-positive-08-00-Taipei", 50),
          ("gmt-positive-09-00-Osaka-Sapporo-Tokyo", 51),
          ("gmt-positive-09-00-Seoul", 52),
          ("gmt-positive-09-00-Yakutsk", 53),
          ("gmt-positive-09-30-Adelaide", 54),
          ("gmt-positive-09-30-Darwin", 55),
          ("gmt-positive-10-00-Brisbane", 56),
          ("gmt-positive-10-00-Canberra-Melbourne-Sydney", 57),
          ("gmt-positive-10-00-Guam-Port-Moresby", 58),
          ("gmt-positive-10-00-Hobart", 59),
          ("gmt-positive-10-00-Vladivostok", 60),
          ("gmt-positive-11-00-Magadan-Solomon-Is-New-Caledonia", 61),
          ("gmt-positive-12-00-Auckland-Wllington", 62),
          ("gmt-positive-12-00-Fiji-Kamchatka-Marshall-Is", 63))
    )


_SntpUTCTimezone_Type.__name__ = "Integer32"
_SntpUTCTimezone_Object = MibScalar
sntpUTCTimezone = _SntpUTCTimezone_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5, 3),
    _SntpUTCTimezone_Type()
)
sntpUTCTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpUTCTimezone.setStatus("current")
_SntpServerIP_Type = IpAddress
_SntpServerIP_Object = MibScalar
sntpServerIP = _SntpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5, 4),
    _SntpServerIP_Type()
)
sntpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerIP.setStatus("current")


class _SntpSwitchTimer_Type(DisplayString):
    """Custom type sntpSwitchTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SntpSwitchTimer_Type.__name__ = "DisplayString"
_SntpSwitchTimer_Object = MibScalar
sntpSwitchTimer = _SntpSwitchTimer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5, 5),
    _SntpSwitchTimer_Type()
)
sntpSwitchTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpSwitchTimer.setStatus("current")


class _SntpDaylightSavingPeriodStart_Type(DisplayString):
    """Custom type sntpDaylightSavingPeriodStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_SntpDaylightSavingPeriodStart_Type.__name__ = "DisplayString"
_SntpDaylightSavingPeriodStart_Object = MibScalar
sntpDaylightSavingPeriodStart = _SntpDaylightSavingPeriodStart_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5, 6),
    _SntpDaylightSavingPeriodStart_Type()
)
sntpDaylightSavingPeriodStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingPeriodStart.setStatus("current")


class _SntpDaylightSavingPeriodEnd_Type(DisplayString):
    """Custom type sntpDaylightSavingPeriodEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_SntpDaylightSavingPeriodEnd_Type.__name__ = "DisplayString"
_SntpDaylightSavingPeriodEnd_Object = MibScalar
sntpDaylightSavingPeriodEnd = _SntpDaylightSavingPeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5, 7),
    _SntpDaylightSavingPeriodEnd_Type()
)
sntpDaylightSavingPeriodEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingPeriodEnd.setStatus("current")
_SntpDaylightSavingOffset_Type = Integer32
_SntpDaylightSavingOffset_Object = MibScalar
sntpDaylightSavingOffset = _SntpDaylightSavingOffset_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 5, 8),
    _SntpDaylightSavingOffset_Type()
)
sntpDaylightSavingOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingOffset.setStatus("current")
_IpSecurityMgt_ObjectIdentity = ObjectIdentity
ipSecurityMgt = _IpSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6)
)


class _IpSecurityStatus_Type(Integer32):
    """Custom type ipSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpSecurityStatus_Type.__name__ = "Integer32"
_IpSecurityStatus_Object = MibScalar
ipSecurityStatus = _IpSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 1),
    _IpSecurityStatus_Type()
)
ipSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityStatus.setStatus("current")


class _IpSecurityHTTPServerStatus_Type(Integer32):
    """Custom type ipSecurityHTTPServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpSecurityHTTPServerStatus_Type.__name__ = "Integer32"
_IpSecurityHTTPServerStatus_Object = MibScalar
ipSecurityHTTPServerStatus = _IpSecurityHTTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 2),
    _IpSecurityHTTPServerStatus_Type()
)
ipSecurityHTTPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityHTTPServerStatus.setStatus("current")


class _IpSecurityTelnetServerStatus_Type(Integer32):
    """Custom type ipSecurityTelnetServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpSecurityTelnetServerStatus_Type.__name__ = "Integer32"
_IpSecurityTelnetServerStatus_Object = MibScalar
ipSecurityTelnetServerStatus = _IpSecurityTelnetServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 3),
    _IpSecurityTelnetServerStatus_Type()
)
ipSecurityTelnetServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityTelnetServerStatus.setStatus("current")
_IpSecuritySecurityIP1_Type = IpAddress
_IpSecuritySecurityIP1_Object = MibScalar
ipSecuritySecurityIP1 = _IpSecuritySecurityIP1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 4),
    _IpSecuritySecurityIP1_Type()
)
ipSecuritySecurityIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP1.setStatus("current")
_IpSecuritySecurityIP2_Type = IpAddress
_IpSecuritySecurityIP2_Object = MibScalar
ipSecuritySecurityIP2 = _IpSecuritySecurityIP2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 5),
    _IpSecuritySecurityIP2_Type()
)
ipSecuritySecurityIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP2.setStatus("current")
_IpSecuritySecurityIP3_Type = IpAddress
_IpSecuritySecurityIP3_Object = MibScalar
ipSecuritySecurityIP3 = _IpSecuritySecurityIP3_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 6),
    _IpSecuritySecurityIP3_Type()
)
ipSecuritySecurityIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP3.setStatus("current")
_IpSecuritySecurityIP4_Type = IpAddress
_IpSecuritySecurityIP4_Object = MibScalar
ipSecuritySecurityIP4 = _IpSecuritySecurityIP4_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 7),
    _IpSecuritySecurityIP4_Type()
)
ipSecuritySecurityIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP4.setStatus("current")
_IpSecuritySecurityIP5_Type = IpAddress
_IpSecuritySecurityIP5_Object = MibScalar
ipSecuritySecurityIP5 = _IpSecuritySecurityIP5_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 8),
    _IpSecuritySecurityIP5_Type()
)
ipSecuritySecurityIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP5.setStatus("current")
_IpSecuritySecurityIP6_Type = IpAddress
_IpSecuritySecurityIP6_Object = MibScalar
ipSecuritySecurityIP6 = _IpSecuritySecurityIP6_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 9),
    _IpSecuritySecurityIP6_Type()
)
ipSecuritySecurityIP6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP6.setStatus("current")
_IpSecuritySecurityIP7_Type = IpAddress
_IpSecuritySecurityIP7_Object = MibScalar
ipSecuritySecurityIP7 = _IpSecuritySecurityIP7_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 10),
    _IpSecuritySecurityIP7_Type()
)
ipSecuritySecurityIP7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP7.setStatus("current")
_IpSecuritySecurityIP8_Type = IpAddress
_IpSecuritySecurityIP8_Object = MibScalar
ipSecuritySecurityIP8 = _IpSecuritySecurityIP8_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 11),
    _IpSecuritySecurityIP8_Type()
)
ipSecuritySecurityIP8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP8.setStatus("current")
_IpSecuritySecurityIP9_Type = IpAddress
_IpSecuritySecurityIP9_Object = MibScalar
ipSecuritySecurityIP9 = _IpSecuritySecurityIP9_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 12),
    _IpSecuritySecurityIP9_Type()
)
ipSecuritySecurityIP9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP9.setStatus("current")
_IpSecuritySecurityIP10_Type = IpAddress
_IpSecuritySecurityIP10_Object = MibScalar
ipSecuritySecurityIP10 = _IpSecuritySecurityIP10_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 6, 13),
    _IpSecuritySecurityIP10_Type()
)
ipSecuritySecurityIP10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP10.setStatus("current")
_SwitchUserAuth_ObjectIdentity = ObjectIdentity
switchUserAuth = _SwitchUserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 7)
)


class _SwUserAuthID_Type(DisplayString):
    """Custom type swUserAuthID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SwUserAuthID_Type.__name__ = "DisplayString"
_SwUserAuthID_Object = MibScalar
swUserAuthID = _SwUserAuthID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 7, 1),
    _SwUserAuthID_Type()
)
swUserAuthID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUserAuthID.setStatus("current")


class _SwUserAuthPassword_Type(DisplayString):
    """Custom type swUserAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SwUserAuthPassword_Type.__name__ = "DisplayString"
_SwUserAuthPassword_Object = MibScalar
swUserAuthPassword = _SwUserAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 7, 2),
    _SwUserAuthPassword_Type()
)
swUserAuthPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swUserAuthPassword.setStatus("current")
_SwitchAdvanceCfg_ObjectIdentity = ObjectIdentity
switchAdvanceCfg = _SwitchAdvanceCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8)
)
_SwBSFCfg_ObjectIdentity = ObjectIdentity
swBSFCfg = _SwBSFCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 1)
)


class _SwBSFFloodedUnicastMulticastPackets_Type(Integer32):
    """Custom type swBSFFloodedUnicastMulticastPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwBSFFloodedUnicastMulticastPackets_Type.__name__ = "Integer32"
_SwBSFFloodedUnicastMulticastPackets_Object = MibScalar
swBSFFloodedUnicastMulticastPackets = _SwBSFFloodedUnicastMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 1, 1),
    _SwBSFFloodedUnicastMulticastPackets_Type()
)
swBSFFloodedUnicastMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBSFFloodedUnicastMulticastPackets.setStatus("current")


class _SwBSFControlPackets_Type(Integer32):
    """Custom type swBSFControlPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwBSFControlPackets_Type.__name__ = "Integer32"
_SwBSFControlPackets_Object = MibScalar
swBSFControlPackets = _SwBSFControlPackets_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 1, 2),
    _SwBSFControlPackets_Type()
)
swBSFControlPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBSFControlPackets.setStatus("current")


class _SwBSFIPMulticastPackets_Type(Integer32):
    """Custom type swBSFIPMulticastPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwBSFIPMulticastPackets_Type.__name__ = "Integer32"
_SwBSFIPMulticastPackets_Object = MibScalar
swBSFIPMulticastPackets = _SwBSFIPMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 1, 3),
    _SwBSFIPMulticastPackets_Type()
)
swBSFIPMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBSFIPMulticastPackets.setStatus("current")


class _SwBSFBroadcastPackets_Type(Integer32):
    """Custom type swBSFBroadcastPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwBSFBroadcastPackets_Type.__name__ = "Integer32"
_SwBSFBroadcastPackets_Object = MibScalar
swBSFBroadcastPackets = _SwBSFBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 1, 4),
    _SwBSFBroadcastPackets_Type()
)
swBSFBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBSFBroadcastPackets.setStatus("current")


class _SwBSFRate_Type(Integer32):
    """Custom type swBSFRate based on Integer32"""
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
        *(("rate-1-2", 1),
          ("rate-1-4", 2),
          ("rate-1-8", 3),
          ("rate-1-16", 4))
    )


_SwBSFRate_Type.__name__ = "Integer32"
_SwBSFRate_Object = MibScalar
swBSFRate = _SwBSFRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 1, 5),
    _SwBSFRate_Type()
)
swBSFRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBSFRate.setStatus("current")


class _SwAgeTime_Type(Integer32):
    """Custom type swAgeTime based on Integer32"""
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
        *(("age-150S", 1),
          ("age-300S", 2),
          ("age-600S", 3),
          ("age-disabled", 4))
    )


_SwAgeTime_Type.__name__ = "Integer32"
_SwAgeTime_Object = MibScalar
swAgeTime = _SwAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 2),
    _SwAgeTime_Type()
)
swAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgeTime.setStatus("current")


class _SwAutoFlush_Type(Integer32):
    """Custom type swAutoFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwAutoFlush_Type.__name__ = "Integer32"
_SwAutoFlush_Object = MibScalar
swAutoFlush = _SwAutoFlush_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 3),
    _SwAutoFlush_Type()
)
swAutoFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAutoFlush.setStatus("current")


class _SwJumboFrame_Type(Integer32):
    """Custom type swJumboFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwJumboFrame_Type.__name__ = "Integer32"
_SwJumboFrame_Object = MibScalar
swJumboFrame = _SwJumboFrame_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 1, 8, 4),
    _SwJumboFrame_Type()
)
swJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJumboFrame.setStatus("current")
_SwitchPortMgt_ObjectIdentity = ObjectIdentity
switchPortMgt = _SwitchPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2)
)
_SwitchPortStatMgt_ObjectIdentity = ObjectIdentity
switchPortStatMgt = _SwitchPortStatMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1)
)
_SwitchPortStatTable_Object = MibTable
switchPortStatTable = _SwitchPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1)
)
if mibBuilder.loadTexts:
    switchPortStatTable.setStatus("current")
_SwitchPortStatEntry_Object = MibTableRow
switchPortStatEntry = _SwitchPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1)
)
switchPortStatEntry.setIndexNames(
    (0, "LES2400RPS", "swPortStatIndex"),
)
if mibBuilder.loadTexts:
    switchPortStatEntry.setStatus("current")
_SwPortStatIndex_Type = Integer32
_SwPortStatIndex_Object = MibTableColumn
swPortStatIndex = _SwPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 1),
    _SwPortStatIndex_Type()
)
swPortStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortStatIndex.setStatus("current")


class _SwPortStatType_Type(Integer32):
    """Custom type swPortStatType based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("thousandBaseTX", 1),
          ("thousandBaseSX", 2),
          ("thousandBaseLX", 3),
          ("hundredBaseTX", 4),
          ("hundredBaseFX-MM", 5),
          ("hundredBaseFX-SM", 6),
          ("thousandBaseSFP", 7),
          ("thousandBaseGBIC", 8),
          ("thousandBaseTXandSFPCombo", 9),
          ("hundredBaseFX-MM-6P", 10),
          ("hundredBaseFX-SM-6P", 11),
          ("hundredBaseWDM15", 12),
          ("hundredBaseWDM13", 13),
          ("hundredBaseSFP", 14))
    )


_SwPortStatType_Type.__name__ = "Integer32"
_SwPortStatType_Object = MibTableColumn
swPortStatType = _SwPortStatType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 2),
    _SwPortStatType_Type()
)
swPortStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatType.setStatus("current")


class _SwPortStatLink_Type(Integer32):
    """Custom type swPortStatLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SwPortStatLink_Type.__name__ = "Integer32"
_SwPortStatLink_Object = MibTableColumn
swPortStatLink = _SwPortStatLink_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 3),
    _SwPortStatLink_Type()
)
swPortStatLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatLink.setStatus("current")


class _SwPortStatState_Type(Integer32):
    """Custom type swPortStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwPortStatState_Type.__name__ = "Integer32"
_SwPortStatState_Object = MibTableColumn
swPortStatState = _SwPortStatState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 4),
    _SwPortStatState_Type()
)
swPortStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatState.setStatus("current")
_SwPortStatTXGoodPkt_Type = Integer32
_SwPortStatTXGoodPkt_Object = MibTableColumn
swPortStatTXGoodPkt = _SwPortStatTXGoodPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 5),
    _SwPortStatTXGoodPkt_Type()
)
swPortStatTXGoodPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatTXGoodPkt.setStatus("current")
_SwPortStatTXBadPkt_Type = Integer32
_SwPortStatTXBadPkt_Object = MibTableColumn
swPortStatTXBadPkt = _SwPortStatTXBadPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 6),
    _SwPortStatTXBadPkt_Type()
)
swPortStatTXBadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatTXBadPkt.setStatus("current")
_SwPortStatRXGoodPkt_Type = Integer32
_SwPortStatRXGoodPkt_Object = MibTableColumn
swPortStatRXGoodPkt = _SwPortStatRXGoodPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 7),
    _SwPortStatRXGoodPkt_Type()
)
swPortStatRXGoodPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatRXGoodPkt.setStatus("current")
_SwPortStatRXBadPkt_Type = Integer32
_SwPortStatRXBadPkt_Object = MibTableColumn
swPortStatRXBadPkt = _SwPortStatRXBadPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 8),
    _SwPortStatRXBadPkt_Type()
)
swPortStatRXBadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatRXBadPkt.setStatus("current")
_SwPortStatTXAbortPkt_Type = Integer32
_SwPortStatTXAbortPkt_Object = MibTableColumn
swPortStatTXAbortPkt = _SwPortStatTXAbortPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 9),
    _SwPortStatTXAbortPkt_Type()
)
swPortStatTXAbortPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatTXAbortPkt.setStatus("current")
_SwPortStatPacketCollision_Type = Integer32
_SwPortStatPacketCollision_Object = MibTableColumn
swPortStatPacketCollision = _SwPortStatPacketCollision_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 10),
    _SwPortStatPacketCollision_Type()
)
swPortStatPacketCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatPacketCollision.setStatus("current")
_SwPortStatPacketDropped_Type = Integer32
_SwPortStatPacketDropped_Object = MibTableColumn
swPortStatPacketDropped = _SwPortStatPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 11),
    _SwPortStatPacketDropped_Type()
)
swPortStatPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatPacketDropped.setStatus("current")
_SwPortStatRxBcastPkt_Type = Integer32
_SwPortStatRxBcastPkt_Object = MibTableColumn
swPortStatRxBcastPkt = _SwPortStatRxBcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 12),
    _SwPortStatRxBcastPkt_Type()
)
swPortStatRxBcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatRxBcastPkt.setStatus("current")
_SwPortStatRxMcastPkt_Type = Integer32
_SwPortStatRxMcastPkt_Object = MibTableColumn
swPortStatRxMcastPkt = _SwPortStatRxMcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 13),
    _SwPortStatRxMcastPkt_Type()
)
swPortStatRxMcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatRxMcastPkt.setStatus("current")


class _SwPortStatPortName_Type(DisplayString):
    """Custom type swPortStatPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwPortStatPortName_Type.__name__ = "DisplayString"
_SwPortStatPortName_Object = MibTableColumn
swPortStatPortName = _SwPortStatPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 1, 1, 14),
    _SwPortStatPortName_Type()
)
swPortStatPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatPortName.setStatus("current")


class _SwitchPortStatClearTable_Type(Integer32):
    """Custom type switchPortStatClearTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SwitchPortStatClearTable_Type.__name__ = "Integer32"
_SwitchPortStatClearTable_Object = MibScalar
switchPortStatClearTable = _SwitchPortStatClearTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 1, 2),
    _SwitchPortStatClearTable_Type()
)
switchPortStatClearTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPortStatClearTable.setStatus("current")
_SwitchPortMgtTable_Object = MibTable
switchPortMgtTable = _SwitchPortMgtTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2)
)
if mibBuilder.loadTexts:
    switchPortMgtTable.setStatus("current")
_SwitchPortMgtEntry_Object = MibTableRow
switchPortMgtEntry = _SwitchPortMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1)
)
switchPortMgtEntry.setIndexNames(
    (0, "LES2400RPS", "swPortMgtIndex"),
)
if mibBuilder.loadTexts:
    switchPortMgtEntry.setStatus("current")
_SwPortMgtIndex_Type = Integer32
_SwPortMgtIndex_Object = MibTableColumn
swPortMgtIndex = _SwPortMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1, 1),
    _SwPortMgtIndex_Type()
)
swPortMgtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortMgtIndex.setStatus("current")


class _SwPortMgtPortName_Type(DisplayString):
    """Custom type swPortMgtPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SwPortMgtPortName_Type.__name__ = "DisplayString"
_SwPortMgtPortName_Object = MibTableColumn
swPortMgtPortName = _SwPortMgtPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1, 2),
    _SwPortMgtPortName_Type()
)
swPortMgtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMgtPortName.setStatus("current")


class _SwPortMgtPortStatus_Type(Integer32):
    """Custom type swPortMgtPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwPortMgtPortStatus_Type.__name__ = "Integer32"
_SwPortMgtPortStatus_Object = MibTableColumn
swPortMgtPortStatus = _SwPortMgtPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1, 3),
    _SwPortMgtPortStatus_Type()
)
swPortMgtPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMgtPortStatus.setStatus("current")


class _SwPortMgtNegotiation_Type(Integer32):
    """Custom type swPortMgtNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force", 2))
    )


_SwPortMgtNegotiation_Type.__name__ = "Integer32"
_SwPortMgtNegotiation_Object = MibTableColumn
swPortMgtNegotiation = _SwPortMgtNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1, 4),
    _SwPortMgtNegotiation_Type()
)
swPortMgtNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMgtNegotiation.setStatus("current")


class _SwPortMgtSpeed_Type(Integer32):
    """Custom type swPortMgtSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed-10M", 1),
          ("speed-100M", 2),
          ("speed-1000M", 3))
    )


_SwPortMgtSpeed_Type.__name__ = "Integer32"
_SwPortMgtSpeed_Object = MibTableColumn
swPortMgtSpeed = _SwPortMgtSpeed_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1, 5),
    _SwPortMgtSpeed_Type()
)
swPortMgtSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMgtSpeed.setStatus("current")


class _SwPortMgtDuplex_Type(Integer32):
    """Custom type swPortMgtDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 1),
          ("halfduplex", 2))
    )


_SwPortMgtDuplex_Type.__name__ = "Integer32"
_SwPortMgtDuplex_Object = MibTableColumn
swPortMgtDuplex = _SwPortMgtDuplex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1, 6),
    _SwPortMgtDuplex_Type()
)
swPortMgtDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMgtDuplex.setStatus("current")


class _SwPortMgtFlowControl_Type(Integer32):
    """Custom type swPortMgtFlowControl based on Integer32"""
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


_SwPortMgtFlowControl_Type.__name__ = "Integer32"
_SwPortMgtFlowControl_Object = MibTableColumn
swPortMgtFlowControl = _SwPortMgtFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1, 7),
    _SwPortMgtFlowControl_Type()
)
swPortMgtFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMgtFlowControl.setStatus("current")


class _SwPortMgtSecurity_Type(Integer32):
    """Custom type swPortMgtSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SwPortMgtSecurity_Type.__name__ = "Integer32"
_SwPortMgtSecurity_Object = MibTableColumn
swPortMgtSecurity = _SwPortMgtSecurity_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 2, 1, 8),
    _SwPortMgtSecurity_Type()
)
swPortMgtSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMgtSecurity.setStatus("current")
_SwitchPortTrunkMgt_ObjectIdentity = ObjectIdentity
switchPortTrunkMgt = _SwitchPortTrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3)
)
_SwPortTrunkSysPri_Type = Integer32
_SwPortTrunkSysPri_Object = MibScalar
swPortTrunkSysPri = _SwPortTrunkSysPri_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 1),
    _SwPortTrunkSysPri_Type()
)
swPortTrunkSysPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkSysPri.setStatus("current")
_SwitchPortTrunkAggregatorTable_Object = MibTable
switchPortTrunkAggregatorTable = _SwitchPortTrunkAggregatorTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 2)
)
if mibBuilder.loadTexts:
    switchPortTrunkAggregatorTable.setStatus("current")
_SwitchPortTrunkAggregatorEntry_Object = MibTableRow
switchPortTrunkAggregatorEntry = _SwitchPortTrunkAggregatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 2, 1)
)
switchPortTrunkAggregatorEntry.setIndexNames(
    (0, "LES2400RPS", "swPortTrunkAggregatorIndex"),
)
if mibBuilder.loadTexts:
    switchPortTrunkAggregatorEntry.setStatus("current")
_SwPortTrunkAggregatorIndex_Type = Integer32
_SwPortTrunkAggregatorIndex_Object = MibTableColumn
swPortTrunkAggregatorIndex = _SwPortTrunkAggregatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 2, 1, 1),
    _SwPortTrunkAggregatorIndex_Type()
)
swPortTrunkAggregatorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkAggregatorIndex.setStatus("current")


class _SwPortTrunkAggregatorGroupName_Type(DisplayString):
    """Custom type swPortTrunkAggregatorGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwPortTrunkAggregatorGroupName_Type.__name__ = "DisplayString"
_SwPortTrunkAggregatorGroupName_Object = MibTableColumn
swPortTrunkAggregatorGroupName = _SwPortTrunkAggregatorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 2, 1, 2),
    _SwPortTrunkAggregatorGroupName_Type()
)
swPortTrunkAggregatorGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkAggregatorGroupName.setStatus("current")
_SwPortTrunkAggregatorMemberPorts_Type = PortList
_SwPortTrunkAggregatorMemberPorts_Object = MibTableColumn
swPortTrunkAggregatorMemberPorts = _SwPortTrunkAggregatorMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 2, 1, 3),
    _SwPortTrunkAggregatorMemberPorts_Type()
)
swPortTrunkAggregatorMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkAggregatorMemberPorts.setStatus("current")


class _SwPortTrunkAggregatorLACPStatus_Type(Integer32):
    """Custom type swPortTrunkAggregatorLACPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwPortTrunkAggregatorLACPStatus_Type.__name__ = "Integer32"
_SwPortTrunkAggregatorLACPStatus_Object = MibTableColumn
swPortTrunkAggregatorLACPStatus = _SwPortTrunkAggregatorLACPStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 2, 1, 4),
    _SwPortTrunkAggregatorLACPStatus_Type()
)
swPortTrunkAggregatorLACPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkAggregatorLACPStatus.setStatus("current")
_SwPortTrunkAggregatorWorkPorts_Type = Integer32
_SwPortTrunkAggregatorWorkPorts_Object = MibTableColumn
swPortTrunkAggregatorWorkPorts = _SwPortTrunkAggregatorWorkPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 2, 1, 5),
    _SwPortTrunkAggregatorWorkPorts_Type()
)
swPortTrunkAggregatorWorkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkAggregatorWorkPorts.setStatus("current")
_SwitchPortTrunkAggregatorInfoTable_Object = MibTable
switchPortTrunkAggregatorInfoTable = _SwitchPortTrunkAggregatorInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 3)
)
if mibBuilder.loadTexts:
    switchPortTrunkAggregatorInfoTable.setStatus("current")
_SwitchPortTrunkAggregatorInfoEntry_Object = MibTableRow
switchPortTrunkAggregatorInfoEntry = _SwitchPortTrunkAggregatorInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 3, 1)
)
switchPortTrunkAggregatorInfoEntry.setIndexNames(
    (0, "LES2400RPS", "swPortTrunkAggregatorInfoIndex"),
)
if mibBuilder.loadTexts:
    switchPortTrunkAggregatorInfoEntry.setStatus("current")
_SwPortTrunkAggregatorInfoIndex_Type = Integer32
_SwPortTrunkAggregatorInfoIndex_Object = MibTableColumn
swPortTrunkAggregatorInfoIndex = _SwPortTrunkAggregatorInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 3, 1, 1),
    _SwPortTrunkAggregatorInfoIndex_Type()
)
swPortTrunkAggregatorInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkAggregatorInfoIndex.setStatus("current")


class _SwPortTrunkAggregatorInfoGroupName_Type(DisplayString):
    """Custom type swPortTrunkAggregatorInfoGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwPortTrunkAggregatorInfoGroupName_Type.__name__ = "DisplayString"
_SwPortTrunkAggregatorInfoGroupName_Object = MibTableColumn
swPortTrunkAggregatorInfoGroupName = _SwPortTrunkAggregatorInfoGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 3, 1, 2),
    _SwPortTrunkAggregatorInfoGroupName_Type()
)
swPortTrunkAggregatorInfoGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkAggregatorInfoGroupName.setStatus("current")


class _SwPortTrunkAggregatorInfoDescription_Type(DisplayString):
    """Custom type swPortTrunkAggregatorInfoDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwPortTrunkAggregatorInfoDescription_Type.__name__ = "DisplayString"
_SwPortTrunkAggregatorInfoDescription_Object = MibTableColumn
swPortTrunkAggregatorInfoDescription = _SwPortTrunkAggregatorInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 3, 1, 3),
    _SwPortTrunkAggregatorInfoDescription_Type()
)
swPortTrunkAggregatorInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkAggregatorInfoDescription.setStatus("current")
_SwitchPortTrunkLACPStateActTable_Object = MibTable
switchPortTrunkLACPStateActTable = _SwitchPortTrunkLACPStateActTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 4)
)
if mibBuilder.loadTexts:
    switchPortTrunkLACPStateActTable.setStatus("current")
_SwitchPortTrunkLACPStateActEntry_Object = MibTableRow
switchPortTrunkLACPStateActEntry = _SwitchPortTrunkLACPStateActEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 4, 1)
)
switchPortTrunkLACPStateActEntry.setIndexNames(
    (0, "LES2400RPS", "swPortTrunkLACPStateActPortNum"),
)
if mibBuilder.loadTexts:
    switchPortTrunkLACPStateActEntry.setStatus("current")
_SwPortTrunkLACPStateActPortNum_Type = Integer32
_SwPortTrunkLACPStateActPortNum_Object = MibTableColumn
swPortTrunkLACPStateActPortNum = _SwPortTrunkLACPStateActPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 4, 1, 1),
    _SwPortTrunkLACPStateActPortNum_Type()
)
swPortTrunkLACPStateActPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkLACPStateActPortNum.setStatus("current")


class _SwPortTrunkLACPStateActStatus_Type(Integer32):
    """Custom type swPortTrunkLACPStateActStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passtive", 2),
          ("disabled", 3))
    )


_SwPortTrunkLACPStateActStatus_Type.__name__ = "Integer32"
_SwPortTrunkLACPStateActStatus_Object = MibTableColumn
swPortTrunkLACPStateActStatus = _SwPortTrunkLACPStateActStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 4, 1, 2),
    _SwPortTrunkLACPStateActStatus_Type()
)
swPortTrunkLACPStateActStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkLACPStateActStatus.setStatus("current")


class _SwPortTrunkLACPStateActPortName_Type(DisplayString):
    """Custom type swPortTrunkLACPStateActPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwPortTrunkLACPStateActPortName_Type.__name__ = "DisplayString"
_SwPortTrunkLACPStateActPortName_Object = MibTableColumn
swPortTrunkLACPStateActPortName = _SwPortTrunkLACPStateActPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 3, 4, 1, 3),
    _SwPortTrunkLACPStateActPortName_Type()
)
swPortTrunkLACPStateActPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkLACPStateActPortName.setStatus("current")
_SwitchPortMirrorMgt_ObjectIdentity = ObjectIdentity
switchPortMirrorMgt = _SwitchPortMirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 4)
)


class _SwPortMirrorStatus_Type(Integer32):
    """Custom type swPortMirrorStatus based on Integer32"""
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
        *(("disable", 1),
          ("rx", 2),
          ("tx", 3),
          ("both", 4))
    )


_SwPortMirrorStatus_Type.__name__ = "Integer32"
_SwPortMirrorStatus_Object = MibScalar
swPortMirrorStatus = _SwPortMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 4, 1),
    _SwPortMirrorStatus_Type()
)
swPortMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorStatus.setStatus("current")


class _SwPortMirrorAnlysisPortName_Type(DisplayString):
    """Custom type swPortMirrorAnlysisPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwPortMirrorAnlysisPortName_Type.__name__ = "DisplayString"
_SwPortMirrorAnlysisPortName_Object = MibScalar
swPortMirrorAnlysisPortName = _SwPortMirrorAnlysisPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 4, 4),
    _SwPortMirrorAnlysisPortName_Type()
)
swPortMirrorAnlysisPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorAnlysisPortName.setStatus("current")


class _SwPortMirrorMonitoredPortName_Type(DisplayString):
    """Custom type swPortMirrorMonitoredPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwPortMirrorMonitoredPortName_Type.__name__ = "DisplayString"
_SwPortMirrorMonitoredPortName_Object = MibScalar
swPortMirrorMonitoredPortName = _SwPortMirrorMonitoredPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 4, 5),
    _SwPortMirrorMonitoredPortName_Type()
)
swPortMirrorMonitoredPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorMonitoredPortName.setStatus("current")
_SwitchPortRateLimitMgt_ObjectIdentity = ObjectIdentity
switchPortRateLimitMgt = _SwitchPortRateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 5)
)
_SwitchPortRateLimitingTable_Object = MibTable
switchPortRateLimitingTable = _SwitchPortRateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 5, 1)
)
if mibBuilder.loadTexts:
    switchPortRateLimitingTable.setStatus("current")
_SwitchPortRateLimitingEntry_Object = MibTableRow
switchPortRateLimitingEntry = _SwitchPortRateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 5, 1, 1)
)
switchPortRateLimitingEntry.setIndexNames(
    (0, "LES2400RPS", "swPortRateLimitingPortNum"),
)
if mibBuilder.loadTexts:
    switchPortRateLimitingEntry.setStatus("current")
_SwPortRateLimitingPortNum_Type = Integer32
_SwPortRateLimitingPortNum_Object = MibTableColumn
swPortRateLimitingPortNum = _SwPortRateLimitingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 5, 1, 1, 1),
    _SwPortRateLimitingPortNum_Type()
)
swPortRateLimitingPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRateLimitingPortNum.setStatus("current")
_SwPortRateLimitingInRate_Type = Integer32
_SwPortRateLimitingInRate_Object = MibTableColumn
swPortRateLimitingInRate = _SwPortRateLimitingInRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 5, 1, 1, 2),
    _SwPortRateLimitingInRate_Type()
)
swPortRateLimitingInRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortRateLimitingInRate.setStatus("current")
_SwPortRateLimitingOutRate_Type = Integer32
_SwPortRateLimitingOutRate_Object = MibTableColumn
swPortRateLimitingOutRate = _SwPortRateLimitingOutRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 5, 1, 1, 3),
    _SwPortRateLimitingOutRate_Type()
)
swPortRateLimitingOutRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortRateLimitingOutRate.setStatus("current")


class _SwPortRateLimitingPortName_Type(DisplayString):
    """Custom type swPortRateLimitingPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwPortRateLimitingPortName_Type.__name__ = "DisplayString"
_SwPortRateLimitingPortName_Object = MibTableColumn
swPortRateLimitingPortName = _SwPortRateLimitingPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 2, 5, 1, 1, 4),
    _SwPortRateLimitingPortName_Type()
)
swPortRateLimitingPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRateLimitingPortName.setStatus("current")
_SwitchProtocolMgt_ObjectIdentity = ObjectIdentity
switchProtocolMgt = _SwitchProtocolMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3)
)
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1)
)


class _VlanOperationMode_Type(Integer32):
    """Custom type vlanOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portbased", 1),
          ("ieee8021q", 2))
    )


_VlanOperationMode_Type.__name__ = "Integer32"
_VlanOperationMode_Object = MibScalar
vlanOperationMode = _VlanOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 1),
    _VlanOperationMode_Type()
)
vlanOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanOperationMode.setStatus("current")


class _VlanGVRP_Type(Integer32):
    """Custom type vlanGVRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_VlanGVRP_Type.__name__ = "Integer32"
_VlanGVRP_Object = MibScalar
vlanGVRP = _VlanGVRP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 2),
    _VlanGVRP_Type()
)
vlanGVRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanGVRP.setStatus("current")
_VlanPortBasedTable_Object = MibTable
vlanPortBasedTable = _VlanPortBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vlanPortBasedTable.setStatus("current")
_VlanPortBasedEntry_Object = MibTableRow
vlanPortBasedEntry = _VlanPortBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 3, 1)
)
vlanPortBasedEntry.setIndexNames(
    (0, "LES2400RPS", "vlanPortBasedIndex"),
)
if mibBuilder.loadTexts:
    vlanPortBasedEntry.setStatus("current")
_VlanPortBasedIndex_Type = Integer32
_VlanPortBasedIndex_Object = MibTableColumn
vlanPortBasedIndex = _VlanPortBasedIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 3, 1, 1),
    _VlanPortBasedIndex_Type()
)
vlanPortBasedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortBasedIndex.setStatus("current")


class _VlanPortBasedGroupName_Type(DisplayString):
    """Custom type vlanPortBasedGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanPortBasedGroupName_Type.__name__ = "DisplayString"
_VlanPortBasedGroupName_Object = MibTableColumn
vlanPortBasedGroupName = _VlanPortBasedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 3, 1, 2),
    _VlanPortBasedGroupName_Type()
)
vlanPortBasedGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedGroupName.setStatus("current")
_VlanPortBasedVid_Type = Integer32
_VlanPortBasedVid_Object = MibTableColumn
vlanPortBasedVid = _VlanPortBasedVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 3, 1, 3),
    _VlanPortBasedVid_Type()
)
vlanPortBasedVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedVid.setStatus("current")
_VlanPortBasedMembers_Type = PortList
_VlanPortBasedMembers_Object = MibTableColumn
vlanPortBasedMembers = _VlanPortBasedMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 3, 1, 4),
    _VlanPortBasedMembers_Type()
)
vlanPortBasedMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedMembers.setStatus("current")


class _VlanPortBasedStatus_Type(Integer32):
    """Custom type vlanPortBasedStatus based on Integer32"""
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
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_VlanPortBasedStatus_Type.__name__ = "Integer32"
_VlanPortBasedStatus_Object = MibTableColumn
vlanPortBasedStatus = _VlanPortBasedStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 3, 1, 5),
    _VlanPortBasedStatus_Type()
)
vlanPortBasedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedStatus.setStatus("current")
_VlanIEEE8021QTable_Object = MibTable
vlanIEEE8021QTable = _VlanIEEE8021QTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 4)
)
if mibBuilder.loadTexts:
    vlanIEEE8021QTable.setStatus("current")
_VlanIEEE8021QEntry_Object = MibTableRow
vlanIEEE8021QEntry = _VlanIEEE8021QEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 4, 1)
)
vlanIEEE8021QEntry.setIndexNames(
    (0, "LES2400RPS", "vlanIEEE8021QIndex"),
)
if mibBuilder.loadTexts:
    vlanIEEE8021QEntry.setStatus("current")
_VlanIEEE8021QIndex_Type = Integer32
_VlanIEEE8021QIndex_Object = MibTableColumn
vlanIEEE8021QIndex = _VlanIEEE8021QIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 4, 1, 1),
    _VlanIEEE8021QIndex_Type()
)
vlanIEEE8021QIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIEEE8021QIndex.setStatus("current")


class _VlanIEEE8021QPortName_Type(DisplayString):
    """Custom type vlanIEEE8021QPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanIEEE8021QPortName_Type.__name__ = "DisplayString"
_VlanIEEE8021QPortName_Object = MibTableColumn
vlanIEEE8021QPortName = _VlanIEEE8021QPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 4, 1, 2),
    _VlanIEEE8021QPortName_Type()
)
vlanIEEE8021QPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIEEE8021QPortName.setStatus("current")


class _VlanIEEE8021QLinkType_Type(Integer32):
    """Custom type vlanIEEE8021QLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accesslink", 1),
          ("trunklink", 2),
          ("hybridlink", 3))
    )


_VlanIEEE8021QLinkType_Type.__name__ = "Integer32"
_VlanIEEE8021QLinkType_Object = MibTableColumn
vlanIEEE8021QLinkType = _VlanIEEE8021QLinkType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 4, 1, 3),
    _VlanIEEE8021QLinkType_Type()
)
vlanIEEE8021QLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QLinkType.setStatus("current")
_VlanIEEE8021QUntaggedVid_Type = Integer32
_VlanIEEE8021QUntaggedVid_Object = MibTableColumn
vlanIEEE8021QUntaggedVid = _VlanIEEE8021QUntaggedVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 4, 1, 4),
    _VlanIEEE8021QUntaggedVid_Type()
)
vlanIEEE8021QUntaggedVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QUntaggedVid.setStatus("current")


class _VlanIEEE8021QTaggedVids_Type(DisplayString):
    """Custom type vlanIEEE8021QTaggedVids based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanIEEE8021QTaggedVids_Type.__name__ = "DisplayString"
_VlanIEEE8021QTaggedVids_Object = MibTableColumn
vlanIEEE8021QTaggedVids = _VlanIEEE8021QTaggedVids_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 4, 1, 5),
    _VlanIEEE8021QTaggedVids_Type()
)
vlanIEEE8021QTaggedVids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QTaggedVids.setStatus("current")
_VlanIEEE8021QGroupTable_Object = MibTable
vlanIEEE8021QGroupTable = _VlanIEEE8021QGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 5)
)
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupTable.setStatus("current")
_VlanIEEE8021QGroupEntry_Object = MibTableRow
vlanIEEE8021QGroupEntry = _VlanIEEE8021QGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 5, 1)
)
vlanIEEE8021QGroupEntry.setIndexNames(
    (0, "LES2400RPS", "vlanIEEE8021QGroupVid"),
)
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupEntry.setStatus("current")
_VlanIEEE8021QGroupVid_Type = Integer32
_VlanIEEE8021QGroupVid_Object = MibTableColumn
vlanIEEE8021QGroupVid = _VlanIEEE8021QGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 5, 1, 1),
    _VlanIEEE8021QGroupVid_Type()
)
vlanIEEE8021QGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupVid.setStatus("current")


class _VlanIEEE8021QGroupName_Type(DisplayString):
    """Custom type vlanIEEE8021QGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanIEEE8021QGroupName_Type.__name__ = "DisplayString"
_VlanIEEE8021QGroupName_Object = MibTableColumn
vlanIEEE8021QGroupName = _VlanIEEE8021QGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 5, 1, 2),
    _VlanIEEE8021QGroupName_Type()
)
vlanIEEE8021QGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupName.setStatus("current")


class _VlanIEEE8021QGroupStatus_Type(Integer32):
    """Custom type vlanIEEE8021QGroupStatus based on Integer32"""
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


_VlanIEEE8021QGroupStatus_Type.__name__ = "Integer32"
_VlanIEEE8021QGroupStatus_Object = MibTableColumn
vlanIEEE8021QGroupStatus = _VlanIEEE8021QGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 5, 1, 3),
    _VlanIEEE8021QGroupStatus_Type()
)
vlanIEEE8021QGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupStatus.setStatus("current")
_VlanMgtVID_Type = Integer32
_VlanMgtVID_Object = MibScalar
vlanMgtVID = _VlanMgtVID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 1, 6),
    _VlanMgtVID_Type()
)
vlanMgtVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMgtVID.setStatus("current")
_RstpMgt_ObjectIdentity = ObjectIdentity
rstpMgt = _RstpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2)
)


class _RstpStatus_Type(Integer32):
    """Custom type rstpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RstpStatus_Type.__name__ = "Integer32"
_RstpStatus_Object = MibScalar
rstpStatus = _RstpStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 1),
    _RstpStatus_Type()
)
rstpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpStatus.setStatus("current")
_RstpPriority_Type = Integer32
_RstpPriority_Object = MibScalar
rstpPriority = _RstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 2),
    _RstpPriority_Type()
)
rstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPriority.setStatus("current")
_RstpMaxAge_Type = Integer32
_RstpMaxAge_Object = MibScalar
rstpMaxAge = _RstpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 3),
    _RstpMaxAge_Type()
)
rstpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpMaxAge.setStatus("current")
_RstpHelloTime_Type = Integer32
_RstpHelloTime_Object = MibScalar
rstpHelloTime = _RstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 4),
    _RstpHelloTime_Type()
)
rstpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpHelloTime.setStatus("current")
_RstpForwardDelayTime_Type = Integer32
_RstpForwardDelayTime_Object = MibScalar
rstpForwardDelayTime = _RstpForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 5),
    _RstpForwardDelayTime_Type()
)
rstpForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpForwardDelayTime.setStatus("current")
_RstpRootBridgeInformationTable_Object = MibTable
rstpRootBridgeInformationTable = _RstpRootBridgeInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6)
)
if mibBuilder.loadTexts:
    rstpRootBridgeInformationTable.setStatus("current")
_RstpRootBridgeInformationEntry_Object = MibTableRow
rstpRootBridgeInformationEntry = _RstpRootBridgeInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1)
)
rstpRootBridgeInformationEntry.setIndexNames(
    (0, "LES2400RPS", "rstpRootBridgeInformationIndex"),
)
if mibBuilder.loadTexts:
    rstpRootBridgeInformationEntry.setStatus("current")
_RstpRootBridgeInformationIndex_Type = Integer32
_RstpRootBridgeInformationIndex_Object = MibTableColumn
rstpRootBridgeInformationIndex = _RstpRootBridgeInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1, 1),
    _RstpRootBridgeInformationIndex_Type()
)
rstpRootBridgeInformationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationIndex.setStatus("current")


class _RstpRootBridgeInformationBridgeID_Type(DisplayString):
    """Custom type rstpRootBridgeInformationBridgeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RstpRootBridgeInformationBridgeID_Type.__name__ = "DisplayString"
_RstpRootBridgeInformationBridgeID_Object = MibTableColumn
rstpRootBridgeInformationBridgeID = _RstpRootBridgeInformationBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1, 2),
    _RstpRootBridgeInformationBridgeID_Type()
)
rstpRootBridgeInformationBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationBridgeID.setStatus("current")
_RstpRootBridgeInformationRootPriority_Type = Integer32
_RstpRootBridgeInformationRootPriority_Object = MibTableColumn
rstpRootBridgeInformationRootPriority = _RstpRootBridgeInformationRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1, 3),
    _RstpRootBridgeInformationRootPriority_Type()
)
rstpRootBridgeInformationRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationRootPriority.setStatus("current")


class _RstpRootBridgeInformationRootPort_Type(DisplayString):
    """Custom type rstpRootBridgeInformationRootPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RstpRootBridgeInformationRootPort_Type.__name__ = "DisplayString"
_RstpRootBridgeInformationRootPort_Object = MibTableColumn
rstpRootBridgeInformationRootPort = _RstpRootBridgeInformationRootPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1, 4),
    _RstpRootBridgeInformationRootPort_Type()
)
rstpRootBridgeInformationRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationRootPort.setStatus("current")
_RstpRootBridgeInformationRootPathCost_Type = Integer32
_RstpRootBridgeInformationRootPathCost_Object = MibTableColumn
rstpRootBridgeInformationRootPathCost = _RstpRootBridgeInformationRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1, 5),
    _RstpRootBridgeInformationRootPathCost_Type()
)
rstpRootBridgeInformationRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationRootPathCost.setStatus("current")
_RstpRootBridgeInformationMaxAge_Type = Integer32
_RstpRootBridgeInformationMaxAge_Object = MibTableColumn
rstpRootBridgeInformationMaxAge = _RstpRootBridgeInformationMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1, 6),
    _RstpRootBridgeInformationMaxAge_Type()
)
rstpRootBridgeInformationMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationMaxAge.setStatus("current")
_RstpRootBridgeInformationHelloTime_Type = Integer32
_RstpRootBridgeInformationHelloTime_Object = MibTableColumn
rstpRootBridgeInformationHelloTime = _RstpRootBridgeInformationHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1, 7),
    _RstpRootBridgeInformationHelloTime_Type()
)
rstpRootBridgeInformationHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationHelloTime.setStatus("current")
_RstpRootBridgeInformationForwardDelay_Type = Integer32
_RstpRootBridgeInformationForwardDelay_Object = MibTableColumn
rstpRootBridgeInformationForwardDelay = _RstpRootBridgeInformationForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 6, 1, 8),
    _RstpRootBridgeInformationForwardDelay_Type()
)
rstpRootBridgeInformationForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationForwardDelay.setStatus("current")
_RstpPerPortCfgTable_Object = MibTable
rstpPerPortCfgTable = _RstpPerPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7)
)
if mibBuilder.loadTexts:
    rstpPerPortCfgTable.setStatus("current")
_RstpPerPortCfgEntry_Object = MibTableRow
rstpPerPortCfgEntry = _RstpPerPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7, 1)
)
rstpPerPortCfgEntry.setIndexNames(
    (0, "LES2400RPS", "rstpPerPortCfgPortNum"),
)
if mibBuilder.loadTexts:
    rstpPerPortCfgEntry.setStatus("current")
_RstpPerPortCfgPortNum_Type = Integer32
_RstpPerPortCfgPortNum_Object = MibTableColumn
rstpPerPortCfgPortNum = _RstpPerPortCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7, 1, 1),
    _RstpPerPortCfgPortNum_Type()
)
rstpPerPortCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortCfgPortNum.setStatus("current")
_RstpPerPortCfgPathCost_Type = Integer32
_RstpPerPortCfgPathCost_Object = MibTableColumn
rstpPerPortCfgPathCost = _RstpPerPortCfgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7, 1, 2),
    _RstpPerPortCfgPathCost_Type()
)
rstpPerPortCfgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgPathCost.setStatus("current")
_RstpPerPortCfgPriority_Type = Integer32
_RstpPerPortCfgPriority_Object = MibTableColumn
rstpPerPortCfgPriority = _RstpPerPortCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7, 1, 3),
    _RstpPerPortCfgPriority_Type()
)
rstpPerPortCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgPriority.setStatus("current")


class _RstpPerPortCfgAdminP2P_Type(Integer32):
    """Custom type rstpPerPortCfgAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("auto", 3))
    )


_RstpPerPortCfgAdminP2P_Type.__name__ = "Integer32"
_RstpPerPortCfgAdminP2P_Object = MibTableColumn
rstpPerPortCfgAdminP2P = _RstpPerPortCfgAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7, 1, 4),
    _RstpPerPortCfgAdminP2P_Type()
)
rstpPerPortCfgAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgAdminP2P.setStatus("current")


class _RstpPerPortCfgAdminEdge_Type(Integer32):
    """Custom type rstpPerPortCfgAdminEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_RstpPerPortCfgAdminEdge_Type.__name__ = "Integer32"
_RstpPerPortCfgAdminEdge_Object = MibTableColumn
rstpPerPortCfgAdminEdge = _RstpPerPortCfgAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7, 1, 5),
    _RstpPerPortCfgAdminEdge_Type()
)
rstpPerPortCfgAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgAdminEdge.setStatus("current")


class _RstpPerPortCfgAdminNonStp_Type(Integer32):
    """Custom type rstpPerPortCfgAdminNonStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_RstpPerPortCfgAdminNonStp_Type.__name__ = "Integer32"
_RstpPerPortCfgAdminNonStp_Object = MibTableColumn
rstpPerPortCfgAdminNonStp = _RstpPerPortCfgAdminNonStp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7, 1, 6),
    _RstpPerPortCfgAdminNonStp_Type()
)
rstpPerPortCfgAdminNonStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgAdminNonStp.setStatus("current")


class _RstpPerPortCfgPortName_Type(DisplayString):
    """Custom type rstpPerPortCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RstpPerPortCfgPortName_Type.__name__ = "DisplayString"
_RstpPerPortCfgPortName_Object = MibTableColumn
rstpPerPortCfgPortName = _RstpPerPortCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 7, 1, 7),
    _RstpPerPortCfgPortName_Type()
)
rstpPerPortCfgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortCfgPortName.setStatus("current")
_RstpPerPortInfoTable_Object = MibTable
rstpPerPortInfoTable = _RstpPerPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8)
)
if mibBuilder.loadTexts:
    rstpPerPortInfoTable.setStatus("current")
_RstpPerPortInfoEntry_Object = MibTableRow
rstpPerPortInfoEntry = _RstpPerPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1)
)
rstpPerPortInfoEntry.setIndexNames(
    (0, "LES2400RPS", "rstpPerPortInfoPortNum"),
)
if mibBuilder.loadTexts:
    rstpPerPortInfoEntry.setStatus("current")
_RstpPerPortInfoPortNum_Type = Integer32
_RstpPerPortInfoPortNum_Object = MibTableColumn
rstpPerPortInfoPortNum = _RstpPerPortInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 1),
    _RstpPerPortInfoPortNum_Type()
)
rstpPerPortInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPortNum.setStatus("current")
_RstpPerPortInfoPathCost_Type = Integer32
_RstpPerPortInfoPathCost_Object = MibTableColumn
rstpPerPortInfoPathCost = _RstpPerPortInfoPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 2),
    _RstpPerPortInfoPathCost_Type()
)
rstpPerPortInfoPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPathCost.setStatus("current")
_RstpPerPortInfoPriority_Type = Integer32
_RstpPerPortInfoPriority_Object = MibTableColumn
rstpPerPortInfoPriority = _RstpPerPortInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 3),
    _RstpPerPortInfoPriority_Type()
)
rstpPerPortInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPriority.setStatus("current")


class _RstpPerPortInfoAdminP2P_Type(Integer32):
    """Custom type rstpPerPortInfoAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("true", 2),
          ("false", 3))
    )


_RstpPerPortInfoAdminP2P_Type.__name__ = "Integer32"
_RstpPerPortInfoAdminP2P_Object = MibTableColumn
rstpPerPortInfoAdminP2P = _RstpPerPortInfoAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 4),
    _RstpPerPortInfoAdminP2P_Type()
)
rstpPerPortInfoAdminP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoAdminP2P.setStatus("current")


class _RstpPerPortInfoAdminEdge_Type(Integer32):
    """Custom type rstpPerPortInfoAdminEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_RstpPerPortInfoAdminEdge_Type.__name__ = "Integer32"
_RstpPerPortInfoAdminEdge_Object = MibTableColumn
rstpPerPortInfoAdminEdge = _RstpPerPortInfoAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 5),
    _RstpPerPortInfoAdminEdge_Type()
)
rstpPerPortInfoAdminEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoAdminEdge.setStatus("current")


class _RstpPerPortInfoStpNeighbor_Type(Integer32):
    """Custom type rstpPerPortInfoStpNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_RstpPerPortInfoStpNeighbor_Type.__name__ = "Integer32"
_RstpPerPortInfoStpNeighbor_Object = MibTableColumn
rstpPerPortInfoStpNeighbor = _RstpPerPortInfoStpNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 6),
    _RstpPerPortInfoStpNeighbor_Type()
)
rstpPerPortInfoStpNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoStpNeighbor.setStatus("current")


class _RstpPerPortInfoState_Type(Integer32):
    """Custom type rstpPerPortInfoState based on Integer32"""
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
        *(("nonStp", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("disabled", 4),
          ("discarding", 5))
    )


_RstpPerPortInfoState_Type.__name__ = "Integer32"
_RstpPerPortInfoState_Object = MibTableColumn
rstpPerPortInfoState = _RstpPerPortInfoState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 7),
    _RstpPerPortInfoState_Type()
)
rstpPerPortInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoState.setStatus("current")


class _RstpPerPortInfoRole_Type(Integer32):
    """Custom type rstpPerPortInfoRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("root", 2),
          ("designated", 3),
          ("alternated", 4),
          ("backup", 5),
          ("nonStp", 6))
    )


_RstpPerPortInfoRole_Type.__name__ = "Integer32"
_RstpPerPortInfoRole_Object = MibTableColumn
rstpPerPortInfoRole = _RstpPerPortInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 8),
    _RstpPerPortInfoRole_Type()
)
rstpPerPortInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoRole.setStatus("current")


class _RstpPerPortInfoPortName_Type(DisplayString):
    """Custom type rstpPerPortInfoPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RstpPerPortInfoPortName_Type.__name__ = "DisplayString"
_RstpPerPortInfoPortName_Object = MibTableColumn
rstpPerPortInfoPortName = _RstpPerPortInfoPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 2, 8, 1, 9),
    _RstpPerPortInfoPortName_Type()
)
rstpPerPortInfoPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPortName.setStatus("current")
_QosMgt_ObjectIdentity = ObjectIdentity
qosMgt = _QosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4)
)


class _QosMode_Type(Integer32):
    """Custom type qosMode based on Integer32"""
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
        *(("high-empty-then-low", 1),
          ("an-8-4-2-1-weighted-queuing-scheme", 2),
          ("an-15-7-3-1-weighted-queuing-scheme", 3),
          ("an-15-10-5-1-weighted-queuing-scheme", 4),
          ("disable-qos-priority", 5))
    )


_QosMode_Type.__name__ = "Integer32"
_QosMode_Object = MibScalar
qosMode = _QosMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 1),
    _QosMode_Type()
)
qosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMode.setStatus("current")
_Qos8021pPriorityTable_Object = MibTable
qos8021pPriorityTable = _Qos8021pPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 2)
)
if mibBuilder.loadTexts:
    qos8021pPriorityTable.setStatus("current")
_Qos8021pPriorityEntry_Object = MibTableRow
qos8021pPriorityEntry = _Qos8021pPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 2, 1)
)
qos8021pPriorityEntry.setIndexNames(
    (0, "LES2400RPS", "qos8021pPriorityIndex"),
)
if mibBuilder.loadTexts:
    qos8021pPriorityEntry.setStatus("current")
_Qos8021pPriorityIndex_Type = Integer32
_Qos8021pPriorityIndex_Object = MibTableColumn
qos8021pPriorityIndex = _Qos8021pPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 2, 1, 1),
    _Qos8021pPriorityIndex_Type()
)
qos8021pPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qos8021pPriorityIndex.setStatus("current")


class _Qos8021pPriority_Type(Integer32):
    """Custom type qos8021pPriority based on Integer32"""
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
        *(("lowest", 1),
          ("seclow", 2),
          ("sechigh", 3),
          ("highest", 4))
    )


_Qos8021pPriority_Type.__name__ = "Integer32"
_Qos8021pPriority_Object = MibTableColumn
qos8021pPriority = _Qos8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 2, 1, 2),
    _Qos8021pPriority_Type()
)
qos8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qos8021pPriority.setStatus("current")
_QosIngressPortPriorityTable_Object = MibTable
qosIngressPortPriorityTable = _QosIngressPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 3)
)
if mibBuilder.loadTexts:
    qosIngressPortPriorityTable.setStatus("current")
_QosIngressPortPriorityEntry_Object = MibTableRow
qosIngressPortPriorityEntry = _QosIngressPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 3, 1)
)
qosIngressPortPriorityEntry.setIndexNames(
    (0, "LES2400RPS", "qosIngressPortPriorityIndex"),
)
if mibBuilder.loadTexts:
    qosIngressPortPriorityEntry.setStatus("current")
_QosIngressPortPriorityIndex_Type = Integer32
_QosIngressPortPriorityIndex_Object = MibTableColumn
qosIngressPortPriorityIndex = _QosIngressPortPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 3, 1, 1),
    _QosIngressPortPriorityIndex_Type()
)
qosIngressPortPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIngressPortPriorityIndex.setStatus("current")


class _QosIngressPortPriority_Type(Integer32):
    """Custom type qosIngressPortPriority based on Integer32"""
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
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_QosIngressPortPriority_Type.__name__ = "Integer32"
_QosIngressPortPriority_Object = MibTableColumn
qosIngressPortPriority = _QosIngressPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 3, 1, 2),
    _QosIngressPortPriority_Type()
)
qosIngressPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosIngressPortPriority.setStatus("current")


class _QosIngressPortPriorityName_Type(DisplayString):
    """Custom type qosIngressPortPriorityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_QosIngressPortPriorityName_Type.__name__ = "DisplayString"
_QosIngressPortPriorityName_Object = MibTableColumn
qosIngressPortPriorityName = _QosIngressPortPriorityName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 3, 1, 3),
    _QosIngressPortPriorityName_Type()
)
qosIngressPortPriorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIngressPortPriorityName.setStatus("current")
_QosTosDscpTable_Object = MibTable
qosTosDscpTable = _QosTosDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 4)
)
if mibBuilder.loadTexts:
    qosTosDscpTable.setStatus("current")
_QosTosDscpEntry_Object = MibTableRow
qosTosDscpEntry = _QosTosDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 4, 1)
)
qosTosDscpEntry.setIndexNames(
    (0, "LES2400RPS", "qosTosDscpIndex"),
)
if mibBuilder.loadTexts:
    qosTosDscpEntry.setStatus("current")
_QosTosDscpIndex_Type = Integer32
_QosTosDscpIndex_Object = MibTableColumn
qosTosDscpIndex = _QosTosDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 4, 1, 1),
    _QosTosDscpIndex_Type()
)
qosTosDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTosDscpIndex.setStatus("current")
_QosTosDscp_Type = Integer32
_QosTosDscp_Object = MibTableColumn
qosTosDscp = _QosTosDscp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 4, 1, 2),
    _QosTosDscp_Type()
)
qosTosDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTosDscp.setStatus("current")
_QosTosDscpPriority_Type = Integer32
_QosTosDscpPriority_Object = MibTableColumn
qosTosDscpPriority = _QosTosDscpPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 4, 4, 1, 3),
    _QosTosDscpPriority_Type()
)
qosTosDscpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTosDscpPriority.setStatus("current")
_IgmpMgt_ObjectIdentity = ObjectIdentity
igmpMgt = _IgmpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5)
)


class _IgmpStatus_Type(Integer32):
    """Custom type igmpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IgmpStatus_Type.__name__ = "Integer32"
_IgmpStatus_Object = MibScalar
igmpStatus = _IgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 1),
    _IgmpStatus_Type()
)
igmpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpStatus.setStatus("current")


class _IgmpQuery_Type(Integer32):
    """Custom type igmpQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_IgmpQuery_Type.__name__ = "Integer32"
_IgmpQuery_Object = MibScalar
igmpQuery = _IgmpQuery_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 2),
    _IgmpQuery_Type()
)
igmpQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQuery.setStatus("current")
_IgmpLastQueryCount_Type = Integer32
_IgmpLastQueryCount_Object = MibScalar
igmpLastQueryCount = _IgmpLastQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 3),
    _IgmpLastQueryCount_Type()
)
igmpLastQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpLastQueryCount.setStatus("current")
_IgmpLastQueryInterval_Type = Integer32
_IgmpLastQueryInterval_Object = MibScalar
igmpLastQueryInterval = _IgmpLastQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 4),
    _IgmpLastQueryInterval_Type()
)
igmpLastQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpLastQueryInterval.setStatus("current")
_IgmpEntriesTable_Object = MibTable
igmpEntriesTable = _IgmpEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 5)
)
if mibBuilder.loadTexts:
    igmpEntriesTable.setStatus("current")
_IgmpEntriesEntry_Object = MibTableRow
igmpEntriesEntry = _IgmpEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 5, 1)
)
igmpEntriesEntry.setIndexNames(
    (0, "LES2400RPS", "igmpEntriesEntryIndex"),
)
if mibBuilder.loadTexts:
    igmpEntriesEntry.setStatus("current")
_IgmpEntriesEntryIndex_Type = Integer32
_IgmpEntriesEntryIndex_Object = MibTableColumn
igmpEntriesEntryIndex = _IgmpEntriesEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 5, 1, 1),
    _IgmpEntriesEntryIndex_Type()
)
igmpEntriesEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEntriesEntryIndex.setStatus("current")
_IgmpEntriesEntryIPAddr_Type = IpAddress
_IgmpEntriesEntryIPAddr_Object = MibTableColumn
igmpEntriesEntryIPAddr = _IgmpEntriesEntryIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 5, 1, 2),
    _IgmpEntriesEntryIPAddr_Type()
)
igmpEntriesEntryIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEntriesEntryIPAddr.setStatus("current")
_IgmpEntriesEntryVID_Type = Integer32
_IgmpEntriesEntryVID_Object = MibTableColumn
igmpEntriesEntryVID = _IgmpEntriesEntryVID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 5, 1, 3),
    _IgmpEntriesEntryVID_Type()
)
igmpEntriesEntryVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEntriesEntryVID.setStatus("current")
_IgmpEntriesEntryMembers_Type = PortList
_IgmpEntriesEntryMembers_Object = MibTableColumn
igmpEntriesEntryMembers = _IgmpEntriesEntryMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 5, 5, 1, 4),
    _IgmpEntriesEntryMembers_Type()
)
igmpEntriesEntryMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEntriesEntryMembers.setStatus("current")
_LldpMgt_ObjectIdentity = ObjectIdentity
lldpMgt = _LldpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 6)
)


class _LldpStatus_Type(Integer32):
    """Custom type lldpStatus based on Integer32"""
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


_LldpStatus_Type.__name__ = "Integer32"
_LldpStatus_Object = MibScalar
lldpStatus = _LldpStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 6, 1),
    _LldpStatus_Type()
)
lldpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpStatus.setStatus("current")
_LldpInterval_Type = Integer32
_LldpInterval_Object = MibScalar
lldpInterval = _LldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 6, 2),
    _LldpInterval_Type()
)
lldpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpInterval.setStatus("current")
_SnmpMgt_ObjectIdentity = ObjectIdentity
snmpMgt = _SnmpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7)
)


class _SnmpAgentMode_Type(Integer32):
    """Custom type snmpAgentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1v2Conly", 1),
          ("v3", 2),
          ("v1v2Cv3", 3))
    )


_SnmpAgentMode_Type.__name__ = "Integer32"
_SnmpAgentMode_Object = MibScalar
snmpAgentMode = _SnmpAgentMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 1),
    _SnmpAgentMode_Type()
)
snmpAgentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentMode.setStatus("current")


class _SnmpSystemName_Type(DisplayString):
    """Custom type snmpSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpSystemName_Type.__name__ = "DisplayString"
_SnmpSystemName_Object = MibScalar
snmpSystemName = _SnmpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 2),
    _SnmpSystemName_Type()
)
snmpSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemName.setStatus("current")


class _SnmpSystemLocation_Type(DisplayString):
    """Custom type snmpSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpSystemLocation_Type.__name__ = "DisplayString"
_SnmpSystemLocation_Object = MibScalar
snmpSystemLocation = _SnmpSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 3),
    _SnmpSystemLocation_Type()
)
snmpSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemLocation.setStatus("current")


class _SnmpSystemContact_Type(DisplayString):
    """Custom type snmpSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpSystemContact_Type.__name__ = "DisplayString"
_SnmpSystemContact_Object = MibScalar
snmpSystemContact = _SnmpSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 4),
    _SnmpSystemContact_Type()
)
snmpSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemContact.setStatus("current")
_SnmpCommunityStringTable_Object = MibTable
snmpCommunityStringTable = _SnmpCommunityStringTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 5)
)
if mibBuilder.loadTexts:
    snmpCommunityStringTable.setStatus("current")
_SnmpCommunityStringEntry_Object = MibTableRow
snmpCommunityStringEntry = _SnmpCommunityStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 5, 1)
)
snmpCommunityStringEntry.setIndexNames(
    (0, "LES2400RPS", "snmpCommunityStringIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityStringEntry.setStatus("current")
_SnmpCommunityStringIndex_Type = Integer32
_SnmpCommunityStringIndex_Object = MibTableColumn
snmpCommunityStringIndex = _SnmpCommunityStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 5, 1, 1),
    _SnmpCommunityStringIndex_Type()
)
snmpCommunityStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpCommunityStringIndex.setStatus("current")


class _SnmpCommunityStringName_Type(DisplayString):
    """Custom type snmpCommunityStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpCommunityStringName_Type.__name__ = "DisplayString"
_SnmpCommunityStringName_Object = MibTableColumn
snmpCommunityStringName = _SnmpCommunityStringName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 5, 1, 2),
    _SnmpCommunityStringName_Type()
)
snmpCommunityStringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityStringName.setStatus("current")


class _SnmpCommunityStringAttribute_Type(Integer32):
    """Custom type snmpCommunityStringAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ro", 1),
          ("rw", 2))
    )


_SnmpCommunityStringAttribute_Type.__name__ = "Integer32"
_SnmpCommunityStringAttribute_Object = MibTableColumn
snmpCommunityStringAttribute = _SnmpCommunityStringAttribute_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 5, 1, 3),
    _SnmpCommunityStringAttribute_Type()
)
snmpCommunityStringAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityStringAttribute.setStatus("current")


class _SnmpCommunityStringStatus_Type(Integer32):
    """Custom type snmpCommunityStringStatus based on Integer32"""
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
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_SnmpCommunityStringStatus_Type.__name__ = "Integer32"
_SnmpCommunityStringStatus_Object = MibTableColumn
snmpCommunityStringStatus = _SnmpCommunityStringStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 5, 1, 4),
    _SnmpCommunityStringStatus_Type()
)
snmpCommunityStringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityStringStatus.setStatus("current")
_SnmpTrapServerTable_Object = MibTable
snmpTrapServerTable = _SnmpTrapServerTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 6)
)
if mibBuilder.loadTexts:
    snmpTrapServerTable.setStatus("current")
_SnmpTrapServerEntry_Object = MibTableRow
snmpTrapServerEntry = _SnmpTrapServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 6, 1)
)
snmpTrapServerEntry.setIndexNames(
    (0, "LES2400RPS", "snmpTrapServerIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapServerEntry.setStatus("current")
_SnmpTrapServerIndex_Type = Integer32
_SnmpTrapServerIndex_Object = MibTableColumn
snmpTrapServerIndex = _SnmpTrapServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 6, 1, 1),
    _SnmpTrapServerIndex_Type()
)
snmpTrapServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTrapServerIndex.setStatus("current")
_SnmpTrapServerIPAddr_Type = IpAddress
_SnmpTrapServerIPAddr_Object = MibTableColumn
snmpTrapServerIPAddr = _SnmpTrapServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 6, 1, 2),
    _SnmpTrapServerIPAddr_Type()
)
snmpTrapServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapServerIPAddr.setStatus("current")


class _SnmpTrapServerTrapComm_Type(DisplayString):
    """Custom type snmpTrapServerTrapComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpTrapServerTrapComm_Type.__name__ = "DisplayString"
_SnmpTrapServerTrapComm_Object = MibTableColumn
snmpTrapServerTrapComm = _SnmpTrapServerTrapComm_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 6, 1, 3),
    _SnmpTrapServerTrapComm_Type()
)
snmpTrapServerTrapComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapServerTrapComm.setStatus("current")


class _SnmpTrapServerTrapVer_Type(Integer32):
    """Custom type snmpTrapServerTrapVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2))
    )


_SnmpTrapServerTrapVer_Type.__name__ = "Integer32"
_SnmpTrapServerTrapVer_Object = MibTableColumn
snmpTrapServerTrapVer = _SnmpTrapServerTrapVer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 6, 1, 4),
    _SnmpTrapServerTrapVer_Type()
)
snmpTrapServerTrapVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapServerTrapVer.setStatus("current")


class _SnmpTrapServerStatus_Type(Integer32):
    """Custom type snmpTrapServerStatus based on Integer32"""
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
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_SnmpTrapServerStatus_Type.__name__ = "Integer32"
_SnmpTrapServerStatus_Object = MibTableColumn
snmpTrapServerStatus = _SnmpTrapServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 6, 1, 5),
    _SnmpTrapServerStatus_Type()
)
snmpTrapServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapServerStatus.setStatus("current")


class _SnmpV3ContextName_Type(DisplayString):
    """Custom type snmpV3ContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpV3ContextName_Type.__name__ = "DisplayString"
_SnmpV3ContextName_Object = MibScalar
snmpV3ContextName = _SnmpV3ContextName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 7),
    _SnmpV3ContextName_Type()
)
snmpV3ContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3ContextName.setStatus("current")
_SnmpV3UsrPrfTable_Object = MibTable
snmpV3UsrPrfTable = _SnmpV3UsrPrfTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 8)
)
if mibBuilder.loadTexts:
    snmpV3UsrPrfTable.setStatus("current")
_SnmpV3UsrPrfEntry_Object = MibTableRow
snmpV3UsrPrfEntry = _SnmpV3UsrPrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 8, 1)
)
snmpV3UsrPrfEntry.setIndexNames(
    (0, "LES2400RPS", "snmpV3UsrPrfIndex"),
)
if mibBuilder.loadTexts:
    snmpV3UsrPrfEntry.setStatus("current")
_SnmpV3UsrPrfIndex_Type = Integer32
_SnmpV3UsrPrfIndex_Object = MibTableColumn
snmpV3UsrPrfIndex = _SnmpV3UsrPrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 8, 1, 1),
    _SnmpV3UsrPrfIndex_Type()
)
snmpV3UsrPrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpV3UsrPrfIndex.setStatus("current")


class _SnmpV3UsrPrfUserID_Type(DisplayString):
    """Custom type snmpV3UsrPrfUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpV3UsrPrfUserID_Type.__name__ = "DisplayString"
_SnmpV3UsrPrfUserID_Object = MibTableColumn
snmpV3UsrPrfUserID = _SnmpV3UsrPrfUserID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 8, 1, 2),
    _SnmpV3UsrPrfUserID_Type()
)
snmpV3UsrPrfUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3UsrPrfUserID.setStatus("current")


class _SnmpV3UsrPrfAuthPw_Type(DisplayString):
    """Custom type snmpV3UsrPrfAuthPw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpV3UsrPrfAuthPw_Type.__name__ = "DisplayString"
_SnmpV3UsrPrfAuthPw_Object = MibTableColumn
snmpV3UsrPrfAuthPw = _SnmpV3UsrPrfAuthPw_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 8, 1, 3),
    _SnmpV3UsrPrfAuthPw_Type()
)
snmpV3UsrPrfAuthPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3UsrPrfAuthPw.setStatus("current")


class _SnmpV3UsrPrfPrivacyPw_Type(DisplayString):
    """Custom type snmpV3UsrPrfPrivacyPw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpV3UsrPrfPrivacyPw_Type.__name__ = "DisplayString"
_SnmpV3UsrPrfPrivacyPw_Object = MibTableColumn
snmpV3UsrPrfPrivacyPw = _SnmpV3UsrPrfPrivacyPw_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 8, 1, 4),
    _SnmpV3UsrPrfPrivacyPw_Type()
)
snmpV3UsrPrfPrivacyPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3UsrPrfPrivacyPw.setStatus("current")


class _SnmpV3UsrPrfOperation_Type(Integer32):
    """Custom type snmpV3UsrPrfOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("remove", 2))
    )


_SnmpV3UsrPrfOperation_Type.__name__ = "Integer32"
_SnmpV3UsrPrfOperation_Object = MibTableColumn
snmpV3UsrPrfOperation = _SnmpV3UsrPrfOperation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 8, 1, 5),
    _SnmpV3UsrPrfOperation_Type()
)
snmpV3UsrPrfOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3UsrPrfOperation.setStatus("current")
_SnmpV3GroupContentTable_Object = MibTable
snmpV3GroupContentTable = _SnmpV3GroupContentTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 9)
)
if mibBuilder.loadTexts:
    snmpV3GroupContentTable.setStatus("current")
_SnmpV3GroupContentEntry_Object = MibTableRow
snmpV3GroupContentEntry = _SnmpV3GroupContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 9, 1)
)
snmpV3GroupContentEntry.setIndexNames(
    (0, "LES2400RPS", "snmpV3GroupContentIndex"),
)
if mibBuilder.loadTexts:
    snmpV3GroupContentEntry.setStatus("current")
_SnmpV3GroupContentIndex_Type = Integer32
_SnmpV3GroupContentIndex_Object = MibTableColumn
snmpV3GroupContentIndex = _SnmpV3GroupContentIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 9, 1, 1),
    _SnmpV3GroupContentIndex_Type()
)
snmpV3GroupContentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpV3GroupContentIndex.setStatus("current")


class _SnmpV3GroupContentSecurityName_Type(DisplayString):
    """Custom type snmpV3GroupContentSecurityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpV3GroupContentSecurityName_Type.__name__ = "DisplayString"
_SnmpV3GroupContentSecurityName_Object = MibTableColumn
snmpV3GroupContentSecurityName = _SnmpV3GroupContentSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 9, 1, 2),
    _SnmpV3GroupContentSecurityName_Type()
)
snmpV3GroupContentSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3GroupContentSecurityName.setStatus("current")


class _SnmpV3GroupContentGroupName_Type(DisplayString):
    """Custom type snmpV3GroupContentGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpV3GroupContentGroupName_Type.__name__ = "DisplayString"
_SnmpV3GroupContentGroupName_Object = MibTableColumn
snmpV3GroupContentGroupName = _SnmpV3GroupContentGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 9, 1, 3),
    _SnmpV3GroupContentGroupName_Type()
)
snmpV3GroupContentGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3GroupContentGroupName.setStatus("current")


class _SnmpV3GroupContentOperation_Type(Integer32):
    """Custom type snmpV3GroupContentOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("remove", 2))
    )


_SnmpV3GroupContentOperation_Type.__name__ = "Integer32"
_SnmpV3GroupContentOperation_Object = MibTableColumn
snmpV3GroupContentOperation = _SnmpV3GroupContentOperation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 9, 1, 4),
    _SnmpV3GroupContentOperation_Type()
)
snmpV3GroupContentOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3GroupContentOperation.setStatus("current")
_SnmpV3AccessTable_Object = MibTable
snmpV3AccessTable = _SnmpV3AccessTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10)
)
if mibBuilder.loadTexts:
    snmpV3AccessTable.setStatus("current")
_SnmpV3AccessEntry_Object = MibTableRow
snmpV3AccessEntry = _SnmpV3AccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1)
)
snmpV3AccessEntry.setIndexNames(
    (0, "LES2400RPS", "snmpV3AccessIndex"),
)
if mibBuilder.loadTexts:
    snmpV3AccessEntry.setStatus("current")
_SnmpV3AccessIndex_Type = Integer32
_SnmpV3AccessIndex_Object = MibTableColumn
snmpV3AccessIndex = _SnmpV3AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 1),
    _SnmpV3AccessIndex_Type()
)
snmpV3AccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpV3AccessIndex.setStatus("current")


class _SnmpV3AccessContextPrefix_Type(DisplayString):
    """Custom type snmpV3AccessContextPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3AccessContextPrefix_Type.__name__ = "DisplayString"
_SnmpV3AccessContextPrefix_Object = MibTableColumn
snmpV3AccessContextPrefix = _SnmpV3AccessContextPrefix_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 2),
    _SnmpV3AccessContextPrefix_Type()
)
snmpV3AccessContextPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3AccessContextPrefix.setStatus("current")


class _SnmpV3AccessGroupName_Type(DisplayString):
    """Custom type snmpV3AccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3AccessGroupName_Type.__name__ = "DisplayString"
_SnmpV3AccessGroupName_Object = MibTableColumn
snmpV3AccessGroupName = _SnmpV3AccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 3),
    _SnmpV3AccessGroupName_Type()
)
snmpV3AccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3AccessGroupName.setStatus("current")


class _SnmpV3AccessSecurityLevel_Type(Integer32):
    """Custom type snmpV3AccessSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_SnmpV3AccessSecurityLevel_Type.__name__ = "Integer32"
_SnmpV3AccessSecurityLevel_Object = MibTableColumn
snmpV3AccessSecurityLevel = _SnmpV3AccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 4),
    _SnmpV3AccessSecurityLevel_Type()
)
snmpV3AccessSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3AccessSecurityLevel.setStatus("current")


class _SnmpV3AccessContextMatchRule_Type(Integer32):
    """Custom type snmpV3AccessContextMatchRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("prefix", 2))
    )


_SnmpV3AccessContextMatchRule_Type.__name__ = "Integer32"
_SnmpV3AccessContextMatchRule_Object = MibTableColumn
snmpV3AccessContextMatchRule = _SnmpV3AccessContextMatchRule_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 5),
    _SnmpV3AccessContextMatchRule_Type()
)
snmpV3AccessContextMatchRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3AccessContextMatchRule.setStatus("current")


class _SnmpV3AccessReadViewName_Type(DisplayString):
    """Custom type snmpV3AccessReadViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3AccessReadViewName_Type.__name__ = "DisplayString"
_SnmpV3AccessReadViewName_Object = MibTableColumn
snmpV3AccessReadViewName = _SnmpV3AccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 6),
    _SnmpV3AccessReadViewName_Type()
)
snmpV3AccessReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3AccessReadViewName.setStatus("current")


class _SnmpV3AccessWriteViewName_Type(DisplayString):
    """Custom type snmpV3AccessWriteViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3AccessWriteViewName_Type.__name__ = "DisplayString"
_SnmpV3AccessWriteViewName_Object = MibTableColumn
snmpV3AccessWriteViewName = _SnmpV3AccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 7),
    _SnmpV3AccessWriteViewName_Type()
)
snmpV3AccessWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3AccessWriteViewName.setStatus("current")


class _SnmpV3AccessNotifyViewName_Type(DisplayString):
    """Custom type snmpV3AccessNotifyViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3AccessNotifyViewName_Type.__name__ = "DisplayString"
_SnmpV3AccessNotifyViewName_Object = MibTableColumn
snmpV3AccessNotifyViewName = _SnmpV3AccessNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 8),
    _SnmpV3AccessNotifyViewName_Type()
)
snmpV3AccessNotifyViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3AccessNotifyViewName.setStatus("current")


class _SnmpV3AccessOperation_Type(Integer32):
    """Custom type snmpV3AccessOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("remove", 2))
    )


_SnmpV3AccessOperation_Type.__name__ = "Integer32"
_SnmpV3AccessOperation_Object = MibTableColumn
snmpV3AccessOperation = _SnmpV3AccessOperation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 10, 1, 9),
    _SnmpV3AccessOperation_Type()
)
snmpV3AccessOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3AccessOperation.setStatus("current")
_SnmpV3MIBViewTable_Object = MibTable
snmpV3MIBViewTable = _SnmpV3MIBViewTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 11)
)
if mibBuilder.loadTexts:
    snmpV3MIBViewTable.setStatus("current")
_SnmpV3MIBViewEntry_Object = MibTableRow
snmpV3MIBViewEntry = _SnmpV3MIBViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 11, 1)
)
snmpV3MIBViewEntry.setIndexNames(
    (0, "LES2400RPS", "snmpV3MIBViewIndex"),
)
if mibBuilder.loadTexts:
    snmpV3MIBViewEntry.setStatus("current")
_SnmpV3MIBViewIndex_Type = Integer32
_SnmpV3MIBViewIndex_Object = MibTableColumn
snmpV3MIBViewIndex = _SnmpV3MIBViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 11, 1, 1),
    _SnmpV3MIBViewIndex_Type()
)
snmpV3MIBViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpV3MIBViewIndex.setStatus("current")


class _SnmpV3MIBViewName_Type(DisplayString):
    """Custom type snmpV3MIBViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3MIBViewName_Type.__name__ = "DisplayString"
_SnmpV3MIBViewName_Object = MibTableColumn
snmpV3MIBViewName = _SnmpV3MIBViewName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 11, 1, 2),
    _SnmpV3MIBViewName_Type()
)
snmpV3MIBViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3MIBViewName.setStatus("current")


class _SnmpV3MIBViewSubOidTree_Type(DisplayString):
    """Custom type snmpV3MIBViewSubOidTree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3MIBViewSubOidTree_Type.__name__ = "DisplayString"
_SnmpV3MIBViewSubOidTree_Object = MibTableColumn
snmpV3MIBViewSubOidTree = _SnmpV3MIBViewSubOidTree_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 11, 1, 3),
    _SnmpV3MIBViewSubOidTree_Type()
)
snmpV3MIBViewSubOidTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3MIBViewSubOidTree.setStatus("current")


class _SnmpV3MIBViewType_Type(Integer32):
    """Custom type snmpV3MIBViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 1),
          ("included", 2))
    )


_SnmpV3MIBViewType_Type.__name__ = "Integer32"
_SnmpV3MIBViewType_Object = MibTableColumn
snmpV3MIBViewType = _SnmpV3MIBViewType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 11, 1, 4),
    _SnmpV3MIBViewType_Type()
)
snmpV3MIBViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3MIBViewType.setStatus("current")


class _SnmpV3MIBViewOperation_Type(Integer32):
    """Custom type snmpV3MIBViewOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("remove", 2))
    )


_SnmpV3MIBViewOperation_Type.__name__ = "Integer32"
_SnmpV3MIBViewOperation_Object = MibTableColumn
snmpV3MIBViewOperation = _SnmpV3MIBViewOperation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 3, 7, 11, 1, 5),
    _SnmpV3MIBViewOperation_Type()
)
snmpV3MIBViewOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3MIBViewOperation.setStatus("current")
_SwitchSecurityMgt_ObjectIdentity = ObjectIdentity
switchSecurityMgt = _SwitchSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4)
)
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1)
)
_RadiusSysCfg_ObjectIdentity = ObjectIdentity
radiusSysCfg = _RadiusSysCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 1)
)


class _Radius8021xProtocolStatus_Type(Integer32):
    """Custom type radius8021xProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Radius8021xProtocolStatus_Type.__name__ = "Integer32"
_Radius8021xProtocolStatus_Object = MibScalar
radius8021xProtocolStatus = _Radius8021xProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 1, 1),
    _Radius8021xProtocolStatus_Type()
)
radius8021xProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radius8021xProtocolStatus.setStatus("current")
_RadiusServerIP_Type = IpAddress
_RadiusServerIP_Object = MibScalar
radiusServerIP = _RadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 1, 2),
    _RadiusServerIP_Type()
)
radiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerIP.setStatus("current")
_RadiusServerPort_Type = Integer32
_RadiusServerPort_Object = MibScalar
radiusServerPort = _RadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 1, 3),
    _RadiusServerPort_Type()
)
radiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerPort.setStatus("current")
_RadiusAccountingPort_Type = Integer32
_RadiusAccountingPort_Object = MibScalar
radiusAccountingPort = _RadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 1, 4),
    _RadiusAccountingPort_Type()
)
radiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountingPort.setStatus("current")


class _RadiusSharedKey_Type(DisplayString):
    """Custom type radiusSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RadiusSharedKey_Type.__name__ = "DisplayString"
_RadiusSharedKey_Object = MibScalar
radiusSharedKey = _RadiusSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 1, 5),
    _RadiusSharedKey_Type()
)
radiusSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSharedKey.setStatus("current")


class _RadiusNASIdentifier_Type(DisplayString):
    """Custom type radiusNASIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RadiusNASIdentifier_Type.__name__ = "DisplayString"
_RadiusNASIdentifier_Object = MibScalar
radiusNASIdentifier = _RadiusNASIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 1, 6),
    _RadiusNASIdentifier_Type()
)
radiusNASIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusNASIdentifier.setStatus("current")
_RadiusPerPortCfgTable_Object = MibTable
radiusPerPortCfgTable = _RadiusPerPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 2)
)
if mibBuilder.loadTexts:
    radiusPerPortCfgTable.setStatus("current")
_RadiusPerPortCfgEntry_Object = MibTableRow
radiusPerPortCfgEntry = _RadiusPerPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 2, 1)
)
radiusPerPortCfgEntry.setIndexNames(
    (0, "LES2400RPS", "radiusPerPortCfgIndex"),
)
if mibBuilder.loadTexts:
    radiusPerPortCfgEntry.setStatus("current")
_RadiusPerPortCfgIndex_Type = Integer32
_RadiusPerPortCfgIndex_Object = MibTableColumn
radiusPerPortCfgIndex = _RadiusPerPortCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 2, 1, 1),
    _RadiusPerPortCfgIndex_Type()
)
radiusPerPortCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusPerPortCfgIndex.setStatus("current")


class _RadiusPerPortCfgPortName_Type(DisplayString):
    """Custom type radiusPerPortCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RadiusPerPortCfgPortName_Type.__name__ = "DisplayString"
_RadiusPerPortCfgPortName_Object = MibTableColumn
radiusPerPortCfgPortName = _RadiusPerPortCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 2, 1, 2),
    _RadiusPerPortCfgPortName_Type()
)
radiusPerPortCfgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusPerPortCfgPortName.setStatus("current")


class _RadiusPerPortCfgState_Type(Integer32):
    """Custom type radiusPerPortCfgState based on Integer32"""
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
        *(("reject", 1),
          ("accept", 2),
          ("authorize", 3),
          ("disabled", 4))
    )


_RadiusPerPortCfgState_Type.__name__ = "Integer32"
_RadiusPerPortCfgState_Object = MibTableColumn
radiusPerPortCfgState = _RadiusPerPortCfgState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 2, 1, 3),
    _RadiusPerPortCfgState_Type()
)
radiusPerPortCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPerPortCfgState.setStatus("current")
_RadiusMiscCfg_ObjectIdentity = ObjectIdentity
radiusMiscCfg = _RadiusMiscCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 3)
)
_RadiusMiscQuietPeriod_Type = Integer32
_RadiusMiscQuietPeriod_Object = MibScalar
radiusMiscQuietPeriod = _RadiusMiscQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 3, 1),
    _RadiusMiscQuietPeriod_Type()
)
radiusMiscQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscQuietPeriod.setStatus("current")
_RadiusMiscTxPeriod_Type = Integer32
_RadiusMiscTxPeriod_Object = MibScalar
radiusMiscTxPeriod = _RadiusMiscTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 3, 2),
    _RadiusMiscTxPeriod_Type()
)
radiusMiscTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscTxPeriod.setStatus("current")
_RadiusMiscSupplicantTimeout_Type = Integer32
_RadiusMiscSupplicantTimeout_Object = MibScalar
radiusMiscSupplicantTimeout = _RadiusMiscSupplicantTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 3, 3),
    _RadiusMiscSupplicantTimeout_Type()
)
radiusMiscSupplicantTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscSupplicantTimeout.setStatus("current")
_RadiusMiscServerTimeout_Type = Integer32
_RadiusMiscServerTimeout_Object = MibScalar
radiusMiscServerTimeout = _RadiusMiscServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 3, 4),
    _RadiusMiscServerTimeout_Type()
)
radiusMiscServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscServerTimeout.setStatus("current")
_RadiusMiscReAuthMax_Type = Integer32
_RadiusMiscReAuthMax_Object = MibScalar
radiusMiscReAuthMax = _RadiusMiscReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 3, 5),
    _RadiusMiscReAuthMax_Type()
)
radiusMiscReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscReAuthMax.setStatus("current")
_RadiusMiscReauthPeriod_Type = Integer32
_RadiusMiscReauthPeriod_Object = MibScalar
radiusMiscReauthPeriod = _RadiusMiscReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 1, 3, 6),
    _RadiusMiscReauthPeriod_Type()
)
radiusMiscReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscReauthPeriod.setStatus("current")
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2)
)
_PortSecurityStaticMACTable_Object = MibTable
portSecurityStaticMACTable = _PortSecurityStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 1)
)
if mibBuilder.loadTexts:
    portSecurityStaticMACTable.setStatus("current")
_PortSecurityStaticMACEntry_Object = MibTableRow
portSecurityStaticMACEntry = _PortSecurityStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 1, 1)
)
portSecurityStaticMACEntry.setIndexNames(
    (0, "LES2400RPS", "portSecurityStaticMACIndex"),
)
if mibBuilder.loadTexts:
    portSecurityStaticMACEntry.setStatus("current")
_PortSecurityStaticMACIndex_Type = Integer32
_PortSecurityStaticMACIndex_Object = MibTableColumn
portSecurityStaticMACIndex = _PortSecurityStaticMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 1, 1, 1),
    _PortSecurityStaticMACIndex_Type()
)
portSecurityStaticMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecurityStaticMACIndex.setStatus("current")


class _PortSecurityStaticMACPortName_Type(DisplayString):
    """Custom type portSecurityStaticMACPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PortSecurityStaticMACPortName_Type.__name__ = "DisplayString"
_PortSecurityStaticMACPortName_Object = MibTableColumn
portSecurityStaticMACPortName = _PortSecurityStaticMACPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 1, 1, 2),
    _PortSecurityStaticMACPortName_Type()
)
portSecurityStaticMACPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityStaticMACPortName.setStatus("current")
_PortSecurityStaticMACAddr_Type = MacAddress
_PortSecurityStaticMACAddr_Object = MibTableColumn
portSecurityStaticMACAddr = _PortSecurityStaticMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 1, 1, 3),
    _PortSecurityStaticMACAddr_Type()
)
portSecurityStaticMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityStaticMACAddr.setStatus("current")
_PortSecurityStaticMACVid_Type = Integer32
_PortSecurityStaticMACVid_Object = MibTableColumn
portSecurityStaticMACVid = _PortSecurityStaticMACVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 1, 1, 4),
    _PortSecurityStaticMACVid_Type()
)
portSecurityStaticMACVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityStaticMACVid.setStatus("current")


class _PortSecurityStaticMACStatus_Type(Integer32):
    """Custom type portSecurityStaticMACStatus based on Integer32"""
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
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_PortSecurityStaticMACStatus_Type.__name__ = "Integer32"
_PortSecurityStaticMACStatus_Object = MibTableColumn
portSecurityStaticMACStatus = _PortSecurityStaticMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 1, 1, 5),
    _PortSecurityStaticMACStatus_Type()
)
portSecurityStaticMACStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityStaticMACStatus.setStatus("current")
_PortSecurityMACFilteringTable_Object = MibTable
portSecurityMACFilteringTable = _PortSecurityMACFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 2)
)
if mibBuilder.loadTexts:
    portSecurityMACFilteringTable.setStatus("current")
_PortSecurityMACFilteringEntry_Object = MibTableRow
portSecurityMACFilteringEntry = _PortSecurityMACFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 2, 1)
)
portSecurityMACFilteringEntry.setIndexNames(
    (0, "LES2400RPS", "portSecurityMACFilteringIndex"),
)
if mibBuilder.loadTexts:
    portSecurityMACFilteringEntry.setStatus("current")
_PortSecurityMACFilteringIndex_Type = Integer32
_PortSecurityMACFilteringIndex_Object = MibTableColumn
portSecurityMACFilteringIndex = _PortSecurityMACFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 2, 1, 1),
    _PortSecurityMACFilteringIndex_Type()
)
portSecurityMACFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecurityMACFilteringIndex.setStatus("current")
_PortSecurityMACFilteringAddr_Type = MacAddress
_PortSecurityMACFilteringAddr_Object = MibTableColumn
portSecurityMACFilteringAddr = _PortSecurityMACFilteringAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 2, 1, 2),
    _PortSecurityMACFilteringAddr_Type()
)
portSecurityMACFilteringAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMACFilteringAddr.setStatus("current")
_PortSecurityMACFilteringVid_Type = Integer32
_PortSecurityMACFilteringVid_Object = MibTableColumn
portSecurityMACFilteringVid = _PortSecurityMACFilteringVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 2, 1, 3),
    _PortSecurityMACFilteringVid_Type()
)
portSecurityMACFilteringVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMACFilteringVid.setStatus("current")


class _PortSecurityMACFilteringStatus_Type(Integer32):
    """Custom type portSecurityMACFilteringStatus based on Integer32"""
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
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_PortSecurityMACFilteringStatus_Type.__name__ = "Integer32"
_PortSecurityMACFilteringStatus_Object = MibTableColumn
portSecurityMACFilteringStatus = _PortSecurityMACFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 2, 1, 4),
    _PortSecurityMACFilteringStatus_Type()
)
portSecurityMACFilteringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityMACFilteringStatus.setStatus("current")
_PortSecurityMulticastFilterTable_Object = MibTable
portSecurityMulticastFilterTable = _PortSecurityMulticastFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 3)
)
if mibBuilder.loadTexts:
    portSecurityMulticastFilterTable.setStatus("current")
_PortSecurityMulticastFilterEntry_Object = MibTableRow
portSecurityMulticastFilterEntry = _PortSecurityMulticastFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 3, 1)
)
portSecurityMulticastFilterEntry.setIndexNames(
    (0, "LES2400RPS", "portSecurityMulticastFilterIndex"),
)
if mibBuilder.loadTexts:
    portSecurityMulticastFilterEntry.setStatus("current")
_PortSecurityMulticastFilterIndex_Type = Integer32
_PortSecurityMulticastFilterIndex_Object = MibTableColumn
portSecurityMulticastFilterIndex = _PortSecurityMulticastFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 3, 1, 1),
    _PortSecurityMulticastFilterIndex_Type()
)
portSecurityMulticastFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecurityMulticastFilterIndex.setStatus("current")
_PortSecurityMulticastFilterAddr_Type = IpAddress
_PortSecurityMulticastFilterAddr_Object = MibTableColumn
portSecurityMulticastFilterAddr = _PortSecurityMulticastFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 3, 1, 2),
    _PortSecurityMulticastFilterAddr_Type()
)
portSecurityMulticastFilterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMulticastFilterAddr.setStatus("current")
_PortSecurityMulticastFilterVid_Type = Integer32
_PortSecurityMulticastFilterVid_Object = MibTableColumn
portSecurityMulticastFilterVid = _PortSecurityMulticastFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 3, 1, 3),
    _PortSecurityMulticastFilterVid_Type()
)
portSecurityMulticastFilterVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMulticastFilterVid.setStatus("current")
_PortSecurityMulticastFilterMembers_Type = PortList
_PortSecurityMulticastFilterMembers_Object = MibTableColumn
portSecurityMulticastFilterMembers = _PortSecurityMulticastFilterMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 3, 1, 4),
    _PortSecurityMulticastFilterMembers_Type()
)
portSecurityMulticastFilterMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityMulticastFilterMembers.setStatus("current")


class _PortSecurityMulticastFilterStatus_Type(Integer32):
    """Custom type portSecurityMulticastFilterStatus based on Integer32"""
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
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_PortSecurityMulticastFilterStatus_Type.__name__ = "Integer32"
_PortSecurityMulticastFilterStatus_Object = MibTableColumn
portSecurityMulticastFilterStatus = _PortSecurityMulticastFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 3, 1, 5),
    _PortSecurityMulticastFilterStatus_Type()
)
portSecurityMulticastFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityMulticastFilterStatus.setStatus("current")
_PortSecurityAllMACTable_Object = MibTable
portSecurityAllMACTable = _PortSecurityAllMACTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 4)
)
if mibBuilder.loadTexts:
    portSecurityAllMACTable.setStatus("current")
_PortSecurityAllMACEntry_Object = MibTableRow
portSecurityAllMACEntry = _PortSecurityAllMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 4, 1)
)
portSecurityAllMACEntry.setIndexNames(
    (0, "LES2400RPS", "portSecurityAllMACIndex"),
)
if mibBuilder.loadTexts:
    portSecurityAllMACEntry.setStatus("current")
_PortSecurityAllMACIndex_Type = Integer32
_PortSecurityAllMACIndex_Object = MibTableColumn
portSecurityAllMACIndex = _PortSecurityAllMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 4, 1, 1),
    _PortSecurityAllMACIndex_Type()
)
portSecurityAllMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityAllMACIndex.setStatus("current")


class _PortSecurityAllMACPortName_Type(DisplayString):
    """Custom type portSecurityAllMACPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PortSecurityAllMACPortName_Type.__name__ = "DisplayString"
_PortSecurityAllMACPortName_Object = MibTableColumn
portSecurityAllMACPortName = _PortSecurityAllMACPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 4, 1, 2),
    _PortSecurityAllMACPortName_Type()
)
portSecurityAllMACPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityAllMACPortName.setStatus("current")
_PortSecurityAllMACAddr_Type = MacAddress
_PortSecurityAllMACAddr_Object = MibTableColumn
portSecurityAllMACAddr = _PortSecurityAllMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 4, 1, 3),
    _PortSecurityAllMACAddr_Type()
)
portSecurityAllMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityAllMACAddr.setStatus("current")
_PortSecurityAllMACVid_Type = Integer32
_PortSecurityAllMACVid_Object = MibTableColumn
portSecurityAllMACVid = _PortSecurityAllMACVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 4, 1, 4),
    _PortSecurityAllMACVid_Type()
)
portSecurityAllMACVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityAllMACVid.setStatus("current")


class _PortSecurityAllMACType_Type(Integer32):
    """Custom type portSecurityAllMACType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_PortSecurityAllMACType_Type.__name__ = "Integer32"
_PortSecurityAllMACType_Object = MibTableColumn
portSecurityAllMACType = _PortSecurityAllMACType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 4, 1, 5),
    _PortSecurityAllMACType_Type()
)
portSecurityAllMACType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityAllMACType.setStatus("current")


class _PortSecurityClearMACTable_Type(Integer32):
    """Custom type portSecurityClearMACTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_PortSecurityClearMACTable_Type.__name__ = "Integer32"
_PortSecurityClearMACTable_Object = MibScalar
portSecurityClearMACTable = _PortSecurityClearMACTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 2, 5),
    _PortSecurityClearMACTable_Type()
)
portSecurityClearMACTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityClearMACTable.setStatus("current")
_AclMgt_ObjectIdentity = ObjectIdentity
aclMgt = _AclMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3)
)
_AclTable_Object = MibTable
aclTable = _AclTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1)
)
if mibBuilder.loadTexts:
    aclTable.setStatus("current")
_AclEntry_Object = MibTableRow
aclEntry = _AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1)
)
aclEntry.setIndexNames(
    (0, "LES2400RPS", "aclIndex"),
)
if mibBuilder.loadTexts:
    aclEntry.setStatus("current")
_AclIndex_Type = Integer32
_AclIndex_Object = MibTableColumn
aclIndex = _AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 1),
    _AclIndex_Type()
)
aclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIndex.setStatus("current")


class _AclGroupID_Type(Integer32):
    """Custom type aclGroupID based on Integer32"""
    defaultValue = 1


_AclGroupID_Type.__name__ = "Integer32"
_AclGroupID_Object = MibTableColumn
aclGroupID = _AclGroupID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 2),
    _AclGroupID_Type()
)
aclGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclGroupID.setStatus("current")


class _AclAction_Type(Integer32):
    """Custom type aclAction based on Integer32"""
    defaultValue = 1

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


_AclAction_Type.__name__ = "Integer32"
_AclAction_Object = MibTableColumn
aclAction = _AclAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 3),
    _AclAction_Type()
)
aclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAction.setStatus("current")
_AclVlanID_Type = Integer32
_AclVlanID_Object = MibTableColumn
aclVlanID = _AclVlanID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 4),
    _AclVlanID_Type()
)
aclVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclVlanID.setStatus("current")


class _AclPacketType_Type(Integer32):
    """Custom type aclPacketType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("non-ipv4", 2))
    )


_AclPacketType_Type.__name__ = "Integer32"
_AclPacketType_Object = MibTableColumn
aclPacketType = _AclPacketType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 5),
    _AclPacketType_Type()
)
aclPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPacketType.setStatus("current")


class _AclSrcIPAddress_Type(IpAddress):
    """Custom type aclSrcIPAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AclSrcIPAddress_Type.__name__ = "IpAddress"
_AclSrcIPAddress_Object = MibTableColumn
aclSrcIPAddress = _AclSrcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 6),
    _AclSrcIPAddress_Type()
)
aclSrcIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclSrcIPAddress.setStatus("current")


class _AclSrcMask_Type(IpAddress):
    """Custom type aclSrcMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AclSrcMask_Type.__name__ = "IpAddress"
_AclSrcMask_Object = MibTableColumn
aclSrcMask = _AclSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 7),
    _AclSrcMask_Type()
)
aclSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclSrcMask.setStatus("current")


class _AclDstIPAddress_Type(IpAddress):
    """Custom type aclDstIPAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AclDstIPAddress_Type.__name__ = "IpAddress"
_AclDstIPAddress_Object = MibTableColumn
aclDstIPAddress = _AclDstIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 8),
    _AclDstIPAddress_Type()
)
aclDstIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclDstIPAddress.setStatus("current")


class _AclDstMask_Type(IpAddress):
    """Custom type aclDstMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AclDstMask_Type.__name__ = "IpAddress"
_AclDstMask_Object = MibTableColumn
aclDstMask = _AclDstMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 9),
    _AclDstMask_Type()
)
aclDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclDstMask.setStatus("current")


class _AclIPFragment_Type(Integer32):
    """Custom type aclIPFragment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uncheck", 1),
          ("check", 2))
    )


_AclIPFragment_Type.__name__ = "Integer32"
_AclIPFragment_Object = MibTableColumn
aclIPFragment = _AclIPFragment_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 10),
    _AclIPFragment_Type()
)
aclIPFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclIPFragment.setStatus("current")


class _AclL4ProtocolType_Type(Integer32):
    """Custom type aclL4ProtocolType based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("icmp", 2),
          ("igmp", 3),
          ("tcp", 4),
          ("tcp-ftp", 5),
          ("tcp-http", 6),
          ("udp", 7),
          ("udp-tftp", 8))
    )


_AclL4ProtocolType_Type.__name__ = "Integer32"
_AclL4ProtocolType_Object = MibTableColumn
aclL4ProtocolType = _AclL4ProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 11),
    _AclL4ProtocolType_Type()
)
aclL4ProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL4ProtocolType.setStatus("current")
_AclL4ProtocolValue_Type = Integer32
_AclL4ProtocolValue_Object = MibTableColumn
aclL4ProtocolValue = _AclL4ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 12),
    _AclL4ProtocolValue_Type()
)
aclL4ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL4ProtocolValue.setStatus("current")


class _AclEtherType_Type(Integer32):
    """Custom type aclEtherType based on Integer32"""
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
        *(("any", 1),
          ("arp", 2),
          ("ipx", 3))
    )


_AclEtherType_Type.__name__ = "Integer32"
_AclEtherType_Object = MibTableColumn
aclEtherType = _AclEtherType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 13),
    _AclEtherType_Type()
)
aclEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEtherType.setStatus("current")


class _AclEtherValue_Type(DisplayString):
    """Custom type aclEtherValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AclEtherValue_Type.__name__ = "DisplayString"
_AclEtherValue_Object = MibTableColumn
aclEtherValue = _AclEtherValue_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 14),
    _AclEtherValue_Type()
)
aclEtherValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEtherValue.setStatus("current")


class _AclStatus_Type(Integer32):
    """Custom type aclStatus based on Integer32"""
    defaultValue = 3

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
        *(("valid", 1),
          ("createrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_AclStatus_Type.__name__ = "Integer32"
_AclStatus_Object = MibTableColumn
aclStatus = _AclStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 4, 3, 1, 1, 15),
    _AclStatus_Type()
)
aclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclStatus.setStatus("current")
_TftpDownloadMgt_ObjectIdentity = ObjectIdentity
tftpDownloadMgt = _TftpDownloadMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 5)
)


class _TftpDownloadServerIP_Type(IpAddress):
    """Custom type tftpDownloadServerIP based on IpAddress"""
    defaultHexValue = "00000000"


_TftpDownloadServerIP_Type.__name__ = "IpAddress"
_TftpDownloadServerIP_Object = MibScalar
tftpDownloadServerIP = _TftpDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 5, 1),
    _TftpDownloadServerIP_Type()
)
tftpDownloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadServerIP.setStatus("current")


class _TftpDownloadAgentBoardFwFileName_Type(DisplayString):
    """Custom type tftpDownloadAgentBoardFwFileName based on DisplayString"""
    defaultValue = OctetString("image.bin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TftpDownloadAgentBoardFwFileName_Type.__name__ = "DisplayString"
_TftpDownloadAgentBoardFwFileName_Object = MibScalar
tftpDownloadAgentBoardFwFileName = _TftpDownloadAgentBoardFwFileName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 5, 2),
    _TftpDownloadAgentBoardFwFileName_Type()
)
tftpDownloadAgentBoardFwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadAgentBoardFwFileName.setStatus("current")


class _TftpDownloadAgentBoardFwDownloadFunction_Type(Integer32):
    """Custom type tftpDownloadAgentBoardFwDownloadFunction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupConfiguration", 1),
          ("restoreConfiguration", 2),
          ("updateFirmware", 3))
    )


_TftpDownloadAgentBoardFwDownloadFunction_Type.__name__ = "Integer32"
_TftpDownloadAgentBoardFwDownloadFunction_Object = MibScalar
tftpDownloadAgentBoardFwDownloadFunction = _TftpDownloadAgentBoardFwDownloadFunction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 5, 3),
    _TftpDownloadAgentBoardFwDownloadFunction_Type()
)
tftpDownloadAgentBoardFwDownloadFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadAgentBoardFwDownloadFunction.setStatus("current")


class _TftpDownloadStatus_Type(Integer32):
    """Custom type tftpDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_TftpDownloadStatus_Type.__name__ = "Integer32"
_TftpDownloadStatus_Object = MibScalar
tftpDownloadStatus = _TftpDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 5, 4),
    _TftpDownloadStatus_Type()
)
tftpDownloadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadStatus.setStatus("current")
_LoadFactoryDefaultMgt_ObjectIdentity = ObjectIdentity
loadFactoryDefaultMgt = _LoadFactoryDefaultMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 6)
)


class _KeepCurrentIPSetting_Type(Integer32):
    """Custom type keepCurrentIPSetting based on Integer32"""
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


_KeepCurrentIPSetting_Type.__name__ = "Integer32"
_KeepCurrentIPSetting_Object = MibScalar
keepCurrentIPSetting = _KeepCurrentIPSetting_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 6, 1),
    _KeepCurrentIPSetting_Type()
)
keepCurrentIPSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keepCurrentIPSetting.setStatus("current")


class _KeepCurrentUsernamePassword_Type(Integer32):
    """Custom type keepCurrentUsernamePassword based on Integer32"""
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


_KeepCurrentUsernamePassword_Type.__name__ = "Integer32"
_KeepCurrentUsernamePassword_Object = MibScalar
keepCurrentUsernamePassword = _KeepCurrentUsernamePassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 6, 2),
    _KeepCurrentUsernamePassword_Type()
)
keepCurrentUsernamePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keepCurrentUsernamePassword.setStatus("current")


class _LoadFactoryDefaultAction_Type(Integer32):
    """Custom type loadFactoryDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_LoadFactoryDefaultAction_Type.__name__ = "Integer32"
_LoadFactoryDefaultAction_Object = MibScalar
loadFactoryDefaultAction = _LoadFactoryDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 6, 3),
    _LoadFactoryDefaultAction_Type()
)
loadFactoryDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFactoryDefaultAction.setStatus("current")
_SaveCfgMgt_ObjectIdentity = ObjectIdentity
saveCfgMgt = _SaveCfgMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 7)
)


class _SaveCfgMgtAction_Type(Integer32):
    """Custom type saveCfgMgtAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_SaveCfgMgtAction_Type.__name__ = "Integer32"
_SaveCfgMgtAction_Object = MibScalar
saveCfgMgtAction = _SaveCfgMgtAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 7, 1),
    _SaveCfgMgtAction_Type()
)
saveCfgMgtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveCfgMgtAction.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 8)
)


class _RestartAction_Type(Integer32):
    """Custom type restartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_RestartAction_Type.__name__ = "Integer32"
_RestartAction_Object = MibScalar
restartAction = _RestartAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 8, 1),
    _RestartAction_Type()
)
restartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartAction.setStatus("current")
_TrapSpecificMgt_ObjectIdentity = ObjectIdentity
trapSpecificMgt = _TrapSpecificMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 11)
)


class _SpecificTrapTopologychange_Type(Integer32):
    """Custom type specificTrapTopologychange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("alarm", 1)
    )


_SpecificTrapTopologychange_Type.__name__ = "Integer32"
_SpecificTrapTopologychange_Object = MibScalar
specificTrapTopologychange = _SpecificTrapTopologychange_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 11, 1),
    _SpecificTrapTopologychange_Type()
)
specificTrapTopologychange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificTrapTopologychange.setStatus("current")


class _SpecificTrapFanfailure_Type(Integer32):
    """Custom type specificTrapFanfailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fan1_failure", 1),
          ("fan2_failure", 2),
          ("fan1_and_fan2_failure", 3))
    )


_SpecificTrapFanfailure_Type.__name__ = "Integer32"
_SpecificTrapFanfailure_Object = MibScalar
specificTrapFanfailure = _SpecificTrapFanfailure_Object(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 11, 4),
    _SpecificTrapFanfailure_Type()
)
specificTrapFanfailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificTrapFanfailure.setStatus("current")

# Managed Objects groups


# Notification objects

fanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 0, 1)
)
fanFailureTrap.setObjects(
    ("LES2400RPS", "specificTrapFanfailure")
)
if mibBuilder.loadTexts:
    fanFailureTrap.setStatus(
        ""
    )

topologyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 37072, 303, 1, 66, 0, 11)
)
topologyChangeTrap.setObjects(
    ("LES2400RPS", "specificTrapTopologychange")
)
if mibBuilder.loadTexts:
    topologyChangeTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LES2400RPS",
    **{"DisplayString": DisplayString,
       "MacAddress": MacAddress,
       "PortList": PortList,
       "private": private,
       "enterprises": enterprises,
       "lantech": lantech,
       "products": products,
       "l2switch": l2switch,
       "les2400rps": les2400rps,
       "contact": contact,
       "fanFailureTrap": fanFailureTrap,
       "topologyChangeTrap": topologyChangeTrap,
       "systemMgt": systemMgt,
       "switchInfo": switchInfo,
       "switchInfoTable": switchInfoTable,
       "switchInfoEntry": switchInfoEntry,
       "swUnitIndex": swUnitIndex,
       "swsysName": swsysName,
       "swsysDescr": swsysDescr,
       "swsysLocation": swsysLocation,
       "swsysContact": swsysContact,
       "swFwVer": swFwVer,
       "swKerVer": swKerVer,
       "swMacAddress": swMacAddress,
       "swSerialNum": swSerialNum,
       "switchCurrentPortNameListTable": switchCurrentPortNameListTable,
       "switchCurrentPortNameListEntry": switchCurrentPortNameListEntry,
       "swCurrentPortNameListIndex": swCurrentPortNameListIndex,
       "swCurrentPortNameListPortName": swCurrentPortNameListPortName,
       "swCurrentPortNameListPortNumber": swCurrentPortNameListPortNumber,
       "switchIpCfg": switchIpCfg,
       "switchIpCfgTable": switchIpCfgTable,
       "switchIpCfgEntry": switchIpCfgEntry,
       "swIpCfgIndex": swIpCfgIndex,
       "swIpCfgDHCPStatus": swIpCfgDHCPStatus,
       "swIpCfgAddress": swIpCfgAddress,
       "swIpCfgSubMask": swIpCfgSubMask,
       "swIpCfgGateway": swIpCfgGateway,
       "swIpCfgDNS1": swIpCfgDNS1,
       "swIpCfgDNS2": swIpCfgDNS2,
       "switchDHCPServerMgt": switchDHCPServerMgt,
       "switchDHCPServerCfgTable": switchDHCPServerCfgTable,
       "switchDHCPServerCfgEntry": switchDHCPServerCfgEntry,
       "swDHCPServerCfgIndex": swDHCPServerCfgIndex,
       "swDHCPServerCfgStatus": swDHCPServerCfgStatus,
       "swDHCPServerCfgLowIPAddr": swDHCPServerCfgLowIPAddr,
       "swDHCPServerCfgHighIPAddr": swDHCPServerCfgHighIPAddr,
       "swDHCPServerCfgSubMask": swDHCPServerCfgSubMask,
       "swDHCPServerCfgGateway": swDHCPServerCfgGateway,
       "swDHCPServerCfgDNS": swDHCPServerCfgDNS,
       "swDHCPServerCfgLeaseTime": swDHCPServerCfgLeaseTime,
       "switchDHCPServerClientInfoTable": switchDHCPServerClientInfoTable,
       "switchDHCPServerClientInfoEntry": switchDHCPServerClientInfoEntry,
       "swDHCPServerClientInfoIndex": swDHCPServerClientInfoIndex,
       "swDHCPServerClientInfoIPAddr": swDHCPServerClientInfoIPAddr,
       "swDHCPServerClientInfoID": swDHCPServerClientInfoID,
       "swDHCPServerClientInfoType": swDHCPServerClientInfoType,
       "swDHCPServerClientInfoStatus": swDHCPServerClientInfoStatus,
       "swDHCPServerClientInfoLease": swDHCPServerClientInfoLease,
       "switchDHCPServerIPBindingTable": switchDHCPServerIPBindingTable,
       "switchDHCPServerIPBindingEntry": switchDHCPServerIPBindingEntry,
       "swDHCPServerIPBindingPortNum": swDHCPServerIPBindingPortNum,
       "swDHCPServerIPBindingAddr": swDHCPServerIPBindingAddr,
       "swDHCPServerIPBindingPortName": swDHCPServerIPBindingPortName,
       "switchSyslogMgt": switchSyslogMgt,
       "switchSyslogCfg": switchSyslogCfg,
       "swSyslogStatus": swSyslogStatus,
       "swSyslogServerAddr": swSyslogServerAddr,
       "switchSyslogLogTable": switchSyslogLogTable,
       "switchSyslogLogEntry": switchSyslogLogEntry,
       "swSyslogLogIndex": swSyslogLogIndex,
       "swSyslogLogDescription": swSyslogLogDescription,
       "swSyslogClearLogTable": swSyslogClearLogTable,
       "switchSyslogSmtpCfg": switchSyslogSmtpCfg,
       "swSyslogEmailAlertStatus": swSyslogEmailAlertStatus,
       "swSyslogEmailAlertAddr": swSyslogEmailAlertAddr,
       "swSyslogEmailAlertSubject": swSyslogEmailAlertSubject,
       "swSyslogEmailAlertSender": swSyslogEmailAlertSender,
       "swSyslogEmailAlertAuthentication": swSyslogEmailAlertAuthentication,
       "swSyslogEmailAlertAccount": swSyslogEmailAlertAccount,
       "swSyslogEmailAlertPassword": swSyslogEmailAlertPassword,
       "switchSyslogEmailAlertRcptTable": switchSyslogEmailAlertRcptTable,
       "switchSyslogEmailAlertRcptEntry": switchSyslogEmailAlertRcptEntry,
       "swSyslogEmailAlertRcptIndex": swSyslogEmailAlertRcptIndex,
       "swSyslogEmailAlertRcptEmailAddr": swSyslogEmailAlertRcptEmailAddr,
       "switchSyslogEventCfg": switchSyslogEventCfg,
       "switchSyslogSystemEventsTable": switchSyslogSystemEventsTable,
       "switchSyslogSystemEventsEntry": switchSyslogSystemEventsEntry,
       "swSyslogSystemEventsIndex": swSyslogSystemEventsIndex,
       "swSyslogDeviceColdStartEvent": swSyslogDeviceColdStartEvent,
       "swSyslogDeviceWarmStartEvent": swSyslogDeviceWarmStartEvent,
       "swSyslogAuthenticationFailureEvent": swSyslogAuthenticationFailureEvent,
       "swSyslogFanFailureEvent": swSyslogFanFailureEvent,
       "switchSyslogPortEventsTable": switchSyslogPortEventsTable,
       "switchSyslogPortEventsEntry": switchSyslogPortEventsEntry,
       "swSyslogPortNumber": swSyslogPortNumber,
       "swSyslogPortEventLog": swSyslogPortEventLog,
       "swSyslogPortEventSMTP": swSyslogPortEventSMTP,
       "swSyslogPortName": swSyslogPortName,
       "sntpMgt": sntpMgt,
       "sntpClientStatus": sntpClientStatus,
       "sntpDaylightSavingTime": sntpDaylightSavingTime,
       "sntpUTCTimezone": sntpUTCTimezone,
       "sntpServerIP": sntpServerIP,
       "sntpSwitchTimer": sntpSwitchTimer,
       "sntpDaylightSavingPeriodStart": sntpDaylightSavingPeriodStart,
       "sntpDaylightSavingPeriodEnd": sntpDaylightSavingPeriodEnd,
       "sntpDaylightSavingOffset": sntpDaylightSavingOffset,
       "ipSecurityMgt": ipSecurityMgt,
       "ipSecurityStatus": ipSecurityStatus,
       "ipSecurityHTTPServerStatus": ipSecurityHTTPServerStatus,
       "ipSecurityTelnetServerStatus": ipSecurityTelnetServerStatus,
       "ipSecuritySecurityIP1": ipSecuritySecurityIP1,
       "ipSecuritySecurityIP2": ipSecuritySecurityIP2,
       "ipSecuritySecurityIP3": ipSecuritySecurityIP3,
       "ipSecuritySecurityIP4": ipSecuritySecurityIP4,
       "ipSecuritySecurityIP5": ipSecuritySecurityIP5,
       "ipSecuritySecurityIP6": ipSecuritySecurityIP6,
       "ipSecuritySecurityIP7": ipSecuritySecurityIP7,
       "ipSecuritySecurityIP8": ipSecuritySecurityIP8,
       "ipSecuritySecurityIP9": ipSecuritySecurityIP9,
       "ipSecuritySecurityIP10": ipSecuritySecurityIP10,
       "switchUserAuth": switchUserAuth,
       "swUserAuthID": swUserAuthID,
       "swUserAuthPassword": swUserAuthPassword,
       "switchAdvanceCfg": switchAdvanceCfg,
       "swBSFCfg": swBSFCfg,
       "swBSFFloodedUnicastMulticastPackets": swBSFFloodedUnicastMulticastPackets,
       "swBSFControlPackets": swBSFControlPackets,
       "swBSFIPMulticastPackets": swBSFIPMulticastPackets,
       "swBSFBroadcastPackets": swBSFBroadcastPackets,
       "swBSFRate": swBSFRate,
       "swAgeTime": swAgeTime,
       "swAutoFlush": swAutoFlush,
       "swJumboFrame": swJumboFrame,
       "switchPortMgt": switchPortMgt,
       "switchPortStatMgt": switchPortStatMgt,
       "switchPortStatTable": switchPortStatTable,
       "switchPortStatEntry": switchPortStatEntry,
       "swPortStatIndex": swPortStatIndex,
       "swPortStatType": swPortStatType,
       "swPortStatLink": swPortStatLink,
       "swPortStatState": swPortStatState,
       "swPortStatTXGoodPkt": swPortStatTXGoodPkt,
       "swPortStatTXBadPkt": swPortStatTXBadPkt,
       "swPortStatRXGoodPkt": swPortStatRXGoodPkt,
       "swPortStatRXBadPkt": swPortStatRXBadPkt,
       "swPortStatTXAbortPkt": swPortStatTXAbortPkt,
       "swPortStatPacketCollision": swPortStatPacketCollision,
       "swPortStatPacketDropped": swPortStatPacketDropped,
       "swPortStatRxBcastPkt": swPortStatRxBcastPkt,
       "swPortStatRxMcastPkt": swPortStatRxMcastPkt,
       "swPortStatPortName": swPortStatPortName,
       "switchPortStatClearTable": switchPortStatClearTable,
       "switchPortMgtTable": switchPortMgtTable,
       "switchPortMgtEntry": switchPortMgtEntry,
       "swPortMgtIndex": swPortMgtIndex,
       "swPortMgtPortName": swPortMgtPortName,
       "swPortMgtPortStatus": swPortMgtPortStatus,
       "swPortMgtNegotiation": swPortMgtNegotiation,
       "swPortMgtSpeed": swPortMgtSpeed,
       "swPortMgtDuplex": swPortMgtDuplex,
       "swPortMgtFlowControl": swPortMgtFlowControl,
       "swPortMgtSecurity": swPortMgtSecurity,
       "switchPortTrunkMgt": switchPortTrunkMgt,
       "swPortTrunkSysPri": swPortTrunkSysPri,
       "switchPortTrunkAggregatorTable": switchPortTrunkAggregatorTable,
       "switchPortTrunkAggregatorEntry": switchPortTrunkAggregatorEntry,
       "swPortTrunkAggregatorIndex": swPortTrunkAggregatorIndex,
       "swPortTrunkAggregatorGroupName": swPortTrunkAggregatorGroupName,
       "swPortTrunkAggregatorMemberPorts": swPortTrunkAggregatorMemberPorts,
       "swPortTrunkAggregatorLACPStatus": swPortTrunkAggregatorLACPStatus,
       "swPortTrunkAggregatorWorkPorts": swPortTrunkAggregatorWorkPorts,
       "switchPortTrunkAggregatorInfoTable": switchPortTrunkAggregatorInfoTable,
       "switchPortTrunkAggregatorInfoEntry": switchPortTrunkAggregatorInfoEntry,
       "swPortTrunkAggregatorInfoIndex": swPortTrunkAggregatorInfoIndex,
       "swPortTrunkAggregatorInfoGroupName": swPortTrunkAggregatorInfoGroupName,
       "swPortTrunkAggregatorInfoDescription": swPortTrunkAggregatorInfoDescription,
       "switchPortTrunkLACPStateActTable": switchPortTrunkLACPStateActTable,
       "switchPortTrunkLACPStateActEntry": switchPortTrunkLACPStateActEntry,
       "swPortTrunkLACPStateActPortNum": swPortTrunkLACPStateActPortNum,
       "swPortTrunkLACPStateActStatus": swPortTrunkLACPStateActStatus,
       "swPortTrunkLACPStateActPortName": swPortTrunkLACPStateActPortName,
       "switchPortMirrorMgt": switchPortMirrorMgt,
       "swPortMirrorStatus": swPortMirrorStatus,
       "swPortMirrorAnlysisPortName": swPortMirrorAnlysisPortName,
       "swPortMirrorMonitoredPortName": swPortMirrorMonitoredPortName,
       "switchPortRateLimitMgt": switchPortRateLimitMgt,
       "switchPortRateLimitingTable": switchPortRateLimitingTable,
       "switchPortRateLimitingEntry": switchPortRateLimitingEntry,
       "swPortRateLimitingPortNum": swPortRateLimitingPortNum,
       "swPortRateLimitingInRate": swPortRateLimitingInRate,
       "swPortRateLimitingOutRate": swPortRateLimitingOutRate,
       "swPortRateLimitingPortName": swPortRateLimitingPortName,
       "switchProtocolMgt": switchProtocolMgt,
       "vlanMgt": vlanMgt,
       "vlanOperationMode": vlanOperationMode,
       "vlanGVRP": vlanGVRP,
       "vlanPortBasedTable": vlanPortBasedTable,
       "vlanPortBasedEntry": vlanPortBasedEntry,
       "vlanPortBasedIndex": vlanPortBasedIndex,
       "vlanPortBasedGroupName": vlanPortBasedGroupName,
       "vlanPortBasedVid": vlanPortBasedVid,
       "vlanPortBasedMembers": vlanPortBasedMembers,
       "vlanPortBasedStatus": vlanPortBasedStatus,
       "vlanIEEE8021QTable": vlanIEEE8021QTable,
       "vlanIEEE8021QEntry": vlanIEEE8021QEntry,
       "vlanIEEE8021QIndex": vlanIEEE8021QIndex,
       "vlanIEEE8021QPortName": vlanIEEE8021QPortName,
       "vlanIEEE8021QLinkType": vlanIEEE8021QLinkType,
       "vlanIEEE8021QUntaggedVid": vlanIEEE8021QUntaggedVid,
       "vlanIEEE8021QTaggedVids": vlanIEEE8021QTaggedVids,
       "vlanIEEE8021QGroupTable": vlanIEEE8021QGroupTable,
       "vlanIEEE8021QGroupEntry": vlanIEEE8021QGroupEntry,
       "vlanIEEE8021QGroupVid": vlanIEEE8021QGroupVid,
       "vlanIEEE8021QGroupName": vlanIEEE8021QGroupName,
       "vlanIEEE8021QGroupStatus": vlanIEEE8021QGroupStatus,
       "vlanMgtVID": vlanMgtVID,
       "rstpMgt": rstpMgt,
       "rstpStatus": rstpStatus,
       "rstpPriority": rstpPriority,
       "rstpMaxAge": rstpMaxAge,
       "rstpHelloTime": rstpHelloTime,
       "rstpForwardDelayTime": rstpForwardDelayTime,
       "rstpRootBridgeInformationTable": rstpRootBridgeInformationTable,
       "rstpRootBridgeInformationEntry": rstpRootBridgeInformationEntry,
       "rstpRootBridgeInformationIndex": rstpRootBridgeInformationIndex,
       "rstpRootBridgeInformationBridgeID": rstpRootBridgeInformationBridgeID,
       "rstpRootBridgeInformationRootPriority": rstpRootBridgeInformationRootPriority,
       "rstpRootBridgeInformationRootPort": rstpRootBridgeInformationRootPort,
       "rstpRootBridgeInformationRootPathCost": rstpRootBridgeInformationRootPathCost,
       "rstpRootBridgeInformationMaxAge": rstpRootBridgeInformationMaxAge,
       "rstpRootBridgeInformationHelloTime": rstpRootBridgeInformationHelloTime,
       "rstpRootBridgeInformationForwardDelay": rstpRootBridgeInformationForwardDelay,
       "rstpPerPortCfgTable": rstpPerPortCfgTable,
       "rstpPerPortCfgEntry": rstpPerPortCfgEntry,
       "rstpPerPortCfgPortNum": rstpPerPortCfgPortNum,
       "rstpPerPortCfgPathCost": rstpPerPortCfgPathCost,
       "rstpPerPortCfgPriority": rstpPerPortCfgPriority,
       "rstpPerPortCfgAdminP2P": rstpPerPortCfgAdminP2P,
       "rstpPerPortCfgAdminEdge": rstpPerPortCfgAdminEdge,
       "rstpPerPortCfgAdminNonStp": rstpPerPortCfgAdminNonStp,
       "rstpPerPortCfgPortName": rstpPerPortCfgPortName,
       "rstpPerPortInfoTable": rstpPerPortInfoTable,
       "rstpPerPortInfoEntry": rstpPerPortInfoEntry,
       "rstpPerPortInfoPortNum": rstpPerPortInfoPortNum,
       "rstpPerPortInfoPathCost": rstpPerPortInfoPathCost,
       "rstpPerPortInfoPriority": rstpPerPortInfoPriority,
       "rstpPerPortInfoAdminP2P": rstpPerPortInfoAdminP2P,
       "rstpPerPortInfoAdminEdge": rstpPerPortInfoAdminEdge,
       "rstpPerPortInfoStpNeighbor": rstpPerPortInfoStpNeighbor,
       "rstpPerPortInfoState": rstpPerPortInfoState,
       "rstpPerPortInfoRole": rstpPerPortInfoRole,
       "rstpPerPortInfoPortName": rstpPerPortInfoPortName,
       "qosMgt": qosMgt,
       "qosMode": qosMode,
       "qos8021pPriorityTable": qos8021pPriorityTable,
       "qos8021pPriorityEntry": qos8021pPriorityEntry,
       "qos8021pPriorityIndex": qos8021pPriorityIndex,
       "qos8021pPriority": qos8021pPriority,
       "qosIngressPortPriorityTable": qosIngressPortPriorityTable,
       "qosIngressPortPriorityEntry": qosIngressPortPriorityEntry,
       "qosIngressPortPriorityIndex": qosIngressPortPriorityIndex,
       "qosIngressPortPriority": qosIngressPortPriority,
       "qosIngressPortPriorityName": qosIngressPortPriorityName,
       "qosTosDscpTable": qosTosDscpTable,
       "qosTosDscpEntry": qosTosDscpEntry,
       "qosTosDscpIndex": qosTosDscpIndex,
       "qosTosDscp": qosTosDscp,
       "qosTosDscpPriority": qosTosDscpPriority,
       "igmpMgt": igmpMgt,
       "igmpStatus": igmpStatus,
       "igmpQuery": igmpQuery,
       "igmpLastQueryCount": igmpLastQueryCount,
       "igmpLastQueryInterval": igmpLastQueryInterval,
       "igmpEntriesTable": igmpEntriesTable,
       "igmpEntriesEntry": igmpEntriesEntry,
       "igmpEntriesEntryIndex": igmpEntriesEntryIndex,
       "igmpEntriesEntryIPAddr": igmpEntriesEntryIPAddr,
       "igmpEntriesEntryVID": igmpEntriesEntryVID,
       "igmpEntriesEntryMembers": igmpEntriesEntryMembers,
       "lldpMgt": lldpMgt,
       "lldpStatus": lldpStatus,
       "lldpInterval": lldpInterval,
       "snmpMgt": snmpMgt,
       "snmpAgentMode": snmpAgentMode,
       "snmpSystemName": snmpSystemName,
       "snmpSystemLocation": snmpSystemLocation,
       "snmpSystemContact": snmpSystemContact,
       "snmpCommunityStringTable": snmpCommunityStringTable,
       "snmpCommunityStringEntry": snmpCommunityStringEntry,
       "snmpCommunityStringIndex": snmpCommunityStringIndex,
       "snmpCommunityStringName": snmpCommunityStringName,
       "snmpCommunityStringAttribute": snmpCommunityStringAttribute,
       "snmpCommunityStringStatus": snmpCommunityStringStatus,
       "snmpTrapServerTable": snmpTrapServerTable,
       "snmpTrapServerEntry": snmpTrapServerEntry,
       "snmpTrapServerIndex": snmpTrapServerIndex,
       "snmpTrapServerIPAddr": snmpTrapServerIPAddr,
       "snmpTrapServerTrapComm": snmpTrapServerTrapComm,
       "snmpTrapServerTrapVer": snmpTrapServerTrapVer,
       "snmpTrapServerStatus": snmpTrapServerStatus,
       "snmpV3ContextName": snmpV3ContextName,
       "snmpV3UsrPrfTable": snmpV3UsrPrfTable,
       "snmpV3UsrPrfEntry": snmpV3UsrPrfEntry,
       "snmpV3UsrPrfIndex": snmpV3UsrPrfIndex,
       "snmpV3UsrPrfUserID": snmpV3UsrPrfUserID,
       "snmpV3UsrPrfAuthPw": snmpV3UsrPrfAuthPw,
       "snmpV3UsrPrfPrivacyPw": snmpV3UsrPrfPrivacyPw,
       "snmpV3UsrPrfOperation": snmpV3UsrPrfOperation,
       "snmpV3GroupContentTable": snmpV3GroupContentTable,
       "snmpV3GroupContentEntry": snmpV3GroupContentEntry,
       "snmpV3GroupContentIndex": snmpV3GroupContentIndex,
       "snmpV3GroupContentSecurityName": snmpV3GroupContentSecurityName,
       "snmpV3GroupContentGroupName": snmpV3GroupContentGroupName,
       "snmpV3GroupContentOperation": snmpV3GroupContentOperation,
       "snmpV3AccessTable": snmpV3AccessTable,
       "snmpV3AccessEntry": snmpV3AccessEntry,
       "snmpV3AccessIndex": snmpV3AccessIndex,
       "snmpV3AccessContextPrefix": snmpV3AccessContextPrefix,
       "snmpV3AccessGroupName": snmpV3AccessGroupName,
       "snmpV3AccessSecurityLevel": snmpV3AccessSecurityLevel,
       "snmpV3AccessContextMatchRule": snmpV3AccessContextMatchRule,
       "snmpV3AccessReadViewName": snmpV3AccessReadViewName,
       "snmpV3AccessWriteViewName": snmpV3AccessWriteViewName,
       "snmpV3AccessNotifyViewName": snmpV3AccessNotifyViewName,
       "snmpV3AccessOperation": snmpV3AccessOperation,
       "snmpV3MIBViewTable": snmpV3MIBViewTable,
       "snmpV3MIBViewEntry": snmpV3MIBViewEntry,
       "snmpV3MIBViewIndex": snmpV3MIBViewIndex,
       "snmpV3MIBViewName": snmpV3MIBViewName,
       "snmpV3MIBViewSubOidTree": snmpV3MIBViewSubOidTree,
       "snmpV3MIBViewType": snmpV3MIBViewType,
       "snmpV3MIBViewOperation": snmpV3MIBViewOperation,
       "switchSecurityMgt": switchSecurityMgt,
       "radiusMgt": radiusMgt,
       "radiusSysCfg": radiusSysCfg,
       "radius8021xProtocolStatus": radius8021xProtocolStatus,
       "radiusServerIP": radiusServerIP,
       "radiusServerPort": radiusServerPort,
       "radiusAccountingPort": radiusAccountingPort,
       "radiusSharedKey": radiusSharedKey,
       "radiusNASIdentifier": radiusNASIdentifier,
       "radiusPerPortCfgTable": radiusPerPortCfgTable,
       "radiusPerPortCfgEntry": radiusPerPortCfgEntry,
       "radiusPerPortCfgIndex": radiusPerPortCfgIndex,
       "radiusPerPortCfgPortName": radiusPerPortCfgPortName,
       "radiusPerPortCfgState": radiusPerPortCfgState,
       "radiusMiscCfg": radiusMiscCfg,
       "radiusMiscQuietPeriod": radiusMiscQuietPeriod,
       "radiusMiscTxPeriod": radiusMiscTxPeriod,
       "radiusMiscSupplicantTimeout": radiusMiscSupplicantTimeout,
       "radiusMiscServerTimeout": radiusMiscServerTimeout,
       "radiusMiscReAuthMax": radiusMiscReAuthMax,
       "radiusMiscReauthPeriod": radiusMiscReauthPeriod,
       "portSecurityMgt": portSecurityMgt,
       "portSecurityStaticMACTable": portSecurityStaticMACTable,
       "portSecurityStaticMACEntry": portSecurityStaticMACEntry,
       "portSecurityStaticMACIndex": portSecurityStaticMACIndex,
       "portSecurityStaticMACPortName": portSecurityStaticMACPortName,
       "portSecurityStaticMACAddr": portSecurityStaticMACAddr,
       "portSecurityStaticMACVid": portSecurityStaticMACVid,
       "portSecurityStaticMACStatus": portSecurityStaticMACStatus,
       "portSecurityMACFilteringTable": portSecurityMACFilteringTable,
       "portSecurityMACFilteringEntry": portSecurityMACFilteringEntry,
       "portSecurityMACFilteringIndex": portSecurityMACFilteringIndex,
       "portSecurityMACFilteringAddr": portSecurityMACFilteringAddr,
       "portSecurityMACFilteringVid": portSecurityMACFilteringVid,
       "portSecurityMACFilteringStatus": portSecurityMACFilteringStatus,
       "portSecurityMulticastFilterTable": portSecurityMulticastFilterTable,
       "portSecurityMulticastFilterEntry": portSecurityMulticastFilterEntry,
       "portSecurityMulticastFilterIndex": portSecurityMulticastFilterIndex,
       "portSecurityMulticastFilterAddr": portSecurityMulticastFilterAddr,
       "portSecurityMulticastFilterVid": portSecurityMulticastFilterVid,
       "portSecurityMulticastFilterMembers": portSecurityMulticastFilterMembers,
       "portSecurityMulticastFilterStatus": portSecurityMulticastFilterStatus,
       "portSecurityAllMACTable": portSecurityAllMACTable,
       "portSecurityAllMACEntry": portSecurityAllMACEntry,
       "portSecurityAllMACIndex": portSecurityAllMACIndex,
       "portSecurityAllMACPortName": portSecurityAllMACPortName,
       "portSecurityAllMACAddr": portSecurityAllMACAddr,
       "portSecurityAllMACVid": portSecurityAllMACVid,
       "portSecurityAllMACType": portSecurityAllMACType,
       "portSecurityClearMACTable": portSecurityClearMACTable,
       "aclMgt": aclMgt,
       "aclTable": aclTable,
       "aclEntry": aclEntry,
       "aclIndex": aclIndex,
       "aclGroupID": aclGroupID,
       "aclAction": aclAction,
       "aclVlanID": aclVlanID,
       "aclPacketType": aclPacketType,
       "aclSrcIPAddress": aclSrcIPAddress,
       "aclSrcMask": aclSrcMask,
       "aclDstIPAddress": aclDstIPAddress,
       "aclDstMask": aclDstMask,
       "aclIPFragment": aclIPFragment,
       "aclL4ProtocolType": aclL4ProtocolType,
       "aclL4ProtocolValue": aclL4ProtocolValue,
       "aclEtherType": aclEtherType,
       "aclEtherValue": aclEtherValue,
       "aclStatus": aclStatus,
       "tftpDownloadMgt": tftpDownloadMgt,
       "tftpDownloadServerIP": tftpDownloadServerIP,
       "tftpDownloadAgentBoardFwFileName": tftpDownloadAgentBoardFwFileName,
       "tftpDownloadAgentBoardFwDownloadFunction": tftpDownloadAgentBoardFwDownloadFunction,
       "tftpDownloadStatus": tftpDownloadStatus,
       "loadFactoryDefaultMgt": loadFactoryDefaultMgt,
       "keepCurrentIPSetting": keepCurrentIPSetting,
       "keepCurrentUsernamePassword": keepCurrentUsernamePassword,
       "loadFactoryDefaultAction": loadFactoryDefaultAction,
       "saveCfgMgt": saveCfgMgt,
       "saveCfgMgtAction": saveCfgMgtAction,
       "restartMgt": restartMgt,
       "restartAction": restartAction,
       "trapSpecificMgt": trapSpecificMgt,
       "specificTrapTopologychange": specificTrapTopologychange,
       "specificTrapFanfailure": specificTrapFanfailure}
)
