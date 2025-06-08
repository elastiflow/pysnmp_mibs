# SNMP MIB module (RUIJIE-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SNMP-AGENT-MIB.mib
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(RuijieTrapType,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "RuijieTrapType")

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
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieSnmpAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5)
)
if mibBuilder.loadTexts:
    ruijieSnmpAgentMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Community(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_RuijieSnmpAgentMIBObjects_ObjectIdentity = ObjectIdentity
ruijieSnmpAgentMIBObjects = _RuijieSnmpAgentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1)
)
_RuijieSnmpCommunityObjects_ObjectIdentity = ObjectIdentity
ruijieSnmpCommunityObjects = _RuijieSnmpCommunityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1)
)
_RuijieCommunityMaxNum_Type = Integer32
_RuijieCommunityMaxNum_Object = MibScalar
ruijieCommunityMaxNum = _RuijieCommunityMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 1),
    _RuijieCommunityMaxNum_Type()
)
ruijieCommunityMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCommunityMaxNum.setStatus("current")
_RuijieCommunityTable_Object = MibTable
ruijieCommunityTable = _RuijieCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieCommunityTable.setStatus("current")
_RuijieCommunityEntry_Object = MibTableRow
ruijieCommunityEntry = _RuijieCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 2, 1)
)
ruijieCommunityEntry.setIndexNames(
    (0, "RUIJIE-SNMP-AGENT-MIB", "ruijieCommunityName"),
)
if mibBuilder.loadTexts:
    ruijieCommunityEntry.setStatus("current")
_RuijieCommunityName_Type = Community
_RuijieCommunityName_Object = MibTableColumn
ruijieCommunityName = _RuijieCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 2, 1, 1),
    _RuijieCommunityName_Type()
)
ruijieCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCommunityName.setStatus("current")


class _RuijieCommunityWritable_Type(Integer32):
    """Custom type ruijieCommunityWritable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2))
    )


_RuijieCommunityWritable_Type.__name__ = "Integer32"
_RuijieCommunityWritable_Object = MibTableColumn
ruijieCommunityWritable = _RuijieCommunityWritable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 2, 1, 2),
    _RuijieCommunityWritable_Type()
)
ruijieCommunityWritable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCommunityWritable.setStatus("current")
_RuijieCommunityUserIpAddr_Type = IpAddress
_RuijieCommunityUserIpAddr_Object = MibTableColumn
ruijieCommunityUserIpAddr = _RuijieCommunityUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 2, 1, 3),
    _RuijieCommunityUserIpAddr_Type()
)
ruijieCommunityUserIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCommunityUserIpAddr.setStatus("current")
_RuijieCommunityEnableIpAddrAuthen_Type = EnabledStatus
_RuijieCommunityEnableIpAddrAuthen_Object = MibTableColumn
ruijieCommunityEnableIpAddrAuthen = _RuijieCommunityEnableIpAddrAuthen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 2, 1, 4),
    _RuijieCommunityEnableIpAddrAuthen_Type()
)
ruijieCommunityEnableIpAddrAuthen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCommunityEnableIpAddrAuthen.setStatus("current")
_RuijieCommunityStatus_Type = RowStatus
_RuijieCommunityStatus_Object = MibTableColumn
ruijieCommunityStatus = _RuijieCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 2, 1, 5),
    _RuijieCommunityStatus_Type()
)
ruijieCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCommunityStatus.setStatus("current")
_RuijieReadCommunityName_Type = DisplayString
_RuijieReadCommunityName_Object = MibScalar
ruijieReadCommunityName = _RuijieReadCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 3),
    _RuijieReadCommunityName_Type()
)
ruijieReadCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieReadCommunityName.setStatus("current")
_RuijieWriteCommunityName_Type = DisplayString
_RuijieWriteCommunityName_Object = MibScalar
ruijieWriteCommunityName = _RuijieWriteCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 1, 4),
    _RuijieWriteCommunityName_Type()
)
ruijieWriteCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWriteCommunityName.setStatus("current")
_RuijieSnmpTrapObjects_ObjectIdentity = ObjectIdentity
ruijieSnmpTrapObjects = _RuijieSnmpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2)
)
_RuijieTrapDstMaxNumber_Type = Integer32
_RuijieTrapDstMaxNumber_Object = MibScalar
ruijieTrapDstMaxNumber = _RuijieTrapDstMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 1),
    _RuijieTrapDstMaxNumber_Type()
)
ruijieTrapDstMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapDstMaxNumber.setStatus("current")
_RuijieTrapDstTable_Object = MibTable
ruijieTrapDstTable = _RuijieTrapDstTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieTrapDstTable.setStatus("current")
_RuijieTrapDstEntry_Object = MibTableRow
ruijieTrapDstEntry = _RuijieTrapDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 2, 1)
)
ruijieTrapDstEntry.setIndexNames(
    (0, "RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDstAddr"),
)
if mibBuilder.loadTexts:
    ruijieTrapDstEntry.setStatus("current")
_RuijieTrapDstAddr_Type = IpAddress
_RuijieTrapDstAddr_Object = MibTableColumn
ruijieTrapDstAddr = _RuijieTrapDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 2, 1, 1),
    _RuijieTrapDstAddr_Type()
)
ruijieTrapDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapDstAddr.setStatus("current")


class _RuijieTrapDstCommunity_Type(Community):
    """Custom type ruijieTrapDstCommunity based on Community"""
    defaultValue = OctetString("public")


_RuijieTrapDstCommunity_Type.__name__ = "Community"
_RuijieTrapDstCommunity_Object = MibTableColumn
ruijieTrapDstCommunity = _RuijieTrapDstCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 2, 1, 2),
    _RuijieTrapDstCommunity_Type()
)
ruijieTrapDstCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTrapDstCommunity.setStatus("current")


class _RuijieTrapDstSendTrapClass_Type(Integer32):
    """Custom type ruijieTrapDstSendTrapClass based on Integer32"""
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
        *(("snmpv1-Trap", 1),
          ("snmpv2c-Trap", 2),
          ("snmpv3-trap", 3))
    )


_RuijieTrapDstSendTrapClass_Type.__name__ = "Integer32"
_RuijieTrapDstSendTrapClass_Object = MibTableColumn
ruijieTrapDstSendTrapClass = _RuijieTrapDstSendTrapClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 2, 1, 3),
    _RuijieTrapDstSendTrapClass_Type()
)
ruijieTrapDstSendTrapClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTrapDstSendTrapClass.setStatus("current")
_RuijieTrapDstEntryStatus_Type = RowStatus
_RuijieTrapDstEntryStatus_Object = MibTableColumn
ruijieTrapDstEntryStatus = _RuijieTrapDstEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 2, 1, 4),
    _RuijieTrapDstEntryStatus_Type()
)
ruijieTrapDstEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTrapDstEntryStatus.setStatus("current")
_RuijieTrapActionTable_Object = MibTable
ruijieTrapActionTable = _RuijieTrapActionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieTrapActionTable.setStatus("current")
_RuijieTrapActionEntry_Object = MibTableRow
ruijieTrapActionEntry = _RuijieTrapActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 3, 1)
)
ruijieTrapActionEntry.setIndexNames(
    (0, "RUIJIE-SNMP-AGENT-MIB", "ruijieTrapType"),
)
if mibBuilder.loadTexts:
    ruijieTrapActionEntry.setStatus("current")
_RuijieTrapType_Type = RuijieTrapType
_RuijieTrapType_Object = MibTableColumn
ruijieTrapType = _RuijieTrapType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 3, 1, 1),
    _RuijieTrapType_Type()
)
ruijieTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapType.setStatus("current")


class _RuijieTrapAction_Type(Integer32):
    """Custom type ruijieTrapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sendtrap", 2))
    )


_RuijieTrapAction_Type.__name__ = "Integer32"
_RuijieTrapAction_Object = MibTableColumn
ruijieTrapAction = _RuijieTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 3, 1, 2),
    _RuijieTrapAction_Type()
)
ruijieTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieTrapAction.setStatus("current")
_RuijieTrapControlTable_Object = MibTable
ruijieTrapControlTable = _RuijieTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieTrapControlTable.setStatus("current")
_RuijieTrapControlEntry_Object = MibTableRow
ruijieTrapControlEntry = _RuijieTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 4, 1)
)
ruijieTrapControlEntry.setIndexNames(
    (0, "RUIJIE-SNMP-AGENT-MIB", "ruijieTrapName"),
)
if mibBuilder.loadTexts:
    ruijieTrapControlEntry.setStatus("current")


class _RuijieTrapName_Type(DisplayString):
    """Custom type ruijieTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieTrapName_Type.__name__ = "DisplayString"
_RuijieTrapName_Object = MibTableColumn
ruijieTrapName = _RuijieTrapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 4, 1, 1),
    _RuijieTrapName_Type()
)
ruijieTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapName.setStatus("current")


class _RuijieTrapDescr_Type(DisplayString):
    """Custom type ruijieTrapDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieTrapDescr_Type.__name__ = "DisplayString"
_RuijieTrapDescr_Object = MibTableColumn
ruijieTrapDescr = _RuijieTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 4, 1, 2),
    _RuijieTrapDescr_Type()
)
ruijieTrapDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieTrapDescr.setStatus("current")


class _RuijieTrapOnOff_Type(Integer32):
    """Custom type ruijieTrapOnOff based on Integer32"""
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


_RuijieTrapOnOff_Type.__name__ = "Integer32"
_RuijieTrapOnOff_Object = MibTableColumn
ruijieTrapOnOff = _RuijieTrapOnOff_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 4, 1, 3),
    _RuijieTrapOnOff_Type()
)
ruijieTrapOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieTrapOnOff.setStatus("current")
_RuijieTrapDesTable_Object = MibTable
ruijieTrapDesTable = _RuijieTrapDesTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ruijieTrapDesTable.setStatus("current")
_RuijieTrapDesEntry_Object = MibTableRow
ruijieTrapDesEntry = _RuijieTrapDesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 5, 1)
)
ruijieTrapDesEntry.setIndexNames(
    (0, "RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDesIndex"),
)
if mibBuilder.loadTexts:
    ruijieTrapDesEntry.setStatus("current")
_RuijieTrapDesIndex_Type = Integer32
_RuijieTrapDesIndex_Object = MibTableColumn
ruijieTrapDesIndex = _RuijieTrapDesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 5, 1, 1),
    _RuijieTrapDesIndex_Type()
)
ruijieTrapDesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapDesIndex.setStatus("current")
_RuijieTrapDesIPAddress_Type = TAddress
_RuijieTrapDesIPAddress_Object = MibTableColumn
ruijieTrapDesIPAddress = _RuijieTrapDesIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 5, 1, 2),
    _RuijieTrapDesIPAddress_Type()
)
ruijieTrapDesIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTrapDesIPAddress.setStatus("current")
_RuijieTrapDesCommunity_Type = Community
_RuijieTrapDesCommunity_Object = MibTableColumn
ruijieTrapDesCommunity = _RuijieTrapDesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 5, 1, 3),
    _RuijieTrapDesCommunity_Type()
)
ruijieTrapDesCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTrapDesCommunity.setStatus("current")


class _RuijieTrapDesVersion_Type(Integer32):
    """Custom type ruijieTrapDesVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1-Trap", 1),
          ("snmpv2c-Trap", 2),
          ("snmpv3-trap", 3))
    )


_RuijieTrapDesVersion_Type.__name__ = "Integer32"
_RuijieTrapDesVersion_Object = MibTableColumn
ruijieTrapDesVersion = _RuijieTrapDesVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 5, 1, 4),
    _RuijieTrapDesVersion_Type()
)
ruijieTrapDesVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTrapDesVersion.setStatus("current")
_RuijieTrapDesStatus_Type = RowStatus
_RuijieTrapDesStatus_Object = MibTableColumn
ruijieTrapDesStatus = _RuijieTrapDesStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 2, 5, 1, 5),
    _RuijieTrapDesStatus_Type()
)
ruijieTrapDesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTrapDesStatus.setStatus("current")
_RuijieSnmpUdpPortObjects_ObjectIdentity = ObjectIdentity
ruijieSnmpUdpPortObjects = _RuijieSnmpUdpPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 3)
)
_RuijieSNMPGetSetPort_Type = Integer32
_RuijieSNMPGetSetPort_Object = MibScalar
ruijieSNMPGetSetPort = _RuijieSNMPGetSetPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 3, 1),
    _RuijieSNMPGetSetPort_Type()
)
ruijieSNMPGetSetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNMPGetSetPort.setStatus("current")
_RuijieSNMPTrapPort_Type = Integer32
_RuijieSNMPTrapPort_Object = MibScalar
ruijieSNMPTrapPort = _RuijieSNMPTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 3, 2),
    _RuijieSNMPTrapPort_Type()
)
ruijieSNMPTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNMPTrapPort.setStatus("current")
_RuijieSnmpNetObjects_ObjectIdentity = ObjectIdentity
ruijieSnmpNetObjects = _RuijieSnmpNetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 4)
)
_RuijieSysNetID_Type = DisplayString
_RuijieSysNetID_Object = MibScalar
ruijieSysNetID = _RuijieSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 1, 4, 1),
    _RuijieSysNetID_Type()
)
ruijieSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSysNetID.setStatus("current")
_RuijieSnmpAgentMIBConformance_ObjectIdentity = ObjectIdentity
ruijieSnmpAgentMIBConformance = _RuijieSnmpAgentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 2)
)
_RuijieSnmpAgentMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieSnmpAgentMIBCompliances = _RuijieSnmpAgentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 2, 1)
)
_RuijieSnmpAgentMIBGroups_ObjectIdentity = ObjectIdentity
ruijieSnmpAgentMIBGroups = _RuijieSnmpAgentMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 2, 2)
)

# Managed Objects groups

ruijieCommunityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 2, 2, 1)
)
ruijieCommunityMIBGroup.setObjects(
      *(("RUIJIE-SNMP-AGENT-MIB", "ruijieCommunityMaxNum"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieCommunityName"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieCommunityWritable"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieCommunityUserIpAddr"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieCommunityEnableIpAddrAuthen"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieCommunityStatus"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieReadCommunityName"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieWriteCommunityName"))
)
if mibBuilder.loadTexts:
    ruijieCommunityMIBGroup.setStatus("current")

ruijieSnmpTrapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 2, 2, 2)
)
ruijieSnmpTrapMIBGroup.setObjects(
      *(("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDstSendTrapClass"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDstMaxNumber"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDstAddr"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDstCommunity"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDstEntryStatus"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapType"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapAction"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapName"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDescr"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapOnOff"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDesIndex"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDesIPAddress"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDesCommunity"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDesVersion"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieTrapDesStatus"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieSysNetID"))
)
if mibBuilder.loadTexts:
    ruijieSnmpTrapMIBGroup.setStatus("current")

ruijieSnmpUdpPortMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 2, 2, 3)
)
ruijieSnmpUdpPortMIBGroup.setObjects(
      *(("RUIJIE-SNMP-AGENT-MIB", "ruijieSNMPGetSetPort"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieSNMPTrapPort"))
)
if mibBuilder.loadTexts:
    ruijieSnmpUdpPortMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieSnmpAgentMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 5, 2, 1, 1)
)
ruijieSnmpAgentMIBCompliance.setObjects(
      *(("RUIJIE-SNMP-AGENT-MIB", "ruijieCommunityMIBGroup"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieSnmpTrapMIBGroup"),
        ("RUIJIE-SNMP-AGENT-MIB", "ruijieSnmpUdpPortMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieSnmpAgentMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SNMP-AGENT-MIB",
    **{"Community": Community,
       "ruijieSnmpAgentMIB": ruijieSnmpAgentMIB,
       "ruijieSnmpAgentMIBObjects": ruijieSnmpAgentMIBObjects,
       "ruijieSnmpCommunityObjects": ruijieSnmpCommunityObjects,
       "ruijieCommunityMaxNum": ruijieCommunityMaxNum,
       "ruijieCommunityTable": ruijieCommunityTable,
       "ruijieCommunityEntry": ruijieCommunityEntry,
       "ruijieCommunityName": ruijieCommunityName,
       "ruijieCommunityWritable": ruijieCommunityWritable,
       "ruijieCommunityUserIpAddr": ruijieCommunityUserIpAddr,
       "ruijieCommunityEnableIpAddrAuthen": ruijieCommunityEnableIpAddrAuthen,
       "ruijieCommunityStatus": ruijieCommunityStatus,
       "ruijieReadCommunityName": ruijieReadCommunityName,
       "ruijieWriteCommunityName": ruijieWriteCommunityName,
       "ruijieSnmpTrapObjects": ruijieSnmpTrapObjects,
       "ruijieTrapDstMaxNumber": ruijieTrapDstMaxNumber,
       "ruijieTrapDstTable": ruijieTrapDstTable,
       "ruijieTrapDstEntry": ruijieTrapDstEntry,
       "ruijieTrapDstAddr": ruijieTrapDstAddr,
       "ruijieTrapDstCommunity": ruijieTrapDstCommunity,
       "ruijieTrapDstSendTrapClass": ruijieTrapDstSendTrapClass,
       "ruijieTrapDstEntryStatus": ruijieTrapDstEntryStatus,
       "ruijieTrapActionTable": ruijieTrapActionTable,
       "ruijieTrapActionEntry": ruijieTrapActionEntry,
       "ruijieTrapType": ruijieTrapType,
       "ruijieTrapAction": ruijieTrapAction,
       "ruijieTrapControlTable": ruijieTrapControlTable,
       "ruijieTrapControlEntry": ruijieTrapControlEntry,
       "ruijieTrapName": ruijieTrapName,
       "ruijieTrapDescr": ruijieTrapDescr,
       "ruijieTrapOnOff": ruijieTrapOnOff,
       "ruijieTrapDesTable": ruijieTrapDesTable,
       "ruijieTrapDesEntry": ruijieTrapDesEntry,
       "ruijieTrapDesIndex": ruijieTrapDesIndex,
       "ruijieTrapDesIPAddress": ruijieTrapDesIPAddress,
       "ruijieTrapDesCommunity": ruijieTrapDesCommunity,
       "ruijieTrapDesVersion": ruijieTrapDesVersion,
       "ruijieTrapDesStatus": ruijieTrapDesStatus,
       "ruijieSnmpUdpPortObjects": ruijieSnmpUdpPortObjects,
       "ruijieSNMPGetSetPort": ruijieSNMPGetSetPort,
       "ruijieSNMPTrapPort": ruijieSNMPTrapPort,
       "ruijieSnmpNetObjects": ruijieSnmpNetObjects,
       "ruijieSysNetID": ruijieSysNetID,
       "ruijieSnmpAgentMIBConformance": ruijieSnmpAgentMIBConformance,
       "ruijieSnmpAgentMIBCompliances": ruijieSnmpAgentMIBCompliances,
       "ruijieSnmpAgentMIBCompliance": ruijieSnmpAgentMIBCompliance,
       "ruijieSnmpAgentMIBGroups": ruijieSnmpAgentMIBGroups,
       "ruijieCommunityMIBGroup": ruijieCommunityMIBGroup,
       "ruijieSnmpTrapMIBGroup": ruijieSnmpTrapMIBGroup,
       "ruijieSnmpUdpPortMIBGroup": ruijieSnmpUdpPortMIBGroup}
)
