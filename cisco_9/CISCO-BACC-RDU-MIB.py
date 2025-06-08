# SNMP MIB module (CISCO-BACC-RDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-BACC-RDU-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:08:31 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoBaccRduMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353)
)
if mibBuilder.loadTexts:
    ciscoBaccRduMIB.setRevisions(
        ("2005-09-02 00:00",
         "2004-03-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoBaccRduMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoBaccRduMIBNotifications = _CiscoBaccRduMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 0)
)
_CiscoBaccRduMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBaccRduMIBObjects = _CiscoBaccRduMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1)
)
_CiscoBaccRduResource_ObjectIdentity = ObjectIdentity
ciscoBaccRduResource = _CiscoBaccRduResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1)
)
_CbrProvGroupTable_Object = MibTable
cbrProvGroupTable = _CbrProvGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cbrProvGroupTable.setStatus("current")
_CbrProvGroupEntry_Object = MibTableRow
cbrProvGroupEntry = _CbrProvGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 1, 1)
)
cbrProvGroupEntry.setIndexNames(
    (0, "CISCO-BACC-RDU-MIB", "cbrProvGroupIndex"),
)
if mibBuilder.loadTexts:
    cbrProvGroupEntry.setStatus("current")
_CbrProvGroupIndex_Type = Unsigned32
_CbrProvGroupIndex_Object = MibTableColumn
cbrProvGroupIndex = _CbrProvGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 1, 1, 1),
    _CbrProvGroupIndex_Type()
)
cbrProvGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbrProvGroupIndex.setStatus("current")
_CbrProvGroupName_Type = SnmpAdminString
_CbrProvGroupName_Object = MibTableColumn
cbrProvGroupName = _CbrProvGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 1, 1, 2),
    _CbrProvGroupName_Type()
)
cbrProvGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrProvGroupName.setStatus("current")
_CbrProvGroupNumDevices_Type = Gauge32
_CbrProvGroupNumDevices_Object = MibTableColumn
cbrProvGroupNumDevices = _CbrProvGroupNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 1, 1, 3),
    _CbrProvGroupNumDevices_Type()
)
cbrProvGroupNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrProvGroupNumDevices.setStatus("current")
_CbrLicenseTable_Object = MibTable
cbrLicenseTable = _CbrLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cbrLicenseTable.setStatus("current")
_CbrLicenseEntry_Object = MibTableRow
cbrLicenseEntry = _CbrLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 2, 1)
)
cbrLicenseEntry.setIndexNames(
    (0, "CISCO-BACC-RDU-MIB", "cbrLicenseIndex"),
)
if mibBuilder.loadTexts:
    cbrLicenseEntry.setStatus("current")
_CbrLicenseIndex_Type = Unsigned32
_CbrLicenseIndex_Object = MibTableColumn
cbrLicenseIndex = _CbrLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 2, 1, 1),
    _CbrLicenseIndex_Type()
)
cbrLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbrLicenseIndex.setStatus("current")
_CbrLicenseName_Type = SnmpAdminString
_CbrLicenseName_Object = MibTableColumn
cbrLicenseName = _CbrLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 2, 1, 2),
    _CbrLicenseName_Type()
)
cbrLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrLicenseName.setStatus("current")
_CbrLicenseMaxAllowed_Type = Unsigned32
_CbrLicenseMaxAllowed_Object = MibTableColumn
cbrLicenseMaxAllowed = _CbrLicenseMaxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 2, 1, 3),
    _CbrLicenseMaxAllowed_Type()
)
cbrLicenseMaxAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrLicenseMaxAllowed.setStatus("current")
_CbrLicenseUsage_Type = Gauge32
_CbrLicenseUsage_Object = MibTableColumn
cbrLicenseUsage = _CbrLicenseUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 1, 2, 1, 4),
    _CbrLicenseUsage_Type()
)
cbrLicenseUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrLicenseUsage.setStatus("current")
_CiscoBaccRduServers_ObjectIdentity = ObjectIdentity
ciscoBaccRduServers = _CiscoBaccRduServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2)
)
_CbrDpeTable_Object = MibTable
cbrDpeTable = _CbrDpeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cbrDpeTable.setStatus("current")
_CbrDpeEntry_Object = MibTableRow
cbrDpeEntry = _CbrDpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1)
)
cbrDpeEntry.setIndexNames(
    (0, "CISCO-BACC-RDU-MIB", "cbrDpeIndex"),
)
if mibBuilder.loadTexts:
    cbrDpeEntry.setStatus("current")
_CbrDpeIndex_Type = Unsigned32
_CbrDpeIndex_Object = MibTableColumn
cbrDpeIndex = _CbrDpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 1),
    _CbrDpeIndex_Type()
)
cbrDpeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbrDpeIndex.setStatus("current")
_CbrDpeName_Type = SnmpAdminString
_CbrDpeName_Object = MibTableColumn
cbrDpeName = _CbrDpeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 2),
    _CbrDpeName_Type()
)
cbrDpeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeName.setStatus("current")
_CbrDpePort_Type = InetPortNumber
_CbrDpePort_Object = MibTableColumn
cbrDpePort = _CbrDpePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 3),
    _CbrDpePort_Type()
)
cbrDpePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpePort.setStatus("current")
_CbrDpeVersion_Type = SnmpAdminString
_CbrDpeVersion_Object = MibTableColumn
cbrDpeVersion = _CbrDpeVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 4),
    _CbrDpeVersion_Type()
)
cbrDpeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeVersion.setStatus("current")
_CbrDpeIsConnected_Type = TruthValue
_CbrDpeIsConnected_Object = MibTableColumn
cbrDpeIsConnected = _CbrDpeIsConnected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 5),
    _CbrDpeIsConnected_Type()
)
cbrDpeIsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeIsConnected.setStatus("current")
_CbrDpeInMessages_Type = Counter32
_CbrDpeInMessages_Object = MibTableColumn
cbrDpeInMessages = _CbrDpeInMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 6),
    _CbrDpeInMessages_Type()
)
cbrDpeInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeInMessages.setStatus("current")
_CbrDpeOutMessages_Type = Counter32
_CbrDpeOutMessages_Object = MibTableColumn
cbrDpeOutMessages = _CbrDpeOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 7),
    _CbrDpeOutMessages_Type()
)
cbrDpeOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeOutMessages.setStatus("current")
_CbrDpeInMsgAvgSize_Type = Gauge32
_CbrDpeInMsgAvgSize_Object = MibTableColumn
cbrDpeInMsgAvgSize = _CbrDpeInMsgAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 8),
    _CbrDpeInMsgAvgSize_Type()
)
cbrDpeInMsgAvgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeInMsgAvgSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrDpeInMsgAvgSize.setUnits("bytes")
_CbrDpeOutMsgAvgSize_Type = Gauge32
_CbrDpeOutMsgAvgSize_Object = MibTableColumn
cbrDpeOutMsgAvgSize = _CbrDpeOutMsgAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 9),
    _CbrDpeOutMsgAvgSize_Type()
)
cbrDpeOutMsgAvgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeOutMsgAvgSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrDpeOutMsgAvgSize.setUnits("bytes")
_CbrDpeInMsgMaxSize_Type = Unsigned32
_CbrDpeInMsgMaxSize_Object = MibTableColumn
cbrDpeInMsgMaxSize = _CbrDpeInMsgMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 10),
    _CbrDpeInMsgMaxSize_Type()
)
cbrDpeInMsgMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeInMsgMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrDpeInMsgMaxSize.setUnits("bytes")
_CbrDpeInMsgMinSize_Type = Unsigned32
_CbrDpeInMsgMinSize_Object = MibTableColumn
cbrDpeInMsgMinSize = _CbrDpeInMsgMinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 11),
    _CbrDpeInMsgMinSize_Type()
)
cbrDpeInMsgMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeInMsgMinSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrDpeInMsgMinSize.setUnits("bytes")
_CbrDpeOutMsgMaxSize_Type = Unsigned32
_CbrDpeOutMsgMaxSize_Object = MibTableColumn
cbrDpeOutMsgMaxSize = _CbrDpeOutMsgMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 12),
    _CbrDpeOutMsgMaxSize_Type()
)
cbrDpeOutMsgMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeOutMsgMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrDpeOutMsgMaxSize.setUnits("bytes")
_CbrDpeOutMsgMinSize_Type = Unsigned32
_CbrDpeOutMsgMinSize_Object = MibTableColumn
cbrDpeOutMsgMinSize = _CbrDpeOutMsgMinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 13),
    _CbrDpeOutMsgMinSize_Type()
)
cbrDpeOutMsgMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeOutMsgMinSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrDpeOutMsgMinSize.setUnits("bytes")
_CbrDpeAvgTimeToRecv_Type = Gauge32
_CbrDpeAvgTimeToRecv_Object = MibTableColumn
cbrDpeAvgTimeToRecv = _CbrDpeAvgTimeToRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 14),
    _CbrDpeAvgTimeToRecv_Type()
)
cbrDpeAvgTimeToRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeAvgTimeToRecv.setStatus("current")
if mibBuilder.loadTexts:
    cbrDpeAvgTimeToRecv.setUnits("milli-seconds")
_CbrDpeAvgTimeToSend_Type = Gauge32
_CbrDpeAvgTimeToSend_Object = MibTableColumn
cbrDpeAvgTimeToSend = _CbrDpeAvgTimeToSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 1, 1, 15),
    _CbrDpeAvgTimeToSend_Type()
)
cbrDpeAvgTimeToSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrDpeAvgTimeToSend.setStatus("current")
if mibBuilder.loadTexts:
    cbrDpeAvgTimeToSend.setUnits("milli-seconds")
_CbrCnrTable_Object = MibTable
cbrCnrTable = _CbrCnrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cbrCnrTable.setStatus("current")
_CbrCnrEntry_Object = MibTableRow
cbrCnrEntry = _CbrCnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1)
)
cbrCnrEntry.setIndexNames(
    (0, "CISCO-BACC-RDU-MIB", "cbrCnrIndex"),
)
if mibBuilder.loadTexts:
    cbrCnrEntry.setStatus("current")
_CbrCnrIndex_Type = Unsigned32
_CbrCnrIndex_Object = MibTableColumn
cbrCnrIndex = _CbrCnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 1),
    _CbrCnrIndex_Type()
)
cbrCnrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbrCnrIndex.setStatus("current")
_CbrCnrName_Type = SnmpAdminString
_CbrCnrName_Object = MibTableColumn
cbrCnrName = _CbrCnrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 2),
    _CbrCnrName_Type()
)
cbrCnrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrName.setStatus("current")
_CbrCnrVersion_Type = SnmpAdminString
_CbrCnrVersion_Object = MibTableColumn
cbrCnrVersion = _CbrCnrVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 3),
    _CbrCnrVersion_Type()
)
cbrCnrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrVersion.setStatus("current")
_CbrCnrIsConnected_Type = TruthValue
_CbrCnrIsConnected_Object = MibTableColumn
cbrCnrIsConnected = _CbrCnrIsConnected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 4),
    _CbrCnrIsConnected_Type()
)
cbrCnrIsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrIsConnected.setStatus("current")
_CbrCnrInMessages_Type = Counter32
_CbrCnrInMessages_Object = MibTableColumn
cbrCnrInMessages = _CbrCnrInMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 5),
    _CbrCnrInMessages_Type()
)
cbrCnrInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrInMessages.setStatus("current")
_CbrCnrOutMessages_Type = Counter32
_CbrCnrOutMessages_Object = MibTableColumn
cbrCnrOutMessages = _CbrCnrOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 6),
    _CbrCnrOutMessages_Type()
)
cbrCnrOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrOutMessages.setStatus("current")
_CbrCnrInMsgAvgSize_Type = Gauge32
_CbrCnrInMsgAvgSize_Object = MibTableColumn
cbrCnrInMsgAvgSize = _CbrCnrInMsgAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 7),
    _CbrCnrInMsgAvgSize_Type()
)
cbrCnrInMsgAvgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrInMsgAvgSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrCnrInMsgAvgSize.setUnits("bytes")
_CbrCnrOutMsgAvgSize_Type = Gauge32
_CbrCnrOutMsgAvgSize_Object = MibTableColumn
cbrCnrOutMsgAvgSize = _CbrCnrOutMsgAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 8),
    _CbrCnrOutMsgAvgSize_Type()
)
cbrCnrOutMsgAvgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrOutMsgAvgSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrCnrOutMsgAvgSize.setUnits("bytes")
_CbrCnrInMsgMaxSize_Type = Unsigned32
_CbrCnrInMsgMaxSize_Object = MibTableColumn
cbrCnrInMsgMaxSize = _CbrCnrInMsgMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 9),
    _CbrCnrInMsgMaxSize_Type()
)
cbrCnrInMsgMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrInMsgMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrCnrInMsgMaxSize.setUnits("bytes")
_CbrCnrInMsgMinSize_Type = Unsigned32
_CbrCnrInMsgMinSize_Object = MibTableColumn
cbrCnrInMsgMinSize = _CbrCnrInMsgMinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 10),
    _CbrCnrInMsgMinSize_Type()
)
cbrCnrInMsgMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrInMsgMinSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrCnrInMsgMinSize.setUnits("bytes")
_CbrCnrOutMsgMaxSize_Type = Unsigned32
_CbrCnrOutMsgMaxSize_Object = MibTableColumn
cbrCnrOutMsgMaxSize = _CbrCnrOutMsgMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 11),
    _CbrCnrOutMsgMaxSize_Type()
)
cbrCnrOutMsgMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrOutMsgMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrCnrOutMsgMaxSize.setUnits("bytes")
_CbrCnrOutMsgMinSize_Type = Unsigned32
_CbrCnrOutMsgMinSize_Object = MibTableColumn
cbrCnrOutMsgMinSize = _CbrCnrOutMsgMinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 12),
    _CbrCnrOutMsgMinSize_Type()
)
cbrCnrOutMsgMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrOutMsgMinSize.setStatus("current")
if mibBuilder.loadTexts:
    cbrCnrOutMsgMinSize.setUnits("bytes")
_CbrCnrAvgTimeToRecv_Type = Gauge32
_CbrCnrAvgTimeToRecv_Object = MibTableColumn
cbrCnrAvgTimeToRecv = _CbrCnrAvgTimeToRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 13),
    _CbrCnrAvgTimeToRecv_Type()
)
cbrCnrAvgTimeToRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrAvgTimeToRecv.setStatus("current")
if mibBuilder.loadTexts:
    cbrCnrAvgTimeToRecv.setUnits("milli-seconds")
_CbrCnrAvgTimeToSend_Type = Gauge32
_CbrCnrAvgTimeToSend_Object = MibTableColumn
cbrCnrAvgTimeToSend = _CbrCnrAvgTimeToSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 14),
    _CbrCnrAvgTimeToSend_Type()
)
cbrCnrAvgTimeToSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrAvgTimeToSend.setStatus("current")
if mibBuilder.loadTexts:
    cbrCnrAvgTimeToSend.setUnits("milli-seconds")
_CbrCnrPacketsRecv_Type = Counter32
_CbrCnrPacketsRecv_Object = MibTableColumn
cbrCnrPacketsRecv = _CbrCnrPacketsRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 15),
    _CbrCnrPacketsRecv_Type()
)
cbrCnrPacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrPacketsRecv.setStatus("current")
_CbrCnrPacketsIgnored_Type = Counter32
_CbrCnrPacketsIgnored_Object = MibTableColumn
cbrCnrPacketsIgnored = _CbrCnrPacketsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 16),
    _CbrCnrPacketsIgnored_Type()
)
cbrCnrPacketsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrPacketsIgnored.setStatus("current")
_CbrCnrPacketsDropped_Type = Counter32
_CbrCnrPacketsDropped_Object = MibTableColumn
cbrCnrPacketsDropped = _CbrCnrPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 17),
    _CbrCnrPacketsDropped_Type()
)
cbrCnrPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrPacketsDropped.setStatus("current")
_CbrCnrPacketsSuccess_Type = Counter32
_CbrCnrPacketsSuccess_Object = MibTableColumn
cbrCnrPacketsSuccess = _CbrCnrPacketsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 18),
    _CbrCnrPacketsSuccess_Type()
)
cbrCnrPacketsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrPacketsSuccess.setStatus("current")
_CbrCnrPacketsFailed_Type = Counter32
_CbrCnrPacketsFailed_Object = MibTableColumn
cbrCnrPacketsFailed = _CbrCnrPacketsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 2, 2, 1, 19),
    _CbrCnrPacketsFailed_Type()
)
cbrCnrPacketsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCnrPacketsFailed.setStatus("current")
_CiscoBaccRduStatistics_ObjectIdentity = ObjectIdentity
ciscoBaccRduStatistics = _CiscoBaccRduStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 3)
)
_CbrBatchesDropped_Type = Counter32
_CbrBatchesDropped_Object = MibScalar
cbrBatchesDropped = _CbrBatchesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 3, 1),
    _CbrBatchesDropped_Type()
)
cbrBatchesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrBatchesDropped.setStatus("current")
_CbrBatchesSucceeded_Type = Counter32
_CbrBatchesSucceeded_Object = MibScalar
cbrBatchesSucceeded = _CbrBatchesSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 3, 2),
    _CbrBatchesSucceeded_Type()
)
cbrBatchesSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrBatchesSucceeded.setStatus("current")
_CbrBatchesFailed_Type = Counter32
_CbrBatchesFailed_Object = MibScalar
cbrBatchesFailed = _CbrBatchesFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 3, 3),
    _CbrBatchesFailed_Type()
)
cbrBatchesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrBatchesFailed.setStatus("current")
_CbrBatchAvgProcessTime_Type = Counter32
_CbrBatchAvgProcessTime_Object = MibScalar
cbrBatchAvgProcessTime = _CbrBatchAvgProcessTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 3, 4),
    _CbrBatchAvgProcessTime_Type()
)
cbrBatchAvgProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrBatchAvgProcessTime.setStatus("current")
if mibBuilder.loadTexts:
    cbrBatchAvgProcessTime.setUnits("milli-seconds")
_CbrCRSReqProcessed_Type = Counter32
_CbrCRSReqProcessed_Object = MibScalar
cbrCRSReqProcessed = _CbrCRSReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 1, 3, 5),
    _CbrCRSReqProcessed_Type()
)
cbrCRSReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbrCRSReqProcessed.setStatus("current")
_CiscoBaccRduMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBaccRduMIBConformance = _CiscoBaccRduMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 2)
)
_CiscoBaccRduMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBaccRduMIBCompliances = _CiscoBaccRduMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 2, 1)
)
_CiscoBaccRduMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBaccRduMIBGroups = _CiscoBaccRduMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 2, 2)
)

# Managed Objects groups

ciscoBaccRduBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 2, 2, 1)
)
ciscoBaccRduBasicGroup.setObjects(
      *(("CISCO-BACC-RDU-MIB", "cbrBatchAvgProcessTime"),
        ("CISCO-BACC-RDU-MIB", "cbrBatchesDropped"),
        ("CISCO-BACC-RDU-MIB", "cbrBatchesFailed"),
        ("CISCO-BACC-RDU-MIB", "cbrBatchesSucceeded"),
        ("CISCO-BACC-RDU-MIB", "cbrCRSReqProcessed"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrName"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrVersion"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeName"),
        ("CISCO-BACC-RDU-MIB", "cbrDpePort"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeVersion"))
)
if mibBuilder.loadTexts:
    ciscoBaccRduBasicGroup.setStatus("current")

ciscoBaccRduResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 2, 2, 2)
)
ciscoBaccRduResourceGroup.setObjects(
      *(("CISCO-BACC-RDU-MIB", "cbrProvGroupName"),
        ("CISCO-BACC-RDU-MIB", "cbrProvGroupNumDevices"),
        ("CISCO-BACC-RDU-MIB", "cbrLicenseName"),
        ("CISCO-BACC-RDU-MIB", "cbrLicenseUsage"),
        ("CISCO-BACC-RDU-MIB", "cbrLicenseMaxAllowed"))
)
if mibBuilder.loadTexts:
    ciscoBaccRduResourceGroup.setStatus("current")

ciscoBaccRduServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 2, 2, 3)
)
ciscoBaccRduServersGroup.setObjects(
      *(("CISCO-BACC-RDU-MIB", "cbrCnrIsConnected"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrAvgTimeToRecv"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrAvgTimeToSend"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrInMessages"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrInMsgAvgSize"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrInMsgMaxSize"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrInMsgMinSize"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrOutMessages"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrOutMsgAvgSize"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrOutMsgMaxSize"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrOutMsgMinSize"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrPacketsRecv"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrPacketsIgnored"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrPacketsDropped"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrPacketsSuccess"),
        ("CISCO-BACC-RDU-MIB", "cbrCnrPacketsFailed"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeIsConnected"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeAvgTimeToRecv"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeAvgTimeToSend"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeInMessages"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeInMsgAvgSize"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeInMsgMaxSize"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeInMsgMinSize"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeOutMessages"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeOutMsgAvgSize"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeOutMsgMaxSize"),
        ("CISCO-BACC-RDU-MIB", "cbrDpeOutMsgMinSize"))
)
if mibBuilder.loadTexts:
    ciscoBaccRduServersGroup.setStatus("current")


# Notification objects

ciscoBaccRduLicenseLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 0, 1)
)
ciscoBaccRduLicenseLimit.setObjects(
      *(("CISCO-BACC-RDU-MIB", "cbrLicenseName"),
        ("CISCO-BACC-RDU-MIB", "cbrLicenseMaxAllowed"),
        ("CISCO-BACC-RDU-MIB", "cbrLicenseUsage"))
)
if mibBuilder.loadTexts:
    ciscoBaccRduLicenseLimit.setStatus(
        "current"
    )


# Notifications groups

ciscoBaccRduBasicEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 2, 2, 4)
)
ciscoBaccRduBasicEventGroup.setObjects(
    ("CISCO-BACC-RDU-MIB", "ciscoBaccRduLicenseLimit")
)
if mibBuilder.loadTexts:
    ciscoBaccRduBasicEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoBaccRduMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 353, 2, 1, 1)
)
ciscoBaccRduMIBCompliance.setObjects(
      *(("CISCO-BACC-RDU-MIB", "ciscoBaccRduBasicGroup"),
        ("CISCO-BACC-RDU-MIB", "ciscoBaccRduResourceGroup"),
        ("CISCO-BACC-RDU-MIB", "ciscoBaccRduServersGroup"))
)
if mibBuilder.loadTexts:
    ciscoBaccRduMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BACC-RDU-MIB",
    **{"ciscoBaccRduMIB": ciscoBaccRduMIB,
       "ciscoBaccRduMIBNotifications": ciscoBaccRduMIBNotifications,
       "ciscoBaccRduLicenseLimit": ciscoBaccRduLicenseLimit,
       "ciscoBaccRduMIBObjects": ciscoBaccRduMIBObjects,
       "ciscoBaccRduResource": ciscoBaccRduResource,
       "cbrProvGroupTable": cbrProvGroupTable,
       "cbrProvGroupEntry": cbrProvGroupEntry,
       "cbrProvGroupIndex": cbrProvGroupIndex,
       "cbrProvGroupName": cbrProvGroupName,
       "cbrProvGroupNumDevices": cbrProvGroupNumDevices,
       "cbrLicenseTable": cbrLicenseTable,
       "cbrLicenseEntry": cbrLicenseEntry,
       "cbrLicenseIndex": cbrLicenseIndex,
       "cbrLicenseName": cbrLicenseName,
       "cbrLicenseMaxAllowed": cbrLicenseMaxAllowed,
       "cbrLicenseUsage": cbrLicenseUsage,
       "ciscoBaccRduServers": ciscoBaccRduServers,
       "cbrDpeTable": cbrDpeTable,
       "cbrDpeEntry": cbrDpeEntry,
       "cbrDpeIndex": cbrDpeIndex,
       "cbrDpeName": cbrDpeName,
       "cbrDpePort": cbrDpePort,
       "cbrDpeVersion": cbrDpeVersion,
       "cbrDpeIsConnected": cbrDpeIsConnected,
       "cbrDpeInMessages": cbrDpeInMessages,
       "cbrDpeOutMessages": cbrDpeOutMessages,
       "cbrDpeInMsgAvgSize": cbrDpeInMsgAvgSize,
       "cbrDpeOutMsgAvgSize": cbrDpeOutMsgAvgSize,
       "cbrDpeInMsgMaxSize": cbrDpeInMsgMaxSize,
       "cbrDpeInMsgMinSize": cbrDpeInMsgMinSize,
       "cbrDpeOutMsgMaxSize": cbrDpeOutMsgMaxSize,
       "cbrDpeOutMsgMinSize": cbrDpeOutMsgMinSize,
       "cbrDpeAvgTimeToRecv": cbrDpeAvgTimeToRecv,
       "cbrDpeAvgTimeToSend": cbrDpeAvgTimeToSend,
       "cbrCnrTable": cbrCnrTable,
       "cbrCnrEntry": cbrCnrEntry,
       "cbrCnrIndex": cbrCnrIndex,
       "cbrCnrName": cbrCnrName,
       "cbrCnrVersion": cbrCnrVersion,
       "cbrCnrIsConnected": cbrCnrIsConnected,
       "cbrCnrInMessages": cbrCnrInMessages,
       "cbrCnrOutMessages": cbrCnrOutMessages,
       "cbrCnrInMsgAvgSize": cbrCnrInMsgAvgSize,
       "cbrCnrOutMsgAvgSize": cbrCnrOutMsgAvgSize,
       "cbrCnrInMsgMaxSize": cbrCnrInMsgMaxSize,
       "cbrCnrInMsgMinSize": cbrCnrInMsgMinSize,
       "cbrCnrOutMsgMaxSize": cbrCnrOutMsgMaxSize,
       "cbrCnrOutMsgMinSize": cbrCnrOutMsgMinSize,
       "cbrCnrAvgTimeToRecv": cbrCnrAvgTimeToRecv,
       "cbrCnrAvgTimeToSend": cbrCnrAvgTimeToSend,
       "cbrCnrPacketsRecv": cbrCnrPacketsRecv,
       "cbrCnrPacketsIgnored": cbrCnrPacketsIgnored,
       "cbrCnrPacketsDropped": cbrCnrPacketsDropped,
       "cbrCnrPacketsSuccess": cbrCnrPacketsSuccess,
       "cbrCnrPacketsFailed": cbrCnrPacketsFailed,
       "ciscoBaccRduStatistics": ciscoBaccRduStatistics,
       "cbrBatchesDropped": cbrBatchesDropped,
       "cbrBatchesSucceeded": cbrBatchesSucceeded,
       "cbrBatchesFailed": cbrBatchesFailed,
       "cbrBatchAvgProcessTime": cbrBatchAvgProcessTime,
       "cbrCRSReqProcessed": cbrCRSReqProcessed,
       "ciscoBaccRduMIBConformance": ciscoBaccRduMIBConformance,
       "ciscoBaccRduMIBCompliances": ciscoBaccRduMIBCompliances,
       "ciscoBaccRduMIBCompliance": ciscoBaccRduMIBCompliance,
       "ciscoBaccRduMIBGroups": ciscoBaccRduMIBGroups,
       "ciscoBaccRduBasicGroup": ciscoBaccRduBasicGroup,
       "ciscoBaccRduResourceGroup": ciscoBaccRduResourceGroup,
       "ciscoBaccRduServersGroup": ciscoBaccRduServersGroup,
       "ciscoBaccRduBasicEventGroup": ciscoBaccRduBasicEventGroup}
)
