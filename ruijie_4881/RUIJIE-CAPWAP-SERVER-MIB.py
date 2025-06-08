# SNMP MIB module (RUIJIE-CAPWAP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CAPWAP-SERVER-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:45 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieCapwapSvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89)
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrMIB.setRevisions(
        ("2010-08-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCapwapSvrMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCapwapSvrMIBObjects = _RuijieCapwapSvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1)
)
_RuijieCapwapSvrWhiteListURLTable_Object = MibTable
ruijieCapwapSvrWhiteListURLTable = _RuijieCapwapSvrWhiteListURLTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListURLTable.setStatus("current")
_RuijieCapwapSvrWhiteListURLEntry_Object = MibTableRow
ruijieCapwapSvrWhiteListURLEntry = _RuijieCapwapSvrWhiteListURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 1, 1)
)
ruijieCapwapSvrWhiteListURLEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListIndex"),
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListURLEntry.setStatus("current")
_RuijieCapwapSvrWhiteListIndex_Type = Unsigned32
_RuijieCapwapSvrWhiteListIndex_Object = MibTableColumn
ruijieCapwapSvrWhiteListIndex = _RuijieCapwapSvrWhiteListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 1, 1, 1),
    _RuijieCapwapSvrWhiteListIndex_Type()
)
ruijieCapwapSvrWhiteListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListIndex.setStatus("current")


class _RuijieCapwapSvrWhiteListURL_Type(DisplayString):
    """Custom type ruijieCapwapSvrWhiteListURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieCapwapSvrWhiteListURL_Type.__name__ = "DisplayString"
_RuijieCapwapSvrWhiteListURL_Object = MibTableColumn
ruijieCapwapSvrWhiteListURL = _RuijieCapwapSvrWhiteListURL_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 1, 1, 2),
    _RuijieCapwapSvrWhiteListURL_Type()
)
ruijieCapwapSvrWhiteListURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListURL.setStatus("current")


class _RuijieCapwapSvrWhiteListURLParserStatus_Type(DisplayString):
    """Custom type ruijieCapwapSvrWhiteListURLParserStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieCapwapSvrWhiteListURLParserStatus_Type.__name__ = "DisplayString"
_RuijieCapwapSvrWhiteListURLParserStatus_Object = MibTableColumn
ruijieCapwapSvrWhiteListURLParserStatus = _RuijieCapwapSvrWhiteListURLParserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 1, 1, 3),
    _RuijieCapwapSvrWhiteListURLParserStatus_Type()
)
ruijieCapwapSvrWhiteListURLParserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListURLParserStatus.setStatus("current")
_RuijieCapwapSvrWhiteListURLRowStatus_Type = RowStatus
_RuijieCapwapSvrWhiteListURLRowStatus_Object = MibTableColumn
ruijieCapwapSvrWhiteListURLRowStatus = _RuijieCapwapSvrWhiteListURLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 1, 1, 4),
    _RuijieCapwapSvrWhiteListURLRowStatus_Type()
)
ruijieCapwapSvrWhiteListURLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListURLRowStatus.setStatus("current")
_RuijieCapwapSvrWhiteListIPTable_Object = MibTable
ruijieCapwapSvrWhiteListIPTable = _RuijieCapwapSvrWhiteListIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListIPTable.setStatus("current")
_RuijieCapwapSvrWhiteListIPEntry_Object = MibTableRow
ruijieCapwapSvrWhiteListIPEntry = _RuijieCapwapSvrWhiteListIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 2, 1)
)
ruijieCapwapSvrWhiteListIPEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListIP"),
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListIPEntry.setStatus("current")
_RuijieCapwapSvrWhiteListIP_Type = IpAddress
_RuijieCapwapSvrWhiteListIP_Object = MibTableColumn
ruijieCapwapSvrWhiteListIP = _RuijieCapwapSvrWhiteListIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 2, 1, 1),
    _RuijieCapwapSvrWhiteListIP_Type()
)
ruijieCapwapSvrWhiteListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListIP.setStatus("current")
_RuijieCapwapSvrWhiteListIPRowStatus_Type = RowStatus
_RuijieCapwapSvrWhiteListIPRowStatus_Object = MibTableColumn
ruijieCapwapSvrWhiteListIPRowStatus = _RuijieCapwapSvrWhiteListIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 2, 1, 2),
    _RuijieCapwapSvrWhiteListIPRowStatus_Type()
)
ruijieCapwapSvrWhiteListIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListIPRowStatus.setStatus("current")
_RuijieCapwapSvrBlackListURLTable_Object = MibTable
ruijieCapwapSvrBlackListURLTable = _RuijieCapwapSvrBlackListURLTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListURLTable.setStatus("current")
_RuijieCapwapSvrBlackListURLEntry_Object = MibTableRow
ruijieCapwapSvrBlackListURLEntry = _RuijieCapwapSvrBlackListURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 3, 1)
)
ruijieCapwapSvrBlackListURLEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListIndex"),
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListURLEntry.setStatus("current")
_RuijieCapwapSvrBlackListIndex_Type = Unsigned32
_RuijieCapwapSvrBlackListIndex_Object = MibTableColumn
ruijieCapwapSvrBlackListIndex = _RuijieCapwapSvrBlackListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 3, 1, 1),
    _RuijieCapwapSvrBlackListIndex_Type()
)
ruijieCapwapSvrBlackListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListIndex.setStatus("current")


class _RuijieCapwapSvrBlackListURL_Type(DisplayString):
    """Custom type ruijieCapwapSvrBlackListURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieCapwapSvrBlackListURL_Type.__name__ = "DisplayString"
_RuijieCapwapSvrBlackListURL_Object = MibTableColumn
ruijieCapwapSvrBlackListURL = _RuijieCapwapSvrBlackListURL_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 3, 1, 2),
    _RuijieCapwapSvrBlackListURL_Type()
)
ruijieCapwapSvrBlackListURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListURL.setStatus("current")


class _RuijieCapwapSvrBlackListURLParserStatus_Type(DisplayString):
    """Custom type ruijieCapwapSvrBlackListURLParserStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieCapwapSvrBlackListURLParserStatus_Type.__name__ = "DisplayString"
_RuijieCapwapSvrBlackListURLParserStatus_Object = MibTableColumn
ruijieCapwapSvrBlackListURLParserStatus = _RuijieCapwapSvrBlackListURLParserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 3, 1, 3),
    _RuijieCapwapSvrBlackListURLParserStatus_Type()
)
ruijieCapwapSvrBlackListURLParserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListURLParserStatus.setStatus("current")
_RuijieCapwapSvrBlackListURLRowStatus_Type = RowStatus
_RuijieCapwapSvrBlackListURLRowStatus_Object = MibTableColumn
ruijieCapwapSvrBlackListURLRowStatus = _RuijieCapwapSvrBlackListURLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 3, 1, 4),
    _RuijieCapwapSvrBlackListURLRowStatus_Type()
)
ruijieCapwapSvrBlackListURLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListURLRowStatus.setStatus("current")
_RuijieCapwapSvrBlackListIPTable_Object = MibTable
ruijieCapwapSvrBlackListIPTable = _RuijieCapwapSvrBlackListIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListIPTable.setStatus("current")
_RuijieCapwapSvrBlackListIPEntry_Object = MibTableRow
ruijieCapwapSvrBlackListIPEntry = _RuijieCapwapSvrBlackListIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 4, 1)
)
ruijieCapwapSvrBlackListIPEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListIP"),
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListIPEntry.setStatus("current")
_RuijieCapwapSvrBlackListIP_Type = IpAddress
_RuijieCapwapSvrBlackListIP_Object = MibTableColumn
ruijieCapwapSvrBlackListIP = _RuijieCapwapSvrBlackListIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 4, 1, 1),
    _RuijieCapwapSvrBlackListIP_Type()
)
ruijieCapwapSvrBlackListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListIP.setStatus("current")
_RuijieCapwapSvrBlackListIPRowStatus_Type = RowStatus
_RuijieCapwapSvrBlackListIPRowStatus_Object = MibTableColumn
ruijieCapwapSvrBlackListIPRowStatus = _RuijieCapwapSvrBlackListIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 4, 1, 2),
    _RuijieCapwapSvrBlackListIPRowStatus_Type()
)
ruijieCapwapSvrBlackListIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListIPRowStatus.setStatus("current")
_RuijieCapwapSvrBlackListPortTable_Object = MibTable
ruijieCapwapSvrBlackListPortTable = _RuijieCapwapSvrBlackListPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListPortTable.setStatus("current")
_RuijieCapwapSvrBlackListPortEntry_Object = MibTableRow
ruijieCapwapSvrBlackListPortEntry = _RuijieCapwapSvrBlackListPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 5, 1)
)
ruijieCapwapSvrBlackListPortEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListPort"),
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListPortEntry.setStatus("current")
_RuijieCapwapSvrBlackListPort_Type = Integer32
_RuijieCapwapSvrBlackListPort_Object = MibTableColumn
ruijieCapwapSvrBlackListPort = _RuijieCapwapSvrBlackListPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 5, 1, 1),
    _RuijieCapwapSvrBlackListPort_Type()
)
ruijieCapwapSvrBlackListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListPort.setStatus("current")
_RuijieCapwapSvrBlackListPortRowStatus_Type = RowStatus
_RuijieCapwapSvrBlackListPortRowStatus_Object = MibTableColumn
ruijieCapwapSvrBlackListPortRowStatus = _RuijieCapwapSvrBlackListPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 5, 1, 2),
    _RuijieCapwapSvrBlackListPortRowStatus_Type()
)
ruijieCapwapSvrBlackListPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrBlackListPortRowStatus.setStatus("current")
_RuijieCapwapSvrWhiteListMacTable_Object = MibTable
ruijieCapwapSvrWhiteListMacTable = _RuijieCapwapSvrWhiteListMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListMacTable.setStatus("current")
_RuijieCapwapSvrWhiteListMacEntry_Object = MibTableRow
ruijieCapwapSvrWhiteListMacEntry = _RuijieCapwapSvrWhiteListMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 6, 1)
)
ruijieCapwapSvrWhiteListMacEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListMacIndex"),
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListMacEntry.setStatus("current")
_RuijieCapwapSvrWhiteListMacIndex_Type = Unsigned32
_RuijieCapwapSvrWhiteListMacIndex_Object = MibTableColumn
ruijieCapwapSvrWhiteListMacIndex = _RuijieCapwapSvrWhiteListMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 6, 1, 1),
    _RuijieCapwapSvrWhiteListMacIndex_Type()
)
ruijieCapwapSvrWhiteListMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListMacIndex.setStatus("current")
_RuijieCapwapSvrWhiteListMac_Type = MacAddress
_RuijieCapwapSvrWhiteListMac_Object = MibTableColumn
ruijieCapwapSvrWhiteListMac = _RuijieCapwapSvrWhiteListMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 6, 1, 2),
    _RuijieCapwapSvrWhiteListMac_Type()
)
ruijieCapwapSvrWhiteListMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListMac.setStatus("current")
_RuijieCapwapSvrWhiteListMacRowStatus_Type = RowStatus
_RuijieCapwapSvrWhiteListMacRowStatus_Object = MibTableColumn
ruijieCapwapSvrWhiteListMacRowStatus = _RuijieCapwapSvrWhiteListMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 1, 6, 1, 3),
    _RuijieCapwapSvrWhiteListMacRowStatus_Type()
)
ruijieCapwapSvrWhiteListMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieCapwapSvrWhiteListMacRowStatus.setStatus("current")
_RuijieCapwapSvrMIBConformance_ObjectIdentity = ObjectIdentity
ruijieCapwapSvrMIBConformance = _RuijieCapwapSvrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 2)
)
_RuijieCapwapSvrMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieCapwapSvrMIBCompliances = _RuijieCapwapSvrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 2, 1)
)
_RuijieCapwapSvrMIBGroups_ObjectIdentity = ObjectIdentity
ruijieCapwapSvrMIBGroups = _RuijieCapwapSvrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 2, 2)
)

# Managed Objects groups

ruijieCapwapSvrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 2, 2, 1)
)
ruijieCapwapSvrMIBGroup.setObjects(
      *(("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListURL"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListURLParserStatus"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListURLRowStatus"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListIP"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListIPRowStatus"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListURL"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListURLParserStatus"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListURLRowStatus"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListIP"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListIPRowStatus"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListPort"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrBlackListPortRowStatus"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListMac"),
        ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrWhiteListMacRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrMIBGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieCapwapSvrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 89, 2, 1, 1)
)
ruijieCapwapSvrMIBCompliance.setObjects(
    ("RUIJIE-CAPWAP-SERVER-MIB", "ruijieCapwapSvrMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieCapwapSvrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CAPWAP-SERVER-MIB",
    **{"ruijieCapwapSvrMIB": ruijieCapwapSvrMIB,
       "ruijieCapwapSvrMIBObjects": ruijieCapwapSvrMIBObjects,
       "ruijieCapwapSvrWhiteListURLTable": ruijieCapwapSvrWhiteListURLTable,
       "ruijieCapwapSvrWhiteListURLEntry": ruijieCapwapSvrWhiteListURLEntry,
       "ruijieCapwapSvrWhiteListIndex": ruijieCapwapSvrWhiteListIndex,
       "ruijieCapwapSvrWhiteListURL": ruijieCapwapSvrWhiteListURL,
       "ruijieCapwapSvrWhiteListURLParserStatus": ruijieCapwapSvrWhiteListURLParserStatus,
       "ruijieCapwapSvrWhiteListURLRowStatus": ruijieCapwapSvrWhiteListURLRowStatus,
       "ruijieCapwapSvrWhiteListIPTable": ruijieCapwapSvrWhiteListIPTable,
       "ruijieCapwapSvrWhiteListIPEntry": ruijieCapwapSvrWhiteListIPEntry,
       "ruijieCapwapSvrWhiteListIP": ruijieCapwapSvrWhiteListIP,
       "ruijieCapwapSvrWhiteListIPRowStatus": ruijieCapwapSvrWhiteListIPRowStatus,
       "ruijieCapwapSvrBlackListURLTable": ruijieCapwapSvrBlackListURLTable,
       "ruijieCapwapSvrBlackListURLEntry": ruijieCapwapSvrBlackListURLEntry,
       "ruijieCapwapSvrBlackListIndex": ruijieCapwapSvrBlackListIndex,
       "ruijieCapwapSvrBlackListURL": ruijieCapwapSvrBlackListURL,
       "ruijieCapwapSvrBlackListURLParserStatus": ruijieCapwapSvrBlackListURLParserStatus,
       "ruijieCapwapSvrBlackListURLRowStatus": ruijieCapwapSvrBlackListURLRowStatus,
       "ruijieCapwapSvrBlackListIPTable": ruijieCapwapSvrBlackListIPTable,
       "ruijieCapwapSvrBlackListIPEntry": ruijieCapwapSvrBlackListIPEntry,
       "ruijieCapwapSvrBlackListIP": ruijieCapwapSvrBlackListIP,
       "ruijieCapwapSvrBlackListIPRowStatus": ruijieCapwapSvrBlackListIPRowStatus,
       "ruijieCapwapSvrBlackListPortTable": ruijieCapwapSvrBlackListPortTable,
       "ruijieCapwapSvrBlackListPortEntry": ruijieCapwapSvrBlackListPortEntry,
       "ruijieCapwapSvrBlackListPort": ruijieCapwapSvrBlackListPort,
       "ruijieCapwapSvrBlackListPortRowStatus": ruijieCapwapSvrBlackListPortRowStatus,
       "ruijieCapwapSvrWhiteListMacTable": ruijieCapwapSvrWhiteListMacTable,
       "ruijieCapwapSvrWhiteListMacEntry": ruijieCapwapSvrWhiteListMacEntry,
       "ruijieCapwapSvrWhiteListMacIndex": ruijieCapwapSvrWhiteListMacIndex,
       "ruijieCapwapSvrWhiteListMac": ruijieCapwapSvrWhiteListMac,
       "ruijieCapwapSvrWhiteListMacRowStatus": ruijieCapwapSvrWhiteListMacRowStatus,
       "ruijieCapwapSvrMIBConformance": ruijieCapwapSvrMIBConformance,
       "ruijieCapwapSvrMIBCompliances": ruijieCapwapSvrMIBCompliances,
       "ruijieCapwapSvrMIBCompliance": ruijieCapwapSvrMIBCompliance,
       "ruijieCapwapSvrMIBGroups": ruijieCapwapSvrMIBGroups,
       "ruijieCapwapSvrMIBGroup": ruijieCapwapSvrMIBGroup}
)
