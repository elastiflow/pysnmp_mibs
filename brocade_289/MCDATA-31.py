# SNMP MIB module (MCDATA-31) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_289/MCDATA-31.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:30:56 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fcMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 8888)
)
if mibBuilder.loadTexts:
    fcMgmtMIB.setRevisions(
        ("2000-12-04 00:00",
         "2000-11-26 00:00",
         "2000-04-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FcNameId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class FcGlobalId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class FcEventSeverity(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("emergency", 2),
          ("alert", 3),
          ("critical", 4),
          ("error", 5),
          ("warning", 6),
          ("notify", 7),
          ("info", 8),
          ("debug", 9),
          ("mark", 10))
    )



class FcUnitType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("hub", 3),
          ("switch", 4),
          ("gateway", 5),
          ("converter", 6),
          ("hba", 7),
          ("proxyAgent", 8),
          ("storageDevice", 9),
          ("host", 10),
          ("storageSubsystem", 11),
          ("module", 12),
          ("swDriver", 13),
          ("storageAccessDevice", 14))
    )



class FcPortFCClass(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("unknown", 0),
          ("classF", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7))
    )


# MIB Managed Objects in the order of their OIDs

_FcMgmtNotifications_ObjectIdentity = ObjectIdentity
fcMgmtNotifications = _FcMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 0)
)
_FcMgmtObjects_ObjectIdentity = ObjectIdentity
fcMgmtObjects = _FcMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 1)
)
_FcMgmtConfig_ObjectIdentity = ObjectIdentity
fcMgmtConfig = _FcMgmtConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1)
)
_FcConnUnitNumber_Type = Unsigned32
_FcConnUnitNumber_Object = MibScalar
fcConnUnitNumber = _FcConnUnitNumber_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 1),
    _FcConnUnitNumber_Type()
)
fcConnUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitNumber.setStatus("current")
_FcConnURL_Type = DisplayString
_FcConnURL_Object = MibScalar
fcConnURL = _FcConnURL_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 2),
    _FcConnURL_Type()
)
fcConnURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnURL.setStatus("current")
_FcConnUnitTable_Object = MibTable
fcConnUnitTable = _FcConnUnitTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fcConnUnitTable.setStatus("current")
_FcConnUnitEntry_Object = MibTableRow
fcConnUnitEntry = _FcConnUnitEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1)
)
fcConnUnitEntry.setIndexNames(
    (0, "MCDATA-31", "fcConnUnitId"),
)
if mibBuilder.loadTexts:
    fcConnUnitEntry.setStatus("current")


class _FcConnUnitId_Type(OctetString):
    """Custom type fcConnUnitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FcConnUnitId_Type.__name__ = "OctetString"
_FcConnUnitId_Object = MibTableColumn
fcConnUnitId = _FcConnUnitId_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 1),
    _FcConnUnitId_Type()
)
fcConnUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcConnUnitId.setStatus("current")
_FcConnUnitGlobalId_Type = FcGlobalId
_FcConnUnitGlobalId_Object = MibTableColumn
fcConnUnitGlobalId = _FcConnUnitGlobalId_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 2),
    _FcConnUnitGlobalId_Type()
)
fcConnUnitGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitGlobalId.setStatus("current")
_FcConnUnitType_Type = FcUnitType
_FcConnUnitType_Object = MibTableColumn
fcConnUnitType = _FcConnUnitType_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 3),
    _FcConnUnitType_Type()
)
fcConnUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitType.setStatus("current")
_FcConnUnitNumPorts_Type = Unsigned32
_FcConnUnitNumPorts_Object = MibTableColumn
fcConnUnitNumPorts = _FcConnUnitNumPorts_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 4),
    _FcConnUnitNumPorts_Type()
)
fcConnUnitNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitNumPorts.setStatus("current")


class _FcConnUnitState_Type(Integer32):
    """Custom type fcConnUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("online", 2),
          ("offline", 3))
    )


_FcConnUnitState_Type.__name__ = "Integer32"
_FcConnUnitState_Object = MibTableColumn
fcConnUnitState = _FcConnUnitState_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 5),
    _FcConnUnitState_Type()
)
fcConnUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitState.setStatus("current")


class _FcConnUnitStatus_Type(Integer32):
    """Custom type fcConnUnitStatus based on Integer32"""
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
        *(("unknown", 1),
          ("unused", 2),
          ("ok", 3),
          ("warning", 4),
          ("failed", 5))
    )


_FcConnUnitStatus_Type.__name__ = "Integer32"
_FcConnUnitStatus_Object = MibTableColumn
fcConnUnitStatus = _FcConnUnitStatus_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 6),
    _FcConnUnitStatus_Type()
)
fcConnUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitStatus.setStatus("current")
_FcConnUnitProduct_Type = SnmpAdminString
_FcConnUnitProduct_Object = MibTableColumn
fcConnUnitProduct = _FcConnUnitProduct_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 7),
    _FcConnUnitProduct_Type()
)
fcConnUnitProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitProduct.setStatus("current")
_FcConnUnitSerialNo_Type = SnmpAdminString
_FcConnUnitSerialNo_Object = MibTableColumn
fcConnUnitSerialNo = _FcConnUnitSerialNo_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 8),
    _FcConnUnitSerialNo_Type()
)
fcConnUnitSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSerialNo.setStatus("current")
_FcConnUnitUpTime_Type = TimeTicks
_FcConnUnitUpTime_Object = MibTableColumn
fcConnUnitUpTime = _FcConnUnitUpTime_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 9),
    _FcConnUnitUpTime_Type()
)
fcConnUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitUpTime.setStatus("current")
_FcConnUnitUrl_Type = DisplayString
_FcConnUnitUrl_Object = MibTableColumn
fcConnUnitUrl = _FcConnUnitUrl_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 10),
    _FcConnUnitUrl_Type()
)
fcConnUnitUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitUrl.setStatus("current")


class _FcConnUnitDomainId_Type(OctetString):
    """Custom type fcConnUnitDomainId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_FcConnUnitDomainId_Type.__name__ = "OctetString"
_FcConnUnitDomainId_Object = MibTableColumn
fcConnUnitDomainId = _FcConnUnitDomainId_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 11),
    _FcConnUnitDomainId_Type()
)
fcConnUnitDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitDomainId.setStatus("current")


class _FcConnUnitProxyMaster_Type(Integer32):
    """Custom type fcConnUnitProxyMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("no", 2),
          ("yes", 3))
    )


_FcConnUnitProxyMaster_Type.__name__ = "Integer32"
_FcConnUnitProxyMaster_Object = MibTableColumn
fcConnUnitProxyMaster = _FcConnUnitProxyMaster_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 12),
    _FcConnUnitProxyMaster_Type()
)
fcConnUnitProxyMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitProxyMaster.setStatus("current")


class _FcConnUnitPrincipal_Type(Integer32):
    """Custom type fcConnUnitPrincipal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("no", 2),
          ("yes", 3))
    )


_FcConnUnitPrincipal_Type.__name__ = "Integer32"
_FcConnUnitPrincipal_Object = MibTableColumn
fcConnUnitPrincipal = _FcConnUnitPrincipal_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 13),
    _FcConnUnitPrincipal_Type()
)
fcConnUnitPrincipal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPrincipal.setStatus("current")
_FcConnUnitNumSensors_Type = Unsigned32
_FcConnUnitNumSensors_Object = MibTableColumn
fcConnUnitNumSensors = _FcConnUnitNumSensors_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 14),
    _FcConnUnitNumSensors_Type()
)
fcConnUnitNumSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitNumSensors.setStatus("current")
_FcConnUnitNumRevs_Type = Unsigned32
_FcConnUnitNumRevs_Object = MibTableColumn
fcConnUnitNumRevs = _FcConnUnitNumRevs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 15),
    _FcConnUnitNumRevs_Type()
)
fcConnUnitNumRevs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitNumRevs.setStatus("current")


class _FcConnUnitModuleId_Type(OctetString):
    """Custom type fcConnUnitModuleId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FcConnUnitModuleId_Type.__name__ = "OctetString"
_FcConnUnitModuleId_Object = MibTableColumn
fcConnUnitModuleId = _FcConnUnitModuleId_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 16),
    _FcConnUnitModuleId_Type()
)
fcConnUnitModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitModuleId.setStatus("current")
_FcConnUnitName_Type = SnmpAdminString
_FcConnUnitName_Object = MibTableColumn
fcConnUnitName = _FcConnUnitName_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 17),
    _FcConnUnitName_Type()
)
fcConnUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnUnitName.setStatus("current")
_FcConnUnitInfo_Type = SnmpAdminString
_FcConnUnitInfo_Object = MibTableColumn
fcConnUnitInfo = _FcConnUnitInfo_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 18),
    _FcConnUnitInfo_Type()
)
fcConnUnitInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnUnitInfo.setStatus("current")


class _FcConnUnitControl_Type(Integer32):
    """Custom type fcConnUnitControl based on Integer32"""
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
        *(("unknown", 1),
          ("invalid", 2),
          ("resetConnUnitColdStart", 3),
          ("resetConnUnitWarmStart", 4),
          ("offlineConnUnit", 5),
          ("onlineConnUnit", 6))
    )


_FcConnUnitControl_Type.__name__ = "Integer32"
_FcConnUnitControl_Object = MibTableColumn
fcConnUnitControl = _FcConnUnitControl_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 19),
    _FcConnUnitControl_Type()
)
fcConnUnitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnUnitControl.setStatus("current")
_FcConnUnitContact_Type = SnmpAdminString
_FcConnUnitContact_Object = MibTableColumn
fcConnUnitContact = _FcConnUnitContact_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 20),
    _FcConnUnitContact_Type()
)
fcConnUnitContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnUnitContact.setStatus("current")
_FcConnUnitLocation_Type = SnmpAdminString
_FcConnUnitLocation_Object = MibTableColumn
fcConnUnitLocation = _FcConnUnitLocation_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 21),
    _FcConnUnitLocation_Type()
)
fcConnUnitLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnUnitLocation.setStatus("current")
_FcConnUnitEventFilter_Type = FcEventSeverity
_FcConnUnitEventFilter_Object = MibTableColumn
fcConnUnitEventFilter = _FcConnUnitEventFilter_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 22),
    _FcConnUnitEventFilter_Type()
)
fcConnUnitEventFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnUnitEventFilter.setStatus("current")
_FcConnUnitNumEvents_Type = Unsigned32
_FcConnUnitNumEvents_Object = MibTableColumn
fcConnUnitNumEvents = _FcConnUnitNumEvents_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 23),
    _FcConnUnitNumEvents_Type()
)
fcConnUnitNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitNumEvents.setStatus("current")
_FcConnUnitMaxEvents_Type = Unsigned32
_FcConnUnitMaxEvents_Object = MibTableColumn
fcConnUnitMaxEvents = _FcConnUnitMaxEvents_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 24),
    _FcConnUnitMaxEvents_Type()
)
fcConnUnitMaxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitMaxEvents.setStatus("current")
_FcConnUnitEventCurrID_Type = Unsigned32
_FcConnUnitEventCurrID_Object = MibTableColumn
fcConnUnitEventCurrID = _FcConnUnitEventCurrID_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 3, 1, 25),
    _FcConnUnitEventCurrID_Type()
)
fcConnUnitEventCurrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitEventCurrID.setStatus("current")
_FcConnUnitRevsTable_Object = MibTable
fcConnUnitRevsTable = _FcConnUnitRevsTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fcConnUnitRevsTable.setStatus("current")
_FcConnUnitRevsEntry_Object = MibTableRow
fcConnUnitRevsEntry = _FcConnUnitRevsEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 4, 1)
)
fcConnUnitRevsEntry.setIndexNames(
    (0, "MCDATA-31", "fcConnUnitId"),
    (0, "MCDATA-31", "fcConnUnitRevsIndex"),
)
if mibBuilder.loadTexts:
    fcConnUnitRevsEntry.setStatus("current")
_FcConnUnitRevsIndex_Type = Unsigned32
_FcConnUnitRevsIndex_Object = MibTableColumn
fcConnUnitRevsIndex = _FcConnUnitRevsIndex_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 4, 1, 1),
    _FcConnUnitRevsIndex_Type()
)
fcConnUnitRevsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcConnUnitRevsIndex.setStatus("current")
_FcConnUnitRevsRevision_Type = SnmpAdminString
_FcConnUnitRevsRevision_Object = MibTableColumn
fcConnUnitRevsRevision = _FcConnUnitRevsRevision_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 4, 1, 2),
    _FcConnUnitRevsRevision_Type()
)
fcConnUnitRevsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitRevsRevision.setStatus("current")
_FcConnUnitRevsDescription_Type = SnmpAdminString
_FcConnUnitRevsDescription_Object = MibTableColumn
fcConnUnitRevsDescription = _FcConnUnitRevsDescription_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 4, 1, 3),
    _FcConnUnitRevsDescription_Type()
)
fcConnUnitRevsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitRevsDescription.setStatus("current")
_FcConnUnitSensorTable_Object = MibTable
fcConnUnitSensorTable = _FcConnUnitSensorTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fcConnUnitSensorTable.setStatus("current")
_FcConnUnitSensorEntry_Object = MibTableRow
fcConnUnitSensorEntry = _FcConnUnitSensorEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5, 1)
)
fcConnUnitSensorEntry.setIndexNames(
    (0, "MCDATA-31", "fcConnUnitId"),
    (0, "MCDATA-31", "fcConnUnitSensorIndex"),
)
if mibBuilder.loadTexts:
    fcConnUnitSensorEntry.setStatus("current")
_FcConnUnitSensorIndex_Type = Unsigned32
_FcConnUnitSensorIndex_Object = MibTableColumn
fcConnUnitSensorIndex = _FcConnUnitSensorIndex_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5, 1, 1),
    _FcConnUnitSensorIndex_Type()
)
fcConnUnitSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcConnUnitSensorIndex.setStatus("current")
_FcConnUnitSensorName_Type = SnmpAdminString
_FcConnUnitSensorName_Object = MibTableColumn
fcConnUnitSensorName = _FcConnUnitSensorName_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5, 1, 2),
    _FcConnUnitSensorName_Type()
)
fcConnUnitSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSensorName.setStatus("current")


class _FcConnUnitSensorStatus_Type(Integer32):
    """Custom type fcConnUnitSensorStatus based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("ok", 3),
          ("warning", 4),
          ("failed", 5))
    )


_FcConnUnitSensorStatus_Type.__name__ = "Integer32"
_FcConnUnitSensorStatus_Object = MibTableColumn
fcConnUnitSensorStatus = _FcConnUnitSensorStatus_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5, 1, 3),
    _FcConnUnitSensorStatus_Type()
)
fcConnUnitSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSensorStatus.setStatus("current")
_FcConnUnitSensorInfo_Type = SnmpAdminString
_FcConnUnitSensorInfo_Object = MibTableColumn
fcConnUnitSensorInfo = _FcConnUnitSensorInfo_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5, 1, 4),
    _FcConnUnitSensorInfo_Type()
)
fcConnUnitSensorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSensorInfo.setStatus("current")
_FcConnUnitSensorMessage_Type = SnmpAdminString
_FcConnUnitSensorMessage_Object = MibTableColumn
fcConnUnitSensorMessage = _FcConnUnitSensorMessage_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5, 1, 5),
    _FcConnUnitSensorMessage_Type()
)
fcConnUnitSensorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSensorMessage.setStatus("current")


class _FcConnUnitSensorType_Type(Integer32):
    """Custom type fcConnUnitSensorType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("battery", 3),
          ("fan", 4),
          ("powerSupply", 5),
          ("transmitter", 6),
          ("enclosure", 7),
          ("board", 8),
          ("receiver", 9))
    )


_FcConnUnitSensorType_Type.__name__ = "Integer32"
_FcConnUnitSensorType_Object = MibTableColumn
fcConnUnitSensorType = _FcConnUnitSensorType_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5, 1, 6),
    _FcConnUnitSensorType_Type()
)
fcConnUnitSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSensorType.setStatus("current")


class _FcConnUnitSensorCharacteristic_Type(Integer32):
    """Custom type fcConnUnitSensorCharacteristic based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("temperature", 3),
          ("pressure", 4),
          ("emf", 5),
          ("currentValue", 6),
          ("airflow", 7),
          ("frequency", 8),
          ("power", 9))
    )


_FcConnUnitSensorCharacteristic_Type.__name__ = "Integer32"
_FcConnUnitSensorCharacteristic_Object = MibTableColumn
fcConnUnitSensorCharacteristic = _FcConnUnitSensorCharacteristic_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 5, 1, 7),
    _FcConnUnitSensorCharacteristic_Type()
)
fcConnUnitSensorCharacteristic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSensorCharacteristic.setStatus("current")
_FcConnUnitPortTable_Object = MibTable
fcConnUnitPortTable = _FcConnUnitPortTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fcConnUnitPortTable.setStatus("current")
_FcConnUnitPortEntry_Object = MibTableRow
fcConnUnitPortEntry = _FcConnUnitPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1)
)
fcConnUnitPortEntry.setIndexNames(
    (0, "MCDATA-31", "fcConnUnitId"),
    (0, "MCDATA-31", "fcConnUnitPortIndex"),
)
if mibBuilder.loadTexts:
    fcConnUnitPortEntry.setStatus("current")
_FcConnUnitPortIndex_Type = Unsigned32
_FcConnUnitPortIndex_Object = MibTableColumn
fcConnUnitPortIndex = _FcConnUnitPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 1),
    _FcConnUnitPortIndex_Type()
)
fcConnUnitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcConnUnitPortIndex.setStatus("current")


class _FcConnUnitPortType_Type(Integer32):
    """Custom type fcConnUnitPortType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("notPresent", 3),
          ("hubPort", 4),
          ("nPort", 5),
          ("lPort", 6),
          ("flPort", 7),
          ("fPort", 8),
          ("ePort", 9),
          ("gPort", 10),
          ("domainController", 11),
          ("hubController", 12),
          ("scsi", 13),
          ("escon", 14),
          ("lan", 15),
          ("wan", 16))
    )


_FcConnUnitPortType_Type.__name__ = "Integer32"
_FcConnUnitPortType_Object = MibTableColumn
fcConnUnitPortType = _FcConnUnitPortType_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 2),
    _FcConnUnitPortType_Type()
)
fcConnUnitPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortType.setStatus("current")
_FcConnUnitPortFCClassCap_Type = FcPortFCClass
_FcConnUnitPortFCClassCap_Object = MibTableColumn
fcConnUnitPortFCClassCap = _FcConnUnitPortFCClassCap_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 3),
    _FcConnUnitPortFCClassCap_Type()
)
fcConnUnitPortFCClassCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortFCClassCap.setStatus("current")
_FcConnUnitPortFCClassOp_Type = FcPortFCClass
_FcConnUnitPortFCClassOp_Object = MibTableColumn
fcConnUnitPortFCClassOp = _FcConnUnitPortFCClassOp_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 4),
    _FcConnUnitPortFCClassOp_Type()
)
fcConnUnitPortFCClassOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortFCClassOp.setStatus("current")


class _FcConnUnitPortState_Type(Integer32):
    """Custom type fcConnUnitPortState based on Integer32"""
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
          ("online", 2),
          ("offline", 3),
          ("bypassed", 4))
    )


_FcConnUnitPortState_Type.__name__ = "Integer32"
_FcConnUnitPortState_Object = MibTableColumn
fcConnUnitPortState = _FcConnUnitPortState_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 5),
    _FcConnUnitPortState_Type()
)
fcConnUnitPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortState.setStatus("current")


class _FcConnUnitPortStatus_Type(Integer32):
    """Custom type fcConnUnitPortStatus based on Integer32"""
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
        *(("unknown", 1),
          ("unused", 2),
          ("ok", 3),
          ("warning", 4),
          ("failure", 5),
          ("notParticipating", 6),
          ("initializing", 7),
          ("bypassed", 8))
    )


_FcConnUnitPortStatus_Type.__name__ = "Integer32"
_FcConnUnitPortStatus_Object = MibTableColumn
fcConnUnitPortStatus = _FcConnUnitPortStatus_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 6),
    _FcConnUnitPortStatus_Type()
)
fcConnUnitPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatus.setStatus("current")


class _FcConnUnitPortTransmitterType_Type(Integer32):
    """Custom type fcConnUnitPortTransmitterType based on Integer32"""
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
          ("unused", 3),
          ("shortwave", 4),
          ("longwave", 5),
          ("copper", 6),
          ("scsi", 7),
          ("longwaveNoOFC", 8),
          ("shortwaveNoOFC", 9),
          ("longwaveLED", 10))
    )


_FcConnUnitPortTransmitterType_Type.__name__ = "Integer32"
_FcConnUnitPortTransmitterType_Object = MibTableColumn
fcConnUnitPortTransmitterType = _FcConnUnitPortTransmitterType_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 7),
    _FcConnUnitPortTransmitterType_Type()
)
fcConnUnitPortTransmitterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortTransmitterType.setStatus("current")


class _FcConnUnitPortModuleType_Type(Integer32):
    """Custom type fcConnUnitPortModuleType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("gbic", 3),
          ("embedded", 4),
          ("glm", 5),
          ("gbicSerialId", 6),
          ("gbicNoSerialId", 7),
          ("gbicNotInstalled", 8),
          ("smallFormFactor", 9))
    )


_FcConnUnitPortModuleType_Type.__name__ = "Integer32"
_FcConnUnitPortModuleType_Object = MibTableColumn
fcConnUnitPortModuleType = _FcConnUnitPortModuleType_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 8),
    _FcConnUnitPortModuleType_Type()
)
fcConnUnitPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortModuleType.setStatus("current")
_FcConnUnitPortWwn_Type = FcNameId
_FcConnUnitPortWwn_Object = MibTableColumn
fcConnUnitPortWwn = _FcConnUnitPortWwn_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 9),
    _FcConnUnitPortWwn_Type()
)
fcConnUnitPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortWwn.setStatus("current")


class _FcConnUnitPortFCId_Type(OctetString):
    """Custom type fcConnUnitPortFCId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_FcConnUnitPortFCId_Type.__name__ = "OctetString"
_FcConnUnitPortFCId_Object = MibTableColumn
fcConnUnitPortFCId = _FcConnUnitPortFCId_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 10),
    _FcConnUnitPortFCId_Type()
)
fcConnUnitPortFCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortFCId.setStatus("current")
_FcConnUnitPortSerialNo_Type = SnmpAdminString
_FcConnUnitPortSerialNo_Object = MibTableColumn
fcConnUnitPortSerialNo = _FcConnUnitPortSerialNo_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 11),
    _FcConnUnitPortSerialNo_Type()
)
fcConnUnitPortSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortSerialNo.setStatus("current")
_FcConnUnitPortRevision_Type = SnmpAdminString
_FcConnUnitPortRevision_Object = MibTableColumn
fcConnUnitPortRevision = _FcConnUnitPortRevision_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 12),
    _FcConnUnitPortRevision_Type()
)
fcConnUnitPortRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortRevision.setStatus("current")
_FcConnUnitPortVendor_Type = SnmpAdminString
_FcConnUnitPortVendor_Object = MibTableColumn
fcConnUnitPortVendor = _FcConnUnitPortVendor_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 13),
    _FcConnUnitPortVendor_Type()
)
fcConnUnitPortVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortVendor.setStatus("current")
_FcConnUnitPortSpeed_Type = Gauge32
_FcConnUnitPortSpeed_Object = MibTableColumn
fcConnUnitPortSpeed = _FcConnUnitPortSpeed_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 14),
    _FcConnUnitPortSpeed_Type()
)
fcConnUnitPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fcConnUnitPortSpeed.setUnits("kilobytes per second")


class _FcConnUnitPortControl_Type(Integer32):
    """Custom type fcConnUnitPortControl based on Integer32"""
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
        *(("unknown", 1),
          ("invalid", 2),
          ("resetConnUnitPort", 3),
          ("bypassConnUnitPort", 4),
          ("unbypassConnUnitPort", 5),
          ("offlineConnUnitPort", 6),
          ("onlineConnUnitPort", 7))
    )


_FcConnUnitPortControl_Type.__name__ = "Integer32"
_FcConnUnitPortControl_Object = MibTableColumn
fcConnUnitPortControl = _FcConnUnitPortControl_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 15),
    _FcConnUnitPortControl_Type()
)
fcConnUnitPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnUnitPortControl.setStatus("current")
_FcConnUnitPortName_Type = SnmpAdminString
_FcConnUnitPortName_Object = MibTableColumn
fcConnUnitPortName = _FcConnUnitPortName_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 16),
    _FcConnUnitPortName_Type()
)
fcConnUnitPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnUnitPortName.setStatus("current")
_FcConnUnitPortPhysicalNumber_Type = Unsigned32
_FcConnUnitPortPhysicalNumber_Object = MibTableColumn
fcConnUnitPortPhysicalNumber = _FcConnUnitPortPhysicalNumber_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 17),
    _FcConnUnitPortPhysicalNumber_Type()
)
fcConnUnitPortPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortPhysicalNumber.setStatus("current")


class _FcConnUnitPortProtocolCap_Type(OctetString):
    """Custom type fcConnUnitPortProtocolCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FcConnUnitPortProtocolCap_Type.__name__ = "OctetString"
_FcConnUnitPortProtocolCap_Object = MibTableColumn
fcConnUnitPortProtocolCap = _FcConnUnitPortProtocolCap_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 18),
    _FcConnUnitPortProtocolCap_Type()
)
fcConnUnitPortProtocolCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortProtocolCap.setStatus("current")


class _FcConnUnitPortProtocolOp_Type(OctetString):
    """Custom type fcConnUnitPortProtocolOp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FcConnUnitPortProtocolOp_Type.__name__ = "OctetString"
_FcConnUnitPortProtocolOp_Object = MibTableColumn
fcConnUnitPortProtocolOp = _FcConnUnitPortProtocolOp_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 19),
    _FcConnUnitPortProtocolOp_Type()
)
fcConnUnitPortProtocolOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortProtocolOp.setStatus("current")
_FcConnUnitPortNodeWwn_Type = FcNameId
_FcConnUnitPortNodeWwn_Object = MibTableColumn
fcConnUnitPortNodeWwn = _FcConnUnitPortNodeWwn_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 20),
    _FcConnUnitPortNodeWwn_Type()
)
fcConnUnitPortNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortNodeWwn.setStatus("current")


class _FcConnUnitPortHWState_Type(Integer32):
    """Custom type fcConnUnitPortHWState based on Integer32"""
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
        *(("unknown", 1),
          ("failed", 2),
          ("bypassed", 3),
          ("active", 4),
          ("loopback", 5),
          ("txfault", 6),
          ("noMedia", 7),
          ("linkDown", 8))
    )


_FcConnUnitPortHWState_Type.__name__ = "Integer32"
_FcConnUnitPortHWState_Object = MibTableColumn
fcConnUnitPortHWState = _FcConnUnitPortHWState_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 6, 1, 21),
    _FcConnUnitPortHWState_Type()
)
fcConnUnitPortHWState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortHWState.setStatus("current")
_FcConnUnitEventTable_Object = MibTable
fcConnUnitEventTable = _FcConnUnitEventTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fcConnUnitEventTable.setStatus("current")
_FcConnUnitEventEntry_Object = MibTableRow
fcConnUnitEventEntry = _FcConnUnitEventEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7, 1)
)
fcConnUnitEventEntry.setIndexNames(
    (0, "MCDATA-31", "fcConnUnitId"),
    (0, "MCDATA-31", "fcConnUnitEventIndex"),
)
if mibBuilder.loadTexts:
    fcConnUnitEventEntry.setStatus("current")
_FcConnUnitEventIndex_Type = Unsigned32
_FcConnUnitEventIndex_Object = MibTableColumn
fcConnUnitEventIndex = _FcConnUnitEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7, 1, 1),
    _FcConnUnitEventIndex_Type()
)
fcConnUnitEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitEventIndex.setStatus("current")


class _FcConnUnitREventTime_Type(DisplayString):
    """Custom type fcConnUnitREventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_FcConnUnitREventTime_Type.__name__ = "DisplayString"
_FcConnUnitREventTime_Object = MibTableColumn
fcConnUnitREventTime = _FcConnUnitREventTime_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7, 1, 2),
    _FcConnUnitREventTime_Type()
)
fcConnUnitREventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitREventTime.setStatus("current")
_FcConnUnitSEventTime_Type = TimeTicks
_FcConnUnitSEventTime_Object = MibTableColumn
fcConnUnitSEventTime = _FcConnUnitSEventTime_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7, 1, 3),
    _FcConnUnitSEventTime_Type()
)
fcConnUnitSEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSEventTime.setStatus("current")
_FcConnUnitEventSeverity_Type = FcEventSeverity
_FcConnUnitEventSeverity_Object = MibTableColumn
fcConnUnitEventSeverity = _FcConnUnitEventSeverity_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7, 1, 4),
    _FcConnUnitEventSeverity_Type()
)
fcConnUnitEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitEventSeverity.setStatus("current")


class _FcConnUnitEventType_Type(Integer32):
    """Custom type fcConnUnitEventType based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("status", 3),
          ("configuration", 4),
          ("topology", 5))
    )


_FcConnUnitEventType_Type.__name__ = "Integer32"
_FcConnUnitEventType_Object = MibTableColumn
fcConnUnitEventType = _FcConnUnitEventType_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7, 1, 5),
    _FcConnUnitEventType_Type()
)
fcConnUnitEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitEventType.setStatus("current")
_FcConnUnitEventObject_Type = ObjectIdentifier
_FcConnUnitEventObject_Object = MibTableColumn
fcConnUnitEventObject = _FcConnUnitEventObject_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7, 1, 6),
    _FcConnUnitEventObject_Type()
)
fcConnUnitEventObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitEventObject.setStatus("current")
_FcConnUnitEventDescr_Type = SnmpAdminString
_FcConnUnitEventDescr_Object = MibTableColumn
fcConnUnitEventDescr = _FcConnUnitEventDescr_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 7, 1, 7),
    _FcConnUnitEventDescr_Type()
)
fcConnUnitEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitEventDescr.setStatus("current")
_FcConnUnitLinkTable_Object = MibTable
fcConnUnitLinkTable = _FcConnUnitLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8)
)
if mibBuilder.loadTexts:
    fcConnUnitLinkTable.setStatus("current")
_FcConnUnitLinkEntry_Object = MibTableRow
fcConnUnitLinkEntry = _FcConnUnitLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1)
)
fcConnUnitLinkEntry.setIndexNames(
    (0, "MCDATA-31", "fcConnUnitId"),
    (0, "MCDATA-31", "fcConnUnitLinkIndex"),
)
if mibBuilder.loadTexts:
    fcConnUnitLinkEntry.setStatus("current")
_FcConnUnitLinkIndex_Type = Unsigned32
_FcConnUnitLinkIndex_Object = MibTableColumn
fcConnUnitLinkIndex = _FcConnUnitLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 1),
    _FcConnUnitLinkIndex_Type()
)
fcConnUnitLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkIndex.setStatus("current")


class _FcConnUnitLinkNodeIdX_Type(OctetString):
    """Custom type fcConnUnitLinkNodeIdX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_FcConnUnitLinkNodeIdX_Type.__name__ = "OctetString"
_FcConnUnitLinkNodeIdX_Object = MibTableColumn
fcConnUnitLinkNodeIdX = _FcConnUnitLinkNodeIdX_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 2),
    _FcConnUnitLinkNodeIdX_Type()
)
fcConnUnitLinkNodeIdX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkNodeIdX.setStatus("current")
_FcConnUnitLinkPortNumberX_Type = Integer32
_FcConnUnitLinkPortNumberX_Object = MibTableColumn
fcConnUnitLinkPortNumberX = _FcConnUnitLinkPortNumberX_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 3),
    _FcConnUnitLinkPortNumberX_Type()
)
fcConnUnitLinkPortNumberX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkPortNumberX.setStatus("current")


class _FcConnUnitLinkPortWwnX_Type(OctetString):
    """Custom type fcConnUnitLinkPortWwnX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FcConnUnitLinkPortWwnX_Type.__name__ = "OctetString"
_FcConnUnitLinkPortWwnX_Object = MibTableColumn
fcConnUnitLinkPortWwnX = _FcConnUnitLinkPortWwnX_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 4),
    _FcConnUnitLinkPortWwnX_Type()
)
fcConnUnitLinkPortWwnX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkPortWwnX.setStatus("current")


class _FcConnUnitLinkNodeIdY_Type(OctetString):
    """Custom type fcConnUnitLinkNodeIdY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_FcConnUnitLinkNodeIdY_Type.__name__ = "OctetString"
_FcConnUnitLinkNodeIdY_Object = MibTableColumn
fcConnUnitLinkNodeIdY = _FcConnUnitLinkNodeIdY_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 5),
    _FcConnUnitLinkNodeIdY_Type()
)
fcConnUnitLinkNodeIdY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkNodeIdY.setStatus("current")
_FcConnUnitLinkPortNumberY_Type = Integer32
_FcConnUnitLinkPortNumberY_Object = MibTableColumn
fcConnUnitLinkPortNumberY = _FcConnUnitLinkPortNumberY_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 6),
    _FcConnUnitLinkPortNumberY_Type()
)
fcConnUnitLinkPortNumberY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkPortNumberY.setStatus("current")


class _FcConnUnitLinkPortWwnY_Type(OctetString):
    """Custom type fcConnUnitLinkPortWwnY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FcConnUnitLinkPortWwnY_Type.__name__ = "OctetString"
_FcConnUnitLinkPortWwnY_Object = MibTableColumn
fcConnUnitLinkPortWwnY = _FcConnUnitLinkPortWwnY_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 7),
    _FcConnUnitLinkPortWwnY_Type()
)
fcConnUnitLinkPortWwnY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkPortWwnY.setStatus("current")


class _FcConnUnitLinkAgentAddressY_Type(OctetString):
    """Custom type fcConnUnitLinkAgentAddressY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FcConnUnitLinkAgentAddressY_Type.__name__ = "OctetString"
_FcConnUnitLinkAgentAddressY_Object = MibTableColumn
fcConnUnitLinkAgentAddressY = _FcConnUnitLinkAgentAddressY_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 8),
    _FcConnUnitLinkAgentAddressY_Type()
)
fcConnUnitLinkAgentAddressY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkAgentAddressY.setStatus("current")
_FcConnUnitLinkAgentAddressTypeY_Type = Unsigned32
_FcConnUnitLinkAgentAddressTypeY_Object = MibTableColumn
fcConnUnitLinkAgentAddressTypeY = _FcConnUnitLinkAgentAddressTypeY_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 9),
    _FcConnUnitLinkAgentAddressTypeY_Type()
)
fcConnUnitLinkAgentAddressTypeY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkAgentAddressTypeY.setStatus("current")
_FcConnUnitLinkAgentPortY_Type = Unsigned32
_FcConnUnitLinkAgentPortY_Object = MibTableColumn
fcConnUnitLinkAgentPortY = _FcConnUnitLinkAgentPortY_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 10),
    _FcConnUnitLinkAgentPortY_Type()
)
fcConnUnitLinkAgentPortY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkAgentPortY.setStatus("current")
_FcConnUnitLinkUnitTypeY_Type = FcUnitType
_FcConnUnitLinkUnitTypeY_Object = MibTableColumn
fcConnUnitLinkUnitTypeY = _FcConnUnitLinkUnitTypeY_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 11),
    _FcConnUnitLinkUnitTypeY_Type()
)
fcConnUnitLinkUnitTypeY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkUnitTypeY.setStatus("current")


class _FcConnUnitLinkConnIdY_Type(OctetString):
    """Custom type fcConnUnitLinkConnIdY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_FcConnUnitLinkConnIdY_Type.__name__ = "OctetString"
_FcConnUnitLinkConnIdY_Object = MibTableColumn
fcConnUnitLinkConnIdY = _FcConnUnitLinkConnIdY_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 8, 1, 12),
    _FcConnUnitLinkConnIdY_Type()
)
fcConnUnitLinkConnIdY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitLinkConnIdY.setStatus("current")
_FcConnUnitSnsMaxRows_Type = Counter32
_FcConnUnitSnsMaxRows_Object = MibScalar
fcConnUnitSnsMaxRows = _FcConnUnitSnsMaxRows_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 1, 9),
    _FcConnUnitSnsMaxRows_Type()
)
fcConnUnitSnsMaxRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsMaxRows.setStatus("current")
_FcMgmtNotifyFilter_ObjectIdentity = ObjectIdentity
fcMgmtNotifyFilter = _FcMgmtNotifyFilter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2)
)
_FcTrapMaxClients_Type = Unsigned32
_FcTrapMaxClients_Object = MibScalar
fcTrapMaxClients = _FcTrapMaxClients_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2, 1),
    _FcTrapMaxClients_Type()
)
fcTrapMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTrapMaxClients.setStatus("current")
_FcTrapClientCount_Type = Unsigned32
_FcTrapClientCount_Object = MibScalar
fcTrapClientCount = _FcTrapClientCount_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2, 2),
    _FcTrapClientCount_Type()
)
fcTrapClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTrapClientCount.setStatus("current")
_FcTrapRegTable_Object = MibTable
fcTrapRegTable = _FcTrapRegTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fcTrapRegTable.setStatus("current")
_FcTrapRegEntry_Object = MibTableRow
fcTrapRegEntry = _FcTrapRegEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2, 3, 1)
)
fcTrapRegEntry.setIndexNames(
    (0, "MCDATA-31", "fcTrapRegIpAddress"),
    (0, "MCDATA-31", "fcTrapRegPort"),
)
if mibBuilder.loadTexts:
    fcTrapRegEntry.setStatus("current")
_FcTrapRegIpAddress_Type = IpAddress
_FcTrapRegIpAddress_Object = MibTableColumn
fcTrapRegIpAddress = _FcTrapRegIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2, 3, 1, 1),
    _FcTrapRegIpAddress_Type()
)
fcTrapRegIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTrapRegIpAddress.setStatus("current")


class _FcTrapRegPort_Type(Unsigned32):
    """Custom type fcTrapRegPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcTrapRegPort_Type.__name__ = "Unsigned32"
_FcTrapRegPort_Object = MibTableColumn
fcTrapRegPort = _FcTrapRegPort_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2, 3, 1, 2),
    _FcTrapRegPort_Type()
)
fcTrapRegPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTrapRegPort.setStatus("current")
_FcTrapRegFilter_Type = FcEventSeverity
_FcTrapRegFilter_Object = MibTableColumn
fcTrapRegFilter = _FcTrapRegFilter_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2, 3, 1, 3),
    _FcTrapRegFilter_Type()
)
fcTrapRegFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTrapRegFilter.setStatus("current")
_FcTrapRegRowState_Type = RowStatus
_FcTrapRegRowState_Object = MibTableColumn
fcTrapRegRowState = _FcTrapRegRowState_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 2, 3, 1, 4),
    _FcTrapRegRowState_Type()
)
fcTrapRegRowState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTrapRegRowState.setStatus("current")
_FcMgmtStatistics_ObjectIdentity = ObjectIdentity
fcMgmtStatistics = _FcMgmtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3)
)
_FcConnUnitPortStatTable_Object = MibTable
fcConnUnitPortStatTable = _FcConnUnitPortStatTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fcConnUnitPortStatTable.setStatus("current")
_FcConnUnitPortStatEntry_Object = MibTableRow
fcConnUnitPortStatEntry = _FcConnUnitPortStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1)
)
fcConnUnitPortStatEntry.setIndexNames(
    (0, "MCDATA-31", "fcConnUnitId"),
    (0, "MCDATA-31", "fcConnUnitPortStatIndex"),
)
if mibBuilder.loadTexts:
    fcConnUnitPortStatEntry.setStatus("current")
_FcConnUnitPortStatIndex_Type = Unsigned32
_FcConnUnitPortStatIndex_Object = MibTableColumn
fcConnUnitPortStatIndex = _FcConnUnitPortStatIndex_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 1),
    _FcConnUnitPortStatIndex_Type()
)
fcConnUnitPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatIndex.setStatus("current")
_FcConnUnitPortStatErrs_Type = Counter64
_FcConnUnitPortStatErrs_Object = MibTableColumn
fcConnUnitPortStatErrs = _FcConnUnitPortStatErrs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 2),
    _FcConnUnitPortStatErrs_Type()
)
fcConnUnitPortStatErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatErrs.setStatus("current")
_FcConnUnitPortStatTxObjects_Type = Counter64
_FcConnUnitPortStatTxObjects_Object = MibTableColumn
fcConnUnitPortStatTxObjects = _FcConnUnitPortStatTxObjects_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 3),
    _FcConnUnitPortStatTxObjects_Type()
)
fcConnUnitPortStatTxObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatTxObjects.setStatus("current")
_FcConnUnitPortStatRxObjects_Type = Counter64
_FcConnUnitPortStatRxObjects_Object = MibTableColumn
fcConnUnitPortStatRxObjects = _FcConnUnitPortStatRxObjects_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 4),
    _FcConnUnitPortStatRxObjects_Type()
)
fcConnUnitPortStatRxObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatRxObjects.setStatus("current")
_FcConnUnitPortStatTxElements_Type = Counter64
_FcConnUnitPortStatTxElements_Object = MibTableColumn
fcConnUnitPortStatTxElements = _FcConnUnitPortStatTxElements_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 5),
    _FcConnUnitPortStatTxElements_Type()
)
fcConnUnitPortStatTxElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatTxElements.setStatus("current")
_FcConnUnitPortStatRxElements_Type = Counter64
_FcConnUnitPortStatRxElements_Object = MibTableColumn
fcConnUnitPortStatRxElements = _FcConnUnitPortStatRxElements_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 6),
    _FcConnUnitPortStatRxElements_Type()
)
fcConnUnitPortStatRxElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatRxElements.setStatus("current")
_FcConnUnitPortStatBBCreditZero_Type = Counter64
_FcConnUnitPortStatBBCreditZero_Object = MibTableColumn
fcConnUnitPortStatBBCreditZero = _FcConnUnitPortStatBBCreditZero_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 7),
    _FcConnUnitPortStatBBCreditZero_Type()
)
fcConnUnitPortStatBBCreditZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatBBCreditZero.setStatus("current")
_FcConnUnitPortStatInputBuffsFull_Type = Counter64
_FcConnUnitPortStatInputBuffsFull_Object = MibTableColumn
fcConnUnitPortStatInputBuffsFull = _FcConnUnitPortStatInputBuffsFull_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 8),
    _FcConnUnitPortStatInputBuffsFull_Type()
)
fcConnUnitPortStatInputBuffsFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatInputBuffsFull.setStatus("current")
_FcConnUnitPortStatFBSYFrames_Type = Counter64
_FcConnUnitPortStatFBSYFrames_Object = MibTableColumn
fcConnUnitPortStatFBSYFrames = _FcConnUnitPortStatFBSYFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 9),
    _FcConnUnitPortStatFBSYFrames_Type()
)
fcConnUnitPortStatFBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatFBSYFrames.setStatus("current")
_FcConnUnitPortStatPBSYFrames_Type = Counter64
_FcConnUnitPortStatPBSYFrames_Object = MibTableColumn
fcConnUnitPortStatPBSYFrames = _FcConnUnitPortStatPBSYFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 10),
    _FcConnUnitPortStatPBSYFrames_Type()
)
fcConnUnitPortStatPBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatPBSYFrames.setStatus("current")
_FcConnUnitPortStatFRJTFrames_Type = Counter64
_FcConnUnitPortStatFRJTFrames_Object = MibTableColumn
fcConnUnitPortStatFRJTFrames = _FcConnUnitPortStatFRJTFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 11),
    _FcConnUnitPortStatFRJTFrames_Type()
)
fcConnUnitPortStatFRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatFRJTFrames.setStatus("current")
_FcConnUnitPortStatPRJTFrames_Type = Counter64
_FcConnUnitPortStatPRJTFrames_Object = MibTableColumn
fcConnUnitPortStatPRJTFrames = _FcConnUnitPortStatPRJTFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 12),
    _FcConnUnitPortStatPRJTFrames_Type()
)
fcConnUnitPortStatPRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatPRJTFrames.setStatus("current")
_FcConnUnitPortStatC1RxFrames_Type = Counter64
_FcConnUnitPortStatC1RxFrames_Object = MibTableColumn
fcConnUnitPortStatC1RxFrames = _FcConnUnitPortStatC1RxFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 13),
    _FcConnUnitPortStatC1RxFrames_Type()
)
fcConnUnitPortStatC1RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC1RxFrames.setStatus("current")
_FcConnUnitPortStatC1TxFrames_Type = Counter64
_FcConnUnitPortStatC1TxFrames_Object = MibTableColumn
fcConnUnitPortStatC1TxFrames = _FcConnUnitPortStatC1TxFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 14),
    _FcConnUnitPortStatC1TxFrames_Type()
)
fcConnUnitPortStatC1TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC1TxFrames.setStatus("current")
_FcConnUnitPortStatC1FBSYFrames_Type = Counter64
_FcConnUnitPortStatC1FBSYFrames_Object = MibTableColumn
fcConnUnitPortStatC1FBSYFrames = _FcConnUnitPortStatC1FBSYFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 15),
    _FcConnUnitPortStatC1FBSYFrames_Type()
)
fcConnUnitPortStatC1FBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC1FBSYFrames.setStatus("current")
_FcConnUnitPortStatC1PBSYFrames_Type = Counter64
_FcConnUnitPortStatC1PBSYFrames_Object = MibTableColumn
fcConnUnitPortStatC1PBSYFrames = _FcConnUnitPortStatC1PBSYFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 16),
    _FcConnUnitPortStatC1PBSYFrames_Type()
)
fcConnUnitPortStatC1PBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC1PBSYFrames.setStatus("current")
_FcConnUnitPortStatC1FRJTFrames_Type = Counter64
_FcConnUnitPortStatC1FRJTFrames_Object = MibTableColumn
fcConnUnitPortStatC1FRJTFrames = _FcConnUnitPortStatC1FRJTFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 17),
    _FcConnUnitPortStatC1FRJTFrames_Type()
)
fcConnUnitPortStatC1FRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC1FRJTFrames.setStatus("current")
_FcConnUnitPortStatC1PRJTFrames_Type = Counter64
_FcConnUnitPortStatC1PRJTFrames_Object = MibTableColumn
fcConnUnitPortStatC1PRJTFrames = _FcConnUnitPortStatC1PRJTFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 18),
    _FcConnUnitPortStatC1PRJTFrames_Type()
)
fcConnUnitPortStatC1PRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC1PRJTFrames.setStatus("current")
_FcConnUnitPortStatC2RxFrames_Type = Counter64
_FcConnUnitPortStatC2RxFrames_Object = MibTableColumn
fcConnUnitPortStatC2RxFrames = _FcConnUnitPortStatC2RxFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 19),
    _FcConnUnitPortStatC2RxFrames_Type()
)
fcConnUnitPortStatC2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC2RxFrames.setStatus("current")
_FcConnUnitPortStatC2TxFrames_Type = Counter64
_FcConnUnitPortStatC2TxFrames_Object = MibTableColumn
fcConnUnitPortStatC2TxFrames = _FcConnUnitPortStatC2TxFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 20),
    _FcConnUnitPortStatC2TxFrames_Type()
)
fcConnUnitPortStatC2TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC2TxFrames.setStatus("current")
_FcConnUnitPortStatC2FBSYFrames_Type = Counter64
_FcConnUnitPortStatC2FBSYFrames_Object = MibTableColumn
fcConnUnitPortStatC2FBSYFrames = _FcConnUnitPortStatC2FBSYFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 21),
    _FcConnUnitPortStatC2FBSYFrames_Type()
)
fcConnUnitPortStatC2FBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC2FBSYFrames.setStatus("current")
_FcConnUnitPortStatC2PBSYFrames_Type = Counter64
_FcConnUnitPortStatC2PBSYFrames_Object = MibTableColumn
fcConnUnitPortStatC2PBSYFrames = _FcConnUnitPortStatC2PBSYFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 22),
    _FcConnUnitPortStatC2PBSYFrames_Type()
)
fcConnUnitPortStatC2PBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC2PBSYFrames.setStatus("current")
_FcConnUnitPortStatC2FRJTFrames_Type = Counter64
_FcConnUnitPortStatC2FRJTFrames_Object = MibTableColumn
fcConnUnitPortStatC2FRJTFrames = _FcConnUnitPortStatC2FRJTFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 23),
    _FcConnUnitPortStatC2FRJTFrames_Type()
)
fcConnUnitPortStatC2FRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC2FRJTFrames.setStatus("current")
_FcConnUnitPortStatC2PRJTFrames_Type = Counter64
_FcConnUnitPortStatC2PRJTFrames_Object = MibTableColumn
fcConnUnitPortStatC2PRJTFrames = _FcConnUnitPortStatC2PRJTFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 24),
    _FcConnUnitPortStatC2PRJTFrames_Type()
)
fcConnUnitPortStatC2PRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC2PRJTFrames.setStatus("current")
_FcConnUnitPortStatC3RxFrames_Type = Counter64
_FcConnUnitPortStatC3RxFrames_Object = MibTableColumn
fcConnUnitPortStatC3RxFrames = _FcConnUnitPortStatC3RxFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 25),
    _FcConnUnitPortStatC3RxFrames_Type()
)
fcConnUnitPortStatC3RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC3RxFrames.setStatus("current")
_FcConnUnitPortStatC3TxFrames_Type = Counter64
_FcConnUnitPortStatC3TxFrames_Object = MibTableColumn
fcConnUnitPortStatC3TxFrames = _FcConnUnitPortStatC3TxFrames_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 26),
    _FcConnUnitPortStatC3TxFrames_Type()
)
fcConnUnitPortStatC3TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC3TxFrames.setStatus("current")
_FcConnUnitPortStatC3Discards_Type = Counter64
_FcConnUnitPortStatC3Discards_Object = MibTableColumn
fcConnUnitPortStatC3Discards = _FcConnUnitPortStatC3Discards_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 27),
    _FcConnUnitPortStatC3Discards_Type()
)
fcConnUnitPortStatC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatC3Discards.setStatus("current")
_FcConnUnitPortStatRxMcastObjects_Type = Counter64
_FcConnUnitPortStatRxMcastObjects_Object = MibTableColumn
fcConnUnitPortStatRxMcastObjects = _FcConnUnitPortStatRxMcastObjects_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 28),
    _FcConnUnitPortStatRxMcastObjects_Type()
)
fcConnUnitPortStatRxMcastObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatRxMcastObjects.setStatus("current")
_FcConnUnitPortStatTxMcastObjects_Type = Counter64
_FcConnUnitPortStatTxMcastObjects_Object = MibTableColumn
fcConnUnitPortStatTxMcastObjects = _FcConnUnitPortStatTxMcastObjects_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 29),
    _FcConnUnitPortStatTxMcastObjects_Type()
)
fcConnUnitPortStatTxMcastObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatTxMcastObjects.setStatus("current")
_FcConnUnitPortStatRxBcastObjects_Type = Counter64
_FcConnUnitPortStatRxBcastObjects_Object = MibTableColumn
fcConnUnitPortStatRxBcastObjects = _FcConnUnitPortStatRxBcastObjects_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 30),
    _FcConnUnitPortStatRxBcastObjects_Type()
)
fcConnUnitPortStatRxBcastObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatRxBcastObjects.setStatus("current")
_FcConnUnitPortStatTxBcastObjects_Type = Counter64
_FcConnUnitPortStatTxBcastObjects_Object = MibTableColumn
fcConnUnitPortStatTxBcastObjects = _FcConnUnitPortStatTxBcastObjects_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 31),
    _FcConnUnitPortStatTxBcastObjects_Type()
)
fcConnUnitPortStatTxBcastObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatTxBcastObjects.setStatus("current")
_FcConnUnitPortStatRxLinkResets_Type = Counter64
_FcConnUnitPortStatRxLinkResets_Object = MibTableColumn
fcConnUnitPortStatRxLinkResets = _FcConnUnitPortStatRxLinkResets_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 32),
    _FcConnUnitPortStatRxLinkResets_Type()
)
fcConnUnitPortStatRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatRxLinkResets.setStatus("current")
_FcConnUnitPortStatTxLinkResets_Type = Counter64
_FcConnUnitPortStatTxLinkResets_Object = MibTableColumn
fcConnUnitPortStatTxLinkResets = _FcConnUnitPortStatTxLinkResets_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 33),
    _FcConnUnitPortStatTxLinkResets_Type()
)
fcConnUnitPortStatTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatTxLinkResets.setStatus("current")
_FcConnUnitPortStatLinkResets_Type = Counter64
_FcConnUnitPortStatLinkResets_Object = MibTableColumn
fcConnUnitPortStatLinkResets = _FcConnUnitPortStatLinkResets_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 34),
    _FcConnUnitPortStatLinkResets_Type()
)
fcConnUnitPortStatLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatLinkResets.setStatus("current")
_FcConnUnitPortStatRxOfflineSeqs_Type = Counter64
_FcConnUnitPortStatRxOfflineSeqs_Object = MibTableColumn
fcConnUnitPortStatRxOfflineSeqs = _FcConnUnitPortStatRxOfflineSeqs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 35),
    _FcConnUnitPortStatRxOfflineSeqs_Type()
)
fcConnUnitPortStatRxOfflineSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatRxOfflineSeqs.setStatus("current")
_FcConnUnitPortStatTxOfflineSeqs_Type = Counter64
_FcConnUnitPortStatTxOfflineSeqs_Object = MibTableColumn
fcConnUnitPortStatTxOfflineSeqs = _FcConnUnitPortStatTxOfflineSeqs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 36),
    _FcConnUnitPortStatTxOfflineSeqs_Type()
)
fcConnUnitPortStatTxOfflineSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatTxOfflineSeqs.setStatus("current")
_FcConnUnitPortStatOfflineSeqs_Type = Counter64
_FcConnUnitPortStatOfflineSeqs_Object = MibTableColumn
fcConnUnitPortStatOfflineSeqs = _FcConnUnitPortStatOfflineSeqs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 37),
    _FcConnUnitPortStatOfflineSeqs_Type()
)
fcConnUnitPortStatOfflineSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatOfflineSeqs.setStatus("current")
_FcConnUnitPortStatLinkFailures_Type = Counter64
_FcConnUnitPortStatLinkFailures_Object = MibTableColumn
fcConnUnitPortStatLinkFailures = _FcConnUnitPortStatLinkFailures_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 38),
    _FcConnUnitPortStatLinkFailures_Type()
)
fcConnUnitPortStatLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatLinkFailures.setStatus("current")
_FcConnUnitPortStatInvalidCRC_Type = Counter64
_FcConnUnitPortStatInvalidCRC_Object = MibTableColumn
fcConnUnitPortStatInvalidCRC = _FcConnUnitPortStatInvalidCRC_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 39),
    _FcConnUnitPortStatInvalidCRC_Type()
)
fcConnUnitPortStatInvalidCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatInvalidCRC.setStatus("current")
_FcConnUnitPortStatInvalidTxWords_Type = Counter64
_FcConnUnitPortStatInvalidTxWords_Object = MibTableColumn
fcConnUnitPortStatInvalidTxWords = _FcConnUnitPortStatInvalidTxWords_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 40),
    _FcConnUnitPortStatInvalidTxWords_Type()
)
fcConnUnitPortStatInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatInvalidTxWords.setStatus("current")
_FcConnUnitPortStatPSPErrs_Type = Counter64
_FcConnUnitPortStatPSPErrs_Object = MibTableColumn
fcConnUnitPortStatPSPErrs = _FcConnUnitPortStatPSPErrs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 41),
    _FcConnUnitPortStatPSPErrs_Type()
)
fcConnUnitPortStatPSPErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatPSPErrs.setStatus("current")
_FcConnUnitPortStatLossOfSignal_Type = Counter64
_FcConnUnitPortStatLossOfSignal_Object = MibTableColumn
fcConnUnitPortStatLossOfSignal = _FcConnUnitPortStatLossOfSignal_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 42),
    _FcConnUnitPortStatLossOfSignal_Type()
)
fcConnUnitPortStatLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatLossOfSignal.setStatus("current")
_FcConnUnitPortStatLossOfSync_Type = Counter64
_FcConnUnitPortStatLossOfSync_Object = MibTableColumn
fcConnUnitPortStatLossOfSync = _FcConnUnitPortStatLossOfSync_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 43),
    _FcConnUnitPortStatLossOfSync_Type()
)
fcConnUnitPortStatLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatLossOfSync.setStatus("current")
_FcConnUnitPortStatInvOrderedSets_Type = Counter64
_FcConnUnitPortStatInvOrderedSets_Object = MibTableColumn
fcConnUnitPortStatInvOrderedSets = _FcConnUnitPortStatInvOrderedSets_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 44),
    _FcConnUnitPortStatInvOrderedSets_Type()
)
fcConnUnitPortStatInvOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatInvOrderedSets.setStatus("current")
_FcConnUnitPortStatFramesTooLong_Type = Counter64
_FcConnUnitPortStatFramesTooLong_Object = MibTableColumn
fcConnUnitPortStatFramesTooLong = _FcConnUnitPortStatFramesTooLong_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 45),
    _FcConnUnitPortStatFramesTooLong_Type()
)
fcConnUnitPortStatFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatFramesTooLong.setStatus("current")
_FcConnUnitPortStatFramesTooShort_Type = Counter64
_FcConnUnitPortStatFramesTooShort_Object = MibTableColumn
fcConnUnitPortStatFramesTooShort = _FcConnUnitPortStatFramesTooShort_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 46),
    _FcConnUnitPortStatFramesTooShort_Type()
)
fcConnUnitPortStatFramesTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatFramesTooShort.setStatus("current")
_FcConnUnitPortStatAddressErrs_Type = Counter64
_FcConnUnitPortStatAddressErrs_Object = MibTableColumn
fcConnUnitPortStatAddressErrs = _FcConnUnitPortStatAddressErrs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 47),
    _FcConnUnitPortStatAddressErrs_Type()
)
fcConnUnitPortStatAddressErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatAddressErrs.setStatus("current")
_FcConnUnitPortStatDelimiterErrs_Type = Counter64
_FcConnUnitPortStatDelimiterErrs_Object = MibTableColumn
fcConnUnitPortStatDelimiterErrs = _FcConnUnitPortStatDelimiterErrs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 48),
    _FcConnUnitPortStatDelimiterErrs_Type()
)
fcConnUnitPortStatDelimiterErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatDelimiterErrs.setStatus("current")
_FcConnUnitPortStatEncodingErrs_Type = Counter64
_FcConnUnitPortStatEncodingErrs_Object = MibTableColumn
fcConnUnitPortStatEncodingErrs = _FcConnUnitPortStatEncodingErrs_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 3, 1, 1, 49),
    _FcConnUnitPortStatEncodingErrs_Type()
)
fcConnUnitPortStatEncodingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitPortStatEncodingErrs.setStatus("current")
_FcMgmtSNS_ObjectIdentity = ObjectIdentity
fcMgmtSNS = _FcMgmtSNS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4)
)
_FcConnUnitSnsTable_Object = MibTable
fcConnUnitSnsTable = _FcConnUnitSnsTable_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fcConnUnitSnsTable.setStatus("current")
_FcConnUnitSnsEntry_Object = MibTableRow
fcConnUnitSnsEntry = _FcConnUnitSnsEntry_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1)
)
fcConnUnitSnsEntry.setIndexNames(
    (0, "MCDATA-31", "fcConnUnitId"),
    (0, "MCDATA-31", "fcConnUnitSnsPortIndex"),
    (0, "MCDATA-31", "fcConnUnitSnsPortIdentifier"),
)
if mibBuilder.loadTexts:
    fcConnUnitSnsEntry.setStatus("current")
_FcConnUnitSnsPortIndex_Type = Counter32
_FcConnUnitSnsPortIndex_Object = MibTableColumn
fcConnUnitSnsPortIndex = _FcConnUnitSnsPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 1),
    _FcConnUnitSnsPortIndex_Type()
)
fcConnUnitSnsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsPortIndex.setStatus("current")
_FcConnUnitSnsPortIdentifier_Type = FcGlobalId
_FcConnUnitSnsPortIdentifier_Object = MibTableColumn
fcConnUnitSnsPortIdentifier = _FcConnUnitSnsPortIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 2),
    _FcConnUnitSnsPortIdentifier_Type()
)
fcConnUnitSnsPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsPortIdentifier.setStatus("current")
_FcConnUnitSnsPortName_Type = FcNameId
_FcConnUnitSnsPortName_Object = MibTableColumn
fcConnUnitSnsPortName = _FcConnUnitSnsPortName_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 3),
    _FcConnUnitSnsPortName_Type()
)
fcConnUnitSnsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsPortName.setStatus("current")
_FcConnUnitSnsNodeName_Type = FcNameId
_FcConnUnitSnsNodeName_Object = MibTableColumn
fcConnUnitSnsNodeName = _FcConnUnitSnsNodeName_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 4),
    _FcConnUnitSnsNodeName_Type()
)
fcConnUnitSnsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsNodeName.setStatus("current")


class _FcConnUnitSnsClassOfSvc_Type(OctetString):
    """Custom type fcConnUnitSnsClassOfSvc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_FcConnUnitSnsClassOfSvc_Type.__name__ = "OctetString"
_FcConnUnitSnsClassOfSvc_Object = MibTableColumn
fcConnUnitSnsClassOfSvc = _FcConnUnitSnsClassOfSvc_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 5),
    _FcConnUnitSnsClassOfSvc_Type()
)
fcConnUnitSnsClassOfSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsClassOfSvc.setStatus("current")


class _FcConnUnitSnsNodeIPAddress_Type(OctetString):
    """Custom type fcConnUnitSnsNodeIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FcConnUnitSnsNodeIPAddress_Type.__name__ = "OctetString"
_FcConnUnitSnsNodeIPAddress_Object = MibTableColumn
fcConnUnitSnsNodeIPAddress = _FcConnUnitSnsNodeIPAddress_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 6),
    _FcConnUnitSnsNodeIPAddress_Type()
)
fcConnUnitSnsNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsNodeIPAddress.setStatus("current")


class _FcConnUnitSnsProcAssoc_Type(OctetString):
    """Custom type fcConnUnitSnsProcAssoc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcConnUnitSnsProcAssoc_Type.__name__ = "OctetString"
_FcConnUnitSnsProcAssoc_Object = MibTableColumn
fcConnUnitSnsProcAssoc = _FcConnUnitSnsProcAssoc_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 7),
    _FcConnUnitSnsProcAssoc_Type()
)
fcConnUnitSnsProcAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsProcAssoc.setStatus("current")


class _FcConnUnitSnsFC4Type_Type(OctetString):
    """Custom type fcConnUnitSnsFC4Type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_FcConnUnitSnsFC4Type_Type.__name__ = "OctetString"
_FcConnUnitSnsFC4Type_Object = MibTableColumn
fcConnUnitSnsFC4Type = _FcConnUnitSnsFC4Type_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 8),
    _FcConnUnitSnsFC4Type_Type()
)
fcConnUnitSnsFC4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsFC4Type.setStatus("current")


class _FcConnUnitSnsPortType_Type(OctetString):
    """Custom type fcConnUnitSnsPortType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_FcConnUnitSnsPortType_Type.__name__ = "OctetString"
_FcConnUnitSnsPortType_Object = MibTableColumn
fcConnUnitSnsPortType = _FcConnUnitSnsPortType_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 9),
    _FcConnUnitSnsPortType_Type()
)
fcConnUnitSnsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsPortType.setStatus("current")


class _FcConnUnitSnsPortIPAddress_Type(OctetString):
    """Custom type fcConnUnitSnsPortIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FcConnUnitSnsPortIPAddress_Type.__name__ = "OctetString"
_FcConnUnitSnsPortIPAddress_Object = MibTableColumn
fcConnUnitSnsPortIPAddress = _FcConnUnitSnsPortIPAddress_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 10),
    _FcConnUnitSnsPortIPAddress_Type()
)
fcConnUnitSnsPortIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsPortIPAddress.setStatus("current")
_FcConnUnitSnsFabricPortName_Type = FcNameId
_FcConnUnitSnsFabricPortName_Object = MibTableColumn
fcConnUnitSnsFabricPortName = _FcConnUnitSnsFabricPortName_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 11),
    _FcConnUnitSnsFabricPortName_Type()
)
fcConnUnitSnsFabricPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsFabricPortName.setStatus("current")
_FcConnUnitSnsHardAddress_Type = FcGlobalId
_FcConnUnitSnsHardAddress_Object = MibTableColumn
fcConnUnitSnsHardAddress = _FcConnUnitSnsHardAddress_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 12),
    _FcConnUnitSnsHardAddress_Type()
)
fcConnUnitSnsHardAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsHardAddress.setStatus("current")


class _FcConnUnitSnsSymbolicPortName_Type(DisplayString):
    """Custom type fcConnUnitSnsSymbolicPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_FcConnUnitSnsSymbolicPortName_Type.__name__ = "DisplayString"
_FcConnUnitSnsSymbolicPortName_Object = MibTableColumn
fcConnUnitSnsSymbolicPortName = _FcConnUnitSnsSymbolicPortName_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 13),
    _FcConnUnitSnsSymbolicPortName_Type()
)
fcConnUnitSnsSymbolicPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsSymbolicPortName.setStatus("current")


class _FcConnUnitSnsSymbolicNodeName_Type(DisplayString):
    """Custom type fcConnUnitSnsSymbolicNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_FcConnUnitSnsSymbolicNodeName_Type.__name__ = "DisplayString"
_FcConnUnitSnsSymbolicNodeName_Object = MibTableColumn
fcConnUnitSnsSymbolicNodeName = _FcConnUnitSnsSymbolicNodeName_Object(
    (1, 3, 6, 1, 2, 1, 8888, 1, 4, 1, 1, 14),
    _FcConnUnitSnsSymbolicNodeName_Type()
)
fcConnUnitSnsSymbolicNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcConnUnitSnsSymbolicNodeName.setStatus("current")
_FcMgmtConformance_ObjectIdentity = ObjectIdentity
fcMgmtConformance = _FcMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 2)
)
_FcMgmtCompliances_ObjectIdentity = ObjectIdentity
fcMgmtCompliances = _FcMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 2, 1)
)
_FcMgmtGroups_ObjectIdentity = ObjectIdentity
fcMgmtGroups = _FcMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8888, 2, 2)
)

# Managed Objects groups

fcConnUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 8888, 2, 2, 1)
)
fcConnUnitGroup.setObjects(
      *(("MCDATA-31", "fcConnUnitNumber"),
        ("MCDATA-31", "fcConnURL"),
        ("MCDATA-31", "fcConnUnitGlobalId"),
        ("MCDATA-31", "fcConnUnitType"),
        ("MCDATA-31", "fcConnUnitNumPorts"),
        ("MCDATA-31", "fcConnUnitState"),
        ("MCDATA-31", "fcConnUnitStatus"),
        ("MCDATA-31", "fcConnUnitProduct"),
        ("MCDATA-31", "fcConnUnitSerialNo"),
        ("MCDATA-31", "fcConnUnitUpTime"),
        ("MCDATA-31", "fcConnUnitUrl"),
        ("MCDATA-31", "fcConnUnitDomainId"),
        ("MCDATA-31", "fcConnUnitProxyMaster"),
        ("MCDATA-31", "fcConnUnitPrincipal"),
        ("MCDATA-31", "fcConnUnitNumSensors"),
        ("MCDATA-31", "fcConnUnitNumRevs"),
        ("MCDATA-31", "fcConnUnitModuleId"),
        ("MCDATA-31", "fcConnUnitName"),
        ("MCDATA-31", "fcConnUnitInfo"),
        ("MCDATA-31", "fcConnUnitControl"),
        ("MCDATA-31", "fcConnUnitContact"),
        ("MCDATA-31", "fcConnUnitLocation"),
        ("MCDATA-31", "fcConnUnitEventFilter"),
        ("MCDATA-31", "fcConnUnitNumEvents"),
        ("MCDATA-31", "fcConnUnitMaxEvents"),
        ("MCDATA-31", "fcConnUnitEventCurrID"),
        ("MCDATA-31", "fcConnUnitRevsRevision"),
        ("MCDATA-31", "fcConnUnitRevsDescription"),
        ("MCDATA-31", "fcConnUnitSensorName"),
        ("MCDATA-31", "fcConnUnitSensorStatus"),
        ("MCDATA-31", "fcConnUnitSensorInfo"),
        ("MCDATA-31", "fcConnUnitSensorMessage"),
        ("MCDATA-31", "fcConnUnitSensorType"),
        ("MCDATA-31", "fcConnUnitSensorCharacteristic"),
        ("MCDATA-31", "fcConnUnitPortType"),
        ("MCDATA-31", "fcConnUnitPortFCClassCap"),
        ("MCDATA-31", "fcConnUnitPortFCClassOp"),
        ("MCDATA-31", "fcConnUnitPortState"),
        ("MCDATA-31", "fcConnUnitPortStatus"),
        ("MCDATA-31", "fcConnUnitPortTransmitterType"),
        ("MCDATA-31", "fcConnUnitPortModuleType"),
        ("MCDATA-31", "fcConnUnitPortWwn"),
        ("MCDATA-31", "fcConnUnitPortFCId"),
        ("MCDATA-31", "fcConnUnitPortSerialNo"),
        ("MCDATA-31", "fcConnUnitPortRevision"),
        ("MCDATA-31", "fcConnUnitPortVendor"),
        ("MCDATA-31", "fcConnUnitPortSpeed"),
        ("MCDATA-31", "fcConnUnitPortControl"),
        ("MCDATA-31", "fcConnUnitPortName"),
        ("MCDATA-31", "fcConnUnitPortPhysicalNumber"),
        ("MCDATA-31", "fcConnUnitPortProtocolCap"),
        ("MCDATA-31", "fcConnUnitPortProtocolOp"),
        ("MCDATA-31", "fcConnUnitPortNodeWwn"),
        ("MCDATA-31", "fcConnUnitPortHWState"))
)
if mibBuilder.loadTexts:
    fcConnUnitGroup.setStatus("current")

fcCuEventGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 8888, 2, 2, 2)
)
fcCuEventGroup.setObjects(
      *(("MCDATA-31", "fcConnUnitEventIndex"),
        ("MCDATA-31", "fcConnUnitREventTime"),
        ("MCDATA-31", "fcConnUnitSEventTime"),
        ("MCDATA-31", "fcConnUnitEventSeverity"),
        ("MCDATA-31", "fcConnUnitEventType"),
        ("MCDATA-31", "fcConnUnitEventObject"),
        ("MCDATA-31", "fcConnUnitEventDescr"))
)
if mibBuilder.loadTexts:
    fcCuEventGroup.setStatus("current")

fcCuLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 8888, 2, 2, 3)
)
fcCuLinkGroup.setObjects(
      *(("MCDATA-31", "fcConnUnitLinkIndex"),
        ("MCDATA-31", "fcConnUnitLinkNodeIdX"),
        ("MCDATA-31", "fcConnUnitLinkPortNumberX"),
        ("MCDATA-31", "fcConnUnitLinkPortWwnX"),
        ("MCDATA-31", "fcConnUnitLinkNodeIdY"),
        ("MCDATA-31", "fcConnUnitLinkPortNumberY"),
        ("MCDATA-31", "fcConnUnitLinkPortWwnY"),
        ("MCDATA-31", "fcConnUnitLinkAgentAddressY"),
        ("MCDATA-31", "fcConnUnitLinkAgentAddressTypeY"),
        ("MCDATA-31", "fcConnUnitLinkAgentPortY"),
        ("MCDATA-31", "fcConnUnitLinkUnitTypeY"),
        ("MCDATA-31", "fcConnUnitLinkConnIdY"))
)
if mibBuilder.loadTexts:
    fcCuLinkGroup.setStatus("current")

fcCuPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 8888, 2, 2, 4)
)
fcCuPortStatsGroup.setObjects(
      *(("MCDATA-31", "fcConnUnitPortStatIndex"),
        ("MCDATA-31", "fcConnUnitPortStatErrs"),
        ("MCDATA-31", "fcConnUnitPortStatTxObjects"),
        ("MCDATA-31", "fcConnUnitPortStatRxObjects"),
        ("MCDATA-31", "fcConnUnitPortStatTxElements"),
        ("MCDATA-31", "fcConnUnitPortStatRxElements"),
        ("MCDATA-31", "fcConnUnitPortStatBBCreditZero"),
        ("MCDATA-31", "fcConnUnitPortStatInputBuffsFull"),
        ("MCDATA-31", "fcConnUnitPortStatFBSYFrames"),
        ("MCDATA-31", "fcConnUnitPortStatPBSYFrames"),
        ("MCDATA-31", "fcConnUnitPortStatFRJTFrames"),
        ("MCDATA-31", "fcConnUnitPortStatPRJTFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC1RxFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC1TxFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC1FBSYFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC1PBSYFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC1FRJTFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC1PRJTFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC2RxFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC2TxFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC2FBSYFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC2PBSYFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC2FRJTFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC2PRJTFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC3RxFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC3TxFrames"),
        ("MCDATA-31", "fcConnUnitPortStatC3Discards"),
        ("MCDATA-31", "fcConnUnitPortStatRxMcastObjects"),
        ("MCDATA-31", "fcConnUnitPortStatTxMcastObjects"),
        ("MCDATA-31", "fcConnUnitPortStatRxBcastObjects"),
        ("MCDATA-31", "fcConnUnitPortStatTxBcastObjects"),
        ("MCDATA-31", "fcConnUnitPortStatRxLinkResets"),
        ("MCDATA-31", "fcConnUnitPortStatTxLinkResets"),
        ("MCDATA-31", "fcConnUnitPortStatLinkResets"),
        ("MCDATA-31", "fcConnUnitPortStatRxOfflineSeqs"),
        ("MCDATA-31", "fcConnUnitPortStatTxOfflineSeqs"),
        ("MCDATA-31", "fcConnUnitPortStatOfflineSeqs"),
        ("MCDATA-31", "fcConnUnitPortStatLinkFailures"),
        ("MCDATA-31", "fcConnUnitPortStatInvalidCRC"),
        ("MCDATA-31", "fcConnUnitPortStatInvalidTxWords"),
        ("MCDATA-31", "fcConnUnitPortStatPSPErrs"),
        ("MCDATA-31", "fcConnUnitPortStatLossOfSignal"),
        ("MCDATA-31", "fcConnUnitPortStatLossOfSync"),
        ("MCDATA-31", "fcConnUnitPortStatInvOrderedSets"),
        ("MCDATA-31", "fcConnUnitPortStatFramesTooLong"),
        ("MCDATA-31", "fcConnUnitPortStatFramesTooShort"),
        ("MCDATA-31", "fcConnUnitPortStatAddressErrs"),
        ("MCDATA-31", "fcConnUnitPortStatDelimiterErrs"),
        ("MCDATA-31", "fcConnUnitPortStatEncodingErrs"))
)
if mibBuilder.loadTexts:
    fcCuPortStatsGroup.setStatus("current")

fcCuSNSGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 8888, 2, 2, 5)
)
fcCuSNSGroup.setObjects(
      *(("MCDATA-31", "fcConnUnitSnsMaxRows"),
        ("MCDATA-31", "fcConnUnitSnsPortIndex"),
        ("MCDATA-31", "fcConnUnitSnsPortIdentifier"),
        ("MCDATA-31", "fcConnUnitSnsPortName"),
        ("MCDATA-31", "fcConnUnitSnsNodeName"),
        ("MCDATA-31", "fcConnUnitSnsClassOfSvc"),
        ("MCDATA-31", "fcConnUnitSnsNodeIPAddress"),
        ("MCDATA-31", "fcConnUnitSnsProcAssoc"),
        ("MCDATA-31", "fcConnUnitSnsFC4Type"),
        ("MCDATA-31", "fcConnUnitSnsPortType"),
        ("MCDATA-31", "fcConnUnitSnsPortIPAddress"),
        ("MCDATA-31", "fcConnUnitSnsFabricPortName"),
        ("MCDATA-31", "fcConnUnitSnsHardAddress"),
        ("MCDATA-31", "fcConnUnitSnsSymbolicPortName"),
        ("MCDATA-31", "fcConnUnitSnsSymbolicNodeName"))
)
if mibBuilder.loadTexts:
    fcCuSNSGroup.setStatus("current")

fcCuTrapFiltersGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 8888, 2, 2, 6)
)
fcCuTrapFiltersGroup.setObjects(
      *(("MCDATA-31", "fcTrapMaxClients"),
        ("MCDATA-31", "fcTrapClientCount"),
        ("MCDATA-31", "fcTrapRegIpAddress"),
        ("MCDATA-31", "fcTrapRegPort"),
        ("MCDATA-31", "fcTrapRegFilter"),
        ("MCDATA-31", "fcTrapRegRowState"))
)
if mibBuilder.loadTexts:
    fcCuTrapFiltersGroup.setStatus("current")


# Notification objects

fcConnUnitStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 8888, 0, 1)
)
fcConnUnitStatusChange.setObjects(
      *(("MCDATA-31", "fcConnUnitStatus"),
        ("MCDATA-31", "fcConnUnitState"))
)
if mibBuilder.loadTexts:
    fcConnUnitStatusChange.setStatus(
        "current"
    )

fcConnUnitDeletedTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 8888, 0, 2)
)
fcConnUnitDeletedTrap.setObjects(
    ("MCDATA-31", "fcConnUnitGlobalId")
)
if mibBuilder.loadTexts:
    fcConnUnitDeletedTrap.setStatus(
        "current"
    )

fcConnUnitEventTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 8888, 0, 3)
)
fcConnUnitEventTrap.setObjects(
      *(("MCDATA-31", "fcConnUnitGlobalId"),
        ("MCDATA-31", "fcConnUnitEventType"),
        ("MCDATA-31", "fcConnUnitEventObject"),
        ("MCDATA-31", "fcConnUnitEventDescr"))
)
if mibBuilder.loadTexts:
    fcConnUnitEventTrap.setStatus(
        "current"
    )

fcConnUnitSensorStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 8888, 0, 4)
)
fcConnUnitSensorStatusChange.setObjects(
    ("MCDATA-31", "fcConnUnitSensorStatus")
)
if mibBuilder.loadTexts:
    fcConnUnitSensorStatusChange.setStatus(
        "current"
    )

fcConnUnitPortStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 8888, 0, 5)
)
fcConnUnitPortStatusChange.setObjects(
      *(("MCDATA-31", "fcConnUnitPortStatus"),
        ("MCDATA-31", "fcConnUnitPortState"))
)
if mibBuilder.loadTexts:
    fcConnUnitPortStatusChange.setStatus(
        "current"
    )


# Notifications groups

fcCuNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 8888, 2, 2, 7)
)
fcCuNotificationsGroup.setObjects(
      *(("MCDATA-31", "fcConnUnitStatusChange"),
        ("MCDATA-31", "fcConnUnitDeletedTrap"),
        ("MCDATA-31", "fcConnUnitEventTrap"),
        ("MCDATA-31", "fcConnUnitSensorStatusChange"),
        ("MCDATA-31", "fcConnUnitPortStatusChange"))
)
if mibBuilder.loadTexts:
    fcCuNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fcMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 8888, 2, 1, 1)
)
fcMgmtCompliance.setObjects(
      *(("MCDATA-31", "fcConnUnitGroup"),
        ("MCDATA-31", "fcCuEventGroup"),
        ("MCDATA-31", "fcCuLinkGroup"),
        ("MCDATA-31", "fcCuPortStatsGroup"),
        ("MCDATA-31", "fcCuTrapFiltersGroup"),
        ("MCDATA-31", "fcCuNotificationsGroup"),
        ("MCDATA-31", "fcCuSNSGroup"))
)
if mibBuilder.loadTexts:
    fcMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCDATA-31",
    **{"FcNameId": FcNameId,
       "FcGlobalId": FcGlobalId,
       "FcEventSeverity": FcEventSeverity,
       "FcUnitType": FcUnitType,
       "FcPortFCClass": FcPortFCClass,
       "fcMgmtMIB": fcMgmtMIB,
       "fcMgmtNotifications": fcMgmtNotifications,
       "fcConnUnitStatusChange": fcConnUnitStatusChange,
       "fcConnUnitDeletedTrap": fcConnUnitDeletedTrap,
       "fcConnUnitEventTrap": fcConnUnitEventTrap,
       "fcConnUnitSensorStatusChange": fcConnUnitSensorStatusChange,
       "fcConnUnitPortStatusChange": fcConnUnitPortStatusChange,
       "fcMgmtObjects": fcMgmtObjects,
       "fcMgmtConfig": fcMgmtConfig,
       "fcConnUnitNumber": fcConnUnitNumber,
       "fcConnURL": fcConnURL,
       "fcConnUnitTable": fcConnUnitTable,
       "fcConnUnitEntry": fcConnUnitEntry,
       "fcConnUnitId": fcConnUnitId,
       "fcConnUnitGlobalId": fcConnUnitGlobalId,
       "fcConnUnitType": fcConnUnitType,
       "fcConnUnitNumPorts": fcConnUnitNumPorts,
       "fcConnUnitState": fcConnUnitState,
       "fcConnUnitStatus": fcConnUnitStatus,
       "fcConnUnitProduct": fcConnUnitProduct,
       "fcConnUnitSerialNo": fcConnUnitSerialNo,
       "fcConnUnitUpTime": fcConnUnitUpTime,
       "fcConnUnitUrl": fcConnUnitUrl,
       "fcConnUnitDomainId": fcConnUnitDomainId,
       "fcConnUnitProxyMaster": fcConnUnitProxyMaster,
       "fcConnUnitPrincipal": fcConnUnitPrincipal,
       "fcConnUnitNumSensors": fcConnUnitNumSensors,
       "fcConnUnitNumRevs": fcConnUnitNumRevs,
       "fcConnUnitModuleId": fcConnUnitModuleId,
       "fcConnUnitName": fcConnUnitName,
       "fcConnUnitInfo": fcConnUnitInfo,
       "fcConnUnitControl": fcConnUnitControl,
       "fcConnUnitContact": fcConnUnitContact,
       "fcConnUnitLocation": fcConnUnitLocation,
       "fcConnUnitEventFilter": fcConnUnitEventFilter,
       "fcConnUnitNumEvents": fcConnUnitNumEvents,
       "fcConnUnitMaxEvents": fcConnUnitMaxEvents,
       "fcConnUnitEventCurrID": fcConnUnitEventCurrID,
       "fcConnUnitRevsTable": fcConnUnitRevsTable,
       "fcConnUnitRevsEntry": fcConnUnitRevsEntry,
       "fcConnUnitRevsIndex": fcConnUnitRevsIndex,
       "fcConnUnitRevsRevision": fcConnUnitRevsRevision,
       "fcConnUnitRevsDescription": fcConnUnitRevsDescription,
       "fcConnUnitSensorTable": fcConnUnitSensorTable,
       "fcConnUnitSensorEntry": fcConnUnitSensorEntry,
       "fcConnUnitSensorIndex": fcConnUnitSensorIndex,
       "fcConnUnitSensorName": fcConnUnitSensorName,
       "fcConnUnitSensorStatus": fcConnUnitSensorStatus,
       "fcConnUnitSensorInfo": fcConnUnitSensorInfo,
       "fcConnUnitSensorMessage": fcConnUnitSensorMessage,
       "fcConnUnitSensorType": fcConnUnitSensorType,
       "fcConnUnitSensorCharacteristic": fcConnUnitSensorCharacteristic,
       "fcConnUnitPortTable": fcConnUnitPortTable,
       "fcConnUnitPortEntry": fcConnUnitPortEntry,
       "fcConnUnitPortIndex": fcConnUnitPortIndex,
       "fcConnUnitPortType": fcConnUnitPortType,
       "fcConnUnitPortFCClassCap": fcConnUnitPortFCClassCap,
       "fcConnUnitPortFCClassOp": fcConnUnitPortFCClassOp,
       "fcConnUnitPortState": fcConnUnitPortState,
       "fcConnUnitPortStatus": fcConnUnitPortStatus,
       "fcConnUnitPortTransmitterType": fcConnUnitPortTransmitterType,
       "fcConnUnitPortModuleType": fcConnUnitPortModuleType,
       "fcConnUnitPortWwn": fcConnUnitPortWwn,
       "fcConnUnitPortFCId": fcConnUnitPortFCId,
       "fcConnUnitPortSerialNo": fcConnUnitPortSerialNo,
       "fcConnUnitPortRevision": fcConnUnitPortRevision,
       "fcConnUnitPortVendor": fcConnUnitPortVendor,
       "fcConnUnitPortSpeed": fcConnUnitPortSpeed,
       "fcConnUnitPortControl": fcConnUnitPortControl,
       "fcConnUnitPortName": fcConnUnitPortName,
       "fcConnUnitPortPhysicalNumber": fcConnUnitPortPhysicalNumber,
       "fcConnUnitPortProtocolCap": fcConnUnitPortProtocolCap,
       "fcConnUnitPortProtocolOp": fcConnUnitPortProtocolOp,
       "fcConnUnitPortNodeWwn": fcConnUnitPortNodeWwn,
       "fcConnUnitPortHWState": fcConnUnitPortHWState,
       "fcConnUnitEventTable": fcConnUnitEventTable,
       "fcConnUnitEventEntry": fcConnUnitEventEntry,
       "fcConnUnitEventIndex": fcConnUnitEventIndex,
       "fcConnUnitREventTime": fcConnUnitREventTime,
       "fcConnUnitSEventTime": fcConnUnitSEventTime,
       "fcConnUnitEventSeverity": fcConnUnitEventSeverity,
       "fcConnUnitEventType": fcConnUnitEventType,
       "fcConnUnitEventObject": fcConnUnitEventObject,
       "fcConnUnitEventDescr": fcConnUnitEventDescr,
       "fcConnUnitLinkTable": fcConnUnitLinkTable,
       "fcConnUnitLinkEntry": fcConnUnitLinkEntry,
       "fcConnUnitLinkIndex": fcConnUnitLinkIndex,
       "fcConnUnitLinkNodeIdX": fcConnUnitLinkNodeIdX,
       "fcConnUnitLinkPortNumberX": fcConnUnitLinkPortNumberX,
       "fcConnUnitLinkPortWwnX": fcConnUnitLinkPortWwnX,
       "fcConnUnitLinkNodeIdY": fcConnUnitLinkNodeIdY,
       "fcConnUnitLinkPortNumberY": fcConnUnitLinkPortNumberY,
       "fcConnUnitLinkPortWwnY": fcConnUnitLinkPortWwnY,
       "fcConnUnitLinkAgentAddressY": fcConnUnitLinkAgentAddressY,
       "fcConnUnitLinkAgentAddressTypeY": fcConnUnitLinkAgentAddressTypeY,
       "fcConnUnitLinkAgentPortY": fcConnUnitLinkAgentPortY,
       "fcConnUnitLinkUnitTypeY": fcConnUnitLinkUnitTypeY,
       "fcConnUnitLinkConnIdY": fcConnUnitLinkConnIdY,
       "fcConnUnitSnsMaxRows": fcConnUnitSnsMaxRows,
       "fcMgmtNotifyFilter": fcMgmtNotifyFilter,
       "fcTrapMaxClients": fcTrapMaxClients,
       "fcTrapClientCount": fcTrapClientCount,
       "fcTrapRegTable": fcTrapRegTable,
       "fcTrapRegEntry": fcTrapRegEntry,
       "fcTrapRegIpAddress": fcTrapRegIpAddress,
       "fcTrapRegPort": fcTrapRegPort,
       "fcTrapRegFilter": fcTrapRegFilter,
       "fcTrapRegRowState": fcTrapRegRowState,
       "fcMgmtStatistics": fcMgmtStatistics,
       "fcConnUnitPortStatTable": fcConnUnitPortStatTable,
       "fcConnUnitPortStatEntry": fcConnUnitPortStatEntry,
       "fcConnUnitPortStatIndex": fcConnUnitPortStatIndex,
       "fcConnUnitPortStatErrs": fcConnUnitPortStatErrs,
       "fcConnUnitPortStatTxObjects": fcConnUnitPortStatTxObjects,
       "fcConnUnitPortStatRxObjects": fcConnUnitPortStatRxObjects,
       "fcConnUnitPortStatTxElements": fcConnUnitPortStatTxElements,
       "fcConnUnitPortStatRxElements": fcConnUnitPortStatRxElements,
       "fcConnUnitPortStatBBCreditZero": fcConnUnitPortStatBBCreditZero,
       "fcConnUnitPortStatInputBuffsFull": fcConnUnitPortStatInputBuffsFull,
       "fcConnUnitPortStatFBSYFrames": fcConnUnitPortStatFBSYFrames,
       "fcConnUnitPortStatPBSYFrames": fcConnUnitPortStatPBSYFrames,
       "fcConnUnitPortStatFRJTFrames": fcConnUnitPortStatFRJTFrames,
       "fcConnUnitPortStatPRJTFrames": fcConnUnitPortStatPRJTFrames,
       "fcConnUnitPortStatC1RxFrames": fcConnUnitPortStatC1RxFrames,
       "fcConnUnitPortStatC1TxFrames": fcConnUnitPortStatC1TxFrames,
       "fcConnUnitPortStatC1FBSYFrames": fcConnUnitPortStatC1FBSYFrames,
       "fcConnUnitPortStatC1PBSYFrames": fcConnUnitPortStatC1PBSYFrames,
       "fcConnUnitPortStatC1FRJTFrames": fcConnUnitPortStatC1FRJTFrames,
       "fcConnUnitPortStatC1PRJTFrames": fcConnUnitPortStatC1PRJTFrames,
       "fcConnUnitPortStatC2RxFrames": fcConnUnitPortStatC2RxFrames,
       "fcConnUnitPortStatC2TxFrames": fcConnUnitPortStatC2TxFrames,
       "fcConnUnitPortStatC2FBSYFrames": fcConnUnitPortStatC2FBSYFrames,
       "fcConnUnitPortStatC2PBSYFrames": fcConnUnitPortStatC2PBSYFrames,
       "fcConnUnitPortStatC2FRJTFrames": fcConnUnitPortStatC2FRJTFrames,
       "fcConnUnitPortStatC2PRJTFrames": fcConnUnitPortStatC2PRJTFrames,
       "fcConnUnitPortStatC3RxFrames": fcConnUnitPortStatC3RxFrames,
       "fcConnUnitPortStatC3TxFrames": fcConnUnitPortStatC3TxFrames,
       "fcConnUnitPortStatC3Discards": fcConnUnitPortStatC3Discards,
       "fcConnUnitPortStatRxMcastObjects": fcConnUnitPortStatRxMcastObjects,
       "fcConnUnitPortStatTxMcastObjects": fcConnUnitPortStatTxMcastObjects,
       "fcConnUnitPortStatRxBcastObjects": fcConnUnitPortStatRxBcastObjects,
       "fcConnUnitPortStatTxBcastObjects": fcConnUnitPortStatTxBcastObjects,
       "fcConnUnitPortStatRxLinkResets": fcConnUnitPortStatRxLinkResets,
       "fcConnUnitPortStatTxLinkResets": fcConnUnitPortStatTxLinkResets,
       "fcConnUnitPortStatLinkResets": fcConnUnitPortStatLinkResets,
       "fcConnUnitPortStatRxOfflineSeqs": fcConnUnitPortStatRxOfflineSeqs,
       "fcConnUnitPortStatTxOfflineSeqs": fcConnUnitPortStatTxOfflineSeqs,
       "fcConnUnitPortStatOfflineSeqs": fcConnUnitPortStatOfflineSeqs,
       "fcConnUnitPortStatLinkFailures": fcConnUnitPortStatLinkFailures,
       "fcConnUnitPortStatInvalidCRC": fcConnUnitPortStatInvalidCRC,
       "fcConnUnitPortStatInvalidTxWords": fcConnUnitPortStatInvalidTxWords,
       "fcConnUnitPortStatPSPErrs": fcConnUnitPortStatPSPErrs,
       "fcConnUnitPortStatLossOfSignal": fcConnUnitPortStatLossOfSignal,
       "fcConnUnitPortStatLossOfSync": fcConnUnitPortStatLossOfSync,
       "fcConnUnitPortStatInvOrderedSets": fcConnUnitPortStatInvOrderedSets,
       "fcConnUnitPortStatFramesTooLong": fcConnUnitPortStatFramesTooLong,
       "fcConnUnitPortStatFramesTooShort": fcConnUnitPortStatFramesTooShort,
       "fcConnUnitPortStatAddressErrs": fcConnUnitPortStatAddressErrs,
       "fcConnUnitPortStatDelimiterErrs": fcConnUnitPortStatDelimiterErrs,
       "fcConnUnitPortStatEncodingErrs": fcConnUnitPortStatEncodingErrs,
       "fcMgmtSNS": fcMgmtSNS,
       "fcConnUnitSnsTable": fcConnUnitSnsTable,
       "fcConnUnitSnsEntry": fcConnUnitSnsEntry,
       "fcConnUnitSnsPortIndex": fcConnUnitSnsPortIndex,
       "fcConnUnitSnsPortIdentifier": fcConnUnitSnsPortIdentifier,
       "fcConnUnitSnsPortName": fcConnUnitSnsPortName,
       "fcConnUnitSnsNodeName": fcConnUnitSnsNodeName,
       "fcConnUnitSnsClassOfSvc": fcConnUnitSnsClassOfSvc,
       "fcConnUnitSnsNodeIPAddress": fcConnUnitSnsNodeIPAddress,
       "fcConnUnitSnsProcAssoc": fcConnUnitSnsProcAssoc,
       "fcConnUnitSnsFC4Type": fcConnUnitSnsFC4Type,
       "fcConnUnitSnsPortType": fcConnUnitSnsPortType,
       "fcConnUnitSnsPortIPAddress": fcConnUnitSnsPortIPAddress,
       "fcConnUnitSnsFabricPortName": fcConnUnitSnsFabricPortName,
       "fcConnUnitSnsHardAddress": fcConnUnitSnsHardAddress,
       "fcConnUnitSnsSymbolicPortName": fcConnUnitSnsSymbolicPortName,
       "fcConnUnitSnsSymbolicNodeName": fcConnUnitSnsSymbolicNodeName,
       "fcMgmtConformance": fcMgmtConformance,
       "fcMgmtCompliances": fcMgmtCompliances,
       "fcMgmtCompliance": fcMgmtCompliance,
       "fcMgmtGroups": fcMgmtGroups,
       "fcConnUnitGroup": fcConnUnitGroup,
       "fcCuEventGroup": fcCuEventGroup,
       "fcCuLinkGroup": fcCuLinkGroup,
       "fcCuPortStatsGroup": fcCuPortStatsGroup,
       "fcCuSNSGroup": fcCuSNSGroup,
       "fcCuTrapFiltersGroup": fcCuTrapFiltersGroup,
       "fcCuNotificationsGroup": fcCuNotificationsGroup}
)
