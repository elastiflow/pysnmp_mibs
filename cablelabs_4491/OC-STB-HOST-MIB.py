# SNMP MIB module (OC-STB-HOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/OC-STB-HOST-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:18 2025
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

(clabProjOpenCable,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjOpenCable")

(TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB",
    "TenthdBmV")

(hrDeviceIndex,
 hrStorageIndex) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex",
    "hrStorageIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ocStbHostMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ocStbHostMibModule.setRevisions(
        ("2012-05-31 00:00",
         "2012-01-12 00:00",
         "2011-02-04 00:00",
         "2010-05-07 00:00",
         "2009-12-11 00:00",
         "2009-09-04 00:00",
         "2009-05-08 00:00",
         "2009-02-06 00:00",
         "2008-11-14 00:00",
         "2008-03-28 00:00",
         "2007-11-13 00:00",
         "2007-09-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VideoOutputFormat(TextualConvention, Integer32):
    status = "current"
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
        *(("format480i", 1),
          ("format480p", 2),
          ("format720p", 3),
          ("format1080i", 4),
          ("format1080p", 5))
    )



class AudioOutputFormat(TextualConvention, Integer32):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("lpcm", 2),
          ("ac3", 3),
          ("eac3", 4),
          ("mpeg1L1L2", 5),
          ("mpeg1L3", 6),
          ("mpeg2", 7),
          ("mpeg4", 8),
          ("dts", 9),
          ("atrac", 10))
    )



class VideoAspectRatio(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("fourByThree", 2),
          ("sixteenByNine", 3))
    )



class VideoContainerFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("mpeg2", 2),
          ("mpeg4", 3))
    )



# MIB Managed Objects in the order of their OIDs

_OcStbHostNotifications_ObjectIdentity = ObjectIdentity
ocStbHostNotifications = _OcStbHostNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 0)
)
_OcStbHostMibObjects_ObjectIdentity = ObjectIdentity
ocStbHostMibObjects = _OcStbHostMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1)
)
_OcStbHostSystem_ObjectIdentity = ObjectIdentity
ocStbHostSystem = _OcStbHostSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1)
)
_OcStbHostHWIdentifiers_ObjectIdentity = ObjectIdentity
ocStbHostHWIdentifiers = _OcStbHostHWIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 1)
)
_OcStbHostSerialNumber_Type = SnmpAdminString
_OcStbHostSerialNumber_Object = MibScalar
ocStbHostSerialNumber = _OcStbHostSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 1, 1),
    _OcStbHostSerialNumber_Type()
)
ocStbHostSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSerialNumber.setStatus("current")


class _OcStbHostHostID_Type(DisplayString):
    """Custom type ocStbHostHostID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixedLength = 17


_OcStbHostHostID_Type.__name__ = "DisplayString"
_OcStbHostHostID_Object = MibScalar
ocStbHostHostID = _OcStbHostHostID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 1, 2),
    _OcStbHostHostID_Type()
)
ocStbHostHostID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostHostID.setStatus("current")


class _OcStbHostCapabilities_Type(Integer32):
    """Custom type ocStbHostCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ochd2", 2),
          ("embedded", 3),
          ("dcas", 4),
          ("ochd21", 5),
          ("bocr", 6),
          ("ochdtc", 7))
    )


_OcStbHostCapabilities_Type.__name__ = "Integer32"
_OcStbHostCapabilities_Object = MibScalar
ocStbHostCapabilities = _OcStbHostCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 1, 3),
    _OcStbHostCapabilities_Type()
)
ocStbHostCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCapabilities.setStatus("current")
_OcStbHostAvcSupport_Type = TruthValue
_OcStbHostAvcSupport_Object = MibScalar
ocStbHostAvcSupport = _OcStbHostAvcSupport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 1, 4),
    _OcStbHostAvcSupport_Type()
)
ocStbHostAvcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostAvcSupport.setStatus("current")
_OcStbHostInterfaces_ObjectIdentity = ObjectIdentity
ocStbHostInterfaces = _OcStbHostInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2)
)
_OcStbHostDevInterfaceTypes_ObjectIdentity = ObjectIdentity
ocStbHostDevInterfaceTypes = _OcStbHostDevInterfaceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1)
)
_OcStbHostOther_ObjectIdentity = ObjectIdentity
ocStbHostOther = _OcStbHostOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ocStbHostOther.setStatus("current")
_OcStbHostScte55FdcRx_ObjectIdentity = ObjectIdentity
ocStbHostScte55FdcRx = _OcStbHostScte55FdcRx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ocStbHostScte55FdcRx.setStatus("current")
_OcStbHostScte55RdcTx_ObjectIdentity = ObjectIdentity
ocStbHostScte55RdcTx = _OcStbHostScte55RdcTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ocStbHostScte55RdcTx.setStatus("current")
_OcStbHostScte40FatRx_ObjectIdentity = ObjectIdentity
ocStbHostScte40FatRx = _OcStbHostScte40FatRx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ocStbHostScte40FatRx.setStatus("current")
_OcStbHostBbVideoIn_ObjectIdentity = ObjectIdentity
ocStbHostBbVideoIn = _OcStbHostBbVideoIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ocStbHostBbVideoIn.setStatus("current")
_OcStbHostBbAudioIn_ObjectIdentity = ObjectIdentity
ocStbHostBbAudioIn = _OcStbHostBbAudioIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ocStbHostBbAudioIn.setStatus("current")
_OcStbHostBbVideoOut_ObjectIdentity = ObjectIdentity
ocStbHostBbVideoOut = _OcStbHostBbVideoOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ocStbHostBbVideoOut.setStatus("current")
_OcStbHostBbAudioOut_ObjectIdentity = ObjectIdentity
ocStbHostBbAudioOut = _OcStbHostBbAudioOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ocStbHostBbAudioOut.setStatus("current")
_OcStbHostRfOutCh_ObjectIdentity = ObjectIdentity
ocStbHostRfOutCh = _OcStbHostRfOutCh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ocStbHostRfOutCh.setStatus("current")
_OcStbHostSVideoIn_ObjectIdentity = ObjectIdentity
ocStbHostSVideoIn = _OcStbHostSVideoIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ocStbHostSVideoIn.setStatus("current")
_OcStbHostSVideoOut_ObjectIdentity = ObjectIdentity
ocStbHostSVideoOut = _OcStbHostSVideoOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ocStbHostSVideoOut.setStatus("current")
_OcStbHostComponentIn_ObjectIdentity = ObjectIdentity
ocStbHostComponentIn = _OcStbHostComponentIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    ocStbHostComponentIn.setStatus("current")
_OcStbHostComponentOut_ObjectIdentity = ObjectIdentity
ocStbHostComponentOut = _OcStbHostComponentOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 13)
)
if mibBuilder.loadTexts:
    ocStbHostComponentOut.setStatus("current")
_OcStbHostDviIn_ObjectIdentity = ObjectIdentity
ocStbHostDviIn = _OcStbHostDviIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 14)
)
if mibBuilder.loadTexts:
    ocStbHostDviIn.setStatus("current")
_OcStbHostDviOut_ObjectIdentity = ObjectIdentity
ocStbHostDviOut = _OcStbHostDviOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 15)
)
if mibBuilder.loadTexts:
    ocStbHostDviOut.setStatus("current")
_OcStbHostHdmiIn_ObjectIdentity = ObjectIdentity
ocStbHostHdmiIn = _OcStbHostHdmiIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 16)
)
if mibBuilder.loadTexts:
    ocStbHostHdmiIn.setStatus("current")
_OcStbHostHdmiOut_ObjectIdentity = ObjectIdentity
ocStbHostHdmiOut = _OcStbHostHdmiOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 17)
)
if mibBuilder.loadTexts:
    ocStbHostHdmiOut.setStatus("current")
_OcStbHostRcaSpdifIn_ObjectIdentity = ObjectIdentity
ocStbHostRcaSpdifIn = _OcStbHostRcaSpdifIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 18)
)
if mibBuilder.loadTexts:
    ocStbHostRcaSpdifIn.setStatus("current")
_OcStbHostRcaSpdifOut_ObjectIdentity = ObjectIdentity
ocStbHostRcaSpdifOut = _OcStbHostRcaSpdifOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    ocStbHostRcaSpdifOut.setStatus("current")
_OcStbHostToslinkSpdifIn_ObjectIdentity = ObjectIdentity
ocStbHostToslinkSpdifIn = _OcStbHostToslinkSpdifIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 20)
)
if mibBuilder.loadTexts:
    ocStbHostToslinkSpdifIn.setStatus("current")
_OcStbHostToslinkSpdifOut_ObjectIdentity = ObjectIdentity
ocStbHostToslinkSpdifOut = _OcStbHostToslinkSpdifOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 21)
)
if mibBuilder.loadTexts:
    ocStbHostToslinkSpdifOut.setStatus("current")
_OcStbHostDisplayOut_ObjectIdentity = ObjectIdentity
ocStbHostDisplayOut = _OcStbHostDisplayOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 22)
)
if mibBuilder.loadTexts:
    ocStbHostDisplayOut.setStatus("current")
_OcStbHost1394In_ObjectIdentity = ObjectIdentity
ocStbHost1394In = _OcStbHost1394In_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 23)
)
if mibBuilder.loadTexts:
    ocStbHost1394In.setStatus("current")
_OcStbHost1394Out_ObjectIdentity = ObjectIdentity
ocStbHost1394Out = _OcStbHost1394Out_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 24)
)
if mibBuilder.loadTexts:
    ocStbHost1394Out.setStatus("current")
_OcStbHostDRIInterface_ObjectIdentity = ObjectIdentity
ocStbHostDRIInterface = _OcStbHostDRIInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 1, 25)
)
if mibBuilder.loadTexts:
    ocStbHostDRIInterface.setStatus("current")
_OcStbHostAVInterfaceTable_Object = MibTable
ocStbHostAVInterfaceTable = _OcStbHostAVInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ocStbHostAVInterfaceTable.setStatus("current")
_OcStbHostAVInterfaceEntry_Object = MibTableRow
ocStbHostAVInterfaceEntry = _OcStbHostAVInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 2, 1)
)
ocStbHostAVInterfaceEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostAVInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostAVInterfaceEntry.setStatus("current")


class _OcStbHostAVInterfaceIndex_Type(Unsigned32):
    """Custom type ocStbHostAVInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcStbHostAVInterfaceIndex_Type.__name__ = "Unsigned32"
_OcStbHostAVInterfaceIndex_Object = MibTableColumn
ocStbHostAVInterfaceIndex = _OcStbHostAVInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 2, 1, 1),
    _OcStbHostAVInterfaceIndex_Type()
)
ocStbHostAVInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostAVInterfaceIndex.setStatus("current")
_OcStbHostAVInterfaceType_Type = AutonomousType
_OcStbHostAVInterfaceType_Object = MibTableColumn
ocStbHostAVInterfaceType = _OcStbHostAVInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 2, 1, 2),
    _OcStbHostAVInterfaceType_Type()
)
ocStbHostAVInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostAVInterfaceType.setStatus("current")
_OcStbHostAVInterfaceDesc_Type = SnmpAdminString
_OcStbHostAVInterfaceDesc_Object = MibTableColumn
ocStbHostAVInterfaceDesc = _OcStbHostAVInterfaceDesc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 2, 1, 3),
    _OcStbHostAVInterfaceDesc_Type()
)
ocStbHostAVInterfaceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostAVInterfaceDesc.setStatus("current")


class _OcStbHostAVInterfaceStatus_Type(Integer32):
    """Custom type ocStbHostAVInterfaceStatus based on Integer32"""
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


_OcStbHostAVInterfaceStatus_Type.__name__ = "Integer32"
_OcStbHostAVInterfaceStatus_Object = MibTableColumn
ocStbHostAVInterfaceStatus = _OcStbHostAVInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 2, 1, 4),
    _OcStbHostAVInterfaceStatus_Type()
)
ocStbHostAVInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostAVInterfaceStatus.setStatus("current")
_OcStbHostIEEE1394Objects_ObjectIdentity = ObjectIdentity
ocStbHostIEEE1394Objects = _OcStbHostIEEE1394Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3)
)
_OcStbHostIEEE1394Table_Object = MibTable
ocStbHostIEEE1394Table = _OcStbHostIEEE1394Table_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ocStbHostIEEE1394Table.setStatus("current")
_OcStbHostIEEE1394Entry_Object = MibTableRow
ocStbHostIEEE1394Entry = _OcStbHostIEEE1394Entry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1)
)
ocStbHostIEEE1394Entry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostAVInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostIEEE1394Entry.setStatus("current")


class _OcStbHostIEEE1394ActiveNodes_Type(Integer32):
    """Custom type ocStbHostIEEE1394ActiveNodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 64),
    )


_OcStbHostIEEE1394ActiveNodes_Type.__name__ = "Integer32"
_OcStbHostIEEE1394ActiveNodes_Object = MibTableColumn
ocStbHostIEEE1394ActiveNodes = _OcStbHostIEEE1394ActiveNodes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 1),
    _OcStbHostIEEE1394ActiveNodes_Type()
)
ocStbHostIEEE1394ActiveNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ActiveNodes.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ActiveNodes.setUnits("nodes")
_OcStbHostIEEE1394DataXMission_Type = TruthValue
_OcStbHostIEEE1394DataXMission_Object = MibTableColumn
ocStbHostIEEE1394DataXMission = _OcStbHostIEEE1394DataXMission_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 2),
    _OcStbHostIEEE1394DataXMission_Type()
)
ocStbHostIEEE1394DataXMission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394DataXMission.setStatus("current")
_OcStbHostIEEE1394DTCPStatus_Type = TruthValue
_OcStbHostIEEE1394DTCPStatus_Object = MibTableColumn
ocStbHostIEEE1394DTCPStatus = _OcStbHostIEEE1394DTCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 3),
    _OcStbHostIEEE1394DTCPStatus_Type()
)
ocStbHostIEEE1394DTCPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394DTCPStatus.setStatus("current")
_OcStbHostIEEE1394LoopStatus_Type = TruthValue
_OcStbHostIEEE1394LoopStatus_Object = MibTableColumn
ocStbHostIEEE1394LoopStatus = _OcStbHostIEEE1394LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 4),
    _OcStbHostIEEE1394LoopStatus_Type()
)
ocStbHostIEEE1394LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394LoopStatus.setStatus("current")
_OcStbHostIEEE1394RootStatus_Type = TruthValue
_OcStbHostIEEE1394RootStatus_Object = MibTableColumn
ocStbHostIEEE1394RootStatus = _OcStbHostIEEE1394RootStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 5),
    _OcStbHostIEEE1394RootStatus_Type()
)
ocStbHostIEEE1394RootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394RootStatus.setStatus("current")
_OcStbHostIEEE1394CycleIsMaster_Type = TruthValue
_OcStbHostIEEE1394CycleIsMaster_Object = MibTableColumn
ocStbHostIEEE1394CycleIsMaster = _OcStbHostIEEE1394CycleIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 6),
    _OcStbHostIEEE1394CycleIsMaster_Type()
)
ocStbHostIEEE1394CycleIsMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394CycleIsMaster.setStatus("current")
_OcStbHostIEEE1394IRMStatus_Type = TruthValue
_OcStbHostIEEE1394IRMStatus_Object = MibTableColumn
ocStbHostIEEE1394IRMStatus = _OcStbHostIEEE1394IRMStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 7),
    _OcStbHostIEEE1394IRMStatus_Type()
)
ocStbHostIEEE1394IRMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394IRMStatus.setStatus("current")
_OcStbHostIEEE1394AudioMuteStatus_Type = TruthValue
_OcStbHostIEEE1394AudioMuteStatus_Object = MibTableColumn
ocStbHostIEEE1394AudioMuteStatus = _OcStbHostIEEE1394AudioMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 8),
    _OcStbHostIEEE1394AudioMuteStatus_Type()
)
ocStbHostIEEE1394AudioMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394AudioMuteStatus.setStatus("current")
_OcStbHostIEEE1394VideoMuteStatus_Type = TruthValue
_OcStbHostIEEE1394VideoMuteStatus_Object = MibTableColumn
ocStbHostIEEE1394VideoMuteStatus = _OcStbHostIEEE1394VideoMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 1, 1, 9),
    _OcStbHostIEEE1394VideoMuteStatus_Type()
)
ocStbHostIEEE1394VideoMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394VideoMuteStatus.setStatus("current")
_OcStbHostIEEE1394ConnectedDevicesTable_Object = MibTable
ocStbHostIEEE1394ConnectedDevicesTable = _OcStbHostIEEE1394ConnectedDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ConnectedDevicesTable.setStatus("current")
_OcStbHostIEEE1394ConnectedDevicesEntry_Object = MibTableRow
ocStbHostIEEE1394ConnectedDevicesEntry = _OcStbHostIEEE1394ConnectedDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 2, 1)
)
ocStbHostIEEE1394ConnectedDevicesEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostIEEE1394ConnectedDevicesIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ConnectedDevicesEntry.setStatus("current")


class _OcStbHostIEEE1394ConnectedDevicesIndex_Type(Unsigned32):
    """Custom type ocStbHostIEEE1394ConnectedDevicesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcStbHostIEEE1394ConnectedDevicesIndex_Type.__name__ = "Unsigned32"
_OcStbHostIEEE1394ConnectedDevicesIndex_Object = MibTableColumn
ocStbHostIEEE1394ConnectedDevicesIndex = _OcStbHostIEEE1394ConnectedDevicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 2, 1, 1),
    _OcStbHostIEEE1394ConnectedDevicesIndex_Type()
)
ocStbHostIEEE1394ConnectedDevicesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ConnectedDevicesIndex.setStatus("current")


class _OcStbHostIEEE1394ConnectedDevicesAVInterfaceIndex_Type(Unsigned32):
    """Custom type ocStbHostIEEE1394ConnectedDevicesAVInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcStbHostIEEE1394ConnectedDevicesAVInterfaceIndex_Type.__name__ = "Unsigned32"
_OcStbHostIEEE1394ConnectedDevicesAVInterfaceIndex_Object = MibTableColumn
ocStbHostIEEE1394ConnectedDevicesAVInterfaceIndex = _OcStbHostIEEE1394ConnectedDevicesAVInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 2, 1, 2),
    _OcStbHostIEEE1394ConnectedDevicesAVInterfaceIndex_Type()
)
ocStbHostIEEE1394ConnectedDevicesAVInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ConnectedDevicesAVInterfaceIndex.setStatus("current")


class _OcStbHostIEEE1394ConnectedDevicesSubUnitType_Type(Integer32):
    """Custom type ocStbHostIEEE1394ConnectedDevicesSubUnitType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 0),
          ("audio", 1),
          ("printer", 2),
          ("disc", 3),
          ("tape", 4),
          ("tuner", 5),
          ("ca", 6),
          ("camera", 7),
          ("reserved", 8),
          ("panel", 9),
          ("other", 10))
    )


_OcStbHostIEEE1394ConnectedDevicesSubUnitType_Type.__name__ = "Integer32"
_OcStbHostIEEE1394ConnectedDevicesSubUnitType_Object = MibTableColumn
ocStbHostIEEE1394ConnectedDevicesSubUnitType = _OcStbHostIEEE1394ConnectedDevicesSubUnitType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 2, 1, 3),
    _OcStbHostIEEE1394ConnectedDevicesSubUnitType_Type()
)
ocStbHostIEEE1394ConnectedDevicesSubUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ConnectedDevicesSubUnitType.setStatus("current")


class _OcStbHostIEEE1394ConnectedDevicesEui64_Type(OctetString):
    """Custom type ocStbHostIEEE1394ConnectedDevicesEui64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_OcStbHostIEEE1394ConnectedDevicesEui64_Type.__name__ = "OctetString"
_OcStbHostIEEE1394ConnectedDevicesEui64_Object = MibTableColumn
ocStbHostIEEE1394ConnectedDevicesEui64 = _OcStbHostIEEE1394ConnectedDevicesEui64_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 2, 1, 4),
    _OcStbHostIEEE1394ConnectedDevicesEui64_Type()
)
ocStbHostIEEE1394ConnectedDevicesEui64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ConnectedDevicesEui64.setStatus("current")
_OcStbHostIEEE1394ConnectedDevicesADSourceSelectSupport_Type = TruthValue
_OcStbHostIEEE1394ConnectedDevicesADSourceSelectSupport_Object = MibTableColumn
ocStbHostIEEE1394ConnectedDevicesADSourceSelectSupport = _OcStbHostIEEE1394ConnectedDevicesADSourceSelectSupport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 3, 2, 1, 5),
    _OcStbHostIEEE1394ConnectedDevicesADSourceSelectSupport_Type()
)
ocStbHostIEEE1394ConnectedDevicesADSourceSelectSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIEEE1394ConnectedDevicesADSourceSelectSupport.setStatus("current")
_OcStbHostDigitalVideoOutput_ObjectIdentity = ObjectIdentity
ocStbHostDigitalVideoOutput = _OcStbHostDigitalVideoOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4)
)
_OcStbHostDVIHDMITable_Object = MibTable
ocStbHostDVIHDMITable = _OcStbHostDVIHDMITable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ocStbHostDVIHDMITable.setStatus("current")
_OcStbHostDVIHDMIEntry_Object = MibTableRow
ocStbHostDVIHDMIEntry = _OcStbHostDVIHDMIEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1)
)
ocStbHostDVIHDMIEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostAVInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIEntry.setStatus("current")


class _OcStbHostDVIHDMIOutputType_Type(Integer32):
    """Custom type ocStbHostDVIHDMIOutputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dvi", 1),
          ("hdmi", 2))
    )


_OcStbHostDVIHDMIOutputType_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIOutputType_Object = MibTableColumn
ocStbHostDVIHDMIOutputType = _OcStbHostDVIHDMIOutputType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 2),
    _OcStbHostDVIHDMIOutputType_Type()
)
ocStbHostDVIHDMIOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIOutputType.setStatus("current")
_OcStbHostDVIHDMIConnectionStatus_Type = TruthValue
_OcStbHostDVIHDMIConnectionStatus_Object = MibTableColumn
ocStbHostDVIHDMIConnectionStatus = _OcStbHostDVIHDMIConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 3),
    _OcStbHostDVIHDMIConnectionStatus_Type()
)
ocStbHostDVIHDMIConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIConnectionStatus.setStatus("current")
_OcStbHostDVIHDMIRepeaterStatus_Type = TruthValue
_OcStbHostDVIHDMIRepeaterStatus_Object = MibTableColumn
ocStbHostDVIHDMIRepeaterStatus = _OcStbHostDVIHDMIRepeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 4),
    _OcStbHostDVIHDMIRepeaterStatus_Type()
)
ocStbHostDVIHDMIRepeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIRepeaterStatus.setStatus("current")
_OcStbHostDVIHDMIVideoXmissionStatus_Type = TruthValue
_OcStbHostDVIHDMIVideoXmissionStatus_Object = MibTableColumn
ocStbHostDVIHDMIVideoXmissionStatus = _OcStbHostDVIHDMIVideoXmissionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 5),
    _OcStbHostDVIHDMIVideoXmissionStatus_Type()
)
ocStbHostDVIHDMIVideoXmissionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIVideoXmissionStatus.setStatus("current")
_OcStbHostDVIHDMIHDCPStatus_Type = TruthValue
_OcStbHostDVIHDMIHDCPStatus_Object = MibTableColumn
ocStbHostDVIHDMIHDCPStatus = _OcStbHostDVIHDMIHDCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 6),
    _OcStbHostDVIHDMIHDCPStatus_Type()
)
ocStbHostDVIHDMIHDCPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIHDCPStatus.setStatus("current")
_OcStbHostDVIHDMIVideoMuteStatus_Type = TruthValue
_OcStbHostDVIHDMIVideoMuteStatus_Object = MibTableColumn
ocStbHostDVIHDMIVideoMuteStatus = _OcStbHostDVIHDMIVideoMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 7),
    _OcStbHostDVIHDMIVideoMuteStatus_Type()
)
ocStbHostDVIHDMIVideoMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIVideoMuteStatus.setStatus("current")
_OcStbHostDVIHDMIOutputFormat_Type = VideoOutputFormat
_OcStbHostDVIHDMIOutputFormat_Object = MibTableColumn
ocStbHostDVIHDMIOutputFormat = _OcStbHostDVIHDMIOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 8),
    _OcStbHostDVIHDMIOutputFormat_Type()
)
ocStbHostDVIHDMIOutputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIOutputFormat.setStatus("current")
_OcStbHostDVIHDMIAspectRatio_Type = VideoAspectRatio
_OcStbHostDVIHDMIAspectRatio_Object = MibTableColumn
ocStbHostDVIHDMIAspectRatio = _OcStbHostDVIHDMIAspectRatio_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 9),
    _OcStbHostDVIHDMIAspectRatio_Type()
)
ocStbHostDVIHDMIAspectRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAspectRatio.setStatus("current")


class _OcStbHostDVIHDMIHostDeviceHDCPStatus_Type(Integer32):
    """Custom type ocStbHostDVIHDMIHostDeviceHDCPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonHDCPdevice", 1),
          ("compliantHDCPdevice", 2),
          ("revokedHDCPdevice", 3))
    )


_OcStbHostDVIHDMIHostDeviceHDCPStatus_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIHostDeviceHDCPStatus_Object = MibTableColumn
ocStbHostDVIHDMIHostDeviceHDCPStatus = _OcStbHostDVIHDMIHostDeviceHDCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 10),
    _OcStbHostDVIHDMIHostDeviceHDCPStatus_Type()
)
ocStbHostDVIHDMIHostDeviceHDCPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIHostDeviceHDCPStatus.setStatus("current")
_OcStbHostDVIHDMIAudioFormat_Type = AudioOutputFormat
_OcStbHostDVIHDMIAudioFormat_Object = MibTableColumn
ocStbHostDVIHDMIAudioFormat = _OcStbHostDVIHDMIAudioFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 11),
    _OcStbHostDVIHDMIAudioFormat_Type()
)
ocStbHostDVIHDMIAudioFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAudioFormat.setStatus("current")


class _OcStbHostDVIHDMIAudioSampleRate_Type(Integer32):
    """Custom type ocStbHostDVIHDMIAudioSampleRate based on Integer32"""
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
        *(("other", 1),
          ("samplerate32kHz", 2),
          ("samplerate44kHz", 3),
          ("samplerate48kHz", 4),
          ("samplerate88kHz", 5),
          ("samplerate96kHz", 6),
          ("samplerate176kHz", 7),
          ("samplerate192kHz", 8))
    )


_OcStbHostDVIHDMIAudioSampleRate_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIAudioSampleRate_Object = MibTableColumn
ocStbHostDVIHDMIAudioSampleRate = _OcStbHostDVIHDMIAudioSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 12),
    _OcStbHostDVIHDMIAudioSampleRate_Type()
)
ocStbHostDVIHDMIAudioSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAudioSampleRate.setStatus("current")


class _OcStbHostDVIHDMIAudioChannelCount_Type(Unsigned32):
    """Custom type ocStbHostDVIHDMIAudioChannelCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_OcStbHostDVIHDMIAudioChannelCount_Type.__name__ = "Unsigned32"
_OcStbHostDVIHDMIAudioChannelCount_Object = MibTableColumn
ocStbHostDVIHDMIAudioChannelCount = _OcStbHostDVIHDMIAudioChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 13),
    _OcStbHostDVIHDMIAudioChannelCount_Type()
)
ocStbHostDVIHDMIAudioChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAudioChannelCount.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAudioChannelCount.setUnits("channels")
_OcStbHostDVIHDMIAudioMuteStatus_Type = TruthValue
_OcStbHostDVIHDMIAudioMuteStatus_Object = MibTableColumn
ocStbHostDVIHDMIAudioMuteStatus = _OcStbHostDVIHDMIAudioMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 14),
    _OcStbHostDVIHDMIAudioMuteStatus_Type()
)
ocStbHostDVIHDMIAudioMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAudioMuteStatus.setStatus("current")


class _OcStbHostDVIHDMIAudioSampleSize_Type(Integer32):
    """Custom type ocStbHostDVIHDMIAudioSampleSize based on Integer32"""
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
        *(("notValid", 0),
          ("sample16Bit", 1),
          ("sample20Bit", 2),
          ("sample24Bit", 3))
    )


_OcStbHostDVIHDMIAudioSampleSize_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIAudioSampleSize_Object = MibTableColumn
ocStbHostDVIHDMIAudioSampleSize = _OcStbHostDVIHDMIAudioSampleSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 15),
    _OcStbHostDVIHDMIAudioSampleSize_Type()
)
ocStbHostDVIHDMIAudioSampleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAudioSampleSize.setStatus("current")


class _OcStbHostDVIHDMIColorSpace_Type(Integer32):
    """Custom type ocStbHostDVIHDMIColorSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rgb", 0),
          ("ycc422", 1),
          ("ycc444", 2))
    )


_OcStbHostDVIHDMIColorSpace_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIColorSpace_Object = MibTableColumn
ocStbHostDVIHDMIColorSpace = _OcStbHostDVIHDMIColorSpace_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 16),
    _OcStbHostDVIHDMIColorSpace_Type()
)
ocStbHostDVIHDMIColorSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIColorSpace.setStatus("current")


class _OcStbHostDVIHDMIFrameRate_Type(Integer32):
    """Custom type ocStbHostDVIHDMIFrameRate based on Integer32"""
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
        *(("frameRateCode1", 1),
          ("frameRateCode2", 2),
          ("frameRateCode3", 3),
          ("frameRateCode4", 4),
          ("frameRateCode5", 5),
          ("frameRateCode6", 6))
    )


_OcStbHostDVIHDMIFrameRate_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIFrameRate_Object = MibTableColumn
ocStbHostDVIHDMIFrameRate = _OcStbHostDVIHDMIFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 17),
    _OcStbHostDVIHDMIFrameRate_Type()
)
ocStbHostDVIHDMIFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIFrameRate.setStatus("current")


class _OcStbHostDVIHDMIAttachedDeviceType_Type(Integer32):
    """Custom type ocStbHostDVIHDMIAttachedDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tv", 0),
          ("recordingDevice", 1),
          ("tuner", 3),
          ("playbackDevice", 4),
          ("audioSystem", 5),
          ("other", 6))
    )


_OcStbHostDVIHDMIAttachedDeviceType_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIAttachedDeviceType_Object = MibTableColumn
ocStbHostDVIHDMIAttachedDeviceType = _OcStbHostDVIHDMIAttachedDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 18),
    _OcStbHostDVIHDMIAttachedDeviceType_Type()
)
ocStbHostDVIHDMIAttachedDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAttachedDeviceType.setStatus("current")
_OcStbHostDVIHDMIEdid_Type = OctetString
_OcStbHostDVIHDMIEdid_Object = MibTableColumn
ocStbHostDVIHDMIEdid = _OcStbHostDVIHDMIEdid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 19),
    _OcStbHostDVIHDMIEdid_Type()
)
ocStbHostDVIHDMIEdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIEdid.setStatus("current")
_OcStbHostDVIHDMILipSyncDelay_Type = Integer32
_OcStbHostDVIHDMILipSyncDelay_Object = MibTableColumn
ocStbHostDVIHDMILipSyncDelay = _OcStbHostDVIHDMILipSyncDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 20),
    _OcStbHostDVIHDMILipSyncDelay_Type()
)
ocStbHostDVIHDMILipSyncDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMILipSyncDelay.setStatus("current")


class _OcStbHostDVIHDMICecFeatures_Type(Bits):
    """Custom type ocStbHostDVIHDMICecFeatures based on Bits"""
    namedValues = NamedValues(
        *(("oneTouchPlay", 0),
          ("systemStandby", 1),
          ("oneTouchRecord", 2),
          ("timerProgramming", 3),
          ("deckControl", 4),
          ("tunerControl", 5),
          ("deviceMenuControl", 6),
          ("remoteControlPassThrough", 7),
          ("systemAudioControl", 8),
          ("deviceOsdNameTransfer", 9),
          ("devicePowerStatus", 10),
          ("osdDisplay", 11),
          ("routingControl", 12),
          ("systemInformation", 13),
          ("vendorSpecificCommands", 14),
          ("audioRateControl", 15))
    )

_OcStbHostDVIHDMICecFeatures_Type.__name__ = "Bits"
_OcStbHostDVIHDMICecFeatures_Object = MibTableColumn
ocStbHostDVIHDMICecFeatures = _OcStbHostDVIHDMICecFeatures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 21),
    _OcStbHostDVIHDMICecFeatures_Type()
)
ocStbHostDVIHDMICecFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMICecFeatures.setStatus("current")


class _OcStbHostDVIHDMIFeatures_Type(Bits):
    """Custom type ocStbHostDVIHDMIFeatures based on Bits"""
    namedValues = NamedValues(
        *(("deepColor", 0),
          ("extendedColorGamut", 1),
          ("oneBitAudio", 2),
          ("lipSync", 3),
          ("cec", 4))
    )

_OcStbHostDVIHDMIFeatures_Type.__name__ = "Bits"
_OcStbHostDVIHDMIFeatures_Object = MibTableColumn
ocStbHostDVIHDMIFeatures = _OcStbHostDVIHDMIFeatures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 22),
    _OcStbHostDVIHDMIFeatures_Type()
)
ocStbHostDVIHDMIFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIFeatures.setStatus("current")
_OcStbHostDVIHDMIMaxDeviceCount_Type = Integer32
_OcStbHostDVIHDMIMaxDeviceCount_Object = MibTableColumn
ocStbHostDVIHDMIMaxDeviceCount = _OcStbHostDVIHDMIMaxDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 23),
    _OcStbHostDVIHDMIMaxDeviceCount_Type()
)
ocStbHostDVIHDMIMaxDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIMaxDeviceCount.setStatus("current")


class _OcStbHostDVIHDMIPreferredVideoFormat_Type(Integer32):
    """Custom type ocStbHostDVIHDMIPreferredVideoFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_OcStbHostDVIHDMIPreferredVideoFormat_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIPreferredVideoFormat_Object = MibTableColumn
ocStbHostDVIHDMIPreferredVideoFormat = _OcStbHostDVIHDMIPreferredVideoFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 24),
    _OcStbHostDVIHDMIPreferredVideoFormat_Type()
)
ocStbHostDVIHDMIPreferredVideoFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIPreferredVideoFormat.setStatus("current")
_OcStbHostDVIHDMIEdidVersion_Type = SnmpAdminString
_OcStbHostDVIHDMIEdidVersion_Object = MibTableColumn
ocStbHostDVIHDMIEdidVersion = _OcStbHostDVIHDMIEdidVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 25),
    _OcStbHostDVIHDMIEdidVersion_Type()
)
ocStbHostDVIHDMIEdidVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIEdidVersion.setStatus("current")


class _OcStbHostDVIHDMI3DCompatibilityControl_Type(Integer32):
    """Custom type ocStbHostDVIHDMI3DCompatibilityControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("passthru3D", 1),
          ("block3D", 2))
    )


_OcStbHostDVIHDMI3DCompatibilityControl_Type.__name__ = "Integer32"
_OcStbHostDVIHDMI3DCompatibilityControl_Object = MibTableColumn
ocStbHostDVIHDMI3DCompatibilityControl = _OcStbHostDVIHDMI3DCompatibilityControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 26),
    _OcStbHostDVIHDMI3DCompatibilityControl_Type()
)
ocStbHostDVIHDMI3DCompatibilityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMI3DCompatibilityControl.setStatus("current")


class _OcStbHostDVIHDMI3DCompatibilityMsgDisplay_Type(TruthValue):
    """Custom type ocStbHostDVIHDMI3DCompatibilityMsgDisplay based on TruthValue"""
    defaultValue = 1


_OcStbHostDVIHDMI3DCompatibilityMsgDisplay_Type.__name__ = "TruthValue"
_OcStbHostDVIHDMI3DCompatibilityMsgDisplay_Object = MibTableColumn
ocStbHostDVIHDMI3DCompatibilityMsgDisplay = _OcStbHostDVIHDMI3DCompatibilityMsgDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 1, 1, 27),
    _OcStbHostDVIHDMI3DCompatibilityMsgDisplay_Type()
)
ocStbHostDVIHDMI3DCompatibilityMsgDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMI3DCompatibilityMsgDisplay.setStatus("current")
_OcStbHostDVIHDMIAvailableVideoFormatTable_Object = MibTable
ocStbHostDVIHDMIAvailableVideoFormatTable = _OcStbHostDVIHDMIAvailableVideoFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAvailableVideoFormatTable.setStatus("current")
_OcStbHostDVIHDMIAvailableVideoFormatEntry_Object = MibTableRow
ocStbHostDVIHDMIAvailableVideoFormatEntry = _OcStbHostDVIHDMIAvailableVideoFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 2, 1)
)
ocStbHostDVIHDMIAvailableVideoFormatEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostDVIHDMIAvailableVideoFormatIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAvailableVideoFormatEntry.setStatus("current")


class _OcStbHostDVIHDMIAvailableVideoFormatIndex_Type(Integer32):
    """Custom type ocStbHostDVIHDMIAvailableVideoFormatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_OcStbHostDVIHDMIAvailableVideoFormatIndex_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIAvailableVideoFormatIndex_Object = MibTableColumn
ocStbHostDVIHDMIAvailableVideoFormatIndex = _OcStbHostDVIHDMIAvailableVideoFormatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 2, 1, 1),
    _OcStbHostDVIHDMIAvailableVideoFormatIndex_Type()
)
ocStbHostDVIHDMIAvailableVideoFormatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAvailableVideoFormatIndex.setStatus("current")


class _OcStbHostDVIHDMIAvailableVideoFormat_Type(Integer32):
    """Custom type ocStbHostDVIHDMIAvailableVideoFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_OcStbHostDVIHDMIAvailableVideoFormat_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIAvailableVideoFormat_Object = MibTableColumn
ocStbHostDVIHDMIAvailableVideoFormat = _OcStbHostDVIHDMIAvailableVideoFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 2, 1, 2),
    _OcStbHostDVIHDMIAvailableVideoFormat_Type()
)
ocStbHostDVIHDMIAvailableVideoFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIAvailableVideoFormat.setStatus("current")


class _OcStbHostDVIHDMISupported3DStructures_Type(Bits):
    """Custom type ocStbHostDVIHDMISupported3DStructures based on Bits"""
    namedValues = NamedValues(
        *(("framePacking", 0),
          ("fieldAlternative", 1),
          ("lineAlternative", 2),
          ("sideBySideFull", 3),
          ("leftPlusDepth", 4),
          ("leftPlusDepthPlusGraphicsPlusGraphicsDepth", 5),
          ("topAndBottom", 6),
          ("sideBySideHalf", 7),
          ("sideBySideHalfQuincunx", 8))
    )

_OcStbHostDVIHDMISupported3DStructures_Type.__name__ = "Bits"
_OcStbHostDVIHDMISupported3DStructures_Object = MibTableColumn
ocStbHostDVIHDMISupported3DStructures = _OcStbHostDVIHDMISupported3DStructures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 2, 1, 3),
    _OcStbHostDVIHDMISupported3DStructures_Type()
)
ocStbHostDVIHDMISupported3DStructures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMISupported3DStructures.setStatus("current")


class _OcStbHostDVIHDMIActive3DStructure_Type(Integer32):
    """Custom type ocStbHostDVIHDMIActive3DStructure based on Integer32"""
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
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("na", 1),
          ("framePacking", 2),
          ("fieldAlternative", 3),
          ("lineAlternative", 4),
          ("sideBySideFull", 5),
          ("leftPlusDepth", 6),
          ("leftPlusDepthPlusGraphicsPlusGraphicsDepth", 7),
          ("topAndBottom", 8),
          ("sideBySideHalf", 9),
          ("sideBySideHalfQuincunx", 10),
          ("noAdditionalHDMIInfo", 17),
          ("no3DInformation", 18),
          ("infoFrameNotAvailable", 19))
    )


_OcStbHostDVIHDMIActive3DStructure_Type.__name__ = "Integer32"
_OcStbHostDVIHDMIActive3DStructure_Object = MibTableColumn
ocStbHostDVIHDMIActive3DStructure = _OcStbHostDVIHDMIActive3DStructure_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 4, 2, 1, 4),
    _OcStbHostDVIHDMIActive3DStructure_Type()
)
ocStbHostDVIHDMIActive3DStructure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDVIHDMIActive3DStructure.setStatus("current")
_OcStbHostAnalogOutput_ObjectIdentity = ObjectIdentity
ocStbHostAnalogOutput = _OcStbHostAnalogOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5)
)
_OcStbHostComponentVideoTable_Object = MibTable
ocStbHostComponentVideoTable = _OcStbHostComponentVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ocStbHostComponentVideoTable.setStatus("current")
_OcStbHostComponentVideoEntry_Object = MibTableRow
ocStbHostComponentVideoEntry = _OcStbHostComponentVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 1, 1)
)
ocStbHostComponentVideoEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostAVInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostComponentVideoEntry.setStatus("current")
_OcStbHostComponentVideoConstrainedStatus_Type = TruthValue
_OcStbHostComponentVideoConstrainedStatus_Object = MibTableColumn
ocStbHostComponentVideoConstrainedStatus = _OcStbHostComponentVideoConstrainedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 1, 1, 1),
    _OcStbHostComponentVideoConstrainedStatus_Type()
)
ocStbHostComponentVideoConstrainedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostComponentVideoConstrainedStatus.setStatus("current")
_OcStbHostComponentOutputFormat_Type = VideoOutputFormat
_OcStbHostComponentOutputFormat_Object = MibTableColumn
ocStbHostComponentOutputFormat = _OcStbHostComponentOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 1, 1, 2),
    _OcStbHostComponentOutputFormat_Type()
)
ocStbHostComponentOutputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostComponentOutputFormat.setStatus("current")
_OcStbHostComponentAspectRatio_Type = VideoAspectRatio
_OcStbHostComponentAspectRatio_Object = MibTableColumn
ocStbHostComponentAspectRatio = _OcStbHostComponentAspectRatio_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 1, 1, 3),
    _OcStbHostComponentAspectRatio_Type()
)
ocStbHostComponentAspectRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostComponentAspectRatio.setStatus("current")
_OcStbHostComponentVideoMuteStatus_Type = TruthValue
_OcStbHostComponentVideoMuteStatus_Object = MibTableColumn
ocStbHostComponentVideoMuteStatus = _OcStbHostComponentVideoMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 1, 1, 4),
    _OcStbHostComponentVideoMuteStatus_Type()
)
ocStbHostComponentVideoMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostComponentVideoMuteStatus.setStatus("current")
_OcStbHostRFChannelOutTable_Object = MibTable
ocStbHostRFChannelOutTable = _OcStbHostRFChannelOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ocStbHostRFChannelOutTable.setStatus("current")
_OcStbHostRFChannelOutEntry_Object = MibTableRow
ocStbHostRFChannelOutEntry = _OcStbHostRFChannelOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 2, 1)
)
ocStbHostRFChannelOutEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostAVInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostRFChannelOutEntry.setStatus("current")


class _OcStbHostRFChannelOut_Type(Unsigned32):
    """Custom type ocStbHostRFChannelOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 99),
    )


_OcStbHostRFChannelOut_Type.__name__ = "Unsigned32"
_OcStbHostRFChannelOut_Object = MibTableColumn
ocStbHostRFChannelOut = _OcStbHostRFChannelOut_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 2, 1, 2),
    _OcStbHostRFChannelOut_Type()
)
ocStbHostRFChannelOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostRFChannelOut.setStatus("current")
_OcStbHostRFChannelOutAudioMuteStatus_Type = TruthValue
_OcStbHostRFChannelOutAudioMuteStatus_Object = MibTableColumn
ocStbHostRFChannelOutAudioMuteStatus = _OcStbHostRFChannelOutAudioMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 2, 1, 3),
    _OcStbHostRFChannelOutAudioMuteStatus_Type()
)
ocStbHostRFChannelOutAudioMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostRFChannelOutAudioMuteStatus.setStatus("current")
_OcStbHostRFChannelOutVideoMuteStatus_Type = TruthValue
_OcStbHostRFChannelOutVideoMuteStatus_Object = MibTableColumn
ocStbHostRFChannelOutVideoMuteStatus = _OcStbHostRFChannelOutVideoMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 5, 2, 1, 4),
    _OcStbHostRFChannelOutVideoMuteStatus_Type()
)
ocStbHostRFChannelOutVideoMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostRFChannelOutVideoMuteStatus.setStatus("current")
_OcStbHostSPDIfTable_Object = MibTable
ocStbHostSPDIfTable = _OcStbHostSPDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ocStbHostSPDIfTable.setStatus("current")
_OcStbHostSPDIfEntry_Object = MibTableRow
ocStbHostSPDIfEntry = _OcStbHostSPDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 6, 1)
)
ocStbHostSPDIfEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostAVInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostSPDIfEntry.setStatus("current")
_OcStbHostSPDIfAudioFormat_Type = AudioOutputFormat
_OcStbHostSPDIfAudioFormat_Object = MibTableColumn
ocStbHostSPDIfAudioFormat = _OcStbHostSPDIfAudioFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 6, 1, 1),
    _OcStbHostSPDIfAudioFormat_Type()
)
ocStbHostSPDIfAudioFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSPDIfAudioFormat.setStatus("current")
_OcStbHostSPDIfAudioMuteStatus_Type = TruthValue
_OcStbHostSPDIfAudioMuteStatus_Object = MibTableColumn
ocStbHostSPDIfAudioMuteStatus = _OcStbHostSPDIfAudioMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 6, 1, 2),
    _OcStbHostSPDIfAudioMuteStatus_Type()
)
ocStbHostSPDIfAudioMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSPDIfAudioMuteStatus.setStatus("current")
_OcStbHostServiceProgramInfo_ObjectIdentity = ObjectIdentity
ocStbHostServiceProgramInfo = _OcStbHostServiceProgramInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7)
)
_OcStbHostInBandTunerTable_Object = MibTable
ocStbHostInBandTunerTable = _OcStbHostInBandTunerTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ocStbHostInBandTunerTable.setStatus("current")
_OcStbHostInBandTunerEntry_Object = MibTableRow
ocStbHostInBandTunerEntry = _OcStbHostInBandTunerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1)
)
ocStbHostInBandTunerEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostAVInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostInBandTunerEntry.setStatus("current")


class _OcStbHostInBandTunerModulationMode_Type(Integer32):
    """Custom type ocStbHostInBandTunerModulationMode based on Integer32"""
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
        *(("other", 1),
          ("analog", 2),
          ("qam64", 3),
          ("qam256", 4))
    )


_OcStbHostInBandTunerModulationMode_Type.__name__ = "Integer32"
_OcStbHostInBandTunerModulationMode_Object = MibTableColumn
ocStbHostInBandTunerModulationMode = _OcStbHostInBandTunerModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 1),
    _OcStbHostInBandTunerModulationMode_Type()
)
ocStbHostInBandTunerModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerModulationMode.setStatus("current")
_OcStbHostInBandTunerFrequency_Type = Unsigned32
_OcStbHostInBandTunerFrequency_Object = MibTableColumn
ocStbHostInBandTunerFrequency = _OcStbHostInBandTunerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 2),
    _OcStbHostInBandTunerFrequency_Type()
)
ocStbHostInBandTunerFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerFrequency.setUnits("hertz")


class _OcStbHostInBandTunerInterleaver_Type(Integer32):
    """Custom type ocStbHostInBandTunerInterleaver based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("taps64Increment2", 3),
          ("taps128Increment1", 4),
          ("taps128increment2", 5),
          ("taps128increment3", 6),
          ("taps128increment4", 7),
          ("taps32increment4", 8),
          ("taps16increment8", 9),
          ("taps8increment16", 10))
    )


_OcStbHostInBandTunerInterleaver_Type.__name__ = "Integer32"
_OcStbHostInBandTunerInterleaver_Object = MibTableColumn
ocStbHostInBandTunerInterleaver = _OcStbHostInBandTunerInterleaver_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 3),
    _OcStbHostInBandTunerInterleaver_Type()
)
ocStbHostInBandTunerInterleaver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerInterleaver.setStatus("current")
_OcStbHostInBandTunerPower_Type = TenthdBmV
_OcStbHostInBandTunerPower_Object = MibTableColumn
ocStbHostInBandTunerPower = _OcStbHostInBandTunerPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 4),
    _OcStbHostInBandTunerPower_Type()
)
ocStbHostInBandTunerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerPower.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerPower.setUnits("dBmV")


class _OcStbHostInBandTunerAGCValue_Type(Unsigned32):
    """Custom type ocStbHostInBandTunerAGCValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OcStbHostInBandTunerAGCValue_Type.__name__ = "Unsigned32"
_OcStbHostInBandTunerAGCValue_Object = MibTableColumn
ocStbHostInBandTunerAGCValue = _OcStbHostInBandTunerAGCValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 5),
    _OcStbHostInBandTunerAGCValue_Type()
)
ocStbHostInBandTunerAGCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerAGCValue.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerAGCValue.setUnits("percentage")
_OcStbHostInBandTunerSNRValue_Type = TenthdB
_OcStbHostInBandTunerSNRValue_Object = MibTableColumn
ocStbHostInBandTunerSNRValue = _OcStbHostInBandTunerSNRValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 6),
    _OcStbHostInBandTunerSNRValue_Type()
)
ocStbHostInBandTunerSNRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerSNRValue.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerSNRValue.setUnits("dB")
_OcStbHostInBandTunerUnerroreds_Type = Counter32
_OcStbHostInBandTunerUnerroreds_Object = MibTableColumn
ocStbHostInBandTunerUnerroreds = _OcStbHostInBandTunerUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 7),
    _OcStbHostInBandTunerUnerroreds_Type()
)
ocStbHostInBandTunerUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerUnerroreds.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerUnerroreds.setUnits("codewords")
_OcStbHostInBandTunerCorrecteds_Type = Counter32
_OcStbHostInBandTunerCorrecteds_Object = MibTableColumn
ocStbHostInBandTunerCorrecteds = _OcStbHostInBandTunerCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 8),
    _OcStbHostInBandTunerCorrecteds_Type()
)
ocStbHostInBandTunerCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerCorrecteds.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerCorrecteds.setUnits("codewords")
_OcStbHostInBandTunerUncorrectables_Type = Counter32
_OcStbHostInBandTunerUncorrectables_Object = MibTableColumn
ocStbHostInBandTunerUncorrectables = _OcStbHostInBandTunerUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 9),
    _OcStbHostInBandTunerUncorrectables_Type()
)
ocStbHostInBandTunerUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerUncorrectables.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerUncorrectables.setUnits("codewords")
_OcStbHostInBandTunerCarrierLockLost_Type = Counter32
_OcStbHostInBandTunerCarrierLockLost_Object = MibTableColumn
ocStbHostInBandTunerCarrierLockLost = _OcStbHostInBandTunerCarrierLockLost_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 10),
    _OcStbHostInBandTunerCarrierLockLost_Type()
)
ocStbHostInBandTunerCarrierLockLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerCarrierLockLost.setStatus("current")
_OcStbHostInBandTunerPCRErrors_Type = Counter32
_OcStbHostInBandTunerPCRErrors_Object = MibTableColumn
ocStbHostInBandTunerPCRErrors = _OcStbHostInBandTunerPCRErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 11),
    _OcStbHostInBandTunerPCRErrors_Type()
)
ocStbHostInBandTunerPCRErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerPCRErrors.setStatus("current")
_OcStbHostInBandTunerPTSErrors_Type = Counter32
_OcStbHostInBandTunerPTSErrors_Object = MibTableColumn
ocStbHostInBandTunerPTSErrors = _OcStbHostInBandTunerPTSErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 12),
    _OcStbHostInBandTunerPTSErrors_Type()
)
ocStbHostInBandTunerPTSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerPTSErrors.setStatus("current")


class _OcStbHostInBandTunerState_Type(Integer32):
    """Custom type ocStbHostInBandTunerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("waitingSync", 2),
          ("waitingQam", 3),
          ("foundSync", 4),
          ("foundQam", 5),
          ("unknown", 6),
          ("standby", 7))
    )


_OcStbHostInBandTunerState_Type.__name__ = "Integer32"
_OcStbHostInBandTunerState_Object = MibTableColumn
ocStbHostInBandTunerState = _OcStbHostInBandTunerState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 13),
    _OcStbHostInBandTunerState_Type()
)
ocStbHostInBandTunerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerState.setStatus("current")


class _OcStbHostInBandTunerBER_Type(Integer32):
    """Custom type ocStbHostInBandTunerBER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("berGreaterThan10e2", 1),
          ("berRange10e2ToGreaterThan10e4", 2),
          ("berRange10e4ToGreaterThan10e6", 3),
          ("berRange10e6ToGreaterThan10e8", 4),
          ("berRange10e8ToGreaterThan10e12", 5),
          ("berEqualToOrLessThan10e12", 6),
          ("berNotApplicable", 7))
    )


_OcStbHostInBandTunerBER_Type.__name__ = "Integer32"
_OcStbHostInBandTunerBER_Object = MibTableColumn
ocStbHostInBandTunerBER = _OcStbHostInBandTunerBER_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 14),
    _OcStbHostInBandTunerBER_Type()
)
ocStbHostInBandTunerBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerBER.setStatus("current")
_OcStbHostInBandTunerSecsSinceLock_Type = Unsigned32
_OcStbHostInBandTunerSecsSinceLock_Object = MibTableColumn
ocStbHostInBandTunerSecsSinceLock = _OcStbHostInBandTunerSecsSinceLock_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 15),
    _OcStbHostInBandTunerSecsSinceLock_Type()
)
ocStbHostInBandTunerSecsSinceLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerSecsSinceLock.setStatus("current")
_OcStbHostInBandTunerEqGain_Type = Integer32
_OcStbHostInBandTunerEqGain_Object = MibTableColumn
ocStbHostInBandTunerEqGain = _OcStbHostInBandTunerEqGain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 16),
    _OcStbHostInBandTunerEqGain_Type()
)
ocStbHostInBandTunerEqGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerEqGain.setStatus("current")


class _OcStbHostInBandTunerMainTapCoeff_Type(Integer32):
    """Custom type ocStbHostInBandTunerMainTapCoeff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_OcStbHostInBandTunerMainTapCoeff_Type.__name__ = "Integer32"
_OcStbHostInBandTunerMainTapCoeff_Object = MibTableColumn
ocStbHostInBandTunerMainTapCoeff = _OcStbHostInBandTunerMainTapCoeff_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 17),
    _OcStbHostInBandTunerMainTapCoeff_Type()
)
ocStbHostInBandTunerMainTapCoeff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerMainTapCoeff.setStatus("current")
_OcStbHostInBandTunerTotalTuneCount_Type = Counter32
_OcStbHostInBandTunerTotalTuneCount_Object = MibTableColumn
ocStbHostInBandTunerTotalTuneCount = _OcStbHostInBandTunerTotalTuneCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 18),
    _OcStbHostInBandTunerTotalTuneCount_Type()
)
ocStbHostInBandTunerTotalTuneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerTotalTuneCount.setStatus("current")
_OcStbHostInBandTunerTuneFailureCount_Type = Counter32
_OcStbHostInBandTunerTuneFailureCount_Object = MibTableColumn
ocStbHostInBandTunerTuneFailureCount = _OcStbHostInBandTunerTuneFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 19),
    _OcStbHostInBandTunerTuneFailureCount_Type()
)
ocStbHostInBandTunerTuneFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerTuneFailureCount.setStatus("current")
_OcStbHostInBandTunerTuneFailFreq_Type = Unsigned32
_OcStbHostInBandTunerTuneFailFreq_Object = MibTableColumn
ocStbHostInBandTunerTuneFailFreq = _OcStbHostInBandTunerTuneFailFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 20),
    _OcStbHostInBandTunerTuneFailFreq_Type()
)
ocStbHostInBandTunerTuneFailFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerTuneFailFreq.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerTuneFailFreq.setUnits("hertz")


class _OcStbHostInBandTunerBandwidth_Type(Integer32):
    """Custom type ocStbHostInBandTunerBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("mHz864", 2),
          ("mHz1002", 3))
    )


_OcStbHostInBandTunerBandwidth_Type.__name__ = "Integer32"
_OcStbHostInBandTunerBandwidth_Object = MibTableColumn
ocStbHostInBandTunerBandwidth = _OcStbHostInBandTunerBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 1, 1, 21),
    _OcStbHostInBandTunerBandwidth_Type()
)
ocStbHostInBandTunerBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostInBandTunerBandwidth.setStatus("current")
_OcStbHostProgramStatusTable_Object = MibTable
ocStbHostProgramStatusTable = _OcStbHostProgramStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    ocStbHostProgramStatusTable.setStatus("current")
_OcStbHostProgramStatusEntry_Object = MibTableRow
ocStbHostProgramStatusEntry = _OcStbHostProgramStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 2, 1)
)
ocStbHostProgramStatusEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostProgramIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostProgramStatusEntry.setStatus("current")


class _OcStbHostProgramIndex_Type(Unsigned32):
    """Custom type ocStbHostProgramIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OcStbHostProgramIndex_Type.__name__ = "Unsigned32"
_OcStbHostProgramIndex_Object = MibTableColumn
ocStbHostProgramIndex = _OcStbHostProgramIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 2, 1, 1),
    _OcStbHostProgramIndex_Type()
)
ocStbHostProgramIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostProgramIndex.setStatus("current")
_OcStbHostProgramAVSource_Type = RowPointer
_OcStbHostProgramAVSource_Object = MibTableColumn
ocStbHostProgramAVSource = _OcStbHostProgramAVSource_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 2, 1, 2),
    _OcStbHostProgramAVSource_Type()
)
ocStbHostProgramAVSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostProgramAVSource.setStatus("current")
_OcStbHostProgramAVDestination_Type = RowPointer
_OcStbHostProgramAVDestination_Object = MibTableColumn
ocStbHostProgramAVDestination = _OcStbHostProgramAVDestination_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 2, 1, 3),
    _OcStbHostProgramAVDestination_Type()
)
ocStbHostProgramAVDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostProgramAVDestination.setStatus("current")
_OcStbHostProgramContentSource_Type = RowPointer
_OcStbHostProgramContentSource_Object = MibTableColumn
ocStbHostProgramContentSource = _OcStbHostProgramContentSource_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 2, 1, 4),
    _OcStbHostProgramContentSource_Type()
)
ocStbHostProgramContentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostProgramContentSource.setStatus("current")
_OcStbHostProgramContentDestination_Type = RowPointer
_OcStbHostProgramContentDestination_Object = MibTableColumn
ocStbHostProgramContentDestination = _OcStbHostProgramContentDestination_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 2, 1, 5),
    _OcStbHostProgramContentDestination_Type()
)
ocStbHostProgramContentDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostProgramContentDestination.setStatus("current")
_OcStbHostMpeg2ContentTable_Object = MibTable
ocStbHostMpeg2ContentTable = _OcStbHostMpeg2ContentTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentTable.setStatus("current")
_OcStbHostMpeg2ContentEntry_Object = MibTableRow
ocStbHostMpeg2ContentEntry = _OcStbHostMpeg2ContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1)
)
ocStbHostMpeg2ContentEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostMpeg2ContentIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentEntry.setStatus("current")


class _OcStbHostMpeg2ContentIndex_Type(Unsigned32):
    """Custom type ocStbHostMpeg2ContentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OcStbHostMpeg2ContentIndex_Type.__name__ = "Unsigned32"
_OcStbHostMpeg2ContentIndex_Object = MibTableColumn
ocStbHostMpeg2ContentIndex = _OcStbHostMpeg2ContentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 1),
    _OcStbHostMpeg2ContentIndex_Type()
)
ocStbHostMpeg2ContentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentIndex.setStatus("current")
_OcStbHostMpeg2ContentProgramNumber_Type = Unsigned32
_OcStbHostMpeg2ContentProgramNumber_Object = MibTableColumn
ocStbHostMpeg2ContentProgramNumber = _OcStbHostMpeg2ContentProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 2),
    _OcStbHostMpeg2ContentProgramNumber_Type()
)
ocStbHostMpeg2ContentProgramNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentProgramNumber.setStatus("current")
_OcStbHostMpeg2ContentTransportStreamID_Type = Unsigned32
_OcStbHostMpeg2ContentTransportStreamID_Object = MibTableColumn
ocStbHostMpeg2ContentTransportStreamID = _OcStbHostMpeg2ContentTransportStreamID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 3),
    _OcStbHostMpeg2ContentTransportStreamID_Type()
)
ocStbHostMpeg2ContentTransportStreamID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentTransportStreamID.setStatus("current")
_OcStbHostMpeg2ContentTotalStreams_Type = Unsigned32
_OcStbHostMpeg2ContentTotalStreams_Object = MibTableColumn
ocStbHostMpeg2ContentTotalStreams = _OcStbHostMpeg2ContentTotalStreams_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 4),
    _OcStbHostMpeg2ContentTotalStreams_Type()
)
ocStbHostMpeg2ContentTotalStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentTotalStreams.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentTotalStreams.setUnits("streams")


class _OcStbHostMpeg2ContentSelectedVideoPID_Type(Integer32):
    """Custom type ocStbHostMpeg2ContentSelectedVideoPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8191),
    )


_OcStbHostMpeg2ContentSelectedVideoPID_Type.__name__ = "Integer32"
_OcStbHostMpeg2ContentSelectedVideoPID_Object = MibTableColumn
ocStbHostMpeg2ContentSelectedVideoPID = _OcStbHostMpeg2ContentSelectedVideoPID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 5),
    _OcStbHostMpeg2ContentSelectedVideoPID_Type()
)
ocStbHostMpeg2ContentSelectedVideoPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentSelectedVideoPID.setStatus("current")


class _OcStbHostMpeg2ContentSelectedAudioPID_Type(Integer32):
    """Custom type ocStbHostMpeg2ContentSelectedAudioPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8191),
    )


_OcStbHostMpeg2ContentSelectedAudioPID_Type.__name__ = "Integer32"
_OcStbHostMpeg2ContentSelectedAudioPID_Object = MibTableColumn
ocStbHostMpeg2ContentSelectedAudioPID = _OcStbHostMpeg2ContentSelectedAudioPID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 6),
    _OcStbHostMpeg2ContentSelectedAudioPID_Type()
)
ocStbHostMpeg2ContentSelectedAudioPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentSelectedAudioPID.setStatus("current")
_OcStbHostMpeg2ContentOtherAudioPIDs_Type = TruthValue
_OcStbHostMpeg2ContentOtherAudioPIDs_Object = MibTableColumn
ocStbHostMpeg2ContentOtherAudioPIDs = _OcStbHostMpeg2ContentOtherAudioPIDs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 7),
    _OcStbHostMpeg2ContentOtherAudioPIDs_Type()
)
ocStbHostMpeg2ContentOtherAudioPIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentOtherAudioPIDs.setStatus("current")


class _OcStbHostMpeg2ContentCCIValue_Type(Integer32):
    """Custom type ocStbHostMpeg2ContentCCIValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("copyFreely", 0),
          ("copyNoMore", 1),
          ("copyOneGeneration", 2),
          ("copyNever", 3),
          ("undefined", 4))
    )


_OcStbHostMpeg2ContentCCIValue_Type.__name__ = "Integer32"
_OcStbHostMpeg2ContentCCIValue_Object = MibTableColumn
ocStbHostMpeg2ContentCCIValue = _OcStbHostMpeg2ContentCCIValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 8),
    _OcStbHostMpeg2ContentCCIValue_Type()
)
ocStbHostMpeg2ContentCCIValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentCCIValue.setStatus("current")


class _OcStbHostMpeg2ContentAPSValue_Type(Integer32):
    """Custom type ocStbHostMpeg2ContentAPSValue based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("noMacrovision", 4),
          ("notDefined", 5))
    )


_OcStbHostMpeg2ContentAPSValue_Type.__name__ = "Integer32"
_OcStbHostMpeg2ContentAPSValue_Object = MibTableColumn
ocStbHostMpeg2ContentAPSValue = _OcStbHostMpeg2ContentAPSValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 9),
    _OcStbHostMpeg2ContentAPSValue_Type()
)
ocStbHostMpeg2ContentAPSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentAPSValue.setStatus("current")
_OcStbHostMpeg2ContentCITStatus_Type = TruthValue
_OcStbHostMpeg2ContentCITStatus_Object = MibTableColumn
ocStbHostMpeg2ContentCITStatus = _OcStbHostMpeg2ContentCITStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 10),
    _OcStbHostMpeg2ContentCITStatus_Type()
)
ocStbHostMpeg2ContentCITStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentCITStatus.setStatus("current")
_OcStbHostMpeg2ContentBroadcastFlagStatus_Type = TruthValue
_OcStbHostMpeg2ContentBroadcastFlagStatus_Object = MibTableColumn
ocStbHostMpeg2ContentBroadcastFlagStatus = _OcStbHostMpeg2ContentBroadcastFlagStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 11),
    _OcStbHostMpeg2ContentBroadcastFlagStatus_Type()
)
ocStbHostMpeg2ContentBroadcastFlagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentBroadcastFlagStatus.setStatus("current")
_OcStbHostMpeg2ContentEPNStatus_Type = TruthValue
_OcStbHostMpeg2ContentEPNStatus_Object = MibTableColumn
ocStbHostMpeg2ContentEPNStatus = _OcStbHostMpeg2ContentEPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 12),
    _OcStbHostMpeg2ContentEPNStatus_Type()
)
ocStbHostMpeg2ContentEPNStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentEPNStatus.setStatus("current")


class _OcStbHostMpeg2ContentPCRPID_Type(Integer32):
    """Custom type ocStbHostMpeg2ContentPCRPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8191),
    )


_OcStbHostMpeg2ContentPCRPID_Type.__name__ = "Integer32"
_OcStbHostMpeg2ContentPCRPID_Object = MibTableColumn
ocStbHostMpeg2ContentPCRPID = _OcStbHostMpeg2ContentPCRPID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 13),
    _OcStbHostMpeg2ContentPCRPID_Type()
)
ocStbHostMpeg2ContentPCRPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentPCRPID.setStatus("current")


class _OcStbHostMpeg2ContentPCRLockStatus_Type(Integer32):
    """Custom type ocStbHostMpeg2ContentPCRLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notLocked", 1),
          ("locked", 2))
    )


_OcStbHostMpeg2ContentPCRLockStatus_Type.__name__ = "Integer32"
_OcStbHostMpeg2ContentPCRLockStatus_Object = MibTableColumn
ocStbHostMpeg2ContentPCRLockStatus = _OcStbHostMpeg2ContentPCRLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 14),
    _OcStbHostMpeg2ContentPCRLockStatus_Type()
)
ocStbHostMpeg2ContentPCRLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentPCRLockStatus.setStatus("current")
_OcStbHostMpeg2ContentDecoderPTS_Type = Integer32
_OcStbHostMpeg2ContentDecoderPTS_Object = MibTableColumn
ocStbHostMpeg2ContentDecoderPTS = _OcStbHostMpeg2ContentDecoderPTS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 15),
    _OcStbHostMpeg2ContentDecoderPTS_Type()
)
ocStbHostMpeg2ContentDecoderPTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentDecoderPTS.setStatus("current")
_OcStbHostMpeg2ContentDiscontinuities_Type = Counter32
_OcStbHostMpeg2ContentDiscontinuities_Object = MibTableColumn
ocStbHostMpeg2ContentDiscontinuities = _OcStbHostMpeg2ContentDiscontinuities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 16),
    _OcStbHostMpeg2ContentDiscontinuities_Type()
)
ocStbHostMpeg2ContentDiscontinuities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentDiscontinuities.setStatus("current")
_OcStbHostMpeg2ContentPktErrors_Type = Counter32
_OcStbHostMpeg2ContentPktErrors_Object = MibTableColumn
ocStbHostMpeg2ContentPktErrors = _OcStbHostMpeg2ContentPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 17),
    _OcStbHostMpeg2ContentPktErrors_Type()
)
ocStbHostMpeg2ContentPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentPktErrors.setStatus("current")
_OcStbHostMpeg2ContentPipelineErrors_Type = Counter32
_OcStbHostMpeg2ContentPipelineErrors_Object = MibTableColumn
ocStbHostMpeg2ContentPipelineErrors = _OcStbHostMpeg2ContentPipelineErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 18),
    _OcStbHostMpeg2ContentPipelineErrors_Type()
)
ocStbHostMpeg2ContentPipelineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentPipelineErrors.setStatus("current")
_OcStbHostMpeg2ContentDecoderRestarts_Type = Counter32
_OcStbHostMpeg2ContentDecoderRestarts_Object = MibTableColumn
ocStbHostMpeg2ContentDecoderRestarts = _OcStbHostMpeg2ContentDecoderRestarts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 19),
    _OcStbHostMpeg2ContentDecoderRestarts_Type()
)
ocStbHostMpeg2ContentDecoderRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContentDecoderRestarts.setStatus("current")
_OcStbHostMpeg2ContainerFormat_Type = VideoContainerFormat
_OcStbHostMpeg2ContainerFormat_Object = MibTableColumn
ocStbHostMpeg2ContainerFormat = _OcStbHostMpeg2ContainerFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 3, 1, 20),
    _OcStbHostMpeg2ContainerFormat_Type()
)
ocStbHostMpeg2ContainerFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg2ContainerFormat.setStatus("current")
_OcStbHostAnalogVideoTable_Object = MibTable
ocStbHostAnalogVideoTable = _OcStbHostAnalogVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 4)
)
if mibBuilder.loadTexts:
    ocStbHostAnalogVideoTable.setStatus("current")
_OcStbHostAnalogVideoEntry_Object = MibTableRow
ocStbHostAnalogVideoEntry = _OcStbHostAnalogVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 4, 1)
)
ocStbHostAnalogVideoEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostAVInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostAnalogVideoEntry.setStatus("current")


class _OcStbHostAnalogVideoProtectionStatus_Type(Integer32):
    """Custom type ocStbHostAnalogVideoProtectionStatus based on Integer32"""
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
        *(("copyProtectionOff", 0),
          ("splitBurstOff", 1),
          ("twoLineSplitBurst", 2),
          ("fourLineSplitBurst", 3))
    )


_OcStbHostAnalogVideoProtectionStatus_Type.__name__ = "Integer32"
_OcStbHostAnalogVideoProtectionStatus_Object = MibTableColumn
ocStbHostAnalogVideoProtectionStatus = _OcStbHostAnalogVideoProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 4, 1, 1),
    _OcStbHostAnalogVideoProtectionStatus_Type()
)
ocStbHostAnalogVideoProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostAnalogVideoProtectionStatus.setStatus("current")
_OcStbHostMpeg4ContentTable_Object = MibTable
ocStbHostMpeg4ContentTable = _OcStbHostMpeg4ContentTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5)
)
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentTable.setStatus("current")
_OcStbHostMpeg4ContentEntry_Object = MibTableRow
ocStbHostMpeg4ContentEntry = _OcStbHostMpeg4ContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1)
)
ocStbHostMpeg4ContentEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostMpeg4ContentIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentEntry.setStatus("current")


class _OcStbHostMpeg4ContentIndex_Type(Unsigned32):
    """Custom type ocStbHostMpeg4ContentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OcStbHostMpeg4ContentIndex_Type.__name__ = "Unsigned32"
_OcStbHostMpeg4ContentIndex_Object = MibTableColumn
ocStbHostMpeg4ContentIndex = _OcStbHostMpeg4ContentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 1),
    _OcStbHostMpeg4ContentIndex_Type()
)
ocStbHostMpeg4ContentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentIndex.setStatus("current")
_OcStbHostMpeg4ContentProgramNumber_Type = Unsigned32
_OcStbHostMpeg4ContentProgramNumber_Object = MibTableColumn
ocStbHostMpeg4ContentProgramNumber = _OcStbHostMpeg4ContentProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 2),
    _OcStbHostMpeg4ContentProgramNumber_Type()
)
ocStbHostMpeg4ContentProgramNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentProgramNumber.setStatus("current")
_OcStbHostMpeg4ContentTransportStreamID_Type = Unsigned32
_OcStbHostMpeg4ContentTransportStreamID_Object = MibTableColumn
ocStbHostMpeg4ContentTransportStreamID = _OcStbHostMpeg4ContentTransportStreamID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 3),
    _OcStbHostMpeg4ContentTransportStreamID_Type()
)
ocStbHostMpeg4ContentTransportStreamID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentTransportStreamID.setStatus("current")
_OcStbHostMpeg4ContentTotalStreams_Type = Unsigned32
_OcStbHostMpeg4ContentTotalStreams_Object = MibTableColumn
ocStbHostMpeg4ContentTotalStreams = _OcStbHostMpeg4ContentTotalStreams_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 4),
    _OcStbHostMpeg4ContentTotalStreams_Type()
)
ocStbHostMpeg4ContentTotalStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentTotalStreams.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentTotalStreams.setUnits("streams")


class _OcStbHostMpeg4ContentSelectedVideoPID_Type(Integer32):
    """Custom type ocStbHostMpeg4ContentSelectedVideoPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8191),
    )


_OcStbHostMpeg4ContentSelectedVideoPID_Type.__name__ = "Integer32"
_OcStbHostMpeg4ContentSelectedVideoPID_Object = MibTableColumn
ocStbHostMpeg4ContentSelectedVideoPID = _OcStbHostMpeg4ContentSelectedVideoPID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 5),
    _OcStbHostMpeg4ContentSelectedVideoPID_Type()
)
ocStbHostMpeg4ContentSelectedVideoPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentSelectedVideoPID.setStatus("current")


class _OcStbHostMpeg4ContentSelectedAudioPID_Type(Integer32):
    """Custom type ocStbHostMpeg4ContentSelectedAudioPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8191),
    )


_OcStbHostMpeg4ContentSelectedAudioPID_Type.__name__ = "Integer32"
_OcStbHostMpeg4ContentSelectedAudioPID_Object = MibTableColumn
ocStbHostMpeg4ContentSelectedAudioPID = _OcStbHostMpeg4ContentSelectedAudioPID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 6),
    _OcStbHostMpeg4ContentSelectedAudioPID_Type()
)
ocStbHostMpeg4ContentSelectedAudioPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentSelectedAudioPID.setStatus("current")
_OcStbHostMpeg4ContentOtherAudioPIDs_Type = TruthValue
_OcStbHostMpeg4ContentOtherAudioPIDs_Object = MibTableColumn
ocStbHostMpeg4ContentOtherAudioPIDs = _OcStbHostMpeg4ContentOtherAudioPIDs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 7),
    _OcStbHostMpeg4ContentOtherAudioPIDs_Type()
)
ocStbHostMpeg4ContentOtherAudioPIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentOtherAudioPIDs.setStatus("current")


class _OcStbHostMpeg4ContentCCIValue_Type(Integer32):
    """Custom type ocStbHostMpeg4ContentCCIValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("copyFreely", 0),
          ("copyNoMore", 1),
          ("copyOneGeneration", 2),
          ("copyNever", 3),
          ("undefined", 4))
    )


_OcStbHostMpeg4ContentCCIValue_Type.__name__ = "Integer32"
_OcStbHostMpeg4ContentCCIValue_Object = MibTableColumn
ocStbHostMpeg4ContentCCIValue = _OcStbHostMpeg4ContentCCIValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 8),
    _OcStbHostMpeg4ContentCCIValue_Type()
)
ocStbHostMpeg4ContentCCIValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentCCIValue.setStatus("current")


class _OcStbHostMpeg4ContentAPSValue_Type(Integer32):
    """Custom type ocStbHostMpeg4ContentAPSValue based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("noMacrovision", 4),
          ("notDefined", 5))
    )


_OcStbHostMpeg4ContentAPSValue_Type.__name__ = "Integer32"
_OcStbHostMpeg4ContentAPSValue_Object = MibTableColumn
ocStbHostMpeg4ContentAPSValue = _OcStbHostMpeg4ContentAPSValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 9),
    _OcStbHostMpeg4ContentAPSValue_Type()
)
ocStbHostMpeg4ContentAPSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentAPSValue.setStatus("current")
_OcStbHostMpeg4ContentCITStatus_Type = TruthValue
_OcStbHostMpeg4ContentCITStatus_Object = MibTableColumn
ocStbHostMpeg4ContentCITStatus = _OcStbHostMpeg4ContentCITStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 10),
    _OcStbHostMpeg4ContentCITStatus_Type()
)
ocStbHostMpeg4ContentCITStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentCITStatus.setStatus("current")
_OcStbHostMpeg4ContentBroadcastFlagStatus_Type = TruthValue
_OcStbHostMpeg4ContentBroadcastFlagStatus_Object = MibTableColumn
ocStbHostMpeg4ContentBroadcastFlagStatus = _OcStbHostMpeg4ContentBroadcastFlagStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 11),
    _OcStbHostMpeg4ContentBroadcastFlagStatus_Type()
)
ocStbHostMpeg4ContentBroadcastFlagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentBroadcastFlagStatus.setStatus("current")
_OcStbHostMpeg4ContentEPNStatus_Type = TruthValue
_OcStbHostMpeg4ContentEPNStatus_Object = MibTableColumn
ocStbHostMpeg4ContentEPNStatus = _OcStbHostMpeg4ContentEPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 12),
    _OcStbHostMpeg4ContentEPNStatus_Type()
)
ocStbHostMpeg4ContentEPNStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentEPNStatus.setStatus("current")


class _OcStbHostMpeg4ContentPCRPID_Type(Integer32):
    """Custom type ocStbHostMpeg4ContentPCRPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8191),
    )


_OcStbHostMpeg4ContentPCRPID_Type.__name__ = "Integer32"
_OcStbHostMpeg4ContentPCRPID_Object = MibTableColumn
ocStbHostMpeg4ContentPCRPID = _OcStbHostMpeg4ContentPCRPID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 13),
    _OcStbHostMpeg4ContentPCRPID_Type()
)
ocStbHostMpeg4ContentPCRPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentPCRPID.setStatus("current")


class _OcStbHostMpeg4ContentPCRLockStatus_Type(Integer32):
    """Custom type ocStbHostMpeg4ContentPCRLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notLocked", 1),
          ("locked", 2))
    )


_OcStbHostMpeg4ContentPCRLockStatus_Type.__name__ = "Integer32"
_OcStbHostMpeg4ContentPCRLockStatus_Object = MibTableColumn
ocStbHostMpeg4ContentPCRLockStatus = _OcStbHostMpeg4ContentPCRLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 14),
    _OcStbHostMpeg4ContentPCRLockStatus_Type()
)
ocStbHostMpeg4ContentPCRLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentPCRLockStatus.setStatus("current")
_OcStbHostMpeg4ContentDecoderPTS_Type = Integer32
_OcStbHostMpeg4ContentDecoderPTS_Object = MibTableColumn
ocStbHostMpeg4ContentDecoderPTS = _OcStbHostMpeg4ContentDecoderPTS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 15),
    _OcStbHostMpeg4ContentDecoderPTS_Type()
)
ocStbHostMpeg4ContentDecoderPTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentDecoderPTS.setStatus("current")
_OcStbHostMpeg4ContentDiscontinuities_Type = Counter32
_OcStbHostMpeg4ContentDiscontinuities_Object = MibTableColumn
ocStbHostMpeg4ContentDiscontinuities = _OcStbHostMpeg4ContentDiscontinuities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 16),
    _OcStbHostMpeg4ContentDiscontinuities_Type()
)
ocStbHostMpeg4ContentDiscontinuities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentDiscontinuities.setStatus("current")
_OcStbHostMpeg4ContentPktErrors_Type = Counter32
_OcStbHostMpeg4ContentPktErrors_Object = MibTableColumn
ocStbHostMpeg4ContentPktErrors = _OcStbHostMpeg4ContentPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 17),
    _OcStbHostMpeg4ContentPktErrors_Type()
)
ocStbHostMpeg4ContentPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentPktErrors.setStatus("current")
_OcStbHostMpeg4ContentPipelineErrors_Type = Counter32
_OcStbHostMpeg4ContentPipelineErrors_Object = MibTableColumn
ocStbHostMpeg4ContentPipelineErrors = _OcStbHostMpeg4ContentPipelineErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 18),
    _OcStbHostMpeg4ContentPipelineErrors_Type()
)
ocStbHostMpeg4ContentPipelineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentPipelineErrors.setStatus("current")
_OcStbHostMpeg4ContentDecoderRestarts_Type = Counter32
_OcStbHostMpeg4ContentDecoderRestarts_Object = MibTableColumn
ocStbHostMpeg4ContentDecoderRestarts = _OcStbHostMpeg4ContentDecoderRestarts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 19),
    _OcStbHostMpeg4ContentDecoderRestarts_Type()
)
ocStbHostMpeg4ContentDecoderRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContentDecoderRestarts.setStatus("current")
_OcStbHostMpeg4ContainerFormat_Type = VideoContainerFormat
_OcStbHostMpeg4ContainerFormat_Object = MibTableColumn
ocStbHostMpeg4ContainerFormat = _OcStbHostMpeg4ContainerFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 5, 1, 20),
    _OcStbHostMpeg4ContainerFormat_Type()
)
ocStbHostMpeg4ContainerFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMpeg4ContainerFormat.setStatus("current")
_OcStbHostVc1ContentTable_Object = MibTable
ocStbHostVc1ContentTable = _OcStbHostVc1ContentTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 6)
)
if mibBuilder.loadTexts:
    ocStbHostVc1ContentTable.setStatus("current")
_OcStbHostVc1ContentEntry_Object = MibTableRow
ocStbHostVc1ContentEntry = _OcStbHostVc1ContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 6, 1)
)
ocStbHostVc1ContentEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostVc1ContentIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostVc1ContentEntry.setStatus("current")


class _OcStbHostVc1ContentIndex_Type(Unsigned32):
    """Custom type ocStbHostVc1ContentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OcStbHostVc1ContentIndex_Type.__name__ = "Unsigned32"
_OcStbHostVc1ContentIndex_Object = MibTableColumn
ocStbHostVc1ContentIndex = _OcStbHostVc1ContentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 6, 1, 1),
    _OcStbHostVc1ContentIndex_Type()
)
ocStbHostVc1ContentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostVc1ContentIndex.setStatus("current")
_OcStbHostVc1ContentProgramNumber_Type = Unsigned32
_OcStbHostVc1ContentProgramNumber_Object = MibTableColumn
ocStbHostVc1ContentProgramNumber = _OcStbHostVc1ContentProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 6, 1, 2),
    _OcStbHostVc1ContentProgramNumber_Type()
)
ocStbHostVc1ContentProgramNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostVc1ContentProgramNumber.setStatus("current")
_OcStbHostVc1ContainerFormat_Type = VideoContainerFormat
_OcStbHostVc1ContainerFormat_Object = MibTableColumn
ocStbHostVc1ContainerFormat = _OcStbHostVc1ContainerFormat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 7, 6, 1, 20),
    _OcStbHostVc1ContainerFormat_Type()
)
ocStbHostVc1ContainerFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostVc1ContainerFormat.setStatus("current")
_OcStbHostQpskObjects_ObjectIdentity = ObjectIdentity
ocStbHostQpskObjects = _OcStbHostQpskObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8)
)
_OcStbHostQpskFDCFreq_Type = Unsigned32
_OcStbHostQpskFDCFreq_Object = MibScalar
ocStbHostQpskFDCFreq = _OcStbHostQpskFDCFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 1),
    _OcStbHostQpskFDCFreq_Type()
)
ocStbHostQpskFDCFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCFreq.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCFreq.setUnits("hertz")
_OcStbHostQpskRDCFreq_Type = Unsigned32
_OcStbHostQpskRDCFreq_Object = MibScalar
ocStbHostQpskRDCFreq = _OcStbHostQpskRDCFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 2),
    _OcStbHostQpskRDCFreq_Type()
)
ocStbHostQpskRDCFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskRDCFreq.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostQpskRDCFreq.setUnits("hertz")


class _OcStbHostQpskFDCBer_Type(Integer32):
    """Custom type ocStbHostQpskFDCBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("berGreaterThan10e2", 1),
          ("berRange10e2ToGreaterThan10e4", 2),
          ("berRange10e4ToGreaterThan10e6", 3),
          ("berRange10e6ToGreaterThan10e8", 4),
          ("berRange10e8ToGreaterThan10e12", 5),
          ("berEqualToOrLessThan10e12", 6),
          ("berNotApplicable", 7))
    )


_OcStbHostQpskFDCBer_Type.__name__ = "Integer32"
_OcStbHostQpskFDCBer_Object = MibScalar
ocStbHostQpskFDCBer = _OcStbHostQpskFDCBer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 3),
    _OcStbHostQpskFDCBer_Type()
)
ocStbHostQpskFDCBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCBer.setStatus("current")


class _OcStbHostQpskFDCStatus_Type(Integer32):
    """Custom type ocStbHostQpskFDCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notLocked", 1),
          ("locked", 2))
    )


_OcStbHostQpskFDCStatus_Type.__name__ = "Integer32"
_OcStbHostQpskFDCStatus_Object = MibScalar
ocStbHostQpskFDCStatus = _OcStbHostQpskFDCStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 4),
    _OcStbHostQpskFDCStatus_Type()
)
ocStbHostQpskFDCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCStatus.setStatus("current")
_OcStbHostQpskFDCBytesRead_Type = Unsigned32
_OcStbHostQpskFDCBytesRead_Object = MibScalar
ocStbHostQpskFDCBytesRead = _OcStbHostQpskFDCBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 5),
    _OcStbHostQpskFDCBytesRead_Type()
)
ocStbHostQpskFDCBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCBytesRead.setStatus("current")
_OcStbHostQpskFDCPower_Type = TenthdBmV
_OcStbHostQpskFDCPower_Object = MibScalar
ocStbHostQpskFDCPower = _OcStbHostQpskFDCPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 6),
    _OcStbHostQpskFDCPower_Type()
)
ocStbHostQpskFDCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCPower.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCPower.setUnits("dBmV")
_OcStbHostQpskFDCLockedTime_Type = Unsigned32
_OcStbHostQpskFDCLockedTime_Object = MibScalar
ocStbHostQpskFDCLockedTime = _OcStbHostQpskFDCLockedTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 7),
    _OcStbHostQpskFDCLockedTime_Type()
)
ocStbHostQpskFDCLockedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCLockedTime.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCLockedTime.setUnits("seconds")
_OcStbHostQpskFDCSNR_Type = TenthdB
_OcStbHostQpskFDCSNR_Object = MibScalar
ocStbHostQpskFDCSNR = _OcStbHostQpskFDCSNR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 8),
    _OcStbHostQpskFDCSNR_Type()
)
ocStbHostQpskFDCSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCSNR.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostQpskFDCSNR.setUnits("dB")
_OcStbHostQpskAGC_Type = Unsigned32
_OcStbHostQpskAGC_Object = MibScalar
ocStbHostQpskAGC = _OcStbHostQpskAGC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 9),
    _OcStbHostQpskAGC_Type()
)
ocStbHostQpskAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskAGC.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostQpskAGC.setUnits("percent")
_OcStbHostQpskRDCPower_Type = TenthdBmV
_OcStbHostQpskRDCPower_Object = MibScalar
ocStbHostQpskRDCPower = _OcStbHostQpskRDCPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 10),
    _OcStbHostQpskRDCPower_Type()
)
ocStbHostQpskRDCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskRDCPower.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostQpskRDCPower.setUnits("dBmV")


class _OcStbHostQpskRDCDataRate_Type(Integer32):
    """Custom type ocStbHostQpskRDCDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps256", 1),
          ("kbps1544", 2),
          ("kbps3088", 3))
    )


_OcStbHostQpskRDCDataRate_Type.__name__ = "Integer32"
_OcStbHostQpskRDCDataRate_Object = MibScalar
ocStbHostQpskRDCDataRate = _OcStbHostQpskRDCDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 2, 8, 11),
    _OcStbHostQpskRDCDataRate_Type()
)
ocStbHostQpskRDCDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostQpskRDCDataRate.setStatus("current")
_OcStbHostEasObjects_ObjectIdentity = ObjectIdentity
ocStbHostEasObjects = _OcStbHostEasObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 3)
)
_OcStbHostEasCodes_ObjectIdentity = ObjectIdentity
ocStbHostEasCodes = _OcStbHostEasCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 3, 1)
)


class _OcStbEasMessageStateCode_Type(Unsigned32):
    """Custom type ocStbEasMessageStateCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OcStbEasMessageStateCode_Type.__name__ = "Unsigned32"
_OcStbEasMessageStateCode_Object = MibScalar
ocStbEasMessageStateCode = _OcStbEasMessageStateCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 3, 1, 1),
    _OcStbEasMessageStateCode_Type()
)
ocStbEasMessageStateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbEasMessageStateCode.setStatus("current")


class _OcStbEasMessageCountyCode_Type(Unsigned32):
    """Custom type ocStbEasMessageCountyCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_OcStbEasMessageCountyCode_Type.__name__ = "Unsigned32"
_OcStbEasMessageCountyCode_Object = MibScalar
ocStbEasMessageCountyCode = _OcStbEasMessageCountyCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 3, 1, 2),
    _OcStbEasMessageCountyCode_Type()
)
ocStbEasMessageCountyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbEasMessageCountyCode.setStatus("current")


class _OcStbEasMessageCountySubdivisionCode_Type(Unsigned32):
    """Custom type ocStbEasMessageCountySubdivisionCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_OcStbEasMessageCountySubdivisionCode_Type.__name__ = "Unsigned32"
_OcStbEasMessageCountySubdivisionCode_Object = MibScalar
ocStbEasMessageCountySubdivisionCode = _OcStbEasMessageCountySubdivisionCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 1, 3, 1, 3),
    _OcStbEasMessageCountySubdivisionCode_Type()
)
ocStbEasMessageCountySubdivisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbEasMessageCountySubdivisionCode.setStatus("current")
_OcStbHostSecuritySubSystem_ObjectIdentity = ObjectIdentity
ocStbHostSecuritySubSystem = _OcStbHostSecuritySubSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 2)
)
_OcStbHostSecurityIdentifier_Type = SnmpAdminString
_OcStbHostSecurityIdentifier_Object = MibScalar
ocStbHostSecurityIdentifier = _OcStbHostSecurityIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 2, 2),
    _OcStbHostSecurityIdentifier_Type()
)
ocStbHostSecurityIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSecurityIdentifier.setStatus("deprecated")
_OcStbHostCASystemIdentifier_Type = SnmpAdminString
_OcStbHostCASystemIdentifier_Object = MibScalar
ocStbHostCASystemIdentifier = _OcStbHostCASystemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 2, 3),
    _OcStbHostCASystemIdentifier_Type()
)
ocStbHostCASystemIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCASystemIdentifier.setStatus("current")


class _OcStbHostCAType_Type(Integer32):
    """Custom type ocStbHostCAType based on Integer32"""
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
        *(("other", 1),
          ("embedded", 2),
          ("cablecard", 3),
          ("dcas", 4))
    )


_OcStbHostCAType_Type.__name__ = "Integer32"
_OcStbHostCAType_Object = MibScalar
ocStbHostCAType = _OcStbHostCAType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 2, 4),
    _OcStbHostCAType_Type()
)
ocStbHostCAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCAType.setStatus("current")
_OcStbHostSoftware_ObjectIdentity = ObjectIdentity
ocStbHostSoftware = _OcStbHostSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3)
)
_OcStbHostDeviceSoftwareBase_ObjectIdentity = ObjectIdentity
ocStbHostDeviceSoftwareBase = _OcStbHostDeviceSoftwareBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 1)
)
_OcStbHostSoftwareFirmwareVersion_Type = SnmpAdminString
_OcStbHostSoftwareFirmwareVersion_Object = MibScalar
ocStbHostSoftwareFirmwareVersion = _OcStbHostSoftwareFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 1, 1),
    _OcStbHostSoftwareFirmwareVersion_Type()
)
ocStbHostSoftwareFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareFirmwareVersion.setStatus("current")
_OcStbHostSoftwareOCAPVersion_Type = SnmpAdminString
_OcStbHostSoftwareOCAPVersion_Object = MibScalar
ocStbHostSoftwareOCAPVersion = _OcStbHostSoftwareOCAPVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 1, 2),
    _OcStbHostSoftwareOCAPVersion_Type()
)
ocStbHostSoftwareOCAPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareOCAPVersion.setStatus("current")
_OcStbHostSoftwareFirmwareReleaseDate_Type = DateAndTime
_OcStbHostSoftwareFirmwareReleaseDate_Object = MibScalar
ocStbHostSoftwareFirmwareReleaseDate = _OcStbHostSoftwareFirmwareReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 1, 3),
    _OcStbHostSoftwareFirmwareReleaseDate_Type()
)
ocStbHostSoftwareFirmwareReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareFirmwareReleaseDate.setStatus("current")
_OcStbHostSoftwareBootloaderVersion_Type = SnmpAdminString
_OcStbHostSoftwareBootloaderVersion_Object = MibScalar
ocStbHostSoftwareBootloaderVersion = _OcStbHostSoftwareBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 1, 4),
    _OcStbHostSoftwareBootloaderVersion_Type()
)
ocStbHostSoftwareBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareBootloaderVersion.setStatus("current")
_OcStbHostFirmwareDownloadStatus_ObjectIdentity = ObjectIdentity
ocStbHostFirmwareDownloadStatus = _OcStbHostFirmwareDownloadStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 2)
)


class _OcStbHostFirmwareImageStatus_Type(Integer32):
    """Custom type ocStbHostFirmwareImageStatus based on Integer32"""
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
        *(("imageAuthorized", 1),
          ("imageCorrupted", 2),
          ("imageCertFailure", 3),
          ("imageMaxDownloadRetry", 4),
          ("imageMaxRebootRetry", 5))
    )


_OcStbHostFirmwareImageStatus_Type.__name__ = "Integer32"
_OcStbHostFirmwareImageStatus_Object = MibScalar
ocStbHostFirmwareImageStatus = _OcStbHostFirmwareImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 2, 1),
    _OcStbHostFirmwareImageStatus_Type()
)
ocStbHostFirmwareImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostFirmwareImageStatus.setStatus("current")


class _OcStbHostFirmwareCodeDownloadStatus_Type(Integer32):
    """Custom type ocStbHostFirmwareCodeDownloadStatus based on Integer32"""
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
        *(("downloadingStarted", 1),
          ("downloadingComplete", 2),
          ("downloadingFailed", 3),
          ("other", 4))
    )


_OcStbHostFirmwareCodeDownloadStatus_Type.__name__ = "Integer32"
_OcStbHostFirmwareCodeDownloadStatus_Object = MibScalar
ocStbHostFirmwareCodeDownloadStatus = _OcStbHostFirmwareCodeDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 2, 2),
    _OcStbHostFirmwareCodeDownloadStatus_Type()
)
ocStbHostFirmwareCodeDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostFirmwareCodeDownloadStatus.setStatus("current")
_OcStbHostFirmwareCodeObjectName_Type = SnmpAdminString
_OcStbHostFirmwareCodeObjectName_Object = MibScalar
ocStbHostFirmwareCodeObjectName = _OcStbHostFirmwareCodeObjectName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 2, 3),
    _OcStbHostFirmwareCodeObjectName_Type()
)
ocStbHostFirmwareCodeObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostFirmwareCodeObjectName.setStatus("current")


class _OcStbHostFirmwareDownloadFailedStatus_Type(Integer32):
    """Custom type ocStbHostFirmwareDownloadFailedStatus based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("cdlError1", 1),
          ("cdlError2", 2),
          ("cdlError3", 3),
          ("cdlError4", 4),
          ("cdlError5", 5),
          ("cdlError6", 6),
          ("cdlError7", 7),
          ("cdlError8", 8),
          ("cdlError9", 9),
          ("cdlError10", 10),
          ("cdlError11", 11),
          ("cdlError12", 12),
          ("cdlError13", 13),
          ("cdlError14", 14),
          ("cdlError15", 15),
          ("cdlError16", 16),
          ("cdlError17", 17),
          ("cdlError18", 18),
          ("cdlError19", 19),
          ("cdlError20", 20),
          ("cdlError21", 21),
          ("cdlError22", 22),
          ("cdlError23", 23),
          ("cdlError24", 24),
          ("cdlError25", 25),
          ("cdlError99", 99))
    )


_OcStbHostFirmwareDownloadFailedStatus_Type.__name__ = "Integer32"
_OcStbHostFirmwareDownloadFailedStatus_Object = MibScalar
ocStbHostFirmwareDownloadFailedStatus = _OcStbHostFirmwareDownloadFailedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 2, 4),
    _OcStbHostFirmwareDownloadFailedStatus_Type()
)
ocStbHostFirmwareDownloadFailedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostFirmwareDownloadFailedStatus.setStatus("current")
_OcStbHostFirmwareDownloadFailedCount_Type = Counter32
_OcStbHostFirmwareDownloadFailedCount_Object = MibScalar
ocStbHostFirmwareDownloadFailedCount = _OcStbHostFirmwareDownloadFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 2, 5),
    _OcStbHostFirmwareDownloadFailedCount_Type()
)
ocStbHostFirmwareDownloadFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostFirmwareDownloadFailedCount.setStatus("current")


class _OcStbHostFirmwareDownloadGroupId_Type(Unsigned32):
    """Custom type ocStbHostFirmwareDownloadGroupId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OcStbHostFirmwareDownloadGroupId_Type.__name__ = "Unsigned32"
_OcStbHostFirmwareDownloadGroupId_Object = MibScalar
ocStbHostFirmwareDownloadGroupId = _OcStbHostFirmwareDownloadGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 2, 6),
    _OcStbHostFirmwareDownloadGroupId_Type()
)
ocStbHostFirmwareDownloadGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostFirmwareDownloadGroupId.setStatus("current")
_OcStbHostSoftwareApplicationInfo_ObjectIdentity = ObjectIdentity
ocStbHostSoftwareApplicationInfo = _OcStbHostSoftwareApplicationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3)
)
_OcStbHostSoftwareApplicationInfoTable_Object = MibTable
ocStbHostSoftwareApplicationInfoTable = _OcStbHostSoftwareApplicationInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationInfoTable.setStatus("current")
_OcStbHostSoftwareApplicationInfoEntry_Object = MibTableRow
ocStbHostSoftwareApplicationInfoEntry = _OcStbHostSoftwareApplicationInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1)
)
ocStbHostSoftwareApplicationInfoEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostSoftwareApplicationInfoIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationInfoEntry.setStatus("current")
_OcStbHostSoftwareAppNameString_Type = SnmpAdminString
_OcStbHostSoftwareAppNameString_Object = MibTableColumn
ocStbHostSoftwareAppNameString = _OcStbHostSoftwareAppNameString_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1, 1),
    _OcStbHostSoftwareAppNameString_Type()
)
ocStbHostSoftwareAppNameString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareAppNameString.setStatus("current")
_OcStbHostSoftwareAppVersionNumber_Type = SnmpAdminString
_OcStbHostSoftwareAppVersionNumber_Object = MibTableColumn
ocStbHostSoftwareAppVersionNumber = _OcStbHostSoftwareAppVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1, 2),
    _OcStbHostSoftwareAppVersionNumber_Type()
)
ocStbHostSoftwareAppVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareAppVersionNumber.setStatus("current")


class _OcStbHostSoftwareStatus_Type(Integer32):
    """Custom type ocStbHostSoftwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 4),
          ("notLoaded", 5),
          ("paused", 6),
          ("running", 7),
          ("destroyed", 8))
    )


_OcStbHostSoftwareStatus_Type.__name__ = "Integer32"
_OcStbHostSoftwareStatus_Object = MibTableColumn
ocStbHostSoftwareStatus = _OcStbHostSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1, 3),
    _OcStbHostSoftwareStatus_Type()
)
ocStbHostSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareStatus.setStatus("current")


class _OcStbHostSoftwareApplicationInfoIndex_Type(Unsigned32):
    """Custom type ocStbHostSoftwareApplicationInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcStbHostSoftwareApplicationInfoIndex_Type.__name__ = "Unsigned32"
_OcStbHostSoftwareApplicationInfoIndex_Object = MibTableColumn
ocStbHostSoftwareApplicationInfoIndex = _OcStbHostSoftwareApplicationInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1, 4),
    _OcStbHostSoftwareApplicationInfoIndex_Type()
)
ocStbHostSoftwareApplicationInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationInfoIndex.setStatus("current")


class _OcStbHostSoftwareOrganizationId_Type(OctetString):
    """Custom type ocStbHostSoftwareOrganizationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_OcStbHostSoftwareOrganizationId_Type.__name__ = "OctetString"
_OcStbHostSoftwareOrganizationId_Object = MibTableColumn
ocStbHostSoftwareOrganizationId = _OcStbHostSoftwareOrganizationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1, 5),
    _OcStbHostSoftwareOrganizationId_Type()
)
ocStbHostSoftwareOrganizationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareOrganizationId.setStatus("current")


class _OcStbHostSoftwareApplicationId_Type(OctetString):
    """Custom type ocStbHostSoftwareApplicationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_OcStbHostSoftwareApplicationId_Type.__name__ = "OctetString"
_OcStbHostSoftwareApplicationId_Object = MibTableColumn
ocStbHostSoftwareApplicationId = _OcStbHostSoftwareApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1, 6),
    _OcStbHostSoftwareApplicationId_Type()
)
ocStbHostSoftwareApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationId.setStatus("current")


class _OcStbHostSoftwareApplicationSigStatus_Type(Integer32):
    """Custom type ocStbHostSoftwareApplicationSigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("okay", 1),
          ("error", 2))
    )


_OcStbHostSoftwareApplicationSigStatus_Type.__name__ = "Integer32"
_OcStbHostSoftwareApplicationSigStatus_Object = MibTableColumn
ocStbHostSoftwareApplicationSigStatus = _OcStbHostSoftwareApplicationSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1, 7),
    _OcStbHostSoftwareApplicationSigStatus_Type()
)
ocStbHostSoftwareApplicationSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationSigStatus.setStatus("deprecated")


class _OcStbHostSoftwareApplicationPriority_Type(Unsigned32):
    """Custom type ocStbHostSoftwareApplicationPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OcStbHostSoftwareApplicationPriority_Type.__name__ = "Unsigned32"
_OcStbHostSoftwareApplicationPriority_Object = MibTableColumn
ocStbHostSoftwareApplicationPriority = _OcStbHostSoftwareApplicationPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 1, 1, 8),
    _OcStbHostSoftwareApplicationPriority_Type()
)
ocStbHostSoftwareApplicationPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationPriority.setStatus("current")
_OcStbHostSoftwareApplicationInfoSigLastReceivedTime_Type = DateAndTime
_OcStbHostSoftwareApplicationInfoSigLastReceivedTime_Object = MibScalar
ocStbHostSoftwareApplicationInfoSigLastReceivedTime = _OcStbHostSoftwareApplicationInfoSigLastReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 2),
    _OcStbHostSoftwareApplicationInfoSigLastReceivedTime_Type()
)
ocStbHostSoftwareApplicationInfoSigLastReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationInfoSigLastReceivedTime.setStatus("current")


class _OcStbHostSoftwareApplicationInfoSigLastReadStatus_Type(Integer32):
    """Custom type ocStbHostSoftwareApplicationInfoSigLastReadStatus based on Integer32"""
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
        *(("unknown", 0),
          ("okay", 1),
          ("error", 2),
          ("okayButRejected", 3))
    )


_OcStbHostSoftwareApplicationInfoSigLastReadStatus_Type.__name__ = "Integer32"
_OcStbHostSoftwareApplicationInfoSigLastReadStatus_Object = MibScalar
ocStbHostSoftwareApplicationInfoSigLastReadStatus = _OcStbHostSoftwareApplicationInfoSigLastReadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 3),
    _OcStbHostSoftwareApplicationInfoSigLastReadStatus_Type()
)
ocStbHostSoftwareApplicationInfoSigLastReadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationInfoSigLastReadStatus.setStatus("current")


class _OcStbHostSoftwareApplicationInfoSigLastNetworkVersionRead_Type(Integer32):
    """Custom type ocStbHostSoftwareApplicationInfoSigLastNetworkVersionRead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_OcStbHostSoftwareApplicationInfoSigLastNetworkVersionRead_Type.__name__ = "Integer32"
_OcStbHostSoftwareApplicationInfoSigLastNetworkVersionRead_Object = MibScalar
ocStbHostSoftwareApplicationInfoSigLastNetworkVersionRead = _OcStbHostSoftwareApplicationInfoSigLastNetworkVersionRead_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 4),
    _OcStbHostSoftwareApplicationInfoSigLastNetworkVersionRead_Type()
)
ocStbHostSoftwareApplicationInfoSigLastNetworkVersionRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationInfoSigLastNetworkVersionRead.setStatus("current")


class _OcStbHostSoftwareApplicationInfoSigVersionInUse_Type(Integer32):
    """Custom type ocStbHostSoftwareApplicationInfoSigVersionInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_OcStbHostSoftwareApplicationInfoSigVersionInUse_Type.__name__ = "Integer32"
_OcStbHostSoftwareApplicationInfoSigVersionInUse_Object = MibScalar
ocStbHostSoftwareApplicationInfoSigVersionInUse = _OcStbHostSoftwareApplicationInfoSigVersionInUse_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 3, 3, 5),
    _OcStbHostSoftwareApplicationInfoSigVersionInUse_Type()
)
ocStbHostSoftwareApplicationInfoSigVersionInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSoftwareApplicationInfoSigVersionInUse.setStatus("current")
_OcStbHostStatus_ObjectIdentity = ObjectIdentity
ocStbHostStatus = _OcStbHostStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4)
)
_OcStbHostPower_ObjectIdentity = ObjectIdentity
ocStbHostPower = _OcStbHostPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 1)
)


class _OcStbHostPowerStatus_Type(Integer32):
    """Custom type ocStbHostPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOn", 1),
          ("standby", 2))
    )


_OcStbHostPowerStatus_Type.__name__ = "Integer32"
_OcStbHostPowerStatus_Object = MibScalar
ocStbHostPowerStatus = _OcStbHostPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 1, 1),
    _OcStbHostPowerStatus_Type()
)
ocStbHostPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostPowerStatus.setStatus("current")


class _OcStbHostAcOutletStatus_Type(Integer32):
    """Custom type ocStbHostAcOutletStatus based on Integer32"""
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
        *(("unSwitched", 1),
          ("switchedOn", 2),
          ("switchedOff", 3),
          ("notInstalled", 4))
    )


_OcStbHostAcOutletStatus_Type.__name__ = "Integer32"
_OcStbHostAcOutletStatus_Object = MibScalar
ocStbHostAcOutletStatus = _OcStbHostAcOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 1, 2),
    _OcStbHostAcOutletStatus_Type()
)
ocStbHostAcOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostAcOutletStatus.setStatus("current")
_OcStbHostUserSettings_ObjectIdentity = ObjectIdentity
ocStbHostUserSettings = _OcStbHostUserSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 2)
)


class _OcStbHostUserSettingsPreferedLanguage_Type(DisplayString):
    """Custom type ocStbHostUserSettingsPreferedLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_OcStbHostUserSettingsPreferedLanguage_Type.__name__ = "DisplayString"
_OcStbHostUserSettingsPreferedLanguage_Object = MibScalar
ocStbHostUserSettingsPreferedLanguage = _OcStbHostUserSettingsPreferedLanguage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 2, 1),
    _OcStbHostUserSettingsPreferedLanguage_Type()
)
ocStbHostUserSettingsPreferedLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostUserSettingsPreferedLanguage.setStatus("current")
_OcStbHostSystemObjects_ObjectIdentity = ObjectIdentity
ocStbHostSystemObjects = _OcStbHostSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3)
)
_OcStbHostSystemTempTable_Object = MibTable
ocStbHostSystemTempTable = _OcStbHostSystemTempTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ocStbHostSystemTempTable.setStatus("current")
_OcStbHostSystemTempEntry_Object = MibTableRow
ocStbHostSystemTempEntry = _OcStbHostSystemTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 1, 1)
)
ocStbHostSystemTempEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "OC-STB-HOST-MIB", "ocStbHostSystemTempIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostSystemTempEntry.setStatus("current")


class _OcStbHostSystemTempIndex_Type(Unsigned32):
    """Custom type ocStbHostSystemTempIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcStbHostSystemTempIndex_Type.__name__ = "Unsigned32"
_OcStbHostSystemTempIndex_Object = MibTableColumn
ocStbHostSystemTempIndex = _OcStbHostSystemTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 1, 1, 1),
    _OcStbHostSystemTempIndex_Type()
)
ocStbHostSystemTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostSystemTempIndex.setStatus("current")
_OcStbHostSystemTempDescr_Type = SnmpAdminString
_OcStbHostSystemTempDescr_Object = MibTableColumn
ocStbHostSystemTempDescr = _OcStbHostSystemTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 1, 1, 2),
    _OcStbHostSystemTempDescr_Type()
)
ocStbHostSystemTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemTempDescr.setStatus("current")
_OcStbHostSystemTempValue_Type = Integer32
_OcStbHostSystemTempValue_Object = MibTableColumn
ocStbHostSystemTempValue = _OcStbHostSystemTempValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 1, 1, 3),
    _OcStbHostSystemTempValue_Type()
)
ocStbHostSystemTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemTempValue.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostSystemTempValue.setUnits("celsius")
_OcStbHostSystemTempLastUpdate_Type = TimeStamp
_OcStbHostSystemTempLastUpdate_Object = MibTableColumn
ocStbHostSystemTempLastUpdate = _OcStbHostSystemTempLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 1, 1, 4),
    _OcStbHostSystemTempLastUpdate_Type()
)
ocStbHostSystemTempLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemTempLastUpdate.setStatus("current")
_OcStbHostSystemTempMaxValue_Type = Integer32
_OcStbHostSystemTempMaxValue_Object = MibTableColumn
ocStbHostSystemTempMaxValue = _OcStbHostSystemTempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 1, 1, 5),
    _OcStbHostSystemTempMaxValue_Type()
)
ocStbHostSystemTempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemTempMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostSystemTempMaxValue.setUnits("celsius")
_OcStbHostSystemHomeNetworkTable_Object = MibTable
ocStbHostSystemHomeNetworkTable = _OcStbHostSystemHomeNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkTable.setStatus("deprecated")
_OcStbHostSystemHomeNetworkEntry_Object = MibTableRow
ocStbHostSystemHomeNetworkEntry = _OcStbHostSystemHomeNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2, 1)
)
ocStbHostSystemHomeNetworkEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostSystemHomeNetworkIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkEntry.setStatus("deprecated")


class _OcStbHostSystemHomeNetworkIndex_Type(Unsigned32):
    """Custom type ocStbHostSystemHomeNetworkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcStbHostSystemHomeNetworkIndex_Type.__name__ = "Unsigned32"
_OcStbHostSystemHomeNetworkIndex_Object = MibTableColumn
ocStbHostSystemHomeNetworkIndex = _OcStbHostSystemHomeNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2, 1, 1),
    _OcStbHostSystemHomeNetworkIndex_Type()
)
ocStbHostSystemHomeNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkIndex.setStatus("deprecated")
_OcStbHostSystemHomeNetworkMaxClients_Type = Integer32
_OcStbHostSystemHomeNetworkMaxClients_Object = MibTableColumn
ocStbHostSystemHomeNetworkMaxClients = _OcStbHostSystemHomeNetworkMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2, 1, 2),
    _OcStbHostSystemHomeNetworkMaxClients_Type()
)
ocStbHostSystemHomeNetworkMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkMaxClients.setStatus("deprecated")


class _OcStbHostSystemHomeNetworkHostDRMStatus_Type(Integer32):
    """Custom type ocStbHostSystemHomeNetworkHostDRMStatus based on Integer32"""
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
        *(("hostHasNoDrmCapability", 1),
          ("hostSupportsDrmButNotForHomeNetworkedClients", 2),
          ("hostSupportsDrmForItselfAndHomeNetworkedClients", 3),
          ("reserved", 4))
    )


_OcStbHostSystemHomeNetworkHostDRMStatus_Type.__name__ = "Integer32"
_OcStbHostSystemHomeNetworkHostDRMStatus_Object = MibTableColumn
ocStbHostSystemHomeNetworkHostDRMStatus = _OcStbHostSystemHomeNetworkHostDRMStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2, 1, 3),
    _OcStbHostSystemHomeNetworkHostDRMStatus_Type()
)
ocStbHostSystemHomeNetworkHostDRMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkHostDRMStatus.setStatus("deprecated")
_OcStbHostSystemHomeNetworkConnectedClients_Type = Integer32
_OcStbHostSystemHomeNetworkConnectedClients_Object = MibTableColumn
ocStbHostSystemHomeNetworkConnectedClients = _OcStbHostSystemHomeNetworkConnectedClients_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2, 1, 4),
    _OcStbHostSystemHomeNetworkConnectedClients_Type()
)
ocStbHostSystemHomeNetworkConnectedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkConnectedClients.setStatus("deprecated")
_OcStbHostSystemHomeNetworkClientMacAddress_Type = MacAddress
_OcStbHostSystemHomeNetworkClientMacAddress_Object = MibTableColumn
ocStbHostSystemHomeNetworkClientMacAddress = _OcStbHostSystemHomeNetworkClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2, 1, 5),
    _OcStbHostSystemHomeNetworkClientMacAddress_Type()
)
ocStbHostSystemHomeNetworkClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkClientMacAddress.setStatus("deprecated")
_OcStbHostSystemHomeNetworkClientIpAddress_Type = InetAddress
_OcStbHostSystemHomeNetworkClientIpAddress_Object = MibTableColumn
ocStbHostSystemHomeNetworkClientIpAddress = _OcStbHostSystemHomeNetworkClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2, 1, 6),
    _OcStbHostSystemHomeNetworkClientIpAddress_Type()
)
ocStbHostSystemHomeNetworkClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkClientIpAddress.setStatus("deprecated")
_OcStbHostSystemHomeNetworkClientDRMStatus_Type = Integer32
_OcStbHostSystemHomeNetworkClientDRMStatus_Object = MibTableColumn
ocStbHostSystemHomeNetworkClientDRMStatus = _OcStbHostSystemHomeNetworkClientDRMStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 2, 1, 7),
    _OcStbHostSystemHomeNetworkClientDRMStatus_Type()
)
ocStbHostSystemHomeNetworkClientDRMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemHomeNetworkClientDRMStatus.setStatus("deprecated")
_OcStbHostSystemMemoryReportTable_Object = MibTable
ocStbHostSystemMemoryReportTable = _OcStbHostSystemMemoryReportTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    ocStbHostSystemMemoryReportTable.setStatus("current")
_OcStbHostSystemMemoryReportEntry_Object = MibTableRow
ocStbHostSystemMemoryReportEntry = _OcStbHostSystemMemoryReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 3, 1)
)
ocStbHostSystemMemoryReportEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostSystemMemoryReportIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostSystemMemoryReportEntry.setStatus("current")


class _OcStbHostSystemMemoryReportIndex_Type(Unsigned32):
    """Custom type ocStbHostSystemMemoryReportIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OcStbHostSystemMemoryReportIndex_Type.__name__ = "Unsigned32"
_OcStbHostSystemMemoryReportIndex_Object = MibTableColumn
ocStbHostSystemMemoryReportIndex = _OcStbHostSystemMemoryReportIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 3, 1, 1),
    _OcStbHostSystemMemoryReportIndex_Type()
)
ocStbHostSystemMemoryReportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostSystemMemoryReportIndex.setStatus("current")


class _OcStbHostSystemMemoryReportMemoryType_Type(Integer32):
    """Custom type ocStbHostSystemMemoryReportMemoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("rom", 1),
          ("dram", 2),
          ("sram", 3),
          ("flash", 4),
          ("nvm", 5),
          ("videomemory", 7),
          ("othermemory", 8),
          ("reserved", 9),
          ("internalHardDrive", 10),
          ("externalHardDrive", 11),
          ("opticalMedia", 12))
    )


_OcStbHostSystemMemoryReportMemoryType_Type.__name__ = "Integer32"
_OcStbHostSystemMemoryReportMemoryType_Object = MibTableColumn
ocStbHostSystemMemoryReportMemoryType = _OcStbHostSystemMemoryReportMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 3, 1, 2),
    _OcStbHostSystemMemoryReportMemoryType_Type()
)
ocStbHostSystemMemoryReportMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemMemoryReportMemoryType.setStatus("current")
_OcStbHostSystemMemoryReportMemorySize_Type = Integer32
_OcStbHostSystemMemoryReportMemorySize_Object = MibTableColumn
ocStbHostSystemMemoryReportMemorySize = _OcStbHostSystemMemoryReportMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 3, 1, 3),
    _OcStbHostSystemMemoryReportMemorySize_Type()
)
ocStbHostSystemMemoryReportMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemMemoryReportMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostSystemMemoryReportMemorySize.setUnits("kilobytes")
_OcStbHostSystemDriveInfoTable_Object = MibTable
ocStbHostSystemDriveInfoTable = _OcStbHostSystemDriveInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    ocStbHostSystemDriveInfoTable.setStatus("current")
_OcStbHostSystemDriveInfoEntry_Object = MibTableRow
ocStbHostSystemDriveInfoEntry = _OcStbHostSystemDriveInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 4, 1)
)
ocStbHostSystemDriveInfoEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostSystemDriveInfoIndex"),
    (0, "OC-STB-HOST-MIB", "ocStbHostSystemMemoryReportIndex"),
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "HOST-RESOURCES-MIB", "hrStorageIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostSystemDriveInfoEntry.setStatus("current")


class _OcStbHostSystemDriveInfoIndex_Type(Integer32):
    """Custom type ocStbHostSystemDriveInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OcStbHostSystemDriveInfoIndex_Type.__name__ = "Integer32"
_OcStbHostSystemDriveInfoIndex_Object = MibTableColumn
ocStbHostSystemDriveInfoIndex = _OcStbHostSystemDriveInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 4, 1, 1),
    _OcStbHostSystemDriveInfoIndex_Type()
)
ocStbHostSystemDriveInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemDriveInfoIndex.setStatus("current")
_OcStbHostSystemDriveInfoVendorId_Type = SnmpAdminString
_OcStbHostSystemDriveInfoVendorId_Object = MibTableColumn
ocStbHostSystemDriveInfoVendorId = _OcStbHostSystemDriveInfoVendorId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 4, 1, 2),
    _OcStbHostSystemDriveInfoVendorId_Type()
)
ocStbHostSystemDriveInfoVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemDriveInfoVendorId.setStatus("current")
_OcStbHostSystemDriveInfoProductId_Type = SnmpAdminString
_OcStbHostSystemDriveInfoProductId_Object = MibTableColumn
ocStbHostSystemDriveInfoProductId = _OcStbHostSystemDriveInfoProductId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 4, 1, 3),
    _OcStbHostSystemDriveInfoProductId_Type()
)
ocStbHostSystemDriveInfoProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemDriveInfoProductId.setStatus("current")
_OcStbHostSystemDriveInfoSerialNumber_Type = SnmpAdminString
_OcStbHostSystemDriveInfoSerialNumber_Object = MibTableColumn
ocStbHostSystemDriveInfoSerialNumber = _OcStbHostSystemDriveInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 4, 1, 4),
    _OcStbHostSystemDriveInfoSerialNumber_Type()
)
ocStbHostSystemDriveInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemDriveInfoSerialNumber.setStatus("current")


class _OcStbHostSystemDriveInfoInterfaceType_Type(Integer32):
    """Custom type ocStbHostSystemDriveInfoInterfaceType based on Integer32"""
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
        *(("ide", 1),
          ("scsi", 2),
          ("sas", 3),
          ("eSata", 4),
          ("usb", 5),
          ("other", 6))
    )


_OcStbHostSystemDriveInfoInterfaceType_Type.__name__ = "Integer32"
_OcStbHostSystemDriveInfoInterfaceType_Object = MibTableColumn
ocStbHostSystemDriveInfoInterfaceType = _OcStbHostSystemDriveInfoInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 4, 1, 5),
    _OcStbHostSystemDriveInfoInterfaceType_Type()
)
ocStbHostSystemDriveInfoInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemDriveInfoInterfaceType.setStatus("current")
_OcStbHostSystemLogging_ObjectIdentity = ObjectIdentity
ocStbHostSystemLogging = _OcStbHostSystemLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5)
)


class _OcStbHostSystemLoggingControlReset_Type(Integer32):
    """Custom type ocStbHostSystemLoggingControlReset based on Integer32"""
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
        *(("resetLog", 1),
          ("pauseLog", 2),
          ("startLog", 3),
          ("useDefaultReporting", 4))
    )


_OcStbHostSystemLoggingControlReset_Type.__name__ = "Integer32"
_OcStbHostSystemLoggingControlReset_Object = MibScalar
ocStbHostSystemLoggingControlReset = _OcStbHostSystemLoggingControlReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 1),
    _OcStbHostSystemLoggingControlReset_Type()
)
ocStbHostSystemLoggingControlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingControlReset.setStatus("current")


class _OcStbHostSystemLoggingSize_Type(Integer32):
    """Custom type ocStbHostSystemLoggingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OcStbHostSystemLoggingSize_Type.__name__ = "Integer32"
_OcStbHostSystemLoggingSize_Object = MibScalar
ocStbHostSystemLoggingSize = _OcStbHostSystemLoggingSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 2),
    _OcStbHostSystemLoggingSize_Type()
)
ocStbHostSystemLoggingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingSize.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingSize.setUnits("bytes")


class _OcStbHostSystemLoggingLevelControl_Type(Integer32):
    """Custom type ocStbHostSystemLoggingLevelControl based on Integer32"""
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
        *(("all", 1),
          ("trace", 2),
          ("debug", 3),
          ("info", 4),
          ("warn", 5),
          ("error", 6),
          ("fatal", 7),
          ("off", 8))
    )


_OcStbHostSystemLoggingLevelControl_Type.__name__ = "Integer32"
_OcStbHostSystemLoggingLevelControl_Object = MibScalar
ocStbHostSystemLoggingLevelControl = _OcStbHostSystemLoggingLevelControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 3),
    _OcStbHostSystemLoggingLevelControl_Type()
)
ocStbHostSystemLoggingLevelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingLevelControl.setStatus("current")


class _OcStbHostSystemloggingGroupControl_Type(Bits):
    """Custom type ocStbHostSystemloggingGroupControl based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("all", 1),
          ("tune", 2),
          ("serviceSelection", 3))
    )

_OcStbHostSystemloggingGroupControl_Type.__name__ = "Bits"
_OcStbHostSystemloggingGroupControl_Object = MibScalar
ocStbHostSystemloggingGroupControl = _OcStbHostSystemloggingGroupControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 4),
    _OcStbHostSystemloggingGroupControl_Type()
)
ocStbHostSystemloggingGroupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostSystemloggingGroupControl.setStatus("current")
_OcStbHostSystemLoggingEventTable_Object = MibTable
ocStbHostSystemLoggingEventTable = _OcStbHostSystemLoggingEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 5)
)
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingEventTable.setStatus("current")
_OcStbHostSystemLoggingEventEntry_Object = MibTableRow
ocStbHostSystemLoggingEventEntry = _OcStbHostSystemLoggingEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 5, 1)
)
ocStbHostSystemLoggingEventEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostSystemLoggingEventIndex"),
)
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingEventEntry.setStatus("current")


class _OcStbHostSystemLoggingEventIndex_Type(Integer32):
    """Custom type ocStbHostSystemLoggingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OcStbHostSystemLoggingEventIndex_Type.__name__ = "Integer32"
_OcStbHostSystemLoggingEventIndex_Object = MibTableColumn
ocStbHostSystemLoggingEventIndex = _OcStbHostSystemLoggingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 5, 1, 1),
    _OcStbHostSystemLoggingEventIndex_Type()
)
ocStbHostSystemLoggingEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingEventIndex.setStatus("current")


class _OcStbHostSystemLoggingEventTimeStamp_Type(OctetString):
    """Custom type ocStbHostSystemLoggingEventTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_OcStbHostSystemLoggingEventTimeStamp_Type.__name__ = "OctetString"
_OcStbHostSystemLoggingEventTimeStamp_Object = MibTableColumn
ocStbHostSystemLoggingEventTimeStamp = _OcStbHostSystemLoggingEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 5, 1, 2),
    _OcStbHostSystemLoggingEventTimeStamp_Type()
)
ocStbHostSystemLoggingEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingEventTimeStamp.setStatus("current")


class _OcStbHostSystemLoggingEventMessage_Type(SnmpAdminString):
    """Custom type ocStbHostSystemLoggingEventMessage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixedLength = 255


_OcStbHostSystemLoggingEventMessage_Type.__name__ = "SnmpAdminString"
_OcStbHostSystemLoggingEventMessage_Object = MibTableColumn
ocStbHostSystemLoggingEventMessage = _OcStbHostSystemLoggingEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 3, 5, 5, 1, 3),
    _OcStbHostSystemLoggingEventMessage_Type()
)
ocStbHostSystemLoggingEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostSystemLoggingEventMessage.setStatus("current")
_OcStbCardInfo_ObjectIdentity = ObjectIdentity
ocStbCardInfo = _OcStbCardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4)
)
_OcStbHostCardMacAddress_Type = MacAddress
_OcStbHostCardMacAddress_Object = MibScalar
ocStbHostCardMacAddress = _OcStbHostCardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 1),
    _OcStbHostCardMacAddress_Type()
)
ocStbHostCardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardMacAddress.setStatus("current")
_OcStbHostCardIpAddressType_Type = InetAddressType
_OcStbHostCardIpAddressType_Object = MibScalar
ocStbHostCardIpAddressType = _OcStbHostCardIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 2),
    _OcStbHostCardIpAddressType_Type()
)
ocStbHostCardIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardIpAddressType.setStatus("current")
_OcStbHostCardIpAddress_Type = InetAddress
_OcStbHostCardIpAddress_Object = MibScalar
ocStbHostCardIpAddress = _OcStbHostCardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 3),
    _OcStbHostCardIpAddress_Type()
)
ocStbHostCardIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardIpAddress.setStatus("current")
_OcStbHostCCMMI_ObjectIdentity = ObjectIdentity
ocStbHostCCMMI = _OcStbHostCCMMI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5)
)
_OcStbHostCCApplications_ObjectIdentity = ObjectIdentity
ocStbHostCCApplications = _OcStbHostCCApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5, 1)
)
_OcStbHostCCAppInfoTable_Object = MibTable
ocStbHostCCAppInfoTable = _OcStbHostCCAppInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ocStbHostCCAppInfoTable.setStatus("current")
_OcStbHostCCAppInfoEntry_Object = MibTableRow
ocStbHostCCAppInfoEntry = _OcStbHostCCAppInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5, 1, 1, 1)
)
ocStbHostCCAppInfoEntry.setIndexNames(
    (0, "OC-STB-HOST-MIB", "ocStbHostCCApplicationType"),
)
if mibBuilder.loadTexts:
    ocStbHostCCAppInfoEntry.setStatus("current")
_OcStbHostCCAppInfoIndex_Type = Unsigned32
_OcStbHostCCAppInfoIndex_Object = MibTableColumn
ocStbHostCCAppInfoIndex = _OcStbHostCCAppInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5, 1, 1, 1, 1),
    _OcStbHostCCAppInfoIndex_Type()
)
ocStbHostCCAppInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCCAppInfoIndex.setStatus("current")


class _OcStbHostCCApplicationType_Type(Unsigned32):
    """Custom type ocStbHostCCApplicationType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OcStbHostCCApplicationType_Type.__name__ = "Unsigned32"
_OcStbHostCCApplicationType_Object = MibTableColumn
ocStbHostCCApplicationType = _OcStbHostCCApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5, 1, 1, 1, 2),
    _OcStbHostCCApplicationType_Type()
)
ocStbHostCCApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCCApplicationType.setStatus("current")
_OcStbHostCCApplicationName_Type = SnmpAdminString
_OcStbHostCCApplicationName_Object = MibTableColumn
ocStbHostCCApplicationName = _OcStbHostCCApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5, 1, 1, 1, 3),
    _OcStbHostCCApplicationName_Type()
)
ocStbHostCCApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCCApplicationName.setStatus("current")
_OcStbHostCCApplicationVersion_Type = Unsigned32
_OcStbHostCCApplicationVersion_Object = MibTableColumn
ocStbHostCCApplicationVersion = _OcStbHostCCApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5, 1, 1, 1, 4),
    _OcStbHostCCApplicationVersion_Type()
)
ocStbHostCCApplicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCCApplicationVersion.setStatus("current")
_OcStbHostCCAppInfoPage_Type = OctetString
_OcStbHostCCAppInfoPage_Object = MibTableColumn
ocStbHostCCAppInfoPage = _OcStbHostCCAppInfoPage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 5, 1, 1, 1, 5),
    _OcStbHostCCAppInfoPage_Type()
)
ocStbHostCCAppInfoPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCCAppInfoPage.setStatus("current")
_OcStbHostSnmpProxyInfo_ObjectIdentity = ObjectIdentity
ocStbHostSnmpProxyInfo = _OcStbHostSnmpProxyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 6)
)


class _OcStbHostCardMfgId_Type(OctetString):
    """Custom type ocStbHostCardMfgId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_OcStbHostCardMfgId_Type.__name__ = "OctetString"
_OcStbHostCardMfgId_Object = MibScalar
ocStbHostCardMfgId = _OcStbHostCardMfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 6, 1),
    _OcStbHostCardMfgId_Type()
)
ocStbHostCardMfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardMfgId.setStatus("current")


class _OcStbHostCardVersion_Type(OctetString):
    """Custom type ocStbHostCardVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_OcStbHostCardVersion_Type.__name__ = "OctetString"
_OcStbHostCardVersion_Object = MibScalar
ocStbHostCardVersion = _OcStbHostCardVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 6, 2),
    _OcStbHostCardVersion_Type()
)
ocStbHostCardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardVersion.setStatus("current")
_OcStbHostCardRootOid_Type = ObjectIdentifier
_OcStbHostCardRootOid_Object = MibScalar
ocStbHostCardRootOid = _OcStbHostCardRootOid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 6, 3),
    _OcStbHostCardRootOid_Type()
)
ocStbHostCardRootOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardRootOid.setStatus("current")
_OcStbHostCardSerialNumber_Type = SnmpAdminString
_OcStbHostCardSerialNumber_Object = MibScalar
ocStbHostCardSerialNumber = _OcStbHostCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 6, 4),
    _OcStbHostCardSerialNumber_Type()
)
ocStbHostCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardSerialNumber.setStatus("current")


class _OcStbHostCardSnmpAccessControl_Type(TruthValue):
    """Custom type ocStbHostCardSnmpAccessControl based on TruthValue"""
    defaultValue = 1


_OcStbHostCardSnmpAccessControl_Type.__name__ = "TruthValue"
_OcStbHostCardSnmpAccessControl_Object = MibScalar
ocStbHostCardSnmpAccessControl = _OcStbHostCardSnmpAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 6, 5),
    _OcStbHostCardSnmpAccessControl_Type()
)
ocStbHostCardSnmpAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostCardSnmpAccessControl.setStatus("current")


class _OcStbHostCardId_Type(DisplayString):
    """Custom type ocStbHostCardId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixedLength = 17


_OcStbHostCardId_Type.__name__ = "DisplayString"
_OcStbHostCardId_Object = MibScalar
ocStbHostCardId = _OcStbHostCardId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 7),
    _OcStbHostCardId_Type()
)
ocStbHostCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardId.setStatus("current")


class _OcStbHostCardBindingStatus_Type(Integer32):
    """Custom type ocStbHostCardBindingStatus based on Integer32"""
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
        *(("unknown", 1),
          ("invalidCertificate", 2),
          ("otherAuthFailure", 3),
          ("bound", 4))
    )


_OcStbHostCardBindingStatus_Type.__name__ = "Integer32"
_OcStbHostCardBindingStatus_Object = MibScalar
ocStbHostCardBindingStatus = _OcStbHostCardBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 8),
    _OcStbHostCardBindingStatus_Type()
)
ocStbHostCardBindingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardBindingStatus.setStatus("current")


class _OcStbHostCardOpenedGenericResource_Type(OctetString):
    """Custom type ocStbHostCardOpenedGenericResource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_OcStbHostCardOpenedGenericResource_Type.__name__ = "OctetString"
_OcStbHostCardOpenedGenericResource_Object = MibScalar
ocStbHostCardOpenedGenericResource = _OcStbHostCardOpenedGenericResource_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 9),
    _OcStbHostCardOpenedGenericResource_Type()
)
ocStbHostCardOpenedGenericResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardOpenedGenericResource.setStatus("current")


class _OcStbHostCardTimeZoneOffset_Type(Integer32):
    """Custom type ocStbHostCardTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_OcStbHostCardTimeZoneOffset_Type.__name__ = "Integer32"
_OcStbHostCardTimeZoneOffset_Object = MibScalar
ocStbHostCardTimeZoneOffset = _OcStbHostCardTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 10),
    _OcStbHostCardTimeZoneOffset_Type()
)
ocStbHostCardTimeZoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardTimeZoneOffset.setStatus("current")


class _OcStbHostCardDaylightSavingsTimeDelta_Type(OctetString):
    """Custom type ocStbHostCardDaylightSavingsTimeDelta based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_OcStbHostCardDaylightSavingsTimeDelta_Type.__name__ = "OctetString"
_OcStbHostCardDaylightSavingsTimeDelta_Object = MibScalar
ocStbHostCardDaylightSavingsTimeDelta = _OcStbHostCardDaylightSavingsTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 11),
    _OcStbHostCardDaylightSavingsTimeDelta_Type()
)
ocStbHostCardDaylightSavingsTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardDaylightSavingsTimeDelta.setStatus("current")
_OcStbHostCardDaylightSavingsTimeEntry_Type = Unsigned32
_OcStbHostCardDaylightSavingsTimeEntry_Object = MibScalar
ocStbHostCardDaylightSavingsTimeEntry = _OcStbHostCardDaylightSavingsTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 12),
    _OcStbHostCardDaylightSavingsTimeEntry_Type()
)
ocStbHostCardDaylightSavingsTimeEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardDaylightSavingsTimeEntry.setStatus("current")
_OcStbHostCardDaylightSavingsTimeExit_Type = Unsigned32
_OcStbHostCardDaylightSavingsTimeExit_Object = MibScalar
ocStbHostCardDaylightSavingsTimeExit = _OcStbHostCardDaylightSavingsTimeExit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 13),
    _OcStbHostCardDaylightSavingsTimeExit_Type()
)
ocStbHostCardDaylightSavingsTimeExit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardDaylightSavingsTimeExit.setStatus("current")


class _OcStbHostCardEaLocationCode_Type(OctetString):
    """Custom type ocStbHostCardEaLocationCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_OcStbHostCardEaLocationCode_Type.__name__ = "OctetString"
_OcStbHostCardEaLocationCode_Object = MibScalar
ocStbHostCardEaLocationCode = _OcStbHostCardEaLocationCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 14),
    _OcStbHostCardEaLocationCode_Type()
)
ocStbHostCardEaLocationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardEaLocationCode.setStatus("current")


class _OcStbHostCardVctId_Type(OctetString):
    """Custom type ocStbHostCardVctId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_OcStbHostCardVctId_Type.__name__ = "OctetString"
_OcStbHostCardVctId_Object = MibScalar
ocStbHostCardVctId = _OcStbHostCardVctId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 15),
    _OcStbHostCardVctId_Type()
)
ocStbHostCardVctId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardVctId.setStatus("current")
_OcStbHostCardCpInfo_ObjectIdentity = ObjectIdentity
ocStbHostCardCpInfo = _OcStbHostCardCpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 16)
)


class _OcStbHostCardCpAuthKeyStatus_Type(Integer32):
    """Custom type ocStbHostCardCpAuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("notReady", 2))
    )


_OcStbHostCardCpAuthKeyStatus_Type.__name__ = "Integer32"
_OcStbHostCardCpAuthKeyStatus_Object = MibScalar
ocStbHostCardCpAuthKeyStatus = _OcStbHostCardCpAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 16, 1),
    _OcStbHostCardCpAuthKeyStatus_Type()
)
ocStbHostCardCpAuthKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardCpAuthKeyStatus.setStatus("current")


class _OcStbHostCardCpCertificateCheck_Type(Integer32):
    """Custom type ocStbHostCardCpCertificateCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2))
    )


_OcStbHostCardCpCertificateCheck_Type.__name__ = "Integer32"
_OcStbHostCardCpCertificateCheck_Object = MibScalar
ocStbHostCardCpCertificateCheck = _OcStbHostCardCpCertificateCheck_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 16, 2),
    _OcStbHostCardCpCertificateCheck_Type()
)
ocStbHostCardCpCertificateCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardCpCertificateCheck.setStatus("current")
_OcStbHostCardCpCciChallengeCount_Type = Counter32
_OcStbHostCardCpCciChallengeCount_Object = MibScalar
ocStbHostCardCpCciChallengeCount = _OcStbHostCardCpCciChallengeCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 16, 3),
    _OcStbHostCardCpCciChallengeCount_Type()
)
ocStbHostCardCpCciChallengeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardCpCciChallengeCount.setStatus("current")
_OcStbHostCardCpKeyGenerationReqCount_Type = Counter32
_OcStbHostCardCpKeyGenerationReqCount_Object = MibScalar
ocStbHostCardCpKeyGenerationReqCount = _OcStbHostCardCpKeyGenerationReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 16, 4),
    _OcStbHostCardCpKeyGenerationReqCount_Type()
)
ocStbHostCardCpKeyGenerationReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardCpKeyGenerationReqCount.setStatus("current")


class _OcStbHostCardCpIdList_Type(OctetString):
    """Custom type ocStbHostCardCpIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_OcStbHostCardCpIdList_Type.__name__ = "OctetString"
_OcStbHostCardCpIdList_Object = MibScalar
ocStbHostCardCpIdList = _OcStbHostCardCpIdList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 4, 16, 5),
    _OcStbHostCardCpIdList_Type()
)
ocStbHostCardCpIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCardCpIdList.setStatus("current")
_OcStbHostInfo_ObjectIdentity = ObjectIdentity
ocStbHostInfo = _OcStbHostInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5)
)
_OcStbHostIpAddressType_Type = InetAddressType
_OcStbHostIpAddressType_Object = MibScalar
ocStbHostIpAddressType = _OcStbHostIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 1),
    _OcStbHostIpAddressType_Type()
)
ocStbHostIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIpAddressType.setStatus("current")
_OcStbHostIpSubNetMask_Type = InetAddress
_OcStbHostIpSubNetMask_Object = MibScalar
ocStbHostIpSubNetMask = _OcStbHostIpSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 2),
    _OcStbHostIpSubNetMask_Type()
)
ocStbHostIpSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostIpSubNetMask.setStatus("current")


class _OcStbHostOobMessageMode_Type(Integer32):
    """Custom type ocStbHostOobMessageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scte55", 1),
          ("dsg", 2),
          ("other", 3))
    )


_OcStbHostOobMessageMode_Type.__name__ = "Integer32"
_OcStbHostOobMessageMode_Object = MibScalar
ocStbHostOobMessageMode = _OcStbHostOobMessageMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 3),
    _OcStbHostOobMessageMode_Type()
)
ocStbHostOobMessageMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostOobMessageMode.setStatus("current")
_OcStbHostDumpTrapInfo_ObjectIdentity = ObjectIdentity
ocStbHostDumpTrapInfo = _OcStbHostDumpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 4)
)


class _OcStbHostDumpEventCount_Type(Integer32):
    """Custom type ocStbHostDumpEventCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_OcStbHostDumpEventCount_Type.__name__ = "Integer32"
_OcStbHostDumpEventCount_Object = MibScalar
ocStbHostDumpEventCount = _OcStbHostDumpEventCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 4, 1),
    _OcStbHostDumpEventCount_Type()
)
ocStbHostDumpEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostDumpEventCount.setStatus("current")
_OcStbHostDumpNow_Type = TruthValue
_OcStbHostDumpNow_Object = MibScalar
ocStbHostDumpNow = _OcStbHostDumpNow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 4, 2),
    _OcStbHostDumpNow_Type()
)
ocStbHostDumpNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostDumpNow.setStatus("current")


class _OcStbHostDumpEventTimeout_Type(Unsigned32):
    """Custom type ocStbHostDumpEventTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_OcStbHostDumpEventTimeout_Type.__name__ = "Unsigned32"
_OcStbHostDumpEventTimeout_Object = MibScalar
ocStbHostDumpEventTimeout = _OcStbHostDumpEventTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 4, 3),
    _OcStbHostDumpEventTimeout_Type()
)
ocStbHostDumpEventTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostDumpEventTimeout.setStatus("current")
_OcStbHostDumpFilePath_Type = SnmpAdminString
_OcStbHostDumpFilePath_Object = MibScalar
ocStbHostDumpFilePath = _OcStbHostDumpFilePath_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 4, 4),
    _OcStbHostDumpFilePath_Type()
)
ocStbHostDumpFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostDumpFilePath.setStatus("current")
_OcStbHostSpecificationsInfo_ObjectIdentity = ObjectIdentity
ocStbHostSpecificationsInfo = _OcStbHostSpecificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 5)
)
_OcStbHostCfrSpecificationIssue_Type = SnmpAdminString
_OcStbHostCfrSpecificationIssue_Object = MibScalar
ocStbHostCfrSpecificationIssue = _OcStbHostCfrSpecificationIssue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 5, 1),
    _OcStbHostCfrSpecificationIssue_Type()
)
ocStbHostCfrSpecificationIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostCfrSpecificationIssue.setStatus("current")
_OcStbHostMibSpecificationIssue_Type = SnmpAdminString
_OcStbHostMibSpecificationIssue_Object = MibScalar
ocStbHostMibSpecificationIssue = _OcStbHostMibSpecificationIssue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 5, 2),
    _OcStbHostMibSpecificationIssue_Type()
)
ocStbHostMibSpecificationIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostMibSpecificationIssue.setStatus("current")


class _OcStbHostBootStatus_Type(Integer32):
    """Custom type ocStbHostBootStatus based on Integer32"""
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
        *(("completedSuccessfully", 1),
          ("completeWithErrors", 2),
          ("inProgressWithCodeDownload", 3),
          ("inProgressNoCodeDownload", 4),
          ("inProgressAwaitingMonitorApp", 5),
          ("unknown", 6))
    )


_OcStbHostBootStatus_Type.__name__ = "Integer32"
_OcStbHostBootStatus_Object = MibScalar
ocStbHostBootStatus = _OcStbHostBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 6),
    _OcStbHostBootStatus_Type()
)
ocStbHostBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostBootStatus.setStatus("current")
_OcStbHostContentErrorSummaryInfo_ObjectIdentity = ObjectIdentity
ocStbHostContentErrorSummaryInfo = _OcStbHostContentErrorSummaryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 7)
)
_OcStbHostPatTimeoutCount_Type = Counter32
_OcStbHostPatTimeoutCount_Object = MibScalar
ocStbHostPatTimeoutCount = _OcStbHostPatTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 7, 1),
    _OcStbHostPatTimeoutCount_Type()
)
ocStbHostPatTimeoutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostPatTimeoutCount.setStatus("current")
_OcStbHostPmtTimeoutCount_Type = Counter32
_OcStbHostPmtTimeoutCount_Object = MibScalar
ocStbHostPmtTimeoutCount = _OcStbHostPmtTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 7, 2),
    _OcStbHostPmtTimeoutCount_Type()
)
ocStbHostPmtTimeoutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostPmtTimeoutCount.setStatus("current")
_OcStbHostOobCarouselTimeoutCount_Type = Counter32
_OcStbHostOobCarouselTimeoutCount_Object = MibScalar
ocStbHostOobCarouselTimeoutCount = _OcStbHostOobCarouselTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 7, 3),
    _OcStbHostOobCarouselTimeoutCount_Type()
)
ocStbHostOobCarouselTimeoutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostOobCarouselTimeoutCount.setStatus("current")
_OcStbHostInbandCarouselTimeoutCount_Type = Counter32
_OcStbHostInbandCarouselTimeoutCount_Object = MibScalar
ocStbHostInbandCarouselTimeoutCount = _OcStbHostInbandCarouselTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 5, 7, 4),
    _OcStbHostInbandCarouselTimeoutCount_Type()
)
ocStbHostInbandCarouselTimeoutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostInbandCarouselTimeoutCount.setStatus("current")
_OcStbHostRebootInfo_ObjectIdentity = ObjectIdentity
ocStbHostRebootInfo = _OcStbHostRebootInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 6)
)


class _OcStbHostRebootType_Type(Integer32):
    """Custom type ocStbHostRebootType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("davicDocsis", 1),
          ("user", 2),
          ("system", 3),
          ("trap", 4),
          ("silentWatchdog", 5),
          ("bootloader", 6),
          ("powerup", 7),
          ("hostUpgrade", 8),
          ("hardware", 9),
          ("cablecardError", 10))
    )


_OcStbHostRebootType_Type.__name__ = "Integer32"
_OcStbHostRebootType_Object = MibScalar
ocStbHostRebootType = _OcStbHostRebootType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 6, 1),
    _OcStbHostRebootType_Type()
)
ocStbHostRebootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostRebootType.setStatus("current")
_OcStbHostRebootReset_Type = TruthValue
_OcStbHostRebootReset_Object = MibScalar
ocStbHostRebootReset = _OcStbHostRebootReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 6, 2),
    _OcStbHostRebootReset_Type()
)
ocStbHostRebootReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostRebootReset.setStatus("current")


class _OcStbHostRebootIpModeTlvChange_Type(Integer32):
    """Custom type ocStbHostRebootIpModeTlvChange based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("immediate", 2))
    )


_OcStbHostRebootIpModeTlvChange_Type.__name__ = "Integer32"
_OcStbHostRebootIpModeTlvChange_Object = MibScalar
ocStbHostRebootIpModeTlvChange = _OcStbHostRebootIpModeTlvChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 6, 3),
    _OcStbHostRebootIpModeTlvChange_Type()
)
ocStbHostRebootIpModeTlvChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocStbHostRebootIpModeTlvChange.setStatus("current")
_OcStbHostMemoryInfo_ObjectIdentity = ObjectIdentity
ocStbHostMemoryInfo = _OcStbHostMemoryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 7)
)
_OcStbHostLargestAvailableBlock_Type = Integer32
_OcStbHostLargestAvailableBlock_Object = MibScalar
ocStbHostLargestAvailableBlock = _OcStbHostLargestAvailableBlock_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 7, 1),
    _OcStbHostLargestAvailableBlock_Type()
)
ocStbHostLargestAvailableBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostLargestAvailableBlock.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostLargestAvailableBlock.setUnits("kilobytes")
_OcStbHostTotalVideoMemory_Type = Integer32
_OcStbHostTotalVideoMemory_Object = MibScalar
ocStbHostTotalVideoMemory = _OcStbHostTotalVideoMemory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 7, 2),
    _OcStbHostTotalVideoMemory_Type()
)
ocStbHostTotalVideoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostTotalVideoMemory.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostTotalVideoMemory.setUnits("kilobytes")
_OcStbHostAvailableVideoMemory_Type = Integer32
_OcStbHostAvailableVideoMemory_Object = MibScalar
ocStbHostAvailableVideoMemory = _OcStbHostAvailableVideoMemory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 7, 3),
    _OcStbHostAvailableVideoMemory_Type()
)
ocStbHostAvailableVideoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostAvailableVideoMemory.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostAvailableVideoMemory.setUnits("kilobytes")
_OcStbHostTotalSystemMemory_Type = Integer32
_OcStbHostTotalSystemMemory_Object = MibScalar
ocStbHostTotalSystemMemory = _OcStbHostTotalSystemMemory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 7, 4),
    _OcStbHostTotalSystemMemory_Type()
)
ocStbHostTotalSystemMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostTotalSystemMemory.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostTotalSystemMemory.setUnits("kilobytes")
_OcStbHostAvailableSystemMemory_Type = Integer32
_OcStbHostAvailableSystemMemory_Object = MibScalar
ocStbHostAvailableSystemMemory = _OcStbHostAvailableSystemMemory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 7, 5),
    _OcStbHostAvailableSystemMemory_Type()
)
ocStbHostAvailableSystemMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostAvailableSystemMemory.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostAvailableSystemMemory.setUnits("kilobytes")
_OcStbHostJVMInfo_ObjectIdentity = ObjectIdentity
ocStbHostJVMInfo = _OcStbHostJVMInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 8)
)
_OcStbHostJVMHeapSize_Type = Integer32
_OcStbHostJVMHeapSize_Object = MibScalar
ocStbHostJVMHeapSize = _OcStbHostJVMHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 8, 1),
    _OcStbHostJVMHeapSize_Type()
)
ocStbHostJVMHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostJVMHeapSize.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostJVMHeapSize.setUnits("kilobytes")
_OcStbHostJVMAvailHeap_Type = Integer32
_OcStbHostJVMAvailHeap_Object = MibScalar
ocStbHostJVMAvailHeap = _OcStbHostJVMAvailHeap_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 8, 2),
    _OcStbHostJVMAvailHeap_Type()
)
ocStbHostJVMAvailHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostJVMAvailHeap.setStatus("current")
if mibBuilder.loadTexts:
    ocStbHostJVMAvailHeap.setUnits("kilobytes")
_OcStbHostJVMLiveObjects_Type = Integer32
_OcStbHostJVMLiveObjects_Object = MibScalar
ocStbHostJVMLiveObjects = _OcStbHostJVMLiveObjects_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 8, 3),
    _OcStbHostJVMLiveObjects_Type()
)
ocStbHostJVMLiveObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostJVMLiveObjects.setStatus("current")
_OcStbHostJVMDeadObjects_Type = Integer32
_OcStbHostJVMDeadObjects_Object = MibScalar
ocStbHostJVMDeadObjects = _OcStbHostJVMDeadObjects_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 1, 4, 8, 4),
    _OcStbHostJVMDeadObjects_Type()
)
ocStbHostJVMDeadObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocStbHostJVMDeadObjects.setStatus("current")
_OcStbHostConformance_ObjectIdentity = ObjectIdentity
ocStbHostConformance = _OcStbHostConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2)
)
_OcStbHostMIBCompliances_ObjectIdentity = ObjectIdentity
ocStbHostMIBCompliances = _OcStbHostMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 1)
)
_OcStbHostMIBGroups_ObjectIdentity = ObjectIdentity
ocStbHostMIBGroups = _OcStbHostMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 2)
)

# Managed Objects groups

ocStbHostSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 2, 1)
)
ocStbHostSystemGroup.setObjects(
      *(("OC-STB-HOST-MIB", "ocStbHostSerialNumber"),
        ("OC-STB-HOST-MIB", "ocStbHostHostID"),
        ("OC-STB-HOST-MIB", "ocStbHostCapabilities"),
        ("OC-STB-HOST-MIB", "ocStbHostAvcSupport"),
        ("OC-STB-HOST-MIB", "ocStbHostAVInterfaceType"),
        ("OC-STB-HOST-MIB", "ocStbHostAVInterfaceDesc"),
        ("OC-STB-HOST-MIB", "ocStbHostAVInterfaceStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerModulationMode"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerFrequency"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerInterleaver"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerPower"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerAGCValue"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerSNRValue"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerUnerroreds"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerCorrecteds"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerUncorrectables"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerCarrierLockLost"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerPCRErrors"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerPTSErrors"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerState"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerBER"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerSecsSinceLock"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerEqGain"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerMainTapCoeff"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerTotalTuneCount"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerTuneFailureCount"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerTuneFailFreq"),
        ("OC-STB-HOST-MIB", "ocStbHostInBandTunerBandwidth"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394ActiveNodes"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394DataXMission"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394DTCPStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394LoopStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394RootStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394CycleIsMaster"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394IRMStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394AudioMuteStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394VideoMuteStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394ConnectedDevicesAVInterfaceIndex"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394ConnectedDevicesSubUnitType"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394ConnectedDevicesEui64"),
        ("OC-STB-HOST-MIB", "ocStbHostIEEE1394ConnectedDevicesADSourceSelectSupport"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIOutputType"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIConnectionStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIRepeaterStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIVideoXmissionStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIHDCPStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIHostDeviceHDCPStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIVideoMuteStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIOutputFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIAspectRatio"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIAudioFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIAudioSampleRate"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIAudioChannelCount"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIAudioMuteStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIAudioSampleSize"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIColorSpace"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIFrameRate"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIAttachedDeviceType"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIEdid"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMILipSyncDelay"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMICecFeatures"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIFeatures"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIMaxDeviceCount"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIEdidVersion"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMI3DCompatibilityControl"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMI3DCompatibilityMsgDisplay"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIPreferredVideoFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIAvailableVideoFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMISupported3DStructures"),
        ("OC-STB-HOST-MIB", "ocStbHostDVIHDMIActive3DStructure"),
        ("OC-STB-HOST-MIB", "ocStbHostSPDIfAudioFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostSPDIfAudioMuteStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostComponentVideoConstrainedStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostComponentOutputFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostComponentAspectRatio"),
        ("OC-STB-HOST-MIB", "ocStbHostComponentVideoMuteStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostRFChannelOut"),
        ("OC-STB-HOST-MIB", "ocStbHostRFChannelOutAudioMuteStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostRFChannelOutVideoMuteStatus"),
        ("OC-STB-HOST-MIB", "ocStbEasMessageStateCode"),
        ("OC-STB-HOST-MIB", "ocStbEasMessageCountyCode"),
        ("OC-STB-HOST-MIB", "ocStbEasMessageCountySubdivisionCode"),
        ("OC-STB-HOST-MIB", "ocStbHostProgramAVSource"),
        ("OC-STB-HOST-MIB", "ocStbHostProgramAVDestination"),
        ("OC-STB-HOST-MIB", "ocStbHostProgramContentSource"),
        ("OC-STB-HOST-MIB", "ocStbHostProgramContentDestination"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentProgramNumber"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentTransportStreamID"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentTotalStreams"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentSelectedVideoPID"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentSelectedAudioPID"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentOtherAudioPIDs"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentCCIValue"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentAPSValue"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentCITStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentBroadcastFlagStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentEPNStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentPCRPID"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentPCRLockStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentDecoderPTS"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentDiscontinuities"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentPktErrors"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentPipelineErrors"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContentDecoderRestarts"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg2ContainerFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentProgramNumber"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentTransportStreamID"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentTotalStreams"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentSelectedVideoPID"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentSelectedAudioPID"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentOtherAudioPIDs"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentCCIValue"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentAPSValue"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentCITStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentBroadcastFlagStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentEPNStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentPCRPID"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentPCRLockStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentDecoderPTS"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentDiscontinuities"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentPktErrors"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentPipelineErrors"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContentDecoderRestarts"),
        ("OC-STB-HOST-MIB", "ocStbHostMpeg4ContainerFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostVc1ContentProgramNumber"),
        ("OC-STB-HOST-MIB", "ocStbHostVc1ContainerFormat"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskFDCFreq"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskRDCFreq"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskFDCBer"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskFDCStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskFDCBytesRead"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskFDCPower"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskFDCLockedTime"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskFDCSNR"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskAGC"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskRDCPower"),
        ("OC-STB-HOST-MIB", "ocStbHostQpskRDCDataRate"),
        ("OC-STB-HOST-MIB", "ocStbHostAnalogVideoProtectionStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemLoggingControlReset"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemLoggingSize"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemLoggingLevelControl"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemloggingGroupControl"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemLoggingEventTimeStamp"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemLoggingEventMessage"))
)
if mibBuilder.loadTexts:
    ocStbHostSystemGroup.setStatus("current")

ocStbHostSoftwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 2, 2)
)
ocStbHostSoftwareGroup.setObjects(
      *(("OC-STB-HOST-MIB", "ocStbHostFirmwareImageStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostFirmwareCodeDownloadStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostFirmwareCodeObjectName"),
        ("OC-STB-HOST-MIB", "ocStbHostFirmwareDownloadFailedStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostFirmwareDownloadFailedCount"),
        ("OC-STB-HOST-MIB", "ocStbHostFirmwareDownloadGroupId"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareOCAPVersion"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareFirmwareReleaseDate"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareBootloaderVersion"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareAppNameString"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareAppVersionNumber"),
        ("OC-STB-HOST-MIB", "ocStbHostCCAppInfoIndex"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareFirmwareVersion"),
        ("OC-STB-HOST-MIB", "ocStbHostCCApplicationName"),
        ("OC-STB-HOST-MIB", "ocStbHostCCApplicationVersion"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareOrganizationId"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareApplicationId"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareApplicationInfoSigLastReceivedTime"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareApplicationInfoSigLastReadStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareApplicationInfoSigLastNetworkVersionRead"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareApplicationInfoSigVersionInUse"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareApplicationPriority"))
)
if mibBuilder.loadTexts:
    ocStbHostSoftwareGroup.setStatus("current")

ocStbHostStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 2, 3)
)
ocStbHostStatusGroup.setObjects(
      *(("OC-STB-HOST-MIB", "ocStbHostPowerStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostAcOutletStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostUserSettingsPreferedLanguage"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemTempDescr"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemTempValue"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemTempLastUpdate"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemTempMaxValue"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemMemoryReportMemoryType"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemMemoryReportMemorySize"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemDriveInfoIndex"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemDriveInfoInterfaceType"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemDriveInfoVendorId"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemDriveInfoProductId"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemDriveInfoSerialNumber"),
        ("OC-STB-HOST-MIB", "ocStbHostCardMacAddress"),
        ("OC-STB-HOST-MIB", "ocStbHostCardIpAddressType"),
        ("OC-STB-HOST-MIB", "ocStbHostCardIpAddress"),
        ("OC-STB-HOST-MIB", "ocStbHostCCApplicationType"),
        ("OC-STB-HOST-MIB", "ocStbHostCCAppInfoPage"),
        ("OC-STB-HOST-MIB", "ocStbHostCardMfgId"),
        ("OC-STB-HOST-MIB", "ocStbHostCardVersion"),
        ("OC-STB-HOST-MIB", "ocStbHostCardRootOid"),
        ("OC-STB-HOST-MIB", "ocStbHostCardSnmpAccessControl"),
        ("OC-STB-HOST-MIB", "ocStbHostCfrSpecificationIssue"),
        ("OC-STB-HOST-MIB", "ocStbHostMibSpecificationIssue"),
        ("OC-STB-HOST-MIB", "ocStbHostPatTimeoutCount"),
        ("OC-STB-HOST-MIB", "ocStbHostPmtTimeoutCount"),
        ("OC-STB-HOST-MIB", "ocStbHostOobCarouselTimeoutCount"),
        ("OC-STB-HOST-MIB", "ocStbHostInbandCarouselTimeoutCount"),
        ("OC-STB-HOST-MIB", "ocStbHostCardSerialNumber"),
        ("OC-STB-HOST-MIB", "ocStbHostCardId"),
        ("OC-STB-HOST-MIB", "ocStbHostCardBindingStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostCardOpenedGenericResource"),
        ("OC-STB-HOST-MIB", "ocStbHostCardTimeZoneOffset"),
        ("OC-STB-HOST-MIB", "ocStbHostCardDaylightSavingsTimeDelta"),
        ("OC-STB-HOST-MIB", "ocStbHostCardDaylightSavingsTimeEntry"),
        ("OC-STB-HOST-MIB", "ocStbHostCardDaylightSavingsTimeExit"),
        ("OC-STB-HOST-MIB", "ocStbHostCardEaLocationCode"),
        ("OC-STB-HOST-MIB", "ocStbHostCardVctId"),
        ("OC-STB-HOST-MIB", "ocStbHostCardCpAuthKeyStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostCardCpCertificateCheck"),
        ("OC-STB-HOST-MIB", "ocStbHostCardCpCciChallengeCount"),
        ("OC-STB-HOST-MIB", "ocStbHostCardCpKeyGenerationReqCount"),
        ("OC-STB-HOST-MIB", "ocStbHostCardCpIdList"),
        ("OC-STB-HOST-MIB", "ocStbHostIpAddressType"),
        ("OC-STB-HOST-MIB", "ocStbHostIpSubNetMask"),
        ("OC-STB-HOST-MIB", "ocStbHostOobMessageMode"),
        ("OC-STB-HOST-MIB", "ocStbHostBootStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostDumpEventCount"),
        ("OC-STB-HOST-MIB", "ocStbHostDumpNow"),
        ("OC-STB-HOST-MIB", "ocStbHostDumpEventTimeout"),
        ("OC-STB-HOST-MIB", "ocStbHostDumpFilePath"),
        ("OC-STB-HOST-MIB", "ocStbHostRebootType"),
        ("OC-STB-HOST-MIB", "ocStbHostRebootReset"),
        ("OC-STB-HOST-MIB", "ocStbHostRebootIpModeTlvChange"),
        ("OC-STB-HOST-MIB", "ocStbHostLargestAvailableBlock"),
        ("OC-STB-HOST-MIB", "ocStbHostTotalVideoMemory"),
        ("OC-STB-HOST-MIB", "ocStbHostAvailableVideoMemory"),
        ("OC-STB-HOST-MIB", "ocStbHostTotalSystemMemory"),
        ("OC-STB-HOST-MIB", "ocStbHostAvailableSystemMemory"),
        ("OC-STB-HOST-MIB", "ocStbHostJVMHeapSize"),
        ("OC-STB-HOST-MIB", "ocStbHostJVMAvailHeap"),
        ("OC-STB-HOST-MIB", "ocStbHostJVMLiveObjects"),
        ("OC-STB-HOST-MIB", "ocStbHostJVMDeadObjects"))
)
if mibBuilder.loadTexts:
    ocStbHostStatusGroup.setStatus("current")

ocStbHostSecuritySubSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 2, 4)
)
ocStbHostSecuritySubSystemGroup.setObjects(
      *(("OC-STB-HOST-MIB", "ocStbHostCASystemIdentifier"),
        ("OC-STB-HOST-MIB", "ocStbHostCAType"))
)
if mibBuilder.loadTexts:
    ocStbHostSecuritySubSystemGroup.setStatus("current")

ocStbHostDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 2, 5)
)
ocStbHostDeprecatedGroup.setObjects(
      *(("OC-STB-HOST-MIB", "ocStbHostSystemHomeNetworkMaxClients"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemHomeNetworkHostDRMStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemHomeNetworkConnectedClients"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemHomeNetworkClientMacAddress"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemHomeNetworkClientIpAddress"),
        ("OC-STB-HOST-MIB", "ocStbHostSystemHomeNetworkClientDRMStatus"),
        ("OC-STB-HOST-MIB", "ocStbHostSecurityIdentifier"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareApplicationSigStatus"))
)
if mibBuilder.loadTexts:
    ocStbHostDeprecatedGroup.setStatus("deprecated")


# Notification objects

ocStbPanicDumpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 0, 1)
)
ocStbPanicDumpTrap.setObjects(
    ("OC-STB-HOST-MIB", "ocStbHostDumpFilePath")
)
if mibBuilder.loadTexts:
    ocStbPanicDumpTrap.setStatus(
        "current"
    )


# Notifications groups

ocStbHostNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 2, 6)
)
ocStbHostNotificationGroup.setObjects(
    ("OC-STB-HOST-MIB", "ocStbPanicDumpTrap")
)
if mibBuilder.loadTexts:
    ocStbHostNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ocStbHostMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3, 1, 2, 1, 1)
)
ocStbHostMIBCompliance.setObjects(
      *(("OC-STB-HOST-MIB", "ocStbHostSystemGroup"),
        ("OC-STB-HOST-MIB", "ocStbHostSoftwareGroup"),
        ("OC-STB-HOST-MIB", "ocStbHostStatusGroup"),
        ("OC-STB-HOST-MIB", "ocStbHostSecuritySubSystemGroup"))
)
if mibBuilder.loadTexts:
    ocStbHostMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OC-STB-HOST-MIB",
    **{"VideoOutputFormat": VideoOutputFormat,
       "AudioOutputFormat": AudioOutputFormat,
       "VideoAspectRatio": VideoAspectRatio,
       "VideoContainerFormat": VideoContainerFormat,
       "ocStbHostMibModule": ocStbHostMibModule,
       "ocStbHostNotifications": ocStbHostNotifications,
       "ocStbPanicDumpTrap": ocStbPanicDumpTrap,
       "ocStbHostMibObjects": ocStbHostMibObjects,
       "ocStbHostSystem": ocStbHostSystem,
       "ocStbHostHWIdentifiers": ocStbHostHWIdentifiers,
       "ocStbHostSerialNumber": ocStbHostSerialNumber,
       "ocStbHostHostID": ocStbHostHostID,
       "ocStbHostCapabilities": ocStbHostCapabilities,
       "ocStbHostAvcSupport": ocStbHostAvcSupport,
       "ocStbHostInterfaces": ocStbHostInterfaces,
       "ocStbHostDevInterfaceTypes": ocStbHostDevInterfaceTypes,
       "ocStbHostOther": ocStbHostOther,
       "ocStbHostScte55FdcRx": ocStbHostScte55FdcRx,
       "ocStbHostScte55RdcTx": ocStbHostScte55RdcTx,
       "ocStbHostScte40FatRx": ocStbHostScte40FatRx,
       "ocStbHostBbVideoIn": ocStbHostBbVideoIn,
       "ocStbHostBbAudioIn": ocStbHostBbAudioIn,
       "ocStbHostBbVideoOut": ocStbHostBbVideoOut,
       "ocStbHostBbAudioOut": ocStbHostBbAudioOut,
       "ocStbHostRfOutCh": ocStbHostRfOutCh,
       "ocStbHostSVideoIn": ocStbHostSVideoIn,
       "ocStbHostSVideoOut": ocStbHostSVideoOut,
       "ocStbHostComponentIn": ocStbHostComponentIn,
       "ocStbHostComponentOut": ocStbHostComponentOut,
       "ocStbHostDviIn": ocStbHostDviIn,
       "ocStbHostDviOut": ocStbHostDviOut,
       "ocStbHostHdmiIn": ocStbHostHdmiIn,
       "ocStbHostHdmiOut": ocStbHostHdmiOut,
       "ocStbHostRcaSpdifIn": ocStbHostRcaSpdifIn,
       "ocStbHostRcaSpdifOut": ocStbHostRcaSpdifOut,
       "ocStbHostToslinkSpdifIn": ocStbHostToslinkSpdifIn,
       "ocStbHostToslinkSpdifOut": ocStbHostToslinkSpdifOut,
       "ocStbHostDisplayOut": ocStbHostDisplayOut,
       "ocStbHost1394In": ocStbHost1394In,
       "ocStbHost1394Out": ocStbHost1394Out,
       "ocStbHostDRIInterface": ocStbHostDRIInterface,
       "ocStbHostAVInterfaceTable": ocStbHostAVInterfaceTable,
       "ocStbHostAVInterfaceEntry": ocStbHostAVInterfaceEntry,
       "ocStbHostAVInterfaceIndex": ocStbHostAVInterfaceIndex,
       "ocStbHostAVInterfaceType": ocStbHostAVInterfaceType,
       "ocStbHostAVInterfaceDesc": ocStbHostAVInterfaceDesc,
       "ocStbHostAVInterfaceStatus": ocStbHostAVInterfaceStatus,
       "ocStbHostIEEE1394Objects": ocStbHostIEEE1394Objects,
       "ocStbHostIEEE1394Table": ocStbHostIEEE1394Table,
       "ocStbHostIEEE1394Entry": ocStbHostIEEE1394Entry,
       "ocStbHostIEEE1394ActiveNodes": ocStbHostIEEE1394ActiveNodes,
       "ocStbHostIEEE1394DataXMission": ocStbHostIEEE1394DataXMission,
       "ocStbHostIEEE1394DTCPStatus": ocStbHostIEEE1394DTCPStatus,
       "ocStbHostIEEE1394LoopStatus": ocStbHostIEEE1394LoopStatus,
       "ocStbHostIEEE1394RootStatus": ocStbHostIEEE1394RootStatus,
       "ocStbHostIEEE1394CycleIsMaster": ocStbHostIEEE1394CycleIsMaster,
       "ocStbHostIEEE1394IRMStatus": ocStbHostIEEE1394IRMStatus,
       "ocStbHostIEEE1394AudioMuteStatus": ocStbHostIEEE1394AudioMuteStatus,
       "ocStbHostIEEE1394VideoMuteStatus": ocStbHostIEEE1394VideoMuteStatus,
       "ocStbHostIEEE1394ConnectedDevicesTable": ocStbHostIEEE1394ConnectedDevicesTable,
       "ocStbHostIEEE1394ConnectedDevicesEntry": ocStbHostIEEE1394ConnectedDevicesEntry,
       "ocStbHostIEEE1394ConnectedDevicesIndex": ocStbHostIEEE1394ConnectedDevicesIndex,
       "ocStbHostIEEE1394ConnectedDevicesAVInterfaceIndex": ocStbHostIEEE1394ConnectedDevicesAVInterfaceIndex,
       "ocStbHostIEEE1394ConnectedDevicesSubUnitType": ocStbHostIEEE1394ConnectedDevicesSubUnitType,
       "ocStbHostIEEE1394ConnectedDevicesEui64": ocStbHostIEEE1394ConnectedDevicesEui64,
       "ocStbHostIEEE1394ConnectedDevicesADSourceSelectSupport": ocStbHostIEEE1394ConnectedDevicesADSourceSelectSupport,
       "ocStbHostDigitalVideoOutput": ocStbHostDigitalVideoOutput,
       "ocStbHostDVIHDMITable": ocStbHostDVIHDMITable,
       "ocStbHostDVIHDMIEntry": ocStbHostDVIHDMIEntry,
       "ocStbHostDVIHDMIOutputType": ocStbHostDVIHDMIOutputType,
       "ocStbHostDVIHDMIConnectionStatus": ocStbHostDVIHDMIConnectionStatus,
       "ocStbHostDVIHDMIRepeaterStatus": ocStbHostDVIHDMIRepeaterStatus,
       "ocStbHostDVIHDMIVideoXmissionStatus": ocStbHostDVIHDMIVideoXmissionStatus,
       "ocStbHostDVIHDMIHDCPStatus": ocStbHostDVIHDMIHDCPStatus,
       "ocStbHostDVIHDMIVideoMuteStatus": ocStbHostDVIHDMIVideoMuteStatus,
       "ocStbHostDVIHDMIOutputFormat": ocStbHostDVIHDMIOutputFormat,
       "ocStbHostDVIHDMIAspectRatio": ocStbHostDVIHDMIAspectRatio,
       "ocStbHostDVIHDMIHostDeviceHDCPStatus": ocStbHostDVIHDMIHostDeviceHDCPStatus,
       "ocStbHostDVIHDMIAudioFormat": ocStbHostDVIHDMIAudioFormat,
       "ocStbHostDVIHDMIAudioSampleRate": ocStbHostDVIHDMIAudioSampleRate,
       "ocStbHostDVIHDMIAudioChannelCount": ocStbHostDVIHDMIAudioChannelCount,
       "ocStbHostDVIHDMIAudioMuteStatus": ocStbHostDVIHDMIAudioMuteStatus,
       "ocStbHostDVIHDMIAudioSampleSize": ocStbHostDVIHDMIAudioSampleSize,
       "ocStbHostDVIHDMIColorSpace": ocStbHostDVIHDMIColorSpace,
       "ocStbHostDVIHDMIFrameRate": ocStbHostDVIHDMIFrameRate,
       "ocStbHostDVIHDMIAttachedDeviceType": ocStbHostDVIHDMIAttachedDeviceType,
       "ocStbHostDVIHDMIEdid": ocStbHostDVIHDMIEdid,
       "ocStbHostDVIHDMILipSyncDelay": ocStbHostDVIHDMILipSyncDelay,
       "ocStbHostDVIHDMICecFeatures": ocStbHostDVIHDMICecFeatures,
       "ocStbHostDVIHDMIFeatures": ocStbHostDVIHDMIFeatures,
       "ocStbHostDVIHDMIMaxDeviceCount": ocStbHostDVIHDMIMaxDeviceCount,
       "ocStbHostDVIHDMIPreferredVideoFormat": ocStbHostDVIHDMIPreferredVideoFormat,
       "ocStbHostDVIHDMIEdidVersion": ocStbHostDVIHDMIEdidVersion,
       "ocStbHostDVIHDMI3DCompatibilityControl": ocStbHostDVIHDMI3DCompatibilityControl,
       "ocStbHostDVIHDMI3DCompatibilityMsgDisplay": ocStbHostDVIHDMI3DCompatibilityMsgDisplay,
       "ocStbHostDVIHDMIAvailableVideoFormatTable": ocStbHostDVIHDMIAvailableVideoFormatTable,
       "ocStbHostDVIHDMIAvailableVideoFormatEntry": ocStbHostDVIHDMIAvailableVideoFormatEntry,
       "ocStbHostDVIHDMIAvailableVideoFormatIndex": ocStbHostDVIHDMIAvailableVideoFormatIndex,
       "ocStbHostDVIHDMIAvailableVideoFormat": ocStbHostDVIHDMIAvailableVideoFormat,
       "ocStbHostDVIHDMISupported3DStructures": ocStbHostDVIHDMISupported3DStructures,
       "ocStbHostDVIHDMIActive3DStructure": ocStbHostDVIHDMIActive3DStructure,
       "ocStbHostAnalogOutput": ocStbHostAnalogOutput,
       "ocStbHostComponentVideoTable": ocStbHostComponentVideoTable,
       "ocStbHostComponentVideoEntry": ocStbHostComponentVideoEntry,
       "ocStbHostComponentVideoConstrainedStatus": ocStbHostComponentVideoConstrainedStatus,
       "ocStbHostComponentOutputFormat": ocStbHostComponentOutputFormat,
       "ocStbHostComponentAspectRatio": ocStbHostComponentAspectRatio,
       "ocStbHostComponentVideoMuteStatus": ocStbHostComponentVideoMuteStatus,
       "ocStbHostRFChannelOutTable": ocStbHostRFChannelOutTable,
       "ocStbHostRFChannelOutEntry": ocStbHostRFChannelOutEntry,
       "ocStbHostRFChannelOut": ocStbHostRFChannelOut,
       "ocStbHostRFChannelOutAudioMuteStatus": ocStbHostRFChannelOutAudioMuteStatus,
       "ocStbHostRFChannelOutVideoMuteStatus": ocStbHostRFChannelOutVideoMuteStatus,
       "ocStbHostSPDIfTable": ocStbHostSPDIfTable,
       "ocStbHostSPDIfEntry": ocStbHostSPDIfEntry,
       "ocStbHostSPDIfAudioFormat": ocStbHostSPDIfAudioFormat,
       "ocStbHostSPDIfAudioMuteStatus": ocStbHostSPDIfAudioMuteStatus,
       "ocStbHostServiceProgramInfo": ocStbHostServiceProgramInfo,
       "ocStbHostInBandTunerTable": ocStbHostInBandTunerTable,
       "ocStbHostInBandTunerEntry": ocStbHostInBandTunerEntry,
       "ocStbHostInBandTunerModulationMode": ocStbHostInBandTunerModulationMode,
       "ocStbHostInBandTunerFrequency": ocStbHostInBandTunerFrequency,
       "ocStbHostInBandTunerInterleaver": ocStbHostInBandTunerInterleaver,
       "ocStbHostInBandTunerPower": ocStbHostInBandTunerPower,
       "ocStbHostInBandTunerAGCValue": ocStbHostInBandTunerAGCValue,
       "ocStbHostInBandTunerSNRValue": ocStbHostInBandTunerSNRValue,
       "ocStbHostInBandTunerUnerroreds": ocStbHostInBandTunerUnerroreds,
       "ocStbHostInBandTunerCorrecteds": ocStbHostInBandTunerCorrecteds,
       "ocStbHostInBandTunerUncorrectables": ocStbHostInBandTunerUncorrectables,
       "ocStbHostInBandTunerCarrierLockLost": ocStbHostInBandTunerCarrierLockLost,
       "ocStbHostInBandTunerPCRErrors": ocStbHostInBandTunerPCRErrors,
       "ocStbHostInBandTunerPTSErrors": ocStbHostInBandTunerPTSErrors,
       "ocStbHostInBandTunerState": ocStbHostInBandTunerState,
       "ocStbHostInBandTunerBER": ocStbHostInBandTunerBER,
       "ocStbHostInBandTunerSecsSinceLock": ocStbHostInBandTunerSecsSinceLock,
       "ocStbHostInBandTunerEqGain": ocStbHostInBandTunerEqGain,
       "ocStbHostInBandTunerMainTapCoeff": ocStbHostInBandTunerMainTapCoeff,
       "ocStbHostInBandTunerTotalTuneCount": ocStbHostInBandTunerTotalTuneCount,
       "ocStbHostInBandTunerTuneFailureCount": ocStbHostInBandTunerTuneFailureCount,
       "ocStbHostInBandTunerTuneFailFreq": ocStbHostInBandTunerTuneFailFreq,
       "ocStbHostInBandTunerBandwidth": ocStbHostInBandTunerBandwidth,
       "ocStbHostProgramStatusTable": ocStbHostProgramStatusTable,
       "ocStbHostProgramStatusEntry": ocStbHostProgramStatusEntry,
       "ocStbHostProgramIndex": ocStbHostProgramIndex,
       "ocStbHostProgramAVSource": ocStbHostProgramAVSource,
       "ocStbHostProgramAVDestination": ocStbHostProgramAVDestination,
       "ocStbHostProgramContentSource": ocStbHostProgramContentSource,
       "ocStbHostProgramContentDestination": ocStbHostProgramContentDestination,
       "ocStbHostMpeg2ContentTable": ocStbHostMpeg2ContentTable,
       "ocStbHostMpeg2ContentEntry": ocStbHostMpeg2ContentEntry,
       "ocStbHostMpeg2ContentIndex": ocStbHostMpeg2ContentIndex,
       "ocStbHostMpeg2ContentProgramNumber": ocStbHostMpeg2ContentProgramNumber,
       "ocStbHostMpeg2ContentTransportStreamID": ocStbHostMpeg2ContentTransportStreamID,
       "ocStbHostMpeg2ContentTotalStreams": ocStbHostMpeg2ContentTotalStreams,
       "ocStbHostMpeg2ContentSelectedVideoPID": ocStbHostMpeg2ContentSelectedVideoPID,
       "ocStbHostMpeg2ContentSelectedAudioPID": ocStbHostMpeg2ContentSelectedAudioPID,
       "ocStbHostMpeg2ContentOtherAudioPIDs": ocStbHostMpeg2ContentOtherAudioPIDs,
       "ocStbHostMpeg2ContentCCIValue": ocStbHostMpeg2ContentCCIValue,
       "ocStbHostMpeg2ContentAPSValue": ocStbHostMpeg2ContentAPSValue,
       "ocStbHostMpeg2ContentCITStatus": ocStbHostMpeg2ContentCITStatus,
       "ocStbHostMpeg2ContentBroadcastFlagStatus": ocStbHostMpeg2ContentBroadcastFlagStatus,
       "ocStbHostMpeg2ContentEPNStatus": ocStbHostMpeg2ContentEPNStatus,
       "ocStbHostMpeg2ContentPCRPID": ocStbHostMpeg2ContentPCRPID,
       "ocStbHostMpeg2ContentPCRLockStatus": ocStbHostMpeg2ContentPCRLockStatus,
       "ocStbHostMpeg2ContentDecoderPTS": ocStbHostMpeg2ContentDecoderPTS,
       "ocStbHostMpeg2ContentDiscontinuities": ocStbHostMpeg2ContentDiscontinuities,
       "ocStbHostMpeg2ContentPktErrors": ocStbHostMpeg2ContentPktErrors,
       "ocStbHostMpeg2ContentPipelineErrors": ocStbHostMpeg2ContentPipelineErrors,
       "ocStbHostMpeg2ContentDecoderRestarts": ocStbHostMpeg2ContentDecoderRestarts,
       "ocStbHostMpeg2ContainerFormat": ocStbHostMpeg2ContainerFormat,
       "ocStbHostAnalogVideoTable": ocStbHostAnalogVideoTable,
       "ocStbHostAnalogVideoEntry": ocStbHostAnalogVideoEntry,
       "ocStbHostAnalogVideoProtectionStatus": ocStbHostAnalogVideoProtectionStatus,
       "ocStbHostMpeg4ContentTable": ocStbHostMpeg4ContentTable,
       "ocStbHostMpeg4ContentEntry": ocStbHostMpeg4ContentEntry,
       "ocStbHostMpeg4ContentIndex": ocStbHostMpeg4ContentIndex,
       "ocStbHostMpeg4ContentProgramNumber": ocStbHostMpeg4ContentProgramNumber,
       "ocStbHostMpeg4ContentTransportStreamID": ocStbHostMpeg4ContentTransportStreamID,
       "ocStbHostMpeg4ContentTotalStreams": ocStbHostMpeg4ContentTotalStreams,
       "ocStbHostMpeg4ContentSelectedVideoPID": ocStbHostMpeg4ContentSelectedVideoPID,
       "ocStbHostMpeg4ContentSelectedAudioPID": ocStbHostMpeg4ContentSelectedAudioPID,
       "ocStbHostMpeg4ContentOtherAudioPIDs": ocStbHostMpeg4ContentOtherAudioPIDs,
       "ocStbHostMpeg4ContentCCIValue": ocStbHostMpeg4ContentCCIValue,
       "ocStbHostMpeg4ContentAPSValue": ocStbHostMpeg4ContentAPSValue,
       "ocStbHostMpeg4ContentCITStatus": ocStbHostMpeg4ContentCITStatus,
       "ocStbHostMpeg4ContentBroadcastFlagStatus": ocStbHostMpeg4ContentBroadcastFlagStatus,
       "ocStbHostMpeg4ContentEPNStatus": ocStbHostMpeg4ContentEPNStatus,
       "ocStbHostMpeg4ContentPCRPID": ocStbHostMpeg4ContentPCRPID,
       "ocStbHostMpeg4ContentPCRLockStatus": ocStbHostMpeg4ContentPCRLockStatus,
       "ocStbHostMpeg4ContentDecoderPTS": ocStbHostMpeg4ContentDecoderPTS,
       "ocStbHostMpeg4ContentDiscontinuities": ocStbHostMpeg4ContentDiscontinuities,
       "ocStbHostMpeg4ContentPktErrors": ocStbHostMpeg4ContentPktErrors,
       "ocStbHostMpeg4ContentPipelineErrors": ocStbHostMpeg4ContentPipelineErrors,
       "ocStbHostMpeg4ContentDecoderRestarts": ocStbHostMpeg4ContentDecoderRestarts,
       "ocStbHostMpeg4ContainerFormat": ocStbHostMpeg4ContainerFormat,
       "ocStbHostVc1ContentTable": ocStbHostVc1ContentTable,
       "ocStbHostVc1ContentEntry": ocStbHostVc1ContentEntry,
       "ocStbHostVc1ContentIndex": ocStbHostVc1ContentIndex,
       "ocStbHostVc1ContentProgramNumber": ocStbHostVc1ContentProgramNumber,
       "ocStbHostVc1ContainerFormat": ocStbHostVc1ContainerFormat,
       "ocStbHostQpskObjects": ocStbHostQpskObjects,
       "ocStbHostQpskFDCFreq": ocStbHostQpskFDCFreq,
       "ocStbHostQpskRDCFreq": ocStbHostQpskRDCFreq,
       "ocStbHostQpskFDCBer": ocStbHostQpskFDCBer,
       "ocStbHostQpskFDCStatus": ocStbHostQpskFDCStatus,
       "ocStbHostQpskFDCBytesRead": ocStbHostQpskFDCBytesRead,
       "ocStbHostQpskFDCPower": ocStbHostQpskFDCPower,
       "ocStbHostQpskFDCLockedTime": ocStbHostQpskFDCLockedTime,
       "ocStbHostQpskFDCSNR": ocStbHostQpskFDCSNR,
       "ocStbHostQpskAGC": ocStbHostQpskAGC,
       "ocStbHostQpskRDCPower": ocStbHostQpskRDCPower,
       "ocStbHostQpskRDCDataRate": ocStbHostQpskRDCDataRate,
       "ocStbHostEasObjects": ocStbHostEasObjects,
       "ocStbHostEasCodes": ocStbHostEasCodes,
       "ocStbEasMessageStateCode": ocStbEasMessageStateCode,
       "ocStbEasMessageCountyCode": ocStbEasMessageCountyCode,
       "ocStbEasMessageCountySubdivisionCode": ocStbEasMessageCountySubdivisionCode,
       "ocStbHostSecuritySubSystem": ocStbHostSecuritySubSystem,
       "ocStbHostSecurityIdentifier": ocStbHostSecurityIdentifier,
       "ocStbHostCASystemIdentifier": ocStbHostCASystemIdentifier,
       "ocStbHostCAType": ocStbHostCAType,
       "ocStbHostSoftware": ocStbHostSoftware,
       "ocStbHostDeviceSoftwareBase": ocStbHostDeviceSoftwareBase,
       "ocStbHostSoftwareFirmwareVersion": ocStbHostSoftwareFirmwareVersion,
       "ocStbHostSoftwareOCAPVersion": ocStbHostSoftwareOCAPVersion,
       "ocStbHostSoftwareFirmwareReleaseDate": ocStbHostSoftwareFirmwareReleaseDate,
       "ocStbHostSoftwareBootloaderVersion": ocStbHostSoftwareBootloaderVersion,
       "ocStbHostFirmwareDownloadStatus": ocStbHostFirmwareDownloadStatus,
       "ocStbHostFirmwareImageStatus": ocStbHostFirmwareImageStatus,
       "ocStbHostFirmwareCodeDownloadStatus": ocStbHostFirmwareCodeDownloadStatus,
       "ocStbHostFirmwareCodeObjectName": ocStbHostFirmwareCodeObjectName,
       "ocStbHostFirmwareDownloadFailedStatus": ocStbHostFirmwareDownloadFailedStatus,
       "ocStbHostFirmwareDownloadFailedCount": ocStbHostFirmwareDownloadFailedCount,
       "ocStbHostFirmwareDownloadGroupId": ocStbHostFirmwareDownloadGroupId,
       "ocStbHostSoftwareApplicationInfo": ocStbHostSoftwareApplicationInfo,
       "ocStbHostSoftwareApplicationInfoTable": ocStbHostSoftwareApplicationInfoTable,
       "ocStbHostSoftwareApplicationInfoEntry": ocStbHostSoftwareApplicationInfoEntry,
       "ocStbHostSoftwareAppNameString": ocStbHostSoftwareAppNameString,
       "ocStbHostSoftwareAppVersionNumber": ocStbHostSoftwareAppVersionNumber,
       "ocStbHostSoftwareStatus": ocStbHostSoftwareStatus,
       "ocStbHostSoftwareApplicationInfoIndex": ocStbHostSoftwareApplicationInfoIndex,
       "ocStbHostSoftwareOrganizationId": ocStbHostSoftwareOrganizationId,
       "ocStbHostSoftwareApplicationId": ocStbHostSoftwareApplicationId,
       "ocStbHostSoftwareApplicationSigStatus": ocStbHostSoftwareApplicationSigStatus,
       "ocStbHostSoftwareApplicationPriority": ocStbHostSoftwareApplicationPriority,
       "ocStbHostSoftwareApplicationInfoSigLastReceivedTime": ocStbHostSoftwareApplicationInfoSigLastReceivedTime,
       "ocStbHostSoftwareApplicationInfoSigLastReadStatus": ocStbHostSoftwareApplicationInfoSigLastReadStatus,
       "ocStbHostSoftwareApplicationInfoSigLastNetworkVersionRead": ocStbHostSoftwareApplicationInfoSigLastNetworkVersionRead,
       "ocStbHostSoftwareApplicationInfoSigVersionInUse": ocStbHostSoftwareApplicationInfoSigVersionInUse,
       "ocStbHostStatus": ocStbHostStatus,
       "ocStbHostPower": ocStbHostPower,
       "ocStbHostPowerStatus": ocStbHostPowerStatus,
       "ocStbHostAcOutletStatus": ocStbHostAcOutletStatus,
       "ocStbHostUserSettings": ocStbHostUserSettings,
       "ocStbHostUserSettingsPreferedLanguage": ocStbHostUserSettingsPreferedLanguage,
       "ocStbHostSystemObjects": ocStbHostSystemObjects,
       "ocStbHostSystemTempTable": ocStbHostSystemTempTable,
       "ocStbHostSystemTempEntry": ocStbHostSystemTempEntry,
       "ocStbHostSystemTempIndex": ocStbHostSystemTempIndex,
       "ocStbHostSystemTempDescr": ocStbHostSystemTempDescr,
       "ocStbHostSystemTempValue": ocStbHostSystemTempValue,
       "ocStbHostSystemTempLastUpdate": ocStbHostSystemTempLastUpdate,
       "ocStbHostSystemTempMaxValue": ocStbHostSystemTempMaxValue,
       "ocStbHostSystemHomeNetworkTable": ocStbHostSystemHomeNetworkTable,
       "ocStbHostSystemHomeNetworkEntry": ocStbHostSystemHomeNetworkEntry,
       "ocStbHostSystemHomeNetworkIndex": ocStbHostSystemHomeNetworkIndex,
       "ocStbHostSystemHomeNetworkMaxClients": ocStbHostSystemHomeNetworkMaxClients,
       "ocStbHostSystemHomeNetworkHostDRMStatus": ocStbHostSystemHomeNetworkHostDRMStatus,
       "ocStbHostSystemHomeNetworkConnectedClients": ocStbHostSystemHomeNetworkConnectedClients,
       "ocStbHostSystemHomeNetworkClientMacAddress": ocStbHostSystemHomeNetworkClientMacAddress,
       "ocStbHostSystemHomeNetworkClientIpAddress": ocStbHostSystemHomeNetworkClientIpAddress,
       "ocStbHostSystemHomeNetworkClientDRMStatus": ocStbHostSystemHomeNetworkClientDRMStatus,
       "ocStbHostSystemMemoryReportTable": ocStbHostSystemMemoryReportTable,
       "ocStbHostSystemMemoryReportEntry": ocStbHostSystemMemoryReportEntry,
       "ocStbHostSystemMemoryReportIndex": ocStbHostSystemMemoryReportIndex,
       "ocStbHostSystemMemoryReportMemoryType": ocStbHostSystemMemoryReportMemoryType,
       "ocStbHostSystemMemoryReportMemorySize": ocStbHostSystemMemoryReportMemorySize,
       "ocStbHostSystemDriveInfoTable": ocStbHostSystemDriveInfoTable,
       "ocStbHostSystemDriveInfoEntry": ocStbHostSystemDriveInfoEntry,
       "ocStbHostSystemDriveInfoIndex": ocStbHostSystemDriveInfoIndex,
       "ocStbHostSystemDriveInfoVendorId": ocStbHostSystemDriveInfoVendorId,
       "ocStbHostSystemDriveInfoProductId": ocStbHostSystemDriveInfoProductId,
       "ocStbHostSystemDriveInfoSerialNumber": ocStbHostSystemDriveInfoSerialNumber,
       "ocStbHostSystemDriveInfoInterfaceType": ocStbHostSystemDriveInfoInterfaceType,
       "ocStbHostSystemLogging": ocStbHostSystemLogging,
       "ocStbHostSystemLoggingControlReset": ocStbHostSystemLoggingControlReset,
       "ocStbHostSystemLoggingSize": ocStbHostSystemLoggingSize,
       "ocStbHostSystemLoggingLevelControl": ocStbHostSystemLoggingLevelControl,
       "ocStbHostSystemloggingGroupControl": ocStbHostSystemloggingGroupControl,
       "ocStbHostSystemLoggingEventTable": ocStbHostSystemLoggingEventTable,
       "ocStbHostSystemLoggingEventEntry": ocStbHostSystemLoggingEventEntry,
       "ocStbHostSystemLoggingEventIndex": ocStbHostSystemLoggingEventIndex,
       "ocStbHostSystemLoggingEventTimeStamp": ocStbHostSystemLoggingEventTimeStamp,
       "ocStbHostSystemLoggingEventMessage": ocStbHostSystemLoggingEventMessage,
       "ocStbCardInfo": ocStbCardInfo,
       "ocStbHostCardMacAddress": ocStbHostCardMacAddress,
       "ocStbHostCardIpAddressType": ocStbHostCardIpAddressType,
       "ocStbHostCardIpAddress": ocStbHostCardIpAddress,
       "ocStbHostCCMMI": ocStbHostCCMMI,
       "ocStbHostCCApplications": ocStbHostCCApplications,
       "ocStbHostCCAppInfoTable": ocStbHostCCAppInfoTable,
       "ocStbHostCCAppInfoEntry": ocStbHostCCAppInfoEntry,
       "ocStbHostCCAppInfoIndex": ocStbHostCCAppInfoIndex,
       "ocStbHostCCApplicationType": ocStbHostCCApplicationType,
       "ocStbHostCCApplicationName": ocStbHostCCApplicationName,
       "ocStbHostCCApplicationVersion": ocStbHostCCApplicationVersion,
       "ocStbHostCCAppInfoPage": ocStbHostCCAppInfoPage,
       "ocStbHostSnmpProxyInfo": ocStbHostSnmpProxyInfo,
       "ocStbHostCardMfgId": ocStbHostCardMfgId,
       "ocStbHostCardVersion": ocStbHostCardVersion,
       "ocStbHostCardRootOid": ocStbHostCardRootOid,
       "ocStbHostCardSerialNumber": ocStbHostCardSerialNumber,
       "ocStbHostCardSnmpAccessControl": ocStbHostCardSnmpAccessControl,
       "ocStbHostCardId": ocStbHostCardId,
       "ocStbHostCardBindingStatus": ocStbHostCardBindingStatus,
       "ocStbHostCardOpenedGenericResource": ocStbHostCardOpenedGenericResource,
       "ocStbHostCardTimeZoneOffset": ocStbHostCardTimeZoneOffset,
       "ocStbHostCardDaylightSavingsTimeDelta": ocStbHostCardDaylightSavingsTimeDelta,
       "ocStbHostCardDaylightSavingsTimeEntry": ocStbHostCardDaylightSavingsTimeEntry,
       "ocStbHostCardDaylightSavingsTimeExit": ocStbHostCardDaylightSavingsTimeExit,
       "ocStbHostCardEaLocationCode": ocStbHostCardEaLocationCode,
       "ocStbHostCardVctId": ocStbHostCardVctId,
       "ocStbHostCardCpInfo": ocStbHostCardCpInfo,
       "ocStbHostCardCpAuthKeyStatus": ocStbHostCardCpAuthKeyStatus,
       "ocStbHostCardCpCertificateCheck": ocStbHostCardCpCertificateCheck,
       "ocStbHostCardCpCciChallengeCount": ocStbHostCardCpCciChallengeCount,
       "ocStbHostCardCpKeyGenerationReqCount": ocStbHostCardCpKeyGenerationReqCount,
       "ocStbHostCardCpIdList": ocStbHostCardCpIdList,
       "ocStbHostInfo": ocStbHostInfo,
       "ocStbHostIpAddressType": ocStbHostIpAddressType,
       "ocStbHostIpSubNetMask": ocStbHostIpSubNetMask,
       "ocStbHostOobMessageMode": ocStbHostOobMessageMode,
       "ocStbHostDumpTrapInfo": ocStbHostDumpTrapInfo,
       "ocStbHostDumpEventCount": ocStbHostDumpEventCount,
       "ocStbHostDumpNow": ocStbHostDumpNow,
       "ocStbHostDumpEventTimeout": ocStbHostDumpEventTimeout,
       "ocStbHostDumpFilePath": ocStbHostDumpFilePath,
       "ocStbHostSpecificationsInfo": ocStbHostSpecificationsInfo,
       "ocStbHostCfrSpecificationIssue": ocStbHostCfrSpecificationIssue,
       "ocStbHostMibSpecificationIssue": ocStbHostMibSpecificationIssue,
       "ocStbHostBootStatus": ocStbHostBootStatus,
       "ocStbHostContentErrorSummaryInfo": ocStbHostContentErrorSummaryInfo,
       "ocStbHostPatTimeoutCount": ocStbHostPatTimeoutCount,
       "ocStbHostPmtTimeoutCount": ocStbHostPmtTimeoutCount,
       "ocStbHostOobCarouselTimeoutCount": ocStbHostOobCarouselTimeoutCount,
       "ocStbHostInbandCarouselTimeoutCount": ocStbHostInbandCarouselTimeoutCount,
       "ocStbHostRebootInfo": ocStbHostRebootInfo,
       "ocStbHostRebootType": ocStbHostRebootType,
       "ocStbHostRebootReset": ocStbHostRebootReset,
       "ocStbHostRebootIpModeTlvChange": ocStbHostRebootIpModeTlvChange,
       "ocStbHostMemoryInfo": ocStbHostMemoryInfo,
       "ocStbHostLargestAvailableBlock": ocStbHostLargestAvailableBlock,
       "ocStbHostTotalVideoMemory": ocStbHostTotalVideoMemory,
       "ocStbHostAvailableVideoMemory": ocStbHostAvailableVideoMemory,
       "ocStbHostTotalSystemMemory": ocStbHostTotalSystemMemory,
       "ocStbHostAvailableSystemMemory": ocStbHostAvailableSystemMemory,
       "ocStbHostJVMInfo": ocStbHostJVMInfo,
       "ocStbHostJVMHeapSize": ocStbHostJVMHeapSize,
       "ocStbHostJVMAvailHeap": ocStbHostJVMAvailHeap,
       "ocStbHostJVMLiveObjects": ocStbHostJVMLiveObjects,
       "ocStbHostJVMDeadObjects": ocStbHostJVMDeadObjects,
       "ocStbHostConformance": ocStbHostConformance,
       "ocStbHostMIBCompliances": ocStbHostMIBCompliances,
       "ocStbHostMIBCompliance": ocStbHostMIBCompliance,
       "ocStbHostMIBGroups": ocStbHostMIBGroups,
       "ocStbHostSystemGroup": ocStbHostSystemGroup,
       "ocStbHostSoftwareGroup": ocStbHostSoftwareGroup,
       "ocStbHostStatusGroup": ocStbHostStatusGroup,
       "ocStbHostSecuritySubSystemGroup": ocStbHostSecuritySubSystemGroup,
       "ocStbHostDeprecatedGroup": ocStbHostDeprecatedGroup,
       "ocStbHostNotificationGroup": ocStbHostNotificationGroup}
)
