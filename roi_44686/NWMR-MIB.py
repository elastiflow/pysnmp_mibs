# SNMP MIB module (NWMR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/roi_44686/NWMR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:04:10 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

newmarPower = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44686)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Spm200_ObjectIdentity = ObjectIdentity
spm200 = _Spm200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44686, 1)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44686, 1, 1)
)
_ProductTitle_Type = DisplayString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductFriendlyName_Type = DisplayString
_ProductFriendlyName_Object = MibScalar
productFriendlyName = _ProductFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 1, 3),
    _ProductFriendlyName_Type()
)
productFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFriendlyName.setStatus("current")
_ProductMacAddress_Type = DisplayString
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 1, 4),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")
_ProductUrl_Type = DisplayString
_ProductUrl_Object = MibScalar
productUrl = _ProductUrl_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 1, 5),
    _ProductUrl_Type()
)
productUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productUrl.setStatus("current")
_AlarmTripType_Type = DisplayString
_AlarmTripType_Object = MibScalar
alarmTripType = _AlarmTripType_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 1, 6),
    _AlarmTripType_Type()
)
alarmTripType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTripType.setStatus("current")
_SpmNames_ObjectIdentity = ObjectIdentity
spmNames = _SpmNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2)
)
_TempCName_Type = DisplayString
_TempCName_Object = MibScalar
tempCName = _TempCName_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 1),
    _TempCName_Type()
)
tempCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCName.setStatus("current")
_TempFName_Type = DisplayString
_TempFName_Object = MibScalar
tempFName = _TempFName_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 2),
    _TempFName_Type()
)
tempFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFName.setStatus("current")
_VoltsDc1Name_Type = DisplayString
_VoltsDc1Name_Object = MibScalar
voltsDc1Name = _VoltsDc1Name_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 3),
    _VoltsDc1Name_Type()
)
voltsDc1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsDc1Name.setStatus("current")
_VoltsDc2Name_Type = DisplayString
_VoltsDc2Name_Object = MibScalar
voltsDc2Name = _VoltsDc2Name_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 4),
    _VoltsDc2Name_Type()
)
voltsDc2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsDc2Name.setStatus("current")
_VoltsDc3Name_Type = DisplayString
_VoltsDc3Name_Object = MibScalar
voltsDc3Name = _VoltsDc3Name_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 5),
    _VoltsDc3Name_Type()
)
voltsDc3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsDc3Name.setStatus("current")
_CurrentName_Type = DisplayString
_CurrentName_Object = MibScalar
currentName = _CurrentName_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 6),
    _CurrentName_Type()
)
currentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentName.setStatus("current")
_InverterVacName_Type = DisplayString
_InverterVacName_Object = MibScalar
inverterVacName = _InverterVacName_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 7),
    _InverterVacName_Type()
)
inverterVacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterVacName.setStatus("current")
_LineVacName_Type = DisplayString
_LineVacName_Object = MibScalar
lineVacName = _LineVacName_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 8),
    _LineVacName_Type()
)
lineVacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineVacName.setStatus("current")
_Contact1Name_Type = DisplayString
_Contact1Name_Object = MibScalar
contact1Name = _Contact1Name_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 9),
    _Contact1Name_Type()
)
contact1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact1Name.setStatus("current")
_Contact2Name_Type = DisplayString
_Contact2Name_Object = MibScalar
contact2Name = _Contact2Name_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 10),
    _Contact2Name_Type()
)
contact2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact2Name.setStatus("current")
_Contact3Name_Type = DisplayString
_Contact3Name_Object = MibScalar
contact3Name = _Contact3Name_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 2, 11),
    _Contact3Name_Type()
)
contact3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact3Name.setStatus("current")
_SpmData_ObjectIdentity = ObjectIdentity
spmData = _SpmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3)
)
_TempCData_Type = Integer32
_TempCData_Object = MibScalar
tempCData = _TempCData_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 1),
    _TempCData_Type()
)
tempCData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCData.setStatus("current")
_TempFData_Type = Integer32
_TempFData_Object = MibScalar
tempFData = _TempFData_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 2),
    _TempFData_Type()
)
tempFData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFData.setStatus("current")
_VoltsDc1Data_Type = Integer32
_VoltsDc1Data_Object = MibScalar
voltsDc1Data = _VoltsDc1Data_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 3),
    _VoltsDc1Data_Type()
)
voltsDc1Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsDc1Data.setStatus("current")
_VoltsDc2Data_Type = Integer32
_VoltsDc2Data_Object = MibScalar
voltsDc2Data = _VoltsDc2Data_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 4),
    _VoltsDc2Data_Type()
)
voltsDc2Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsDc2Data.setStatus("current")
_VoltsDc3Data_Type = Integer32
_VoltsDc3Data_Object = MibScalar
voltsDc3Data = _VoltsDc3Data_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 5),
    _VoltsDc3Data_Type()
)
voltsDc3Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsDc3Data.setStatus("current")
_CurrentData_Type = Integer32
_CurrentData_Object = MibScalar
currentData = _CurrentData_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 6),
    _CurrentData_Type()
)
currentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentData.setStatus("current")
_InverterVacData_Type = Integer32
_InverterVacData_Object = MibScalar
inverterVacData = _InverterVacData_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 7),
    _InverterVacData_Type()
)
inverterVacData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterVacData.setStatus("current")
_LineVacData_Type = Integer32
_LineVacData_Object = MibScalar
lineVacData = _LineVacData_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 8),
    _LineVacData_Type()
)
lineVacData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineVacData.setStatus("current")
_Contact1Data_Type = Integer32
_Contact1Data_Object = MibScalar
contact1Data = _Contact1Data_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 9),
    _Contact1Data_Type()
)
contact1Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact1Data.setStatus("current")
_Contact2Data_Type = Integer32
_Contact2Data_Object = MibScalar
contact2Data = _Contact2Data_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 10),
    _Contact2Data_Type()
)
contact2Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact2Data.setStatus("current")
_Contact3Data_Type = Integer32
_Contact3Data_Object = MibScalar
contact3Data = _Contact3Data_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 11),
    _Contact3Data_Type()
)
contact3Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact3Data.setStatus("current")
_CurrentX10Data_Type = Integer32
_CurrentX10Data_Object = MibScalar
currentX10Data = _CurrentX10Data_Object(
    (1, 3, 6, 1, 4, 1, 44686, 1, 3, 12),
    _CurrentX10Data_Type()
)
currentX10Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentX10Data.setStatus("current")
_SpmTraps_ObjectIdentity = ObjectIdentity
spmTraps = _SpmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255)
)
_SpmTrapPrefix_ObjectIdentity = ObjectIdentity
spmTrapPrefix = _SpmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0)
)

# Managed Objects groups


# Notification objects

tempCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 1)
)
tempCAlarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "tempCName"),
        ("NWMR-MIB", "tempCData"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    tempCAlarm.setStatus(
        "current"
    )

tempFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 2)
)
tempFAlarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "tempFName"),
        ("NWMR-MIB", "tempFData"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    tempFAlarm.setStatus(
        "current"
    )

voltsDc1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 3)
)
voltsDc1Alarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "voltsDc1Name"),
        ("NWMR-MIB", "voltsDc1Data"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    voltsDc1Alarm.setStatus(
        "current"
    )

voltsDc2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 4)
)
voltsDc2Alarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "voltsDc2Name"),
        ("NWMR-MIB", "voltsDc2Data"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    voltsDc2Alarm.setStatus(
        "current"
    )

voltsDc3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 5)
)
voltsDc3Alarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "voltsDc3Name"),
        ("NWMR-MIB", "voltsDc3Data"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    voltsDc3Alarm.setStatus(
        "current"
    )

currentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 6)
)
currentAlarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "currentName"),
        ("NWMR-MIB", "currentData"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    currentAlarm.setStatus(
        "current"
    )

inverterVacAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 7)
)
inverterVacAlarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "inverterVacName"),
        ("NWMR-MIB", "inverterVacData"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    inverterVacAlarm.setStatus(
        "current"
    )

lineVacAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 8)
)
lineVacAlarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "lineVacName"),
        ("NWMR-MIB", "lineVacData"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    lineVacAlarm.setStatus(
        "current"
    )

contact1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 9)
)
contact1Alarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "contact1Name"),
        ("NWMR-MIB", "contact1Data"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    contact1Alarm.setStatus(
        "current"
    )

contact2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 10)
)
contact2Alarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "contact2Name"),
        ("NWMR-MIB", "contact2Data"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    contact2Alarm.setStatus(
        "current"
    )

contact3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 11)
)
contact3Alarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "contact3Name"),
        ("NWMR-MIB", "contact3Data"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    contact3Alarm.setStatus(
        "current"
    )

testAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44686, 1, 255, 0, 255)
)
testAlarm.setObjects(
      *(("NWMR-MIB", "productTitle"),
        ("NWMR-MIB", "productFriendlyName"),
        ("NWMR-MIB", "tempCName"),
        ("NWMR-MIB", "tempCData"),
        ("NWMR-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    testAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NWMR-MIB",
    **{"newmarPower": newmarPower,
       "spm200": spm200,
       "deviceInfo": deviceInfo,
       "productTitle": productTitle,
       "productVersion": productVersion,
       "productFriendlyName": productFriendlyName,
       "productMacAddress": productMacAddress,
       "productUrl": productUrl,
       "alarmTripType": alarmTripType,
       "spmNames": spmNames,
       "tempCName": tempCName,
       "tempFName": tempFName,
       "voltsDc1Name": voltsDc1Name,
       "voltsDc2Name": voltsDc2Name,
       "voltsDc3Name": voltsDc3Name,
       "currentName": currentName,
       "inverterVacName": inverterVacName,
       "lineVacName": lineVacName,
       "contact1Name": contact1Name,
       "contact2Name": contact2Name,
       "contact3Name": contact3Name,
       "spmData": spmData,
       "tempCData": tempCData,
       "tempFData": tempFData,
       "voltsDc1Data": voltsDc1Data,
       "voltsDc2Data": voltsDc2Data,
       "voltsDc3Data": voltsDc3Data,
       "currentData": currentData,
       "inverterVacData": inverterVacData,
       "lineVacData": lineVacData,
       "contact1Data": contact1Data,
       "contact2Data": contact2Data,
       "contact3Data": contact3Data,
       "currentX10Data": currentX10Data,
       "spmTraps": spmTraps,
       "spmTrapPrefix": spmTrapPrefix,
       "tempCAlarm": tempCAlarm,
       "tempFAlarm": tempFAlarm,
       "voltsDc1Alarm": voltsDc1Alarm,
       "voltsDc2Alarm": voltsDc2Alarm,
       "voltsDc3Alarm": voltsDc3Alarm,
       "currentAlarm": currentAlarm,
       "inverterVacAlarm": inverterVacAlarm,
       "lineVacAlarm": lineVacAlarm,
       "contact1Alarm": contact1Alarm,
       "contact2Alarm": contact2Alarm,
       "contact3Alarm": contact3Alarm,
       "testAlarm": testAlarm}
)
