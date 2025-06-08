# SNMP MIB module (RUBICA-EXPERIMENTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/rubica_49808/RUBICA-EXPERIMENTAL-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:56:10 2025
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

(research,) = mibBuilder.importSymbols(
    "RUBICA-MIB",
    "research")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rubicaExperimental = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1)
)
if mibBuilder.loadTexts:
    rubicaExperimental.setRevisions(
        ("2017-05-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DeviceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class AddressIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class StorageIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class KBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 1)
)
_Name_Type = SnmpAdminString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 1, 2),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = SnmpAdminString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 1, 3),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Date_Type = SnmpAdminString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 1, 4),
    _Date_Type()
)
date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    date.setStatus("current")
_Metadata_ObjectIdentity = ObjectIdentity
metadata = _Metadata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2)
)
_HostName_Type = SnmpAdminString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_CurrentDateTime_Type = DateAndTime
_CurrentDateTime_Object = MibScalar
currentDateTime = _CurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 3),
    _CurrentDateTime_Type()
)
currentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDateTime.setStatus("current")
_Uptime_Type = TimeTicks
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 4),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 5)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("current")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 5, 1)
)
interfaceEntry.setIndexNames(
    (0, "RUBICA-EXPERIMENTAL-MIB", "interfaceIndex"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("current")
_InterfaceIndex_Type = DeviceIndex
_InterfaceIndex_Object = MibTableColumn
interfaceIndex = _InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 5, 1, 1),
    _InterfaceIndex_Type()
)
interfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceIndex.setStatus("current")
_InterfaceName_Type = SnmpAdminString
_InterfaceName_Object = MibTableColumn
interfaceName = _InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 5, 1, 2),
    _InterfaceName_Type()
)
interfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceName.setStatus("current")


class _InterfaceStatus_Type(Bits):
    """Custom type interfaceStatus based on Bits"""
    defaultBinValue = "001"

    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1),
          ("unknown", 2))
    )

_InterfaceStatus_Type.__name__ = "Bits"
_InterfaceStatus_Object = MibTableColumn
interfaceStatus = _InterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 5, 1, 3),
    _InterfaceStatus_Type()
)
interfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatus.setStatus("current")
_InterfaceAddressTable_Object = MibTable
interfaceAddressTable = _InterfaceAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 6)
)
if mibBuilder.loadTexts:
    interfaceAddressTable.setStatus("current")
_InterfaceAddressEntry_Object = MibTableRow
interfaceAddressEntry = _InterfaceAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 6, 1)
)
interfaceAddressEntry.setIndexNames(
    (0, "RUBICA-EXPERIMENTAL-MIB", "interfaceIndex"),
    (0, "RUBICA-EXPERIMENTAL-MIB", "interfaceAddressIndex"),
)
if mibBuilder.loadTexts:
    interfaceAddressEntry.setStatus("current")
_InterfaceAddressIndex_Type = AddressIndex
_InterfaceAddressIndex_Object = MibTableColumn
interfaceAddressIndex = _InterfaceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 6, 1, 1),
    _InterfaceAddressIndex_Type()
)
interfaceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceAddressIndex.setStatus("current")
_InterfaceAddressIP_Type = InetAddress
_InterfaceAddressIP_Object = MibTableColumn
interfaceAddressIP = _InterfaceAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 6, 1, 2),
    _InterfaceAddressIP_Type()
)
interfaceAddressIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAddressIP.setStatus("current")
_InterfaceAddressType_Type = InetAddressType
_InterfaceAddressType_Object = MibTableColumn
interfaceAddressType = _InterfaceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 6, 1, 3),
    _InterfaceAddressType_Type()
)
interfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAddressType.setStatus("current")
_InterfaceMacAddress_Type = MacAddress
_InterfaceMacAddress_Object = MibTableColumn
interfaceMacAddress = _InterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 6, 1, 4),
    _InterfaceMacAddress_Type()
)
interfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMacAddress.setStatus("current")
_InterfaceTransferTable_Object = MibTable
interfaceTransferTable = _InterfaceTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 7)
)
if mibBuilder.loadTexts:
    interfaceTransferTable.setStatus("current")
_InterfaceTransferEntry_Object = MibTableRow
interfaceTransferEntry = _InterfaceTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 7, 1)
)
interfaceTransferEntry.setIndexNames(
    (0, "RUBICA-EXPERIMENTAL-MIB", "interfaceIndex"),
    (0, "RUBICA-EXPERIMENTAL-MIB", "interfaceTransferIndex"),
)
if mibBuilder.loadTexts:
    interfaceTransferEntry.setStatus("current")
_InterfaceTransferIndex_Type = AddressIndex
_InterfaceTransferIndex_Object = MibTableColumn
interfaceTransferIndex = _InterfaceTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 7, 1, 1),
    _InterfaceTransferIndex_Type()
)
interfaceTransferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceTransferIndex.setStatus("current")
_InterfaceTransferRx_Type = Counter64
_InterfaceTransferRx_Object = MibTableColumn
interfaceTransferRx = _InterfaceTransferRx_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 7, 1, 2),
    _InterfaceTransferRx_Type()
)
interfaceTransferRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTransferRx.setStatus("current")
if mibBuilder.loadTexts:
    interfaceTransferRx.setUnits("bytes")
_InterfaceTransferTx_Type = Counter64
_InterfaceTransferTx_Object = MibTableColumn
interfaceTransferTx = _InterfaceTransferTx_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 7, 1, 3),
    _InterfaceTransferTx_Type()
)
interfaceTransferTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTransferTx.setStatus("current")
if mibBuilder.loadTexts:
    interfaceTransferTx.setUnits("bytes")
_InterfaceTransferTotal_Type = Counter64
_InterfaceTransferTotal_Object = MibTableColumn
interfaceTransferTotal = _InterfaceTransferTotal_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 7, 1, 4),
    _InterfaceTransferTotal_Type()
)
interfaceTransferTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTransferTotal.setStatus("current")
if mibBuilder.loadTexts:
    interfaceTransferTotal.setUnits("bytes")
_StorageTable_Object = MibTable
storageTable = _StorageTable_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 8)
)
if mibBuilder.loadTexts:
    storageTable.setStatus("current")
_StorageEntry_Object = MibTableRow
storageEntry = _StorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 8, 1)
)
storageEntry.setIndexNames(
    (0, "RUBICA-EXPERIMENTAL-MIB", "storageIndex"),
)
if mibBuilder.loadTexts:
    storageEntry.setStatus("current")
_StorageIndex_Type = StorageIndex
_StorageIndex_Object = MibTableColumn
storageIndex = _StorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 8, 1, 1),
    _StorageIndex_Type()
)
storageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    storageIndex.setStatus("current")
_StorageMountPoint_Type = SnmpAdminString
_StorageMountPoint_Object = MibTableColumn
storageMountPoint = _StorageMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 8, 1, 2),
    _StorageMountPoint_Type()
)
storageMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMountPoint.setStatus("current")
_StorageDiskFree_Type = KBytes
_StorageDiskFree_Object = MibTableColumn
storageDiskFree = _StorageDiskFree_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 8, 1, 3),
    _StorageDiskFree_Type()
)
storageDiskFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDiskFree.setStatus("current")
if mibBuilder.loadTexts:
    storageDiskFree.setUnits("KBytes")
_StorageDiskSize_Type = KBytes
_StorageDiskSize_Object = MibTableColumn
storageDiskSize = _StorageDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 8, 1, 4),
    _StorageDiskSize_Type()
)
storageDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDiskSize.setStatus("current")
if mibBuilder.loadTexts:
    storageDiskSize.setUnits("KBytes")


class _StoragePercentFree_Type(Integer32):
    """Custom type storagePercentFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StoragePercentFree_Type.__name__ = "Integer32"
_StoragePercentFree_Object = MibTableColumn
storagePercentFree = _StoragePercentFree_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 8, 1, 5),
    _StoragePercentFree_Type()
)
storagePercentFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storagePercentFree.setStatus("current")
if mibBuilder.loadTexts:
    storagePercentFree.setUnits("percent")
_StorageFilesystem_Type = SnmpAdminString
_StorageFilesystem_Object = MibTableColumn
storageFilesystem = _StorageFilesystem_Object(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 8, 1, 6),
    _StorageFilesystem_Type()
)
storageFilesystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageFilesystem.setStatus("current")

# Managed Objects groups

info = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 1, 1)
)
info.setObjects(
      *(("RUBICA-EXPERIMENTAL-MIB", "date"),
        ("RUBICA-EXPERIMENTAL-MIB", "name"),
        ("RUBICA-EXPERIMENTAL-MIB", "version"))
)
if mibBuilder.loadTexts:
    info.setStatus("current")

host = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 49808, 9999, 1, 2, 1)
)
host.setObjects(
      *(("RUBICA-EXPERIMENTAL-MIB", "currentDateTime"),
        ("RUBICA-EXPERIMENTAL-MIB", "hostName"),
        ("RUBICA-EXPERIMENTAL-MIB", "interfaceAddressIP"),
        ("RUBICA-EXPERIMENTAL-MIB", "interfaceAddressType"),
        ("RUBICA-EXPERIMENTAL-MIB", "interfaceMacAddress"),
        ("RUBICA-EXPERIMENTAL-MIB", "interfaceName"),
        ("RUBICA-EXPERIMENTAL-MIB", "interfaceStatus"),
        ("RUBICA-EXPERIMENTAL-MIB", "interfaceTransferRx"),
        ("RUBICA-EXPERIMENTAL-MIB", "interfaceTransferTotal"),
        ("RUBICA-EXPERIMENTAL-MIB", "interfaceTransferTx"),
        ("RUBICA-EXPERIMENTAL-MIB", "storageDiskFree"),
        ("RUBICA-EXPERIMENTAL-MIB", "storageDiskSize"),
        ("RUBICA-EXPERIMENTAL-MIB", "storageFilesystem"),
        ("RUBICA-EXPERIMENTAL-MIB", "storageMountPoint"),
        ("RUBICA-EXPERIMENTAL-MIB", "storagePercentFree"),
        ("RUBICA-EXPERIMENTAL-MIB", "uptime"))
)
if mibBuilder.loadTexts:
    host.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUBICA-EXPERIMENTAL-MIB",
    **{"DeviceIndex": DeviceIndex,
       "AddressIndex": AddressIndex,
       "StorageIndex": StorageIndex,
       "KBytes": KBytes,
       "rubicaExperimental": rubicaExperimental,
       "product": product,
       "info": info,
       "name": name,
       "version": version,
       "date": date,
       "metadata": metadata,
       "host": host,
       "hostName": hostName,
       "currentDateTime": currentDateTime,
       "uptime": uptime,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceIndex": interfaceIndex,
       "interfaceName": interfaceName,
       "interfaceStatus": interfaceStatus,
       "interfaceAddressTable": interfaceAddressTable,
       "interfaceAddressEntry": interfaceAddressEntry,
       "interfaceAddressIndex": interfaceAddressIndex,
       "interfaceAddressIP": interfaceAddressIP,
       "interfaceAddressType": interfaceAddressType,
       "interfaceMacAddress": interfaceMacAddress,
       "interfaceTransferTable": interfaceTransferTable,
       "interfaceTransferEntry": interfaceTransferEntry,
       "interfaceTransferIndex": interfaceTransferIndex,
       "interfaceTransferRx": interfaceTransferRx,
       "interfaceTransferTx": interfaceTransferTx,
       "interfaceTransferTotal": interfaceTransferTotal,
       "storageTable": storageTable,
       "storageEntry": storageEntry,
       "storageIndex": storageIndex,
       "storageMountPoint": storageMountPoint,
       "storageDiskFree": storageDiskFree,
       "storageDiskSize": storageDiskSize,
       "storagePercentFree": storagePercentFree,
       "storageFilesystem": storageFilesystem}
)
