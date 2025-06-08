# SNMP MIB module (RUIJIE-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ADDRESS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:23 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ruijieAddressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22)
)
if mibBuilder.loadTexts:
    ruijieAddressMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieAddressMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAddressMIBObjects = _RuijieAddressMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1)
)
_RuijieAddressManagementObjects_ObjectIdentity = ObjectIdentity
ruijieAddressManagementObjects = _RuijieAddressManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1)
)
_RuijieDynamicAddressCurrentNum_Type = Integer32
_RuijieDynamicAddressCurrentNum_Object = MibScalar
ruijieDynamicAddressCurrentNum = _RuijieDynamicAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 1),
    _RuijieDynamicAddressCurrentNum_Type()
)
ruijieDynamicAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDynamicAddressCurrentNum.setStatus("current")
_RuijieStaticAddressCurrentNum_Type = Integer32
_RuijieStaticAddressCurrentNum_Object = MibScalar
ruijieStaticAddressCurrentNum = _RuijieStaticAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 2),
    _RuijieStaticAddressCurrentNum_Type()
)
ruijieStaticAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaticAddressCurrentNum.setStatus("current")
_RuijieFilterAddressCurrentNum_Type = Integer32
_RuijieFilterAddressCurrentNum_Object = MibScalar
ruijieFilterAddressCurrentNum = _RuijieFilterAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 3),
    _RuijieFilterAddressCurrentNum_Type()
)
ruijieFilterAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFilterAddressCurrentNum.setStatus("current")
_RuijieAddressAvailableNum_Type = Integer32
_RuijieAddressAvailableNum_Object = MibScalar
ruijieAddressAvailableNum = _RuijieAddressAvailableNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 4),
    _RuijieAddressAvailableNum_Type()
)
ruijieAddressAvailableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAddressAvailableNum.setStatus("current")
_RuijieMacAddressTable_Object = MibTable
ruijieMacAddressTable = _RuijieMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieMacAddressTable.setStatus("current")
_RuijieMacAddressEntry_Object = MibTableRow
ruijieMacAddressEntry = _RuijieMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 5, 1)
)
ruijieMacAddressEntry.setIndexNames(
    (0, "RUIJIE-ADDRESS-MIB", "ruijieMacAddressFdbId"),
    (0, "RUIJIE-ADDRESS-MIB", "ruijieMacAddress"),
)
if mibBuilder.loadTexts:
    ruijieMacAddressEntry.setStatus("current")
_RuijieMacAddressFdbId_Type = Unsigned32
_RuijieMacAddressFdbId_Object = MibTableColumn
ruijieMacAddressFdbId = _RuijieMacAddressFdbId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 5, 1, 1),
    _RuijieMacAddressFdbId_Type()
)
ruijieMacAddressFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMacAddressFdbId.setStatus("current")
_RuijieMacAddress_Type = MacAddress
_RuijieMacAddress_Object = MibTableColumn
ruijieMacAddress = _RuijieMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 5, 1, 2),
    _RuijieMacAddress_Type()
)
ruijieMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMacAddress.setStatus("current")
_RuijieMacAddressPort_Type = IfIndex
_RuijieMacAddressPort_Object = MibTableColumn
ruijieMacAddressPort = _RuijieMacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 5, 1, 3),
    _RuijieMacAddressPort_Type()
)
ruijieMacAddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMacAddressPort.setStatus("current")


class _RuijieMacAddressType_Type(Integer32):
    """Custom type ruijieMacAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2),
          ("filter", 3))
    )


_RuijieMacAddressType_Type.__name__ = "Integer32"
_RuijieMacAddressType_Object = MibTableColumn
ruijieMacAddressType = _RuijieMacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 5, 1, 4),
    _RuijieMacAddressType_Type()
)
ruijieMacAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMacAddressType.setStatus("current")
_RuijieMacAddressStatus_Type = RowStatus
_RuijieMacAddressStatus_Object = MibTableColumn
ruijieMacAddressStatus = _RuijieMacAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 1, 5, 1, 5),
    _RuijieMacAddressStatus_Type()
)
ruijieMacAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMacAddressStatus.setStatus("current")
_RuijieAddressNotificationObjects_ObjectIdentity = ObjectIdentity
ruijieAddressNotificationObjects = _RuijieAddressNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2)
)
_RuijieMacNotiGlobalEnabled_Type = EnabledStatus
_RuijieMacNotiGlobalEnabled_Object = MibScalar
ruijieMacNotiGlobalEnabled = _RuijieMacNotiGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 1),
    _RuijieMacNotiGlobalEnabled_Type()
)
ruijieMacNotiGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMacNotiGlobalEnabled.setStatus("current")


class _RuijieMacNotificationInterval_Type(Unsigned32):
    """Custom type ruijieMacNotificationInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RuijieMacNotificationInterval_Type.__name__ = "Unsigned32"
_RuijieMacNotificationInterval_Object = MibScalar
ruijieMacNotificationInterval = _RuijieMacNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 2),
    _RuijieMacNotificationInterval_Type()
)
ruijieMacNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMacNotificationInterval.setStatus("current")


class _RuijieMacNotiHisTableMaxLength_Type(Unsigned32):
    """Custom type ruijieMacNotiHisTableMaxLength based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_RuijieMacNotiHisTableMaxLength_Type.__name__ = "Unsigned32"
_RuijieMacNotiHisTableMaxLength_Object = MibScalar
ruijieMacNotiHisTableMaxLength = _RuijieMacNotiHisTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 3),
    _RuijieMacNotiHisTableMaxLength_Type()
)
ruijieMacNotiHisTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMacNotiHisTableMaxLength.setStatus("current")
_RuijieMacNotiHisTableCurrentLength_Type = Unsigned32
_RuijieMacNotiHisTableCurrentLength_Object = MibScalar
ruijieMacNotiHisTableCurrentLength = _RuijieMacNotiHisTableCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 4),
    _RuijieMacNotiHisTableCurrentLength_Type()
)
ruijieMacNotiHisTableCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMacNotiHisTableCurrentLength.setStatus("current")
_RuijieMacNotiHisTable_Object = MibTable
ruijieMacNotiHisTable = _RuijieMacNotiHisTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ruijieMacNotiHisTable.setStatus("current")
_RuijieMacNotiHisEntry_Object = MibTableRow
ruijieMacNotiHisEntry = _RuijieMacNotiHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 5, 1)
)
ruijieMacNotiHisEntry.setIndexNames(
    (0, "RUIJIE-ADDRESS-MIB", "ruijieMacNotiHisIndex"),
)
if mibBuilder.loadTexts:
    ruijieMacNotiHisEntry.setStatus("current")


class _RuijieMacNotiHisIndex_Type(Unsigned32):
    """Custom type ruijieMacNotiHisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieMacNotiHisIndex_Type.__name__ = "Unsigned32"
_RuijieMacNotiHisIndex_Object = MibTableColumn
ruijieMacNotiHisIndex = _RuijieMacNotiHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 5, 1, 1),
    _RuijieMacNotiHisIndex_Type()
)
ruijieMacNotiHisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMacNotiHisIndex.setStatus("current")


class _RuijieMacNotiHisMacChangedMsg_Type(OctetString):
    """Custom type ruijieMacNotiHisMacChangedMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_RuijieMacNotiHisMacChangedMsg_Type.__name__ = "OctetString"
_RuijieMacNotiHisMacChangedMsg_Object = MibTableColumn
ruijieMacNotiHisMacChangedMsg = _RuijieMacNotiHisMacChangedMsg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 5, 1, 2),
    _RuijieMacNotiHisMacChangedMsg_Type()
)
ruijieMacNotiHisMacChangedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMacNotiHisMacChangedMsg.setStatus("current")
_RuijieMacNotiHisTimestamp_Type = TimeStamp
_RuijieMacNotiHisTimestamp_Object = MibTableColumn
ruijieMacNotiHisTimestamp = _RuijieMacNotiHisTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 5, 1, 3),
    _RuijieMacNotiHisTimestamp_Type()
)
ruijieMacNotiHisTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMacNotiHisTimestamp.setStatus("current")
_RuijieMacNotiIfCfgTable_Object = MibTable
ruijieMacNotiIfCfgTable = _RuijieMacNotiIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ruijieMacNotiIfCfgTable.setStatus("current")
_RuijieMacNotiIfCfgEntry_Object = MibTableRow
ruijieMacNotiIfCfgEntry = _RuijieMacNotiIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 6, 1)
)
ruijieMacNotiIfCfgEntry.setIndexNames(
    (0, "RUIJIE-ADDRESS-MIB", "ruijieMacNotiIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieMacNotiIfCfgEntry.setStatus("current")
_RuijieMacNotiIfIndex_Type = IfIndex
_RuijieMacNotiIfIndex_Object = MibTableColumn
ruijieMacNotiIfIndex = _RuijieMacNotiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 6, 1, 1),
    _RuijieMacNotiIfIndex_Type()
)
ruijieMacNotiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMacNotiIfIndex.setStatus("current")


class _RuijieIfMacAddrLearntEnable_Type(EnabledStatus):
    """Custom type ruijieIfMacAddrLearntEnable based on EnabledStatus"""
    defaultValue = 2


_RuijieIfMacAddrLearntEnable_Type.__name__ = "EnabledStatus"
_RuijieIfMacAddrLearntEnable_Object = MibTableColumn
ruijieIfMacAddrLearntEnable = _RuijieIfMacAddrLearntEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 6, 1, 2),
    _RuijieIfMacAddrLearntEnable_Type()
)
ruijieIfMacAddrLearntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfMacAddrLearntEnable.setStatus("current")


class _RuijieIfMacAddrRemovedEnable_Type(EnabledStatus):
    """Custom type ruijieIfMacAddrRemovedEnable based on EnabledStatus"""
    defaultValue = 2


_RuijieIfMacAddrRemovedEnable_Type.__name__ = "EnabledStatus"
_RuijieIfMacAddrRemovedEnable_Object = MibTableColumn
ruijieIfMacAddrRemovedEnable = _RuijieIfMacAddrRemovedEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 6, 1, 3),
    _RuijieIfMacAddrRemovedEnable_Type()
)
ruijieIfMacAddrRemovedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfMacAddrRemovedEnable.setStatus("current")
_RuijieMacIfLearnTable_Object = MibTable
ruijieMacIfLearnTable = _RuijieMacIfLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ruijieMacIfLearnTable.setStatus("current")
_RuijieMacIfLearnEntry_Object = MibTableRow
ruijieMacIfLearnEntry = _RuijieMacIfLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 7, 1)
)
ruijieMacIfLearnEntry.setIndexNames(
    (0, "RUIJIE-ADDRESS-MIB", "ruijieMacIfLearnIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieMacIfLearnEntry.setStatus("current")
_RuijieMacIfLearnIfIndex_Type = IfIndex
_RuijieMacIfLearnIfIndex_Object = MibTableColumn
ruijieMacIfLearnIfIndex = _RuijieMacIfLearnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 7, 1, 1),
    _RuijieMacIfLearnIfIndex_Type()
)
ruijieMacIfLearnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMacIfLearnIfIndex.setStatus("current")


class _RuijieMacIfLearnEnable_Type(EnabledStatus):
    """Custom type ruijieMacIfLearnEnable based on EnabledStatus"""
    defaultValue = 1


_RuijieMacIfLearnEnable_Type.__name__ = "EnabledStatus"
_RuijieMacIfLearnEnable_Object = MibTableColumn
ruijieMacIfLearnEnable = _RuijieMacIfLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 7, 1, 2),
    _RuijieMacIfLearnEnable_Type()
)
ruijieMacIfLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMacIfLearnEnable.setStatus("current")


class _RuijieMacGlobalLearnEnabled_Type(EnabledStatus):
    """Custom type ruijieMacGlobalLearnEnabled based on EnabledStatus"""
    defaultValue = 1


_RuijieMacGlobalLearnEnabled_Type.__name__ = "EnabledStatus"
_RuijieMacGlobalLearnEnabled_Object = MibScalar
ruijieMacGlobalLearnEnabled = _RuijieMacGlobalLearnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 1, 2, 8),
    _RuijieMacGlobalLearnEnabled_Type()
)
ruijieMacGlobalLearnEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMacGlobalLearnEnabled.setStatus("current")
_RuijieAddressTraps_ObjectIdentity = ObjectIdentity
ruijieAddressTraps = _RuijieAddressTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 2)
)
_RuijieAddressMIBConformance_ObjectIdentity = ObjectIdentity
ruijieAddressMIBConformance = _RuijieAddressMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 3)
)
_RuijieAddressMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieAddressMIBCompliances = _RuijieAddressMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 3, 1)
)
_RuijieAddressMIBGroups_ObjectIdentity = ObjectIdentity
ruijieAddressMIBGroups = _RuijieAddressMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 3, 2)
)

# Managed Objects groups

ruijieMacAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 3, 2, 1)
)
ruijieMacAddressMIBGroup.setObjects(
      *(("RUIJIE-ADDRESS-MIB", "ruijieDynamicAddressCurrentNum"),
        ("RUIJIE-ADDRESS-MIB", "ruijieStaticAddressCurrentNum"),
        ("RUIJIE-ADDRESS-MIB", "ruijieFilterAddressCurrentNum"),
        ("RUIJIE-ADDRESS-MIB", "ruijieAddressAvailableNum"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacAddressFdbId"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacAddress"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacAddressPort"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacAddressType"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacAddressStatus"))
)
if mibBuilder.loadTexts:
    ruijieMacAddressMIBGroup.setStatus("current")

ruijieAddressNotificationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 3, 2, 2)
)
ruijieAddressNotificationMIBGroup.setObjects(
      *(("RUIJIE-ADDRESS-MIB", "ruijieMacNotiGlobalEnabled"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacNotificationInterval"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacNotiHisTableMaxLength"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacNotiHisTableCurrentLength"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacNotiHisIndex"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacNotiHisMacChangedMsg"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacNotiHisTimestamp"),
        ("RUIJIE-ADDRESS-MIB", "ruijieMacNotiIfIndex"),
        ("RUIJIE-ADDRESS-MIB", "ruijieIfMacAddrLearntEnable"),
        ("RUIJIE-ADDRESS-MIB", "ruijieIfMacAddrRemovedEnable"))
)
if mibBuilder.loadTexts:
    ruijieAddressNotificationMIBGroup.setStatus("current")


# Notification objects

macChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 2, 1)
)
macChangedNotification.setObjects(
    ("RUIJIE-ADDRESS-MIB", "ruijieMacNotiHisMacChangedMsg")
)
if mibBuilder.loadTexts:
    macChangedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieAddressMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 22, 3, 1, 1)
)
ruijieAddressMIBCompliance.setObjects(
      *(("RUIJIE-ADDRESS-MIB", "ruijieMacAddressMIBGroup"),
        ("RUIJIE-ADDRESS-MIB", "ruijieAddressNotificationMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieAddressMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ADDRESS-MIB",
    **{"ruijieAddressMIB": ruijieAddressMIB,
       "ruijieAddressMIBObjects": ruijieAddressMIBObjects,
       "ruijieAddressManagementObjects": ruijieAddressManagementObjects,
       "ruijieDynamicAddressCurrentNum": ruijieDynamicAddressCurrentNum,
       "ruijieStaticAddressCurrentNum": ruijieStaticAddressCurrentNum,
       "ruijieFilterAddressCurrentNum": ruijieFilterAddressCurrentNum,
       "ruijieAddressAvailableNum": ruijieAddressAvailableNum,
       "ruijieMacAddressTable": ruijieMacAddressTable,
       "ruijieMacAddressEntry": ruijieMacAddressEntry,
       "ruijieMacAddressFdbId": ruijieMacAddressFdbId,
       "ruijieMacAddress": ruijieMacAddress,
       "ruijieMacAddressPort": ruijieMacAddressPort,
       "ruijieMacAddressType": ruijieMacAddressType,
       "ruijieMacAddressStatus": ruijieMacAddressStatus,
       "ruijieAddressNotificationObjects": ruijieAddressNotificationObjects,
       "ruijieMacNotiGlobalEnabled": ruijieMacNotiGlobalEnabled,
       "ruijieMacNotificationInterval": ruijieMacNotificationInterval,
       "ruijieMacNotiHisTableMaxLength": ruijieMacNotiHisTableMaxLength,
       "ruijieMacNotiHisTableCurrentLength": ruijieMacNotiHisTableCurrentLength,
       "ruijieMacNotiHisTable": ruijieMacNotiHisTable,
       "ruijieMacNotiHisEntry": ruijieMacNotiHisEntry,
       "ruijieMacNotiHisIndex": ruijieMacNotiHisIndex,
       "ruijieMacNotiHisMacChangedMsg": ruijieMacNotiHisMacChangedMsg,
       "ruijieMacNotiHisTimestamp": ruijieMacNotiHisTimestamp,
       "ruijieMacNotiIfCfgTable": ruijieMacNotiIfCfgTable,
       "ruijieMacNotiIfCfgEntry": ruijieMacNotiIfCfgEntry,
       "ruijieMacNotiIfIndex": ruijieMacNotiIfIndex,
       "ruijieIfMacAddrLearntEnable": ruijieIfMacAddrLearntEnable,
       "ruijieIfMacAddrRemovedEnable": ruijieIfMacAddrRemovedEnable,
       "ruijieMacIfLearnTable": ruijieMacIfLearnTable,
       "ruijieMacIfLearnEntry": ruijieMacIfLearnEntry,
       "ruijieMacIfLearnIfIndex": ruijieMacIfLearnIfIndex,
       "ruijieMacIfLearnEnable": ruijieMacIfLearnEnable,
       "ruijieMacGlobalLearnEnabled": ruijieMacGlobalLearnEnabled,
       "ruijieAddressTraps": ruijieAddressTraps,
       "macChangedNotification": macChangedNotification,
       "ruijieAddressMIBConformance": ruijieAddressMIBConformance,
       "ruijieAddressMIBCompliances": ruijieAddressMIBCompliances,
       "ruijieAddressMIBCompliance": ruijieAddressMIBCompliance,
       "ruijieAddressMIBGroups": ruijieAddressMIBGroups,
       "ruijieMacAddressMIBGroup": ruijieMacAddressMIBGroup,
       "ruijieAddressNotificationMIBGroup": ruijieAddressNotificationMIBGroup}
)
